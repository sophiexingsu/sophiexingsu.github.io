---
title: "How Action Performance Influences Segmentation and Memory"
excerpt: "Investigating the role of mimicry and action execution in event perception and memory encoding"
collection: portfolio
permalink: /portfolio/action-segmentation-memory/
date: 2023-01-01
status: "In Progress"

# GitHub Repository
github_repos:
  - name: act_seg_mem
    url: https://github.com/sophiexingsu/act_seg_mem
    description: "Action segmentation and memory analysis codes for two-study paradigm"
    languages: [Python, R]

# Technology Stack
tech_stack:
  languages: [Python, R]
  tools: [Video Analysis, Statistical Modeling, Memory Assessment]

# Tags
tags: [action-perception, memory, event-segmentation, embodied-cognition, mimicry]

# Layout Options
header:
  teaser: /files/projects/action-segmentation-memory.gif
---

## Research Question

{% include research-question.html question="Does mimicking actions while watching affect how people segment events and remember what they saw?" %}

## Overview

This project investigates whether **action performance**—specifically, mimicry during observation—influences event segmentation and subsequent memory. Using a two-study design with everyday activity videos, I examine:

1. How action memory relates to event segmentation
2. Whether mimicking actions while watching changes segmentation patterns and memory encoding

## Theoretical Background

### Embodied Cognition and Event Perception

Traditional theories of event perception emphasize **visual** and **conceptual** processing. However, **embodied cognition** theories suggest that motor simulation plays a key role in understanding actions. This project tests whether:

- **Motor engagement** during viewing affects event boundary detection
- **Mimicry** changes the granularity of segmentation (coarse vs. fine boundaries)
- **Action execution** enhances memory for event structure

### Event Segmentation and Memory

Event segmentation theory proposes that:
- Events are encoded as discrete **chunks** in memory
- Event boundaries serve as **retrieval cues**
- Better segmentation → better memory

If mimicry affects segmentation, it should also affect memory.

## Study Design

This project includes **two complementary studies**:

### Study 1: Action Memory and Segmentation

**Goal**: Establish baseline relationship between action memory and segmentation ability

**Design**:
1. Participants watch 4 everyday activity videos:
   - Making breakfast
   - Gardening
   - Preparing for a party
   - Building with Legos
2. Segmentation task: Press button at event boundaries (coarse and fine)
3. Memory test: Free recall and recognition for actions

**Measures**:
- Segmentation agreement with normative boundaries
- Memory accuracy (% actions recalled)
- Correlation between segmentation and memory

### Study 2: Mimicry While Watching

**Goal**: Test whether mimicry causally affects segmentation and memory

**Design**:
1. Participants watch the same 4 videos under **two conditions**:
   - **Passive viewing**: Watch normally
   - **Mimicry**: Mirror actor's hand movements while watching
2. Segmentation task after each video
3. Memory test for actions

**Predictions**:
- Mimicry increases **fine-grained** segmentation (more boundaries detected)
- Mimicry enhances **action memory** (better recall for performed actions)
- Effect stronger for **goal-directed actions** vs. transitional movements

## Video Stimuli

Four everyday activities selected for ecological validity:

### 1. Breakfast Activity
- Making scrambled eggs, toast, and coffee
- Clear action sequences (crack eggs → stir → pour → cook)
- Duration: ~5 minutes

### 2. Gardening Activity
- Planting seeds, watering, arranging pots
- Object manipulation and spatial arrangement
- Duration: ~4 minutes

### 3. Party Preparation
- Setting table, arranging decorations, preparing snacks
- Social context, multiple sub-goals
- Duration: ~6 minutes

### 4. Lego Building
- Constructing a model from instructions
- Hierarchical structure (sub-assemblies → final model)
- Duration: ~5 minutes

All videos filmed from **observer perspective** to facilitate mimicry.

## Methodology

### Performance Extraction (Python)

Action performance was coded and extracted using custom Python scripts:

```python
# Pseudocode for performance extraction
def extract_actions(video_path, segmentation_data):
    """
    Extract action units from video based on segmentation

    Returns:
    - action_list: Sequence of action labels
    - timestamps: Start/end times for each action
    - features: Visual features per action
    """
    # 1. Load video frames
    # 2. Align with segmentation boundaries
    # 3. Extract action units
    # 4. Code action types (reach, grasp, move, etc.)
```

### Statistical Analysis (R)

Mixed-effects models testing:
- Effect of mimicry on number of boundaries detected
- Effect of mimicry on memory accuracy
- Individual differences in mimicry benefit
- Correlation between segmentation changes and memory improvements

## Preliminary Findings

**Study 1** (Action Memory & Segmentation):
- Positive correlation between segmentation agreement and memory accuracy
- Participants who segment more consistently also remember more actions
- Effect strongest for goal-directed actions (vs. transitional movements)

**Study 2** (Mimicry):
- Data collection in progress
- Preliminary data suggests mimicry increases fine-grained segmentation
- Mixed results for memory enhancement (may depend on individual differences)

## Analysis Pipeline

The [act_seg_mem repository](https://github.com/sophiexingsu/act_seg_mem) includes:

### Scripts:
- **`performance_extraction.py`**: Extract action units from video and segmentation data
- **`segmentation_analysis.R`**: Analyze boundary detection and agreement
- **`memory_analysis.R`**: Test memory accuracy and correlations
- **`mimicry_comparison.R`**: Compare passive viewing vs. mimicry conditions

### Data Structure:
```
data/
  segmentation/
    coarse_boundaries.csv
    fine_boundaries.csv
  memory/
    recall_data.csv
    recognition_data.csv
  mimicry/
    passive_condition.csv
    mimicry_condition.csv
```

## Challenges and Solutions

### Challenge 1: Coding Action Units
**Problem**: Difficult to objectively segment continuous action into discrete units
**Solution**: Multiple coders + hierarchical coding scheme (low-level movements → high-level goals)

### Challenge 2: Individual Differences in Mimicry
**Problem**: Participants vary widely in mimicry fidelity
**Solution**: Record mimicry with video + code fidelity as covariate

### Challenge 3: Memory Test Design
**Problem**: Free recall may be influenced by verbal ability, not just memory
**Solution**: Add recognition test + action ordering test

## Implications

If mimicry enhances segmentation and memory:

- **Embodied cognition**: Motor simulation is not epiphenomenal but functional
- **Learning applications**: Active imitation may improve skill acquisition
- **Clinical applications**: Mimicry training for individuals with action understanding deficits (e.g., apraxia)

## Future Directions

- **fMRI version**: Neural correlates of mimicry-enhanced segmentation
- **Motor cortex stimulation**: Causal role of motor cortex in event perception
- **Developmental studies**: When does mimicry start influencing event perception?
- **Individual differences**: Relate mimicry benefit to motor imagery ability

## Related Projects

- [Predictive Looking](/portfolio/predictive-looking/): How prediction errors drive segmentation
- [Gaze Entropy & Event Boundaries](/portfolio/gaze-entropy-event-boundaries/): Proactive cognitive control during viewing
- [Incremental vs. Global Updating](/portfolio/incremental-global-updating/): How event models are updated

---

**Keywords**: Action Perception, Memory, Event Segmentation, Embodied Cognition, Mimicry, Motor Simulation, Everyday Activities
