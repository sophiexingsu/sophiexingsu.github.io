---
title: 'Attractor and Integrator Networks in the Brain'
date: 2024-02-04
permalink: /posts/2024/02/blog-post-6/
tags:
- memory
- neuroscience
---


## Attractor and Integrator Networks in the Brain

To comprehend the concept of an attractor, we must first delineate a dynamical system and its various states. A dynamical system comprises a set of variables coupled with the rules that govern their evolution over time. An exemplary instance of an attractor is a stable fixed point, where all neighboring states converge towards it. Attractors manifest in diverse forms: they can be a solitary state, a collection of discrete sets, or a continuum of states behaving as a unified set.

The underlying principle behind the formation of non-trivial attractor states in neural circuits is strong recurrent positive feedback. This feedback mechanism counters activity decay, thereby stabilizing certain states, and is posited to underpin the stabilization of memory traces and persistent activity in the brain. A notable illustration of discrete attractors at user-defined points is the Hopfield model. Here, neural activation patterns are inscribed into the network's weights through a Hebbian-like learning rule, promoting excitatory interactions among co-active neurons and inhibiting the rest. When a sufficiently small number of patterns are learned, they can be retrieved from partial or corrupted versions of the stored states, enabling the network to encapsulate these contextual memories. Thus, memories are represented as distinct weight combinations within an attractor network.

The formation of stationary continuous attractors is principally driven by pattern formation. Simple, spatially localized competitive interactions across the neural sheet culminate in the emergence of spatially structured, stable activity patterns. This process, known as linear tuning instability, involves neurons with excitatory coupling becoming co-active and suppressing their neighbors through inhibition.

Theoretically, a system could be finely tuned so that every point in state space becomes a naturally stable attractor, endowing the system with maximally high-dimensional attractor dynamics. For instance, in representational memory, representing a set of inputs involves assigning inputs to representational states (not necessarily on a one-to-one basis) while ensuring the consistent retrievability of those states ("labels") when prompted. Attractor networks provide a stable set of internal states that can reliably represent discrete or continuous variables by mapping external states to corresponding attractor states. This can be achieved through a feedforward learning process that associates each external state with an internal attractor state.

Attractor networks can manifest two types of memory. The first resides in the structure of the weights, delineating the set of all possible attractors. When these weights are defined through an input-driven learning process, it constitutes a form of long-term memory about the inputs. However, this conceptualization challenges prevailing assumptions about the formation of long-term memory. The second type of memory pertains to the capacity to maintain persistent activity in stationary attractor states. If a system with multiple stationary attractor states is initialized in one of them, it tends to persist in or near that state for an extended period. This enduring activity response, representing a form of short-term memory, signifies the input that initiated the circuitry.