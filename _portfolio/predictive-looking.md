cd ..---
title: "Predictive Looking Errors and Event Segmentation"
excerpt: "Investigating how gaze anticipation errors reveal event boundaries during movie watching — Published in Journal of Experimental Psychology: General"
collection: portfolio
permalink: /portfolio/predictive-looking/
date: 2024-02-01
status: "Published"

# Publications
publications:
  - title: "Predictive Looking and Predictive Looking Errors in Everyday Activities"
    venue: "Journal of Experimental Psychology: General"
    date: 2025-10
    url: https://psycnet.apa.org/record/2026-84598-001
    type: "paper"

# GitHub Repository
github_repos:
  - name: Predictive_Looking
    url: https://github.com/sophiexingsu/Predictive_Looking
    description: "Codes for predictive looking analysis including gaze2grid pipeline"
    languages: [Python, R]

# Technology Stack
tech_stack:
  languages: [Python, R]
  tools: [Eye-tracking, Grid-based Analysis, Statistical Modeling]

# Tags
tags: [eye-tracking, event-segmentation, predictive-looking, attention, prediction-error]

# Layout Options
header:
  teaser: /images/projects/predicitve_looking.gif
---

## Research Question

{% include research-question.html question="Can we derive continuous measures of prediction error based on gaze patterns? How would they be related to event comprehension structures" %}

## Overview

This project investigates the relationship between **predictive looking** (anticipatory eye movements toward future action locations) and **event segmentation** (how people divide continuous experience into discrete events). Using high-frequency eye-tracking during naturalistic movie viewing, I show that viewers anticipate actors' hand movements up to 9 seconds in advance, and that **prediction failures** align closely with event boundaries.

![Gaze heatmap overlayed on actor's performance](../files/output.gif)

## Theoretical Motivation

Event segmentation theory posits that people continuously update mental models of "what is happening now" during perception. When these models fail to predict incoming information, an **event boundary** is perceived. This project tests whether:

1. Viewers make **predictive eye movements** during everyday activities
2. These predictions sometimes **fail** (predictive looking errors)
3. Prediction failures align with **event boundaries**
4. Gaze-based prediction error correlates with **computational model error**

## Methodology

### Participants and Stimuli

- Participants watched videos of everyday activities (e.g., making breakfast, assembling objects, social interactions)
- Manual event segmentation collected separately

### Eye-Tracking Protocol

- High-frequency eye-tracking (1000 Hz)
- Gaze mapped to video frame coordinates
- Fixations classified as on-target (actor's hands/objects) or off-target

### Gaze-to-Grid Pipeline (`gaze2grid.py`)

A key methodological contribution is the **gaze2grid pipeline**, which converts raw gaze coordinates into spatial density grids for analysis:

```python
# Pseudocode for gaze2grid pipeline
def gaze2grid(gaze_data, grid_size=10):
    """
    Convert raw gaze coordinates to spatial density grid

    Parameters:
    - gaze_data: Timeseries of (x, y) gaze coordinates
    - grid_size: Number of grid cells per dimension

    Returns:
    - density_grid: Grid of gaze density values
    """
    # 1. Normalize gaze coordinates to [0, 1]
    # 2. Bin coordinates into grid cells
    # 3. Compute density per cell
    # 4. Return density matrix
```

This pipeline enables:
- Spatial analysis of gaze patterns
- Comparison with model predictions
- Quantification of prediction error

### Predictive Looking Analysis

**Predictive looking** was operationalized as:

1. Identify actor's hand position at time `t` (currentlocation)
2. Check if viewer's gaze at time `t-Δt` can predict the actor's hand position at time `t`
3. Compute **lead time**: How far in advance gaze arrives at future location

**Predictive looking errors** occur when:
- Gaze anticipates location A, but actor moves to location B
- Quantified as spatial distance between predicted and actual locations

### Statistical Analysis

Mixed-effects models tested:
- Relationship between prediction error and event boundary probability
- Individual differences in predictive looking ability
- Comparison with computational model error (Predictive, Associative, and Retrospective – PAR model)

## Key Findings

### 1. Viewers Anticipate Actions Up to 9 Seconds in Advance

- Gaze moves to future action locations **before** the actor's hands arrive
- Median lead time: 2-3 seconds
- Some viewers anticipate up to 9 seconds ahead

### 2. Prediction Errors Align with Event Boundaries

- When gaze predictions fail, event boundary probability increases significantly

### 3. Gaze-Based Error Mirrors Computational Model Error

- Prediction errors from gaze data correlate with errors from SEM computational model
- Suggests gaze-based error is a valid proxy for internal model error

### 4. Individual Differences in Predictive Looking

- Viewers with higher boundary agreement show more reliable predictive looking
- Suggests predictive looking is related to event segmentation ability

## Interpretation

These findings support the hypothesis that **event segmentation is driven by prediction failure**, not passive perception. Specifically:

- **Viewers actively predict** future action locations during naturalistic perception
- **Prediction errors trigger event boundaries**: When predictions fail, viewers perceive a boundary
- **Gaze as a window into cognitive state**: Eye movements reveal the content and success of internal predictions

## Repository Contents

The [Predictive_Looking repository](https://github.com/sophiexingsu/Predictive_Looking) includes:

### Key Files:
- **`gaze2grid.py`**: Converts raw eye-tracking data to spatial density grids
- **`predictive_looking_analysis.R`**: Mixed-effects models and statistical tests
- **`visualization.R`**: Generate gaze density maps and timecourse plots
- **`outputs/`**: Example figures including the gaze heatmap shown above

### Pipeline:
1. **Preprocessing**: Clean eye-tracking data (blink removal, interpolation)
2. **Gaze2Grid**: Convert gaze to spatial grids
3. **Predictive Looking Detection**: Identify anticipatory fixations
4. **Error Calculation**: Quantify prediction failures
5. **Statistical Analysis**: Mixed-effects models in R
6. **Visualization**: Generate plots and heatmaps

## Ongoing Extensions

- **Incremental vs. Global Updating**: Do prediction errors trigger incremental model updates or global restructuring?
- **fMRI Integration**: Neural correlates of prediction error and event boundaries
- **Hierarchical Models**: Multiple levels of prediction (low-level actions → high-level goals)

## Publication

**Predictive Looking and Predictive Looking Errors in Everyday Activities**
*Journal of Experimental Psychology: General* (October 2025)

[Read the full paper](https://psycnet.apa.org/record/2026-84598-001)

---

**Keywords**: Eye-tracking, Predictive Processing, Event Segmentation, Anticipatory Eye Movements, Prediction Error, Naturalistic Perception
