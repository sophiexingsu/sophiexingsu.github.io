---
title: "Incremental vs. Global Updating of Event Representations"
excerpt: "Investigating whether event model updating occurs gradually or suddenly during narrative comprehension — Dissertation Project"
collection: portfolio
permalink: /portfolio/incremental-global-updating/
date: 2023-09-01
status: "Dissertation Project"

# Collaborators
collaborators:
  - name: "Dr. Jeff Zacks"
    role: "Advisor"

# Technology Stack
tech_stack:
  languages: [Python, R, MATLAB]
  tools: [fMRI, Eye-tracking, Computational Modeling]

# Tags
tags: [event-segmentation, fMRI, computational-modeling, event-models, dissertation, prediction-error]

# Layout Options
header:
  teaser: /files/projects/incremental-global-updating.gif
---

## Research Question

{% include research-question.html question="When something changes in an event, does the mind update *only what changed* or *everything at once*?" %}

## Overview

This dissertation project investigates the **dynamics of event model updating**: when people perceive a change during an ongoing event (e.g., a character's goal shifts, a new object appears), do they update their mental representation **incrementally** (changing only the affected features) or **globally** (restructuring the entire event model)?

This question has profound implications for understanding:
- How cognitive resources are allocated during comprehension
- Whether event models are compositional or holistic
- The computational principles underlying event cognition

## Theoretical Background

### Event Segmentation Theory

**Event Segmentation Theory (EST)** proposes that:
1. People maintain **working models** of "what is happening now" (event models)
2. When prediction error increases, an **event boundary** is perceived
3. The event model is **updated** with new information

However, EST does not specify the **nature of updating**:
- **Incremental updating**: Only changed features are revised (efficient, local)
- **Global updating**: Entire model is restructured (resource-intensive, holistic)

### Computational Predictions

**Incremental Updating** predicts:
- Gradual changes in neural representations
- Feature-specific memory updates
- Linear relationship between change magnitude and update cost

**Global Updating** predicts:
- Sudden shifts in neural representations (phase transitions)
- Whole-model reactivation
- All-or-none update dynamics

### Hybrid Models

A **hierarchical hybrid model** suggests:
- **Low-level features**: Incrementally updated (e.g., object locations)
- **High-level structure**: Globally updated (e.g., goals, causal relations)

## Dissertation Studies

This dissertation includes **three complementary studies**:

### Study 1: Behavioral Evidence for Global Updating

**Method**: Controlled narrative reading task

**Design**:
- Participants read short narratives describing everyday events
- **Critical manipulation**: Mid-narrative change in protagonist's goal or location
- Measure: Reading times, memory probes, prediction accuracy

**Predictions**:
- **Incremental**: Gradual increase in reading time post-change
- **Global**: Sudden spike in reading time, followed by stabilization
- **Hybrid**: Depends on feature type (location → incremental; goal → global)

**Preliminary Results**:
- Goal changes trigger **sudden** reading time increases
- Location changes show more **gradual** patterns
- Suggests hierarchical updating (features vs. goals)

### Study 2: fMRI Evidence for Neural Reorganization

**Method**: fMRI during movie watching with embedded event changes

**Design**:
- Participants watch movie clips with controlled event changes
- **Representational Similarity Analysis (RSA)**: Compare neural patterns before vs. after changes
- Regions of interest: Medial prefrontal cortex (mPFC), posterior medial cortex (PMC), hippocampus

**Predictions**:
- **Incremental**: Smooth trajectory in representational space
- **Global**: Discontinuous jump in representational space
- **Hybrid**: PMC shows global shifts; early visual cortex shows incremental changes

**Current Status**: Data collection completed, analysis in progress

**Analysis Approach**:
```python
# Pseudocode for RSA analysis
def compute_representational_trajectory(neural_data, event_boundaries):
    """
    Compute trajectory of neural representations across event boundaries

    Returns:
    - trajectory: Timecourse of representational change
    - discontinuity_score: Measure of sudden vs. gradual change
    """
    # 1. Extract neural patterns per timepoint
    # 2. Compute pairwise similarity matrix
    # 3. Track trajectory across event boundary
    # 4. Quantify discontinuity (derivative analysis)
```

### Study 3: Computational Modeling of Updating Dynamics

**Method**: Implement and compare computational models

**Models**:

1. **Incremental Model**: Feature-by-feature updating
   ```
   Update(t) = Model(t-1) + α × Error(feature_i)
   ```

2. **Global Model**: Whole-model resampling
   ```
   if Error > threshold:
       Model(t) = Resample(prior, evidence)
   ```

3. **Hierarchical Hybrid**: Multi-level updating
   ```
   Low-level: Incremental
   High-level: Global (if error exceeds threshold)
   ```

**Evaluation**:
- Fit models to behavioral data (reading times, memory)
- Test neural predictions (fMRI representational dynamics)
- Compare model evidence (Bayesian model comparison)

**Preliminary Results**:
- Hierarchical hybrid model best explains behavioral and neural data
- Threshold for global updating varies by individual
- Prediction error accumulates before global reset

## Methodology

### Behavioral Paradigms

**Narrative Reading**:
- Sentence-by-sentence self-paced reading
- Memory probes after each narrative
- Prediction questions (what happens next?)

**Movie Watching**:
- Naturalistic movie clips (2-3 minutes)
- Event segmentation task (button press at boundaries)
- Post-viewing memory test

### fMRI Protocol

**Acquisition**:
- 3T scanner, TR = 2s
- Whole-brain coverage
- High-resolution structural scan for registration

**Preprocessing**:
- Motion correction, slice-timing correction
- Spatial smoothing (6mm FWHM)
- High-pass filtering (128s)

**Analysis**:
- **GLM**: Model event boundaries and changes
- **RSA**: Compare neural patterns across time
- **Searchlight analysis**: Identify regions showing global vs. incremental updating

### Computational Modeling

**Implementation**:
- Python + PyMC3 for Bayesian modeling
- Simulate updating dynamics under different models
- Parameter estimation via MCMC

## Key Questions

1. **Is updating incremental or global?**
   - Hypothesis: Depends on hierarchical level (features → incremental; goals → global)

2. **What triggers global updating?**
   - Hypothesis: Cumulative prediction error exceeds threshold

3. **Which brain regions implement global updating?**
   - Hypothesis: mPFC and PMC show global dynamics; sensory cortex shows incremental

4. **Are there individual differences?**
   - Hypothesis: Working memory capacity predicts global updating threshold

## Implications

If global updating is confirmed:

- **Cognitive Architecture**: Event models are not compositional but holistic
- **Resource Allocation**: Updating is costly but discrete (not continuous monitoring)
- **Neural Implementation**: Requires mechanisms for sudden state transitions (attractor dynamics?)

If hierarchical hybrid is confirmed:

- **Structured Representations**: Event models have hierarchical organization
- **Efficient Updating**: Balance between local efficiency and global coherence
- **Flexibility**: Adapt updating strategy to task demands

## Timeline

- **2023 Fall**: Behavioral studies completed
- **2024 Spring**: fMRI data collection completed
- **2024 Fall**: Computational modeling (current phase)
- **2025 Spring**: Manuscript preparation
- **2025 Summer**: Dissertation defense (target)

## Related Projects

- [Predictive Looking](/portfolio/predictive-looking/): Prediction errors trigger event boundaries
- [Gaze Entropy](/portfolio/gaze-entropy-event-boundaries/): Gaze patterns before boundaries suggest proactive control
- [Mental Representations (CLIP)](/portfolio/gaze-mental-representations/): Semantic content of event models

## Publications & Presentations

**In Preparation**:
- "Global vs. Incremental Updating of Event Models: Behavioral and Neural Evidence" (target: *Psychological Science*)
- "Hierarchical Event Model Updating: A Computational Framework" (target: *Cognitive Science*)

**Conference Presentations**:
- Subject matter exam: "Incremental vs. Global Updating in Event Cognition" (June 2024)
- Departmental talks: Fall 2023, Spring 2024

---

**Keywords**: Event Segmentation, Event Models, Incremental Updating, Global Updating, fMRI, Computational Modeling, Prediction Error, Hierarchical Representations, Dissertation
