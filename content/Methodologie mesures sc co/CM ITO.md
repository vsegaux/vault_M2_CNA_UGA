---
prof: " ITO Takayuki"
date: 2025-10-10
publish: true
---
# Introduction

**Purpose**:
- *Descriptive*: Know how articulatory organs are moved
- *Functional*: How articulatory organs are controlled

**Challenges**:
- Multiple articulator organs, requiring specific measurement devices
- Most articulator organs are interior
- Measurements should not impair speech movement

Speech production : [[Physiologie de la production de la parole]] [[Consonnes et voyelles]]
Speech production study is usually made in the [[Modèle source-filtre]]

# Mesure des mouvements des articulateurs non visibles

The tongue is as *muscular hydrostat*, by opposition to most other muscles which aim to make bones move.
## Electromagnétométrie

ElectroMagnetic Midsagittal Articulometer (EM(M)A):
![[EMMA_liptongue.png]]

EMA uses *sensor coils* (~3mm) placed on the tongue and other parts of the mouth to measure *their position and movement over time* during speech and swallowing. (Three) *Induction coils around the head* produce an *electromagnetic field* (at different frequencies around 60kHz) that creates, or induces, a current in the sensors in the mouth. Because the *current induced* is inversely proportional to the cube of the distance, a computer is able to analyse the current produced and determine the sensor coil's location in space.
$$ i(t) = \frac{k*\phi(t)}{d^3}$$

Depending on the system used, head movement can be corrected in order to extracted just the tongue and other articulators movement.

Based on the measured current, the position of every sensor coil can be deduced and movement characterisics such as velocity and acceleration can then be computed for each articulatory organ.

> [!NOTE] TODO
> Get pictures from slides!

## Echographie - Ultrasound

Ultrasound pulses are sent and echo at tissues edges are then recorded and studied:
![[Echo_tongue.png]]

Transducer frequency effect (2-4MHz):
- Lower frequency has worth resolution
- Higher frequency has shorter range
Sampling frequency is about 28Hz, every 'impulse' is spaced by $\frac{1}{28}s$.

Results are analysed using:
- Contour Analysis and Visualization Technique (*CAVITE*) (ok...?).
- Speckle Tracking: comparing variations between successive images, alows tracking of specific movements.

This technique is used both in research and orthophonic applications.

This technique is affected by the following *limits*:
- *Bone* cast *shadows*
- Measurement is heavily dependent on *head movement*
	- This can be addressed by compensating for such movements (typically using IREDs LED to track head position)

## Endoscopie & Transillumination
## Electroglottographie - EEG
## Electropalatographie - EPG

# Mesures dynamiques
# Exemples de paradigmes expérimentaux