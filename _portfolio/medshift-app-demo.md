---
title: "MedShift: Research-Based Medication Memory App"
excerpt: "A UX demo applying EMRC theory from cognitive neuroscience to help patients remember medication changes"
collection: portfolio
permalink: /portfolio/medshift-app-demo/
date: 2025-01-20
status: "Concept Demo"
category: "other"

# Technology Stack
tech_stack:
  languages: [JavaScript, HTML, CSS]
  frameworks: [Vanilla JS]
  tools: [UX Design, Interactive Demo, Cognitive Science Translation]

# Tags
tags: [applied-research, UX-design, EMRC-theory, medication-adherence, memory-updating, translational-science]

# Layout Options
header:
  teaser: /files/projects/medshift-demo.png
---

## Research-to-Application Translation

{% include research-question.html question="How can findings from cognitive neuroscience research on memory updating be translated into practical tools that help people in everyday life?" %}

## Overview

**MedShift** is a concept app demonstrating how cognitive neuroscience research can be translated into practical health tools. The app applies **Event Memory Retrieval and Comparison (EMRC) theory** to address a common problem: patients forgetting medication changes and accidentally taking old medications.

This interactive demo showcases the core UX flow, explaining the cognitive science principles at each step.

## The Problem

When medications change, patients often:
- Forget they switched medications
- Take the old medication by mistake
- Can't remember which medication is current
- Experience confusion at the pharmacy

Traditional reminder apps simply notify patients to take medication—they don't address the underlying **memory interference** problem.

## The Science: EMRC Theory

MedShift is based on **Event Memory Retrieval and Comparison (EMRC) theory** (Wahlheim & Zacks, 2024, *Trends in Cognitive Sciences*), which describes how the brain naturally updates memories:

### Key Principles

1. **Retrieval**: Actively recalling old information before encountering new information
2. **Prediction**: Generating expectations based on past experience
3. **Prediction Error**: Detecting mismatches between expectation and reality
4. **Integration**: Encoding the full change sequence into a "recursive representation"

### Why This Matters

Research shows that when people encode **both the old and new information together with an explicit change marker**, memory interference is reduced. The old memory actually *helps* rather than *hurts* recall of the new information—a phenomenon called **proactive facilitation**.

## The MedShift Solution

MedShift guides users through a 4-step process based on EMRC principles:

### Step 1: Pre-Retrieval
Before taking the new medication, the app prompts users to actively recall their old medication routine.

### Step 2: Prediction Generation
Users confirm what they *expect* to take based on their old routine.

### Step 3: Prediction Error Alert
The app explicitly highlights the change—creating a clear prediction error signal.

### Step 4: Recursive Encoding
Users encode the complete change narrative: "I used to take X, but now I take Y because Z."

## Demo Walkthrough

The interactive demo follows **Sarah**, a 68-year-old patient whose doctor changed her diabetes medication from a blue pill (Metformin 500mg) to a white pill (Metformin XR 750mg).

### Key Screens

**Morning Reminder** → **Old Medication Retrieval** → **Prediction Confirmation** → **Change Alert** → **Memory Encoding** → **Memory Test (1 week later)**

Each screen includes a "Memory Science" explanation box showing how that step relates to cognitive neuroscience research.

## Design Philosophy

### 1. Evidence-Based Intervention
Every UX decision is grounded in published cognitive science research, not intuition.

### 2. Transparent Science Communication
Users see *why* each step matters through embedded "Memory Science" explanations.

### 3. Active Engagement
Rather than passive reminders, the app requires active cognitive engagement with the change.

### 4. Complete Memory Encoding
The app ensures users encode the full change narrative, not just the new information.

## Research Foundation

**Primary Theory**:
- Wahlheim, C. N., & Zacks, J. M. (2024). Memory updating and the structure of event representations. *Trends in Cognitive Sciences*.

**Supporting Research**:
- Work on proactive interference and facilitation
- Event segmentation and memory encoding
- Prediction error in learning and memory

## Broader Implications

This demo illustrates how cognitive neuroscience research can be translated into:

- **Health technology**: Medication adherence, habit change, behavior modification
- **Education**: Helping students update misconceptions
- **Training**: Professional skill updating (e.g., medical protocols, safety procedures)
- **Therapy**: Cognitive restructuring interventions

## Technical Implementation

The demo is built as a lightweight, interactive prototype:

- Pure HTML/CSS/JavaScript (no dependencies)
- Mobile-responsive design
- 13-screen interactive walkthrough
- Embedded science explanations at each step

## Try the Demo

<a href="/files/projects/medshift-demo/" class="btn btn--primary btn--large" target="_blank">Launch Interactive Demo</a>

## Future Directions

This concept could be extended to:

1. **Validated clinical trials** testing efficacy vs. standard reminder apps
2. **Generalization** to other memory updating contexts (address changes, password updates, routine changes)
3. **Personalization** based on individual memory updating patterns
4. **Integration** with healthcare systems and prescription databases

---

**Keywords**: Applied Cognitive Science, EMRC Theory, Medication Adherence, UX Design, Memory Updating, Translational Research, Health Technology
