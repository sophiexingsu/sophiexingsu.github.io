---
title: "Human Movement Analysis Dashboard"
excerpt: "Interactive visualization platform for pose estimation and pantomimed action recognition research"
collection: portfolio
permalink: /portfolio/movement-analysis-dashboard/
date: 2024-06-01
status: "Active Demo"

# GitHub Repository
github_repos:
  - name: pantomimed-action-recognition
    url: https://github.com/sophiexingsu/pantomimed-action-recognition
    description: "Pose estimation pipeline and action recognition research"
    languages: [Python, JavaScript]

# Technology Stack
tech_stack:
  languages: [Python, JavaScript, HTML/CSS]
  tools: [Plotly.js, MediaPipe, OpenCV, Pose Estimation]

# Tags
tags: [action-recognition, pose-estimation, computer-vision, interactive-dashboard, machine-learning]

# Layout Options
header:
  teaser: /files/projects/movement-dashboard/thumbnail.svg
---

## Research Question

{% include research-question.html question="Can machine learning models recognize human actions from body movements alone, without object context?" %}

## Live Demo

<div style="background: linear-gradient(135deg, #2c3e50, #4a90a4); padding: 1.5em; border-radius: 8px; margin: 1em 0;">
  <p style="color: white; margin: 0 0 0.5em 0; font-weight: bold;">Interactive Dashboard</p>
  <p style="color: rgba(255,255,255,0.8); margin: 0 0 1em 0;">Explore pose estimation data, movement timelines, and skeleton visualizations</p>
  <a href="/files/projects/movement-dashboard/" class="btn btn--light-outline" style="color: white; border-color: white;">Launch Dashboard →</a>
</div>

## Overview

This project develops computational tools for analyzing human movement patterns from video recordings of **pantomimed actions**—everyday activities performed without the actual objects present. The dashboard provides real-time visualization of:

- **Skeleton tracking** from pose estimation
- **Joint position trajectories** over time
- **Movement intensity timelines**
- **Video playback** with privacy-preserving face blocking

## Research Goals

### Goal 1: Action Quality Assessment
**Objective:** Develop methods to distinguish between high-quality and low-quality pantomimed action performances.

Our dataset includes recordings where participants demonstrated varying levels of effort and accuracy. Some executed actions with high fidelity to real-world movements, while others showed reduced effort or less accurate representations.

**Approach:**
- Post-processing analysis using pose tracking from extracted joint data
- Calculating joint movement patterns, smoothness, and trajectory analysis
- Quantifying movement characteristics that correlate with action quality

### Goal 2: Object-Free Action Recognition
**Objective:** Train machine learning models to recognize actions based solely on human movement patterns, without visual object cues.

**Research Questions:**
- Can ML models accurately recognize pantomimed actions without object context?
- Will training on pantomimed data improve generalization capabilities?
- How do object-free models compare to traditional approaches?

### Goal 3: Enhancing State-of-the-Art Recognition
**Objective:** Improve current action recognition systems by leveraging spatial-temporal relationships learned from pantomimed actions.

Recent research suggests that learning from human movement patterns rather than relying on object cues develops more robust and generalizable action understanding.

## Dataset

The dataset consists of video recordings of participants performing everyday activities in pantomimed form:

**Scale:**
- ~8,800 video files across multiple studies
- ~118 unique participants
- 3.2GB of video data
- Comprehensive pose tracking data (CSV format)

**Action Categories:**
- **Gardening:** planting, digging, watering, arranging pots
- **Kitchen activities:** cooking, preparing food, using utensils
- **Personal care:** brushing teeth, grooming
- **Object manipulation:** moving, stacking, organizing

**Data Processing Pipeline:**
1. Original video recording
2. Automated pose detection (MediaPipe)
3. Joint coordinate extraction to CSV
4. Movement metric computation
5. Privacy-preserving face blocking

## Dashboard Features

### Skeleton Visualization
Real-time rendering of body joint positions with anatomical connections:
- Shoulders, elbows, wrists
- Finger tracking (thumb, index, pinky)
- Frame-by-frame playback with slider control

### Movement Timeline
Normalized movement intensity showing:
- Periods of high vs. low activity
- Action segmentation opportunities
- Quality assessment metrics

### Joint Trajectories
2D visualization of how joints move through space:
- Color-coded by time progression
- Comparison across different joints
- Pattern recognition for action classification

### Privacy-Preserving Video
Original performance videos with:
- Automated face detection and blocking
- Synchronized playback with pose data
- Safe for research sharing and publication

## Technical Implementation

**Frontend (Static Dashboard):**
```
- Plotly.js for interactive charts
- Canvas API for skeleton rendering
- Bootstrap 5 for responsive layout
- Vanilla JavaScript (no framework dependencies)
```

**Backend (Data Processing):**
```python
- MediaPipe for pose estimation
- OpenCV for video processing
- Pandas/NumPy for data analysis
- Custom preprocessing pipeline
```

**Deployment:**
- Static hosting on GitHub Pages
- Pre-processed JSON data files
- No server-side computation required

## Significance

This project addresses fundamental questions in computer vision and cognitive science:

1. **Theoretical:** Understanding how human actions can be recognized independently of object interactions
2. **Practical:** Improving action recognition for scenarios where objects may be occluded or absent
3. **Methodological:** Developing quality metrics for human action performance
4. **Applied:** Enabling robust action recognition for real-world deployment

## Connection to Cognitive Research

This computational work complements my behavioral research on action perception:

- **Action Segmentation & Memory:** How does action quality affect event boundary detection?
- **Embodied Cognition:** What movement features are essential for action understanding?
- **Motor Simulation:** Can pose-based recognition mirror human action perception?

The dashboard serves both as a research tool and a demonstration of the computational approaches we're developing.

## Future Directions

- **Model Development:** Train action classifiers on pose sequences
- **Quality Metrics:** Validate automated quality assessment against human ratings
- **Cross-Dataset Transfer:** Test generalization to other action recognition benchmarks
- **Real-Time Processing:** Deploy models for live action recognition

## Related Projects

- [How Action Performance Influences Segmentation and Memory](/portfolio/action-segmentation-memory/): Behavioral studies using the same video stimuli
- [Predictive Looking & Event Segmentation](/portfolio/predictive-looking/): How prediction errors drive action parsing

---

**Keywords**: Action Recognition, Pose Estimation, Computer Vision, Machine Learning, Human Movement Analysis, Pantomimed Actions, Interactive Dashboard
