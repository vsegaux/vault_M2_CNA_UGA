---
prof: FAIVRE Nathan
date: 2025-10-07
publish: true
---
# Le problème de la conscience
- *Mind/Body* (Descartes): Dualisme; comment faire le lien entre la conscience et ses substrats biologiques?
- *Fonctions* (T. Huxley): Quel est la fonction de la conscience? Comment pourrait on l'étudier comme on étudie une autre 'fonction' comme la vision, l'audition..?
- *Intimacy and subjectivity* (T. Nagel): Même en comprenant parfaitement les substrats biologiques, on ne pourrait pas faire l'expérience subjective d'autres individus/être vivants.

 
# Comment définir la conscience?
 By "consciousness" I mean those states of sentience or awareness that typically begin when we wake up in the morning from a dreamless sleep and continue throughout the day until we fall asleep again. Other ways in which consciousness can cease is if we die, go into a coma, or otherwise become unconscious. (John Searle, 1993)

![[conscience_bidim.png]]

# Neural correlates of consciousness (NCC)

"The minimal neuronal mechanisms jointly sufficient for any one specific conscious percept (Crick & Koch, 1990)"

Premier tests empiriques de la conscience:
![[consicen.png]]
**Approche contrastive**: on montre une image à un patient et on regarde quels sont les neurones qui sont activés. On fait alors varier les conditions afin d'estimer (toujours en présentant l'image), quelles conditions donnent lieu à une vision consciente (la personne voit, et le perçoit) VS quelles conditions n'y donnent pas lieu (vision non consciente).

## Detection and conscious contents

![[consciHIT_rej.png]]
Si on s'intéresse au contenu de conscience, on comparera l'activité cérébrale pendant les *hit* avec celle pendant les *miss* (donc à stimuli visuels constants, ce qui se rapproche de l'approche contrastive ci-cessus).

Les expériences basées sur le phénomène d'amorce permettent aussi des progrès sur la conscience:
![[amorceconscienc.png]]
L'amorce présentée a un effet sur la vitesse de réponse, malgré que le sujet n'en ai pas conscience (50% de performance de détection de l'amorce ~ hasard).


### Confounding factors

Le fait de demander aux sujets de rapporter les stimuli implique des zones cérébrales particulière, certaines tâches/mesures permettent de ne pas avoir à demander aux sujets de rapporter leurs perceptions, on peut alors discriminer des zones particulières qui entrent en jeux dans la détection consciente (mais pas dans le rapport):
![[inferring_region.png]]
On s'aperçoit en particulier que le lobe préfrontal ne semble plus être impliqué si l'on ne demande pas de rapport.

# Théories de la conscience
- Disclaimer: we only cover a small subset of neuroscientific theories (no quantum physics, dualism, spiritualism, etc.) 
- No consensus as the field is relatively young 
- Goals for a theory of consciousness: 
	- explain empirical data (why cerebellum not involved, why fades out at night, etc.) 
	- make predictions (x is conscious, y is unconscious) 
	- falsifiable (if data shows x, then T is false) 
- Easy problem: how a stimulus becomes reportable Hard problem: how and why physical processes give rise to experience
- Selected candidates:
	- Recurrent Processing Theory (RPT)
	- Global Neuronal Workspace (GNW)
	- Higher Order Theory (HOT)
	- Integrated Information Theory (IIT)

## Recurrent processing theory

![[recprocthe.png]]
Pendant l'étape (a): le feedforward sweep, aucun rapport conscient n'est fait. Pendant la phase (b), il y a rétro-action des aires visuelles V2,V4 et TE; ce serait ces activités qui permettrait la conscience visuelle des stimuli. Finalement, cette conscience serait rapportable seulement plus tard, pendant l'étape (c): widespread recurrent processing.

## Global neuronal workspace

En opposition à la théorie précédente, ici, c'est justement l'implication du lobe  préfrontale qui est à l'origine de la conscience.

## Higher order theory
Non traitée en cours
## Integrated information theory
Non traitée en cours

## Sommaire des théories
**Formal criticisms**
- Small network & panpsychism: des systèmes minimaux suffisent
- Unfolding argument: Non traité en cours
- Generalizability to other systems: Théorie pensées pour les humains, non applicable à la conscience en général.
**Common pitfalls** 
- Distinct levels of explanation and unclear predictions 
- Most empirical studies report positive evidence (post-hoc?)
- Need for more diagnostic empirical evidence

# Perceptual consciousness and metacognition

**Metacognition**: "A set of capabilities thanks to which a cognitive system is evaluated by an other cognitive system." (Adapted from Proust, 2013)
- Prospective metacognition: 'Future oriented', 'Will i perform in this tournament?'
- Retrospective metacognition: Passed oriented, Did i answer correctly..?

**Dunning-Kruger effect**:
![[dunningKruger.png]]
Tendency for people with less knowledge/skill to feel more confident than people with better knowledge/skill. This effect was debunked in a recent study, as shown on the graph on the right, in the above picture.

## Confidence judgments
**Experience**:
Subject is shown 2 images for a short period of time, and has to determine which is the brightest, then tell how confident he is about his response.
![[conf_judg_exp.png]]
*Type 1* performance is about the luminance *decision*.
*Type 2* performance is about the *confidence*.

### Functional correlates of confidence
Correlation with lateral prefrontal cortex, posterior parietal cortex and dorsal anterior cingulate cortex:
![[functionnal_correlates_conf.png]]

### Metacognitive sensivity

**Metacognitive sensivity**: Ability to adapt one’s confidence to one’s type 1 performance (being confident about right answers and less so about wrong answers).
**Confidence bias**: Overall level of confidence, no matter if one is right or wrong.

![[sensivity_measures.png]]
How do measure metacognitive sensivity:
- logistic regression
- AUC (area under curve)

### Influence of physical intensity
Type 1 performance is controlled to be around 75% accuracy so that confidence can be assessed properly. Stimuli are adapted accordingly (so that the brightness can be recognized in the previous example), the procedure is given in the following figure (this is made for each subject, so they all have around 75% accuracy in the end):
![[type1_perf_adjust.png]]

*Perceptual noise*: Can be caused internally (fatigue, attention, ...) or externally (ambiant light, glasses, ...). Causes subject to percieve a same stimulus differently over the trials:
![[perceptualNoise_onconfidence.png]]

Type 1 performance control allows to reduce the perceptual noise, in the end, subject have the same Type 1 performance, and their metacognitive sensivity can be evaluated:
![[sensivity_evaluated_config.png]]

Further studies have shown that metacognitive sensivity is positively correlated to grey matter volume.

**Metacognitive noise**:
-  Noise in the signal for confidence: the data used by the brain to give a confidence value is the exact same data that is perceived and used to give a decision. It tends to get mixed up and decay quickly, leading to less accurate confidence.
	- E.g. Signal decay / metacognitive noise 
- Noise in the confidence computation: thresholds to take confidence decision tend to constantly evolve (due to tension, fatigue etc...) and lead to varying confidence judgments.
	- E.g. Criterion jitter 
- Non-random factors affecting confidence but not accuracy: 
	- Confidence leaks
	- Positive evidence bias: confidence is boosted greatly by expectations

![[model_of_metacognition_full.png]]

> [!NOTE] Examen
> Important concepts:
> - Confidence judgments: 
> 	- Type 1 vs. type 2 (responses/judgements vs. performance) 
> - Metacognitive sensitivity 
> 	- *Bias vs. sensitivity*. 
> 	- Definition of metacognitive sensitivity 
> 	- Example methods: Confidence gap and AUC 
> - A model of metacognition
> 	- A perceptual representation at the origin of decisions AND confidence. 
> 	- Perceptual vs. metacognitive noise 
> 	- *The influence of type 1 performance*

## Metacognition and motor signals

2015 study: distrubing pre-motor cortex (using TMS: Transcranial Magnetic Stimulation) leads to less confidence accuracy without affecting type 1 performance:
![[motor_metacog.png]]

## Schizophrenia
**SKIPPED???**
![[Schizophrenia_metacog.png]]

## Animal metacognition
***Opt-out task***: Animals are exposed to two different smells A and B at two different sources.
Then, they are presented and odour and, in order to get some food, they are supposed to go to the odour A or B source and stay there. Their confidence is measured implicitly as how long they stay with the A or B odour source. Supposedly they stay longer if they're sure, results are shown in the following figure:

![[animal_metacog.png]]

When the animal (rat) stays in place longer, there are differences in the neuronal activity of the obritofrontal cortex (which is much higher in a case of error). When the rat is unsure, such difference in neuronal activity between error and correct is not observed.

A visual search task was used on 12month old toddlers. Similarly to rats, they would stay with their arm drawn on their confidence position and hesitate more otherwise.


## Theories of consciousness

![[theoriesofconsciousness.png]]

*Higher order theory*: A mental state becomes conscious only when a higher order system forms the thought. *Metago IS consciosness*
*Global workspace theory*: Consciousness emerges when information is boradcasted globally; to make metacognitive judgment, the brain needs to access to the information globally. => Stable+accessible information = confidence. *Metacog depends on consciousness*
*recurrent processing theory*: Consciousness raises from local feedback loops. Metacognitive judgment rely on stability of those loops. *Metacog monitors consciousness*.

(division between A consciosness (accessible) and P conscioucness (phenomenological))

> [!NOTE] Examen
> Important concepts:
> - Influence of motor signals 
> 	- TMS over premotor cortex influence metacognition 
> - Animal metacognition? 
> 	- Opt-out tasks 
> 	- Is it really type 2? 
> - Link to consciousness
> 	- Shared markers -> Between metacognition and consciousness
> 	- Theories of consciousness
