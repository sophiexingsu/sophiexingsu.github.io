---
title: "Structured Event Memory Model: A Computational Framework"
excerpt: "Python 3 + TensorFlow 2+ implementation of the SEM cognitive model for event memory research"
collection: portfolio
permalink: /portfolio/structured-event-memory-model/
date: 2022-01-01
status: "Published"

# GitHub Repository
github_repos:
  - name: SEM2
    url: https://github.com/sophiexingsu/SEM2
    description: "Python 3 port of SEM model updated to TensorFlow 2.3.1+"
    languages: [Python]

# Publications
publications:
  - title: "Structured Event Memory: A neuro-symbolic model of event cognition (Franklin et al., 2020)"
    venue: "Psychological Review"
    type: "paper"
    url: https://psycnet.apa.org/record/2020-15074-001

# Technology Stack
tech_stack:
  languages: [Python]
  frameworks: [TensorFlow]
  tools: [Google Colab, Neural Networks, Cognitive Modeling]

# Tags
tags: [computational-modeling, event-memory, neural-networks, tensorflow, cognitive-architecture, SEM]

# Layout Options
header:
  teaser: /files/projects/structured-event-memory-model.gif
---

## Overview

**SEM2** is a modernized Python 3 + TensorFlow 2+ implementation of the **Structured Event Memory (SEM)** model, a neuro-symbolic cognitive architecture for simulating how people organize and retrieve event memories.

This repository provides:
- Updated implementation compatible with TensorFlow 2.3.1+
- Google Colab tutorials for easy experimentation
- Extensible framework for event cognition research
- Documentation and examples for researchers

## What is the Structured Event Memory Model?

The **Structured Event Memory (SEM)** model, developed by Franklin et al. (2020), is a computational cognitive architecture that simulates:

1. **Event Segmentation**: How continuous experience is parsed into discrete events
2. **Memory Encoding**: How event representations are stored in long-term memory
3. **Memory Retrieval**: How events are retrieved based on cues
4. **Temporal Context**: How temporal relationships between events are encoded

### Key Features of SEM

**Neuro-Symbolic Architecture**:
- Combines neural network learning with symbolic structure
- Distributed representations + discrete event boundaries

**Hierarchical Organization**:
- Events organized hierarchically (sub-events within events)
- Captures nested structure of complex activities

**Temporal Context Model**:
- Gradually drifting context representation
- Captures temporal contiguity effects in memory

**Prediction-Based Segmentation**:
- Event boundaries triggered by prediction errors
- Aligns with Event Segmentation Theory

## Original SEM Model (Franklin et al., 2020)

The original SEM model demonstrated:

- **Event segmentation**: Model detects boundaries when prediction error increases
- **Boundary advantage**: Better memory for information at event boundaries
- **Temporal clustering**: Events closer in time are more confusable
- **Hierarchical recall**: Coarse event structure retrieved before fine details

**Publication**:
Franklin, N. T., Norman, K. A., Ranganath, C., Zacks, J. M., & Gershman, S. J. (2020). Structured Event Memory: A neuro-symbolic model of event cognition. *Psychological Review, 127*(3), 327-361.

## SEM2: Modernization Contributions

The original SEM implementation used TensorFlow 1.x, which is no longer supported. **SEM2** provides:

### 1. TensorFlow 2+ Compatibility
- Updated to TensorFlow 2.3.1+
- Uses modern TensorFlow API (no `tf.Session`, `tf.placeholder`)
- Eager execution by default
- Compatible with current Python 3.x versions

### 2. Improved Usability
- Modular code structure
- Clear documentation
- Google Colab tutorials (run in browser, no installation)
- Example datasets included

### 3. Extended Functionality
- Flexible input formats
- Visualization tools for model predictions
- Parameter sweeps for sensitivity analysis
- Integration with common neuroimaging data formats

## Model Architecture

### Core Components

#### 1. Event Segmentation Module
```python
class EventSegmenter:
    """
    Detects event boundaries based on prediction error

    Input: Sequence of feature vectors
    Output: Event boundary probabilities
    """
    def __init__(self, hidden_dim=128):
        self.lstm = LSTM(hidden_dim, return_sequences=True)
        self.predictor = Dense(input_dim)

    def segment(self, features):
        # Predict next feature
        predictions = self.lstm(features)
        # Compute prediction error
        error = compute_error(predictions, features)
        # Threshold for boundaries
        boundaries = error > threshold
        return boundaries
```

#### 2. Memory Encoding Module
```python
class MemoryEncoder:
    """
    Encodes event representations into long-term memory

    Combines:
    - Content features (what happened)
    - Temporal context (when it happened)
    """
    def encode_event(self, features, context):
        event_rep = self.content_encoder(features)
        temporal_rep = self.context_encoder(context)
        return concatenate([event_rep, temporal_rep])
```

#### 3. Temporal Context Module
```python
class TemporalContext:
    """
    Gradually drifting context representation

    Models temporal contiguity:
    - Context changes slowly over time
    - Rapid change at event boundaries
    """
    def __init__(self, context_dim=64, drift_rate=0.1):
        self.context = np.random.randn(context_dim)
        self.drift_rate = drift_rate

    def update(self, event_boundary=False):
        if event_boundary:
            # Large context shift at boundaries
            self.context += np.random.randn(len(self.context)) * 0.5
        else:
            # Gradual drift
            self.context += np.random.randn(len(self.context)) * self.drift_rate
```

#### 4. Memory Retrieval Module
```python
class MemoryRetriever:
    """
    Retrieves events based on cues

    Uses attention mechanism over stored events
    """
    def retrieve(self, cue, memory_store):
        # Compute similarity between cue and stored events
        similarities = cosine_similarity(cue, memory_store)
        # Retrieve most similar events
        retrieved_events = memory_store[similarities > threshold]
        return retrieved_events
```

## Applications in Research

### 1. Modeling Event Segmentation Data

Fit SEM to human segmentation data:
- Predict boundary locations from feature sequences
- Compare model vs. human segmentation agreement
- Identify features driving segmentation

### 2. Simulating Memory Experiments

Simulate classic memory phenomena:
- **Boundary advantage**: Better memory at event boundaries
- **Temporal clustering**: Confusions for temporally proximate events
- **Hierarchical effects**: Coarse-to-fine recall

### 3. Testing Cognitive Theories

Test competing theories:
- **Incremental vs. global updating**: Modify context update rules
- **Predictive processing**: Vary prediction error sensitivity
- **Hierarchical structure**: Add multiple temporal scales

## Google Colab Tutorials

The SEM2 repository includes interactive Colab notebooks:

### Tutorial 1: Basic Event Segmentation
- Load example data
- Run segmentation
- Visualize predicted boundaries vs. ground truth

### Tutorial 2: Memory Encoding and Retrieval
- Simulate event memory encoding
- Test cued recall
- Analyze temporal clustering effects

### Tutorial 3: Parameter Sensitivity
- Sweep key parameters (drift rate, boundary threshold)
- Plot model behavior
- Identify optimal parameter ranges

### Tutorial 4: Custom Applications
- Load your own data
- Customize model architecture
- Export predictions for further analysis

**Access Tutorials**: [SEM2 Colab Notebooks](https://github.com/sophiexingsu/SEM2/tree/main/tutorials)

## Installation and Usage

### Quick Start (Google Colab)

No installation required! Open a Colab notebook and run:

```python
# Clone repository
!git clone https://github.com/sophiexingsu/SEM2.git
%cd SEM2

# Install dependencies
!pip install -r requirements.txt

# Run example
from sem2 import EventSegmenter
segmenter = EventSegmenter()
boundaries = segmenter.segment(features)
```

### Local Installation

```bash
# Clone repository
git clone https://github.com/sophiexingsu/SEM2.git
cd SEM2

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

## Repository Structure

```
SEM2/
├── sem2/
│   ├── __init__.py
│   ├── segmentation.py      # Event segmentation module
│   ├── memory.py             # Memory encoding/retrieval
│   ├── context.py            # Temporal context model
│   ├── utils.py              # Helper functions
│   └── visualization.py      # Plotting functions
├── tutorials/
│   ├── 01_basic_segmentation.ipynb
│   ├── 02_memory_simulation.ipynb
│   ├── 03_parameter_sweep.ipynb
│   └── 04_custom_application.ipynb
├── examples/
│   ├── example_data/         # Sample datasets
│   └── example_scripts/      # Example usage scripts
├── tests/
│   └── test_*.py             # Unit tests
├── requirements.txt
├── README.md
└── LICENSE
```

## Citation

If you use SEM2 in your research, please cite:

**Original SEM Model**:
```
Franklin, N. T., Norman, K. A., Ranganath, C., Zacks, J. M., & Gershman, S. J. (2020).
Structured Event Memory: A neuro-symbolic model of event cognition.
Psychological Review, 127(3), 327-361.
```

**SEM2 Implementation**:
```
Su, S. (2022). SEM2: Python 3 + TensorFlow 2+ implementation of Structured Event Memory.
GitHub: https://github.com/sophiexingsu/SEM2
```

## Related Projects

- [Incremental vs. Global Updating](/portfolio/incremental-global-updating/): Testing updating dynamics in event models
- [Gaze Entropy & Event Boundaries](/portfolio/gaze-entropy-event-boundaries/): Empirical event segmentation research
- [Predictive Looking](/portfolio/predictive-looking/): Prediction errors and event boundaries

## Contributions Welcome

SEM2 is an open-source project. Contributions are welcome:

- Bug fixes and improvements
- New tutorials and examples
- Extensions to the model architecture
- Documentation improvements

See [Contributing Guidelines](https://github.com/sophiexingsu/SEM2/blob/main/CONTRIBUTING.md)

---

**Keywords**: Computational Modeling, Event Memory, Neural Networks, TensorFlow, Cognitive Architecture, Event Segmentation, Temporal Context, Neuro-Symbolic Models, Python, SEM
