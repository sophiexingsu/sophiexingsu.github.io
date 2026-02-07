#!/usr/bin/env python3
"""
Pre-process pose data CSVs into JSON for the static dashboard.
Run this script locally to generate the data files, then commit them to GitHub.

Usage:
    python preprocess_data.py --source /path/to/act_seg_mem/data --output ./data
"""

import os
import json
import argparse
import pandas as pd
import numpy as np
from pathlib import Path
import glob


def process_pose_csv(csv_path):
    """Process a single pose CSV file and return summary data."""
    try:
        df = pd.read_csv(csv_path)

        if df.empty:
            return None

        # Get column structure
        coordinate_cols = [col for col in df.columns if '_x' in col or '_y' in col]

        if not coordinate_cols:
            return None

        # Extract joint names
        joint_names = set()
        for col in coordinate_cols:
            if '_x' in col:
                joint_name = col.replace('_x', '')
                joint_names.add(joint_name)

        joint_names = list(joint_names)

        # Sample every 5th frame to reduce data size
        sampled_df = df.iloc[::5].reset_index(drop=True)

        # Prepare timeline data (sampled positions)
        timeline_data = []
        for idx, row in sampled_df.iterrows():
            frame = idx * 5
            timestamp = row.get('timestamp', frame / 30)

            frame_joints = {}
            for joint in joint_names:
                x_col = f"{joint}_x"
                y_col = f"{joint}_y"
                if x_col in df.columns and y_col in df.columns:
                    x = row[x_col]
                    y = row[y_col]
                    if not (pd.isna(x) or pd.isna(y)):
                        frame_joints[joint] = [float(x), float(y)]

            if frame_joints:
                timeline_data.append({
                    'frame': int(frame),
                    'timestamp': float(timestamp),
                    'joints': frame_joints
                })

        # Calculate movement metrics
        movement_values = []
        for joint in joint_names:
            x_col = f"{joint}_x"
            y_col = f"{joint}_y"
            if x_col in df.columns and y_col in df.columns:
                x_diff = df[x_col].diff()
                y_diff = df[y_col].diff()
                velocity = np.sqrt(x_diff**2 + y_diff**2)
                movement_values.append(velocity.fillna(0))

        if movement_values:
            avg_velocity = sum(movement_values) / len(movement_values)
            max_vel = avg_velocity.max() if avg_velocity.max() > 0 else 1
            normalized_movement = (avg_velocity / max_vel).tolist()
        else:
            normalized_movement = [0] * len(df)

        # Sample movement timeline too
        sampled_movement = normalized_movement[::5]

        return {
            'joint_names': joint_names,
            'frame_count': len(df),
            'sampled_frames': len(sampled_df),
            'timeline_data': timeline_data[:50],  # Limit to 50 samples for file size
            'movement_timeline': {
                'frames': list(range(0, len(df), 5))[:50],
                'values': sampled_movement[:50]
            }
        }

    except Exception as e:
        print(f"Error processing {csv_path}: {e}")
        return None


def get_study_structure(base_path):
    """Scan directory structure to find available data."""
    structure = {}

    for study in ['study1', 'study2', 'study3', 'study4']:
        pose_path = os.path.join(base_path, study, 'all_pose_data')
        if not os.path.exists(pose_path):
            continue

        structure[study] = {'participants': {}}

        # Get participants
        for participant in os.listdir(pose_path):
            participant_path = os.path.join(pose_path, participant)
            if not os.path.isdir(participant_path):
                continue

            # Get actions for this participant
            actions = []
            csv_files = glob.glob(os.path.join(participant_path, '*.csv'))

            for csv_file in csv_files:
                filename = os.path.basename(csv_file)
                # Extract action name: {participant}_{action}_body_joints.csv
                action = filename.replace(f"{participant}_", "").replace("_body_joints.csv", "")
                actions.append(action)

            if actions:
                structure[study]['participants'][participant] = {
                    'actions': sorted(actions)
                }

    return structure


def preprocess_sample_data(base_path, output_path, max_participants=3, max_actions=5):
    """
    Pre-process a sample of the data for the static dashboard.
    Limits data to keep file sizes manageable for GitHub Pages.
    """
    os.makedirs(output_path, exist_ok=True)

    # Get structure
    structure = get_study_structure(base_path)

    # Save structure index
    with open(os.path.join(output_path, 'index.json'), 'w') as f:
        json.dump(structure, f, indent=2)

    print(f"Found studies: {list(structure.keys())}")

    # Process sample data for each study
    processed_count = 0

    for study, study_data in structure.items():
        study_output = os.path.join(output_path, study)
        os.makedirs(study_output, exist_ok=True)

        participants = list(study_data['participants'].keys())[:max_participants]

        for participant in participants:
            participant_output = os.path.join(study_output, participant)
            os.makedirs(participant_output, exist_ok=True)

            actions = study_data['participants'][participant]['actions'][:max_actions]

            for action in actions:
                # Find the CSV file
                csv_filename = f"{participant}_{action}_body_joints.csv"
                csv_path = os.path.join(base_path, study, 'all_pose_data', participant, csv_filename)

                if not os.path.exists(csv_path):
                    # Try with spaces converted
                    continue

                # Process the CSV
                pose_data = process_pose_csv(csv_path)

                if pose_data:
                    # Save as JSON
                    safe_action = action.replace(' ', '_').replace('/', '_')
                    json_path = os.path.join(participant_output, f"{safe_action}.json")

                    with open(json_path, 'w') as f:
                        json.dump(pose_data, f)

                    processed_count += 1
                    print(f"Processed: {study}/{participant}/{action}")

    print(f"\nTotal files processed: {processed_count}")
    print(f"Output directory: {output_path}")

    # Update index with only processed data
    processed_structure = {}
    for study in os.listdir(output_path):
        study_path = os.path.join(output_path, study)
        if not os.path.isdir(study_path) or study == 'index.json':
            continue

        processed_structure[study] = {'participants': {}}

        for participant in os.listdir(study_path):
            participant_path = os.path.join(study_path, participant)
            if not os.path.isdir(participant_path):
                continue

            actions = []
            for f in os.listdir(participant_path):
                if f.endswith('.json'):
                    actions.append(f.replace('.json', '').replace('_', ' '))

            if actions:
                processed_structure[study]['participants'][participant] = {
                    'actions': sorted(actions)
                }

    # Save updated index
    with open(os.path.join(output_path, 'index.json'), 'w') as f:
        json.dump(processed_structure, f, indent=2)

    return processed_structure


def main():
    parser = argparse.ArgumentParser(description='Pre-process pose data for static dashboard')
    parser.add_argument('--source', type=str,
                       default='/Users/sophie/Library/CloudStorage/Box-Box/DCL_ARCHIVE/Documents/Events/exp168_ActionsInfluenceMemory/Analysis/act_seg_mem/data',
                       help='Source data directory')
    parser.add_argument('--output', type=str,
                       default='./data',
                       help='Output directory for JSON files')
    parser.add_argument('--max-participants', type=int, default=3,
                       help='Maximum participants per study to process')
    parser.add_argument('--max-actions', type=int, default=5,
                       help='Maximum actions per participant to process')

    args = parser.parse_args()

    print(f"Source: {args.source}")
    print(f"Output: {args.output}")
    print(f"Max participants: {args.max_participants}")
    print(f"Max actions: {args.max_actions}")
    print()

    preprocess_sample_data(
        args.source,
        args.output,
        args.max_participants,
        args.max_actions
    )


if __name__ == '__main__':
    main()
