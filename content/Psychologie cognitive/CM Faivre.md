---
prof: FAIVRE Nathan
date: 2025-10-07
publish: true
---
# The Problem of Consciousness

- **Mind/Body Problem (Descartes)** — Dualism: How can we connect subjective conscious experience to its biological substrates? How does something physical (the brain) give rise to something mental (the mind)?
    
- **Functional Question (T. Huxley)** — What is the _function_ of consciousness? Can it be studied as we study other cognitive functions like vision or hearing?
    
- **Intimacy and Subjectivity (T. Nagel)** — Even if we fully understand the biological mechanisms of consciousness, we can never access _what it feels like_ to be another being (“What is it like to be a bat?”).
    

# Defining Consciousness

> “By _consciousness_ I mean those states of sentience or awareness that typically begin when we wake up in the morning from a dreamless sleep and continue throughout the day until we fall asleep again. Other ways in which consciousness can cease are death, coma, or other forms of unconsciousness.”  
> — _John Searle (1993)_

![[conscience_bidim.png]]

Consciousness thus refers to the continuous stream of subjective experiences — sensations, thoughts, and awareness — that mark our waking life.


# Neural Correlates of Consciousness (NCC)

> “The minimal neuronal mechanisms jointly sufficient for any one specific conscious percept.”  
> — _Crick & Koch, 1990_

The search for the NCC aims to identify the **brain processes that are necessary and sufficient for a specific conscious experience**.

### The Contrastive Approach

![[consicen.png]]


This empirical method compares brain activity between conditions in which the same stimulus is consciously perceived versus when it is not.

- A visual stimulus is presented repeatedly.
    
- Some trials lead to conscious perception (_the subject reports seeing it_), others do not (_the subject is unaware_).
    
- By comparing neural activity between these two conditions, researchers infer the brain regions specifically involved in _conscious awareness_, not just perception.
    

## Detection and Conscious Contents

![[consciHIT_rej.png]]

To isolate neural correlates of _conscious content_, researchers often compare **hits** (correct detection of a stimulus) vs. **misses** (stimulus presented but not detected).  
Because the visual input is identical in both cases, any difference in brain activity can be attributed to _conscious access_.

![[amorceconscienc.png]]

**Priming experiments** also provide insights into unconscious processing.  
Even when participants are unaware of a _prime_ (e.g., a briefly flashed word), their response times to a related stimulus are influenced — demonstrating that unconscious information still affects behavior.

### Confounding Factors

Asking participants to _report_ their perception recruits additional brain areas (especially prefrontal regions).  
To isolate the true correlates of conscious perception, **no-report paradigms** are used — where consciousness is inferred from behavior or physiological markers rather than explicit verbal reports.

![[inferring_region.png]]

Findings show that **the prefrontal cortex is less involved** when no explicit report is required, suggesting that some prefrontal activations may reflect reporting processes, not consciousness itself.

# Theories of Consciousness

> **Disclaimer:** Only a few neuroscientific theories are covered here (excluding quantum, dualist, or spiritualist accounts).

There is currently **no consensus** on a unified theory of consciousness. However, a good theory should:

- Explain empirical findings (e.g., why the cerebellum is not involved in conscious experience, why consciousness fades during sleep).
    
- Make **testable predictions** about when and where consciousness arises.
    
- Be **falsifiable**.
    

**The “easy” problem:** How is sensory information processed and reported?  
**The “hard” problem:** Why and how do physical processes give rise to subjective experience?

Main candidate theories:

- **Recurrent Processing Theory (RPT)**
    
- **Global Neuronal Workspace (GNW)**
    
- **Higher-Order Theory (HOT)**
    
- **Integrated Information Theory (IIT)**
    

## Recurrent Processing Theory (RPT)

![[recprocthe.png]]

According to RPT, consciousness emerges from **local recurrent feedback loops** within sensory areas.

- **Stage (a): Feedforward sweep** — Information flows from lower to higher visual areas (V1 → V4 → IT), but the experience is _not yet conscious_.
    
- **Stage (b): Local recurrent activity** — Feedback connections between areas (V2, V4, TE) create a sustained network activity that gives rise to _conscious perception_.
    
- **Stage (c): Widespread recurrence** — The conscious content becomes _reportable_ and accessible to other brain systems.
    

## Global Neuronal Workspace (GNW)

In contrast, GNW emphasizes **global broadcasting** of information.  
Here, consciousness arises when information is _amplified and shared_ across widespread cortical networks — especially involving the **prefrontal cortex** and **parietal regions**.

Thus, while RPT sees consciousness as local feedback, GNW attributes it to **global accessibility** and **integration**.


## Higher-Order Theory (HOT)

Not covered in class.

## Integrated Information Theory (IIT)

Not covered in class.

## Summary of Theories

**Formal Criticisms**

- _Small network & panpsychism_: Even minimal systems could be considered conscious — leading to overly broad implications.
    
- _Unfolding argument_: (Not covered)
    
- _Generalizability_: Many theories are human-centric and may not extend to other species or artificial systems.
    

**Common Pitfalls**

- Mixing explanatory levels (physiology vs. phenomenology).
    
- Ambiguous or unfalsifiable predictions.
    
- Overreliance on post-hoc interpretations.
    
- Need for more diagnostic, causal evidence.
    

# Perceptual Consciousness and Metacognition

**Metacognition** — “A set of capabilities allowing one cognitive system to evaluate or monitor another cognitive system.”  
(_Adapted from Proust, 2013_)

It is the ability to think about and evaluate one’s own mental processes.

- **Prospective metacognition:** Future-oriented (“Will I perform well in this task?”)
    
- **Retrospective metacognition:** Past-oriented (“Did I answer correctly?”)
    

## The Dunning–Kruger Effect

![[dunningKruger.png]]

The Dunning–Kruger effect describes the tendency for people with low skill to overestimate their ability, while highly skilled individuals may underestimate theirs.  
Recent research has nuanced or challenged the strength of this effect, showing that it may be partially due to statistical artifacts.

## Confidence Judgments

![[conf_judg_exp.png]]

In a typical experiment:

- The participant sees two briefly presented images and must decide which is brighter.
    
- Then, they rate their _confidence_ in that decision.
    
- **Type 1 performance:** Objective decision accuracy (which image was brighter).
    
- **Type 2 performance:** Confidence judgment (how sure the participant was).
    

### Functional Correlates of Confidence

Neural activity correlating with confidence involves:

- **Lateral prefrontal cortex**
    
- **Posterior parietal cortex**
    
- **Dorsal anterior cingulate cortex**
    

![[functionnal_correlates_conf.png]]

These regions are thought to contribute to self-monitoring and error evaluation.


### Metacognitive Sensitivity

**Definition:** The ability to align one’s confidence with one’s actual performance — being confident when right, uncertain when wrong.

- **Metacognitive sensitivity** — how well confidence tracks accuracy.
    
- **Confidence bias** — overall tendency to be more or less confident, regardless of correctness.
    

![[sensivity_measures.png]]

**Common measures:**

- Logistic regression models.
    
- AUC (_Area Under the ROC Curve_), capturing how well confidence discriminates correct from incorrect trials.
    

### Influence of Physical Intensity and Perceptual Noise

Type 1 performance is usually **kept around 75% accuracy** for all subjects, so confidence can be assessed independently of task difficulty.

![[type1_perf_adjust.png]]

**Perceptual noise** can come from:

- _Internal sources_ (fatigue, attention, expectation)
    
- _External sources_ (lighting, glasses, ambient noise)
    

This noise makes perception unstable across trials (even for a given, fixed stimulus):

![[perceptualNoise_onconfidence.png]]

By controlling for Type 1 performance, researchers can isolate _metacognitive sensitivity_:

![[sensivity_evaluated_config.png]]

Greater metacognitive sensitivity correlates positively with **gray matter volume** in the anterior prefrontal cortex.

### Metacognitive Noise

![[model_of_metacognition_full.png]]

Metacognitive noise arises from two main sources:

1. **Noise in the confidence signal** — The same perceptual data used to make the decision is also used to estimate confidence, but it decays quickly and introduces errors (signal decay).
    
2. **Noise in confidence computation** — Decision thresholds fluctuate due to tension, fatigue, or motivation (criterion jitter).
    
3. **Non-random confidence distortions** — Factors that bias confidence without affecting accuracy:
    
    - _Confidence leaks_ (carryover effects from previous trials)
        
    - _Positive evidence bias_ (expectations increase confidence)
        

> [!NOTE] **Exam**  
> **Important concepts:**
> 
> - **Confidence judgments:**
>     
>     - Difference between _Type 1_ (decision) and _Type 2_ (confidence).
>         
> - **Metacognitive sensitivity:**
>     
>     - Distinction between _bias_ and _sensitivity_.
>         
>     - Methods of measurement (confidence gap, AUC).
>         
> - **Model of metacognition:**
>     
>     - Shared perceptual representation underlying both decision and confidence.
>         
>     - Role of _perceptual noise_ vs. _metacognitive noise_.
>         
>     - _Influence of Type 1 performance_ on metacognitive evaluation.
>         


## Metacognition and Motor Signals

A 2015 TMS study showed that disrupting the **premotor cortex** decreases the _accuracy of confidence judgments_ without affecting Type 1 performance.

![[motor_metacog.png]]

This suggests that **motor signals** contribute to metacognitive evaluation — possibly through monitoring the ease or fluency of action execution.

## Animal Metacognition

Animals can exhibit behaviors interpreted as _metacognitive_, though the interpretation is debated.

### Opt-Out Task

![[animal_metacog.png]]

- Animals (e.g., rats) learn to discriminate between two odors, A and B.
    
- When presented with an uncertain odor, they can “opt out” or hesitate.
    
- **Confidence** is inferred from how long they persist in choosing an odor.
    
    - Longer persistence → higher confidence.
        
    - Neural data show differences in orbitofrontal cortex activity between correct and incorrect trials — but only when the animal is confident.
        

Similar paradigms with toddlers show that they also hesitate more when uncertain, suggesting an early form of metacognitive monitoring, event before learning the language.

## Theories Linking Consciousness and Metacognition

![[theoriesofconsciousness.png]]

|Theory|Core Idea|Relation to Metacognition|
|---|---|---|
|**Higher-Order Theory**|A mental state becomes conscious only when a higher-order thought represents it.|Metacognition _is_ consciousness itself.|
|**Global Workspace Theory**|Consciousness arises from globally broadcast information.|Metacognition requires access to this global workspace — stable, accessible information = confidence.|
|**Recurrent Processing Theory**|Consciousness arises from local feedback loops.|Metacognition monitors the stability of these loops — it reflects how stable and consistent the perceptual representation is.|

This also echoes the distinction between:

- **A-consciousness** (accessible consciousness): information that can be reported and used.
    
- **P-consciousness** (phenomenal consciousness): the raw subjective experience.
    

> [!NOTE] **Exam**  
> **Important concepts:**
> 
> - **Influence of motor signals:**
>     
>     - TMS over premotor cortex disrupts metacognitive accuracy.
>         
> - **Animal metacognition:**
>     
>     - Opt-out tasks and their interpretation (are they truly Type 2 judgments?).
>         
> - **Link between metacognition and consciousness:**
>     
>     - Shared neural markers and functional similarities.
>         
>     - Theories explaining their overlap.
>         
