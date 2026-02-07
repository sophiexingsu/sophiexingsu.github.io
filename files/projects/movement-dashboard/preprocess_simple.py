#!/usr/bin/env python3
"""
Simple pre-processor that doesn't require pandas.
"""

import os
import json
import csv
import math
from pathlib import Path
import glob


def process_pose_csv(csv_path):
    """Process a single pose CSV file using only stdlib."""
    try:
        with open(csv_path, 'r') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        if not rows:
            return None

        # Get column names
        columns = rows[0].keys()

        # Extract joint names from columns ending in _x
        joint_names = set()
        for col in columns:
            if '_x' in col:
                joint_name = col.replace('_x', '')
                joint_names.add(joint_name)

        joint_names = list(joint_names)

        # Sample every 5th frame
        sampled_rows = rows[::5]

        # Prepare timeline data
        timeline_data = []
        for idx, row in enumerate(sampled_rows[:50]):  # Limit to 50 samples
            frame = idx * 5
            timestamp = float(row.get('timestamp', frame / 30))

            frame_joints = {}
            for joint in joint_names:
                x_col = f"{joint}_x"
                y_col = f"{joint}_y"
                if x_col in row and y_col in row:
                    try:
                        x = float(row[x_col])
                        y = float(row[y_col])
                        if not (math.isnan(x) or math.isnan(y)):
                            frame_joints[joint] = [x, y]
                    except (ValueError, TypeError):
                        pass

            if frame_joints:
                timeline_data.append({
                    'frame': frame,
                    'timestamp': timestamp,
                    'joints': frame_joints
                })

        # Calculate movement timeline
        movement_values = []
        prev_positions = {}

        for row in rows[::5][:50]:
            total_movement = 0
            count = 0

            for joint in joint_names:
                x_col = f"{joint}_x"
                y_col = f"{joint}_y"
                if x_col in row and y_col in row:
                    try:
                        x = float(row[x_col])
                        y = float(row[y_col])

                        if joint in prev_positions:
                            px, py = prev_positions[joint]
                            dist = math.sqrt((x - px)**2 + (y - py)**2)
                            total_movement += dist
                            count += 1

                        prev_positions[joint] = (x, y)
                    except (ValueError, TypeError):
                        pass

            if count > 0:
                movement_values.append(total_movement / count)
            else:
                movement_values.append(0)

        # Normalize movement values
        max_movement = max(movement_values) if movement_values else 1
        if max_movement > 0:
            movement_values = [v / max_movement for v in movement_values]

        return {
            'joint_names': joint_names,
            'frame_count': len(rows),
            'sampled_frames': len(sampled_rows),
            'timeline_data': timeline_data,
            'movement_timeline': {
                'frames': list(range(0, len(rows), 5))[:50],
                'values': movement_values
            }
        }

    except Exception as e:
        print(f"Error processing {csv_path}: {e}")
        return None


def main():
    base_path = "/Users/sophie/Library/CloudStorage/Box-Box/DCL_ARCHIVE/Documents/Events/exp168_ActionsInfluenceMemory/Analysis/act_seg_mem/data"
    output_path = "/Users/sophie/Library/CloudStorage/Box-Box/sophiexingsu.github.io/files/projects/movement-dashboard/data"
    blocked_video_path = "/Users/sophie/Library/CloudStorage/Box-Box/DCL_ARCHIVE/Documents/Events/exp168_ActionsInfluenceMemory/Analysis/act_seg_mem/data/study2/blocked/performance"

    os.makedirs(output_path, exist_ok=True)

    # Specific participants to use
    participants = [
        '5ef981cf234db67251c1e0d7',
        '65a038f02fb72900ba2653fc',
        '65e1f75ab3efd22e847cfbf0'
    ]

    structure = {'study2': {'participants': {}}}
    processed_count = 0

    study = 'study2'
    pose_path = os.path.join(base_path, study, 'all_pose_data')

    for participant in participants:
        participant_pose_path = os.path.join(pose_path, participant)
        if not os.path.exists(participant_pose_path):
            print(f"Pose data not found for {participant}")
            continue

        participant_output = os.path.join(output_path, study, participant)
        os.makedirs(participant_output, exist_ok=True)

        # Create videos directory
        videos_output = os.path.join(participant_output, 'videos')
        os.makedirs(videos_output, exist_ok=True)

        # Get CSV files (pose data)
        csv_files = sorted(glob.glob(os.path.join(participant_pose_path, '*.csv')))[:10]  # Up to 10 actions

        actions = []
        for csv_file in csv_files:
            filename = os.path.basename(csv_file)
            action = filename.replace(f"{participant}_", "").replace("_body_joints.csv", "")

            # Process the CSV
            pose_data = process_pose_csv(csv_file)

            if pose_data:
                # Save as JSON
                safe_action = action.replace(' ', '_').replace('/', '_')
                json_path = os.path.join(participant_output, f"{safe_action}.json")

                with open(json_path, 'w') as f:
                    json.dump(pose_data, f)

                # Copy corresponding blocked video if exists
                video_src = os.path.join(blocked_video_path, participant, f"{participant}_{action}.mp4")
                video_dst = os.path.join(videos_output, f"{safe_action}.mp4")

                if os.path.exists(video_src):
                    import shutil
                    shutil.copy2(video_src, video_dst)
                    print(f"Processed + video: {participant}/{action}")
                else:
                    print(f"Processed (no video): {participant}/{action}")

                actions.append(action)
                processed_count += 1

        if actions:
            structure[study]['participants'][participant] = {'actions': actions}

    # Save index
    with open(os.path.join(output_path, 'index.json'), 'w') as f:
        json.dump(structure, f, indent=2)

    print(f"\nTotal files processed: {processed_count}")
    print(f"Output directory: {output_path}")


if __name__ == '__main__':
    main()
