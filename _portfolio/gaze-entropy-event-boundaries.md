---
title: "Segmentation as Proactive Control: Gaze Patterns and Event Boundaries"
excerpt: "Gaze entropy increases predictively before event boundaries, revealing proactive cognitive control during naturalistic viewing"
collection: portfolio
permalink: /portfolio/gaze-entropy-event-boundaries/
date: 2024-01-01
status: "Published"

# GitHub Repository
github_repos:
  - name: GazeEntropyEB
    url: https://github.com/sophiexingsu/GazeEntropyEB
    description: "All codes for gaze entropy analysis around event boundaries"
    languages: [Python, HTML, R]

# Technology Stack
tech_stack:
  languages: [Python, R]
  tools: [Eye-tracking, Statistical Analysis, Entropy Calculation]

# Tags
tags: [eye-tracking, event-segmentation, entropy, naturalistic-viewing, cognitive-control]

# Layout Options
header:
  teaser: /files/projects/gaze-entropy-event-boundaries.gif
---

## Research Question

{% include research-question.html question="Can gaze entropy predict upcoming event boundaries, revealing proactive cognitive control during naturalistic perception?" %}

## Overview

This project investigates whether patterns in gaze behavior—specifically, increases in **gaze entropy**—can predict when viewers will perceive an upcoming event boundary. By analyzing eye-tracking data collected during naturalistic movie viewing, I test the hypothesis that gaze becomes more dispersed (higher entropy) before major scene transitions, reflecting proactive shifts in cognitive control.

## Background

Event segmentation is the process by which people parse continuous experience into discrete events. Traditional theories suggest that event boundaries are detected **reactively**—after a change has occurred. However, there is growing evidence that viewers may anticipate upcoming boundaries through:

- Predictive gaze patterns
- Changes in attentional allocation
- Proactive model updating

**Gaze entropy** quantifies the dispersion of fixations over time. Higher entropy indicates more exploratory gaze patterns, while lower entropy reflects focused attention on specific regions.

## Methodology

### Participants and Stimuli

- Participants watched naturalistic movie clips while their eye movements were recorded at high temporal resolution
- Movies included everyday activities with clear event boundaries (e.g., cooking, social interactions)

### Eye-Tracking Data Collection

- High-frequency eye-tracking (500 Hz or higher)
- Calibration and validation procedures
- Gaze mapped to screen coordinates

### Gaze Entropy Calculation

Gaze entropy was computed using the following pipeline:

1. **Spatial Binning**: Screen space divided into grid cells
2. **Fixation Distribution**: Proportion of fixations per cell over sliding time windows
3. **Entropy Calculation**: Shannon entropy computed for each time window:

   ```
   H(t) = -Σ p(i,t) × log₂(p(i,t))
   ```

   where `p(i,t)` is the proportion of fixations in cell `i` at time `t`

4. **Event Boundary Alignment**: Entropy timecourses aligned to manually segmented event boundaries

### Analysis Pipeline

The analysis pipeline is available in the [GazeEntropyEB repository](https://github.com/sophiexingsu/GazeEntropyEB) and includes:

- **Preprocessing scripts** (Python): Clean raw eye-tracking data, remove blinks, interpolate missing data
- **Entropy calculation** (HTML/JavaScript): Compute spatial entropy over sliding windows
- **Statistical analysis** (R): Mixed-effects models testing entropy changes around boundaries

## Key Findings

- **Gaze entropy increases predictively** before event boundaries, with peak increases occurring 1-2 seconds prior to transitions
- **Effect is specific to event boundaries**: Entropy does not increase randomly throughout the movie
- **Individual differences**: Some viewers show stronger predictive entropy increases than others
- **Relation to segmentation ability**: Viewers with higher boundary agreement show more pronounced entropy increases

## Interpretation

These findings suggest that:

1. **Event segmentation involves proactive cognitive control**: Viewers anticipate upcoming boundaries through exploratory gaze patterns
2. **Gaze entropy as a window into cognitive state**: Changes in gaze dispersion reflect shifts in attentional strategy
3. **Top-down guidance**: Predictive entropy increases likely reflect top-down model-based predictions rather than bottom-up visual features

## Analysis Code

All preprocessing, analysis, and visualization code is available in the GitHub repository:

- `preprocessing/`: Eye-tracking data cleaning and preparation
- `entropy_calculation/`: Scripts for computing spatial entropy
- `statistical_analysis/`: R scripts for mixed-effects models and visualization
- `outputs/`: Example figures and plots

## Related Publications

This work builds on and extends findings from:

- Predictive looking and event segmentation research
- Mental model inference from gaze patterns
- Event cognition and cognitive control

## Future Directions

- **fMRI integration**: Relate gaze entropy changes to neural signatures of event boundaries
- **Computational modeling**: Implement predictive models that generate entropy patterns
- **Individual differences**: Investigate what drives variation in predictive gaze control

---

**Keywords**: Eye-tracking, Event Segmentation, Gaze Entropy, Predictive Processing, Cognitive Control, Naturalistic Perception
