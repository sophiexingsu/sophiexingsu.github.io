---
title: "Inferring Mental Representations from Gaze Using Vision-Language Models"
excerpt: "Using CLIP embeddings to decode the semantic content of mental models from eye-tracking data during naturalistic viewing"
collection: portfolio
permalink: /portfolio/gaze-mental-representations/
date: 2025-01-01
status: "Ongoing"

# Publications
publications:
  - title: "Vision–Language Model Derived Action Semantics Shape Gaze During Movie Viewing"
    venue: "VSS 2025"
    type: "poster"
    url: /files/VSS2025_Sophie_Su_CLIP_Gaze.pdf

# Technology Stack
tech_stack:
  languages: [Python]
  frameworks: [CLIP, PyTorch]
  tools: [Eye-tracking, Vision-Language Models, Deep Learning]

# Tags
tags: [CLIP, vision-language-models, eye-tracking, mental-representations, semantics, deep-learning]

# Layout Options
header:
  teaser: /files/projects/gaze-mental-representations.gif
---

## Research Question

{% include research-question.html question="Can we recover the *content* of people's mental models by analyzing where and when they look during naturalistic perception?" %}

## Overview

This project combines **high-frequency eye-tracking** with **vision-language model embeddings (CLIP)** to infer the semantic content of viewers' mental representations during naturalistic movie viewing. By analyzing how gaze patterns align with CLIP-derived semantic features, I test whether gaze is guided by high-level semantic representations or low-level visual features.

![Gaze heatmap overlayed on actor's performance](../files/output.gif)

## Theoretical Motivation

Traditional approaches to understanding visual attention focus on **low-level visual features** (contrast, motion, saliency). However, recent work suggests that gaze during naturalistic tasks is guided by:

- **Task goals** and action predictions
- **Semantic understanding** of the scene
- **Mental models** of "what is happening"

**Vision-language models** like CLIP learn joint embeddings of images and text, capturing semantic content. If gaze is semantically guided, then:

1. Gaze distributions should align with CLIP embeddings
2. Disrupting semantic structure (e.g., inverting frames) should reduce gaze prediction accuracy
3. CLIP embeddings should predict gaze better than low-level visual features

## CLIP: Vision-Language Models

### What is CLIP?

**CLIP** (Contrastive Language-Image Pre-training) is a neural network trained to:
- Map images and text descriptions into a shared embedding space
- Learn semantic relationships between visual and linguistic content
- Generalize to new images and descriptions without fine-tuning

### Why CLIP for Gaze Analysis?

CLIP embeddings capture:
- **Object identities** ("person", "cup", "table")
- **Action semantics** ("pouring", "reaching", "picking up")
- **Scene context** ("kitchen", "living room")

If viewers' gaze is guided by semantic understanding, CLIP embeddings should predict where people look.

## Methodology

### Experimental Design

**Stimuli**:
- Naturalistic movie clips showing everyday activities
- Two conditions:
  1. **Upright**: Normal viewing
  2. **Inverted**: Frames inverted 180° (preserves low-level features, disrupts semantics)

**Eye-Tracking**:
- High-frequency eye-tracking (500 Hz)
- Fixations aggregated into gaze density maps per frame

**CLIP Embedding Extraction**:
- Each video frame → CLIP image embedding (512-dimensional vector)
- Action descriptions (e.g., "person pouring water") → CLIP text embedding
- Compute cosine similarity between image and text embeddings

### Analysis Pipeline

#### 1. Gaze-CLIP Alignment

For each frame:
1. Extract CLIP image embedding `E_img`
2. Generate gaze density map `G(x, y)`
3. Extract CLIP embeddings for image patches at high-gaze locations
4. Compute alignment: Correlation between gaze density and CLIP embedding similarity to action labels

#### 2. Gaze Prediction Model

Train a model to predict gaze distributions from CLIP embeddings:

```
Gaze(x, y) = f(CLIP(frame), CLIP(action_label))
```

Compare prediction accuracy:
- **Upright condition**: Semantics intact
- **Inverted condition**: Semantics disrupted

#### 3. Semantic Disruption Analysis

Quantify semantic disruption by inversion:
- Compute CLIP text-image similarity for action descriptions
- Compare upright vs. inverted frames
- Expect: Lower similarity for inverted frames

### Python Implementation

Key analysis steps implemented in Python:

```python
import torch
import clip
from PIL import Image

# Load CLIP model
model, preprocess = clip.load("ViT-B/32", device="cuda")

# Extract image embedding
def get_clip_embedding(image_path):
    image = preprocess(Image.open(image_path)).unsqueeze(0).to("cuda")
    with torch.no_grad():
        image_features = model.encode_image(image)
    return image_features

# Compute text-image similarity
def compute_similarity(image_features, text_descriptions):
    text_tokens = clip.tokenize(text_descriptions).to("cuda")
    with torch.no_grad():
        text_features = model.encode_text(text_tokens)

    # Normalize features
    image_features = image_features / image_features.norm(dim=-1, keepdim=True)
    text_features = text_features / text_features.norm(dim=-1, keepdim=True)

    # Cosine similarity
    similarity = (image_features @ text_features.T).squeeze()
    return similarity
```

## Key Findings

### 1. Gaze is Semantically Guided

- Gaze distributions align with CLIP embeddings of action-relevant regions
- Alignment stronger than with low-level saliency models
- Effect holds across different movie types (cooking, social, object manipulation)

### 2. Inversion Disrupts Semantic Structure

- **Upright frames**: High CLIP text-image similarity for action descriptions
- **Inverted frames**: Lower similarity, despite identical low-level statistics
- Inversion preserves contrast, edges, motion energy but disrupts semantic content

### 3. Gaze Prediction Accuracy Drops for Inverted Scenes

- **Upright**: Gaze predicted with ~70% accuracy using CLIP embeddings
- **Inverted**: Accuracy drops to ~55% (chance ~50%)
- Low-level features (contrast, motion) do not show this difference

### 4. Individual Differences

- Viewers with higher semantic alignment show:
  - Better action prediction (predictive looking)
  - More consistent event segmentation
  - Stronger CLIP-gaze correlation

## Interpretation

These findings demonstrate that:

1. **Gaze is guided by high-level semantic representations**, not just visual salience
2. **CLIP embeddings capture the semantic content** that guides attention
3. **Semantic disruption** (via inversion) impairs gaze prediction, even with intact low-level features
4. **Mental models drive gaze**: Viewers look where their semantic understanding predicts relevant information

## VSS 2025 Poster

This work was presented at **Vision Sciences Society (VSS) 2025**:

**Vision–Language Model Derived Action Semantics Shape Gaze During Movie Viewing**

[Download Poster (PDF)](/files/VSS2025_Sophie_Su_CLIP_Gaze.pdf)

## Ongoing Extensions

### 1. Hierarchical Semantic Representations

Test whether gaze aligns with different levels of semantic abstraction:
- **Low-level**: Object features ("red", "round")
- **Mid-level**: Object categories ("cup", "hand")
- **High-level**: Actions and goals ("pouring", "preparing breakfast")

### 2. Event Structure and Hierarchy

Relate CLIP-based gaze analysis to event segmentation:
- Do semantic shifts in CLIP space predict event boundaries?
- Are event boundaries marked by semantic prediction errors?

### 3. Predictive Gaze Modeling

Extend to predict **future gaze** based on:
- Current CLIP embeddings
- Action context from previous frames
- Viewer-specific semantic biases

### 4. fMRI Integration

Relate CLIP embeddings to brain activity:
- Do CLIP embeddings predict activity in semantic processing regions (e.g., ventral temporal cortex)?
- Does gaze-CLIP alignment correlate with neural response patterns?

## Technical Details

### CLIP Model Variants Tested
- **ViT-B/32**: Standard vision transformer
- **RN50x16**: ResNet-50 with higher capacity
- **ViT-L/14**: Larger vision transformer

Best results with **ViT-B/32** (balance of accuracy and computational efficiency).

### Hyperparameters
- Embedding dimension: 512
- Frame sampling: 3 fps (sufficient for action semantics)
- Gaze aggregation window: 1 second
- Cosine similarity threshold: 0.3 for action alignment

## Related Projects

- [Predictive Looking](/portfolio/predictive-looking/): How gaze predictions fail at event boundaries
- [Gaze Entropy & Event Boundaries](/portfolio/gaze-entropy-event-boundaries/): Proactive gaze control before boundaries
- [Incremental vs. Global Updating](/portfolio/incremental-global-updating/): How mental models are updated

## Code Availability

Analysis code will be made available on GitHub upon publication.

---

**Keywords**: CLIP, Vision-Language Models, Eye-tracking, Mental Representations, Semantic Guidance, Deep Learning, Naturalistic Perception, Attention
