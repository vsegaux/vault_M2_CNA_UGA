---
prof: " ITO Takayuki"
date: 2025-10-10
publish: true
---
> [!NOTE] Exam  
> **Needed knowledge:**
> 
> - Which technique is used to study which organ.
>     
> - The specificities, limitations, and advantages of each technique.
>     

# Introduction

The study of **articulatory movements** aims to understand both the **anatomical description** and the **functional control** of the organs involved in speech production.

## Objectives

- **Descriptive:** to understand _how_ articulatory organs (tongue, lips, soft palate, vocal folds, etc.) move.
    
- **Functional:** to understand _how_ these movements are controlled and coordinated by the nervous system.
    

## Experimental challenges

- Articulators are **numerous**, each requiring specific measuring devices.
    
- Many are **internal** (e.g., tongue, larynx), making them difficult to access directly.
    
- Measurement systems must **minimize interference** so as not to alter natural speech movements.
    

# Measuring movements of non-visible articulators

Unlike most skeletal muscles, the tongue is a **muscular hydrostat**: it deforms without a rigid skeletal structure, making its movement particularly complex to measure.

## Electromagnetic Articulography (EMA / EMMA)

![[EMMA_liptongue.png]]

### Principle

The **ElectroMagnetic Midsagittal Articulometer (EMA)** uses small **sensor coils** (≈3 mm) placed on different points of the tongue, lips, and palate.  
Around the head, **induction coils** produce an **electromagnetic field** at multiple frequencies (around 60 kHz).  
The induced current in each sensor depends on its distance from the transmitter coil, following:

$$ i(t) = \frac{k \times \phi(t)}{d^3} $$

A computer then deduces the **3D position** of each sensor and can compute **velocity** and **acceleration** of the articulators.

### Advantages

- Excellent **spatial and temporal precision** (continuous measurements).
    
- Allows full **articulatory trajectory tracking**.
    
- Can be combined with **head-tracking** systems to correct for unwanted motion.
    

### Limitations

- **Invasive** setup: sensors placed inside the mouth.
    
- Expensive and requires precise calibration.
    

### Studied organs

- **Tongue**
    
- Lips
    
- Jaw
    

### Applications

- **Articulatory kinematics** research
    
- **Coarticulation** and **orofacial dysfunction** studies
    

## Ultrasound Imaging

![[Echo_tongue.png]]

### Principle

**Ultrasound pulses** are emitted from a probe placed beneath the chin.  
The returning **echoes** from tissue boundaries are recorded to create a real-time image of the tongue’s contour.

### Technical parameters

- **Transducer frequency:** 2–4 MHz
    
    - Lower frequency → greater depth, lower resolution
        
    - Higher frequency → higher resolution, shorter range
        
- **Sampling rate:** ~28 Hz
    

### Analysis methods

- **Contour Analysis and Visualization Technique (CAVITE):** automatic detection of tongue contours.
    
- **Speckle Tracking:** compares pixel patterns across frames to track subtle tongue movements.
    

### Advantages

- **Non-invasive** and completely safe.
    
- Enables **real-time visualization** of tongue movements.
    

### Limitations

- **Bones create acoustic shadows**, obscuring some structures.
    
- **Head movement** can distort measurements (usually corrected via LED or IRED markers).
    
- Difficult to visualize the **posterior tongue** or **soft palate**.
    

### Studied organs

- **Tongue**
    


## Endoscopy and Transillumination

![[endoscopie.png]]

### Principle

- **Endoscopy:** insertion of a thin camera (through mouth or nose) to observe the **vocal folds** directly in real time.
    
- **Transillumination:** a light source (LED) placed in the trachea shines through the vocal folds, while an external sensor on the neck detects the transmitted light.
    

### Advantages

- Enables **direct observation** of the **larynx** and **vocal folds** opening.
    

### Limitations

- **Invasive and uncomfortable** for subjects.
    
- Transillumination only provides a **binary signal** (open/closed), not detailed vibration data.
    

### Studied organs

- **Vocal folds**
    
- Larynx
    

## Electroglottography (EGG)

![[electroglottographie.png]]  
![[mesureImpedance.png]]

### Principle

Two electrodes placed on each side of the neck measure **changes in electrical impedance** as the vocal folds open and close.  
When closed → low impedance; when open → high impedance.

### Advantages

- **Non-invasive** and **easy to use**.
    
- Provides **continuous vocal folds activity** signals.
    

### Limitations

- Affected by **neck morphology** and skin conductivity?
    

### Studied organs

- **Vocal folds** (glottal contact)
    


## Electropalatography (EPG)

![[EPG.png]]  
![[EPG_measures.png]]

### Principle

A **custom-made artificial palate** (thin plastic plate) is molded to fit the speaker’s hard palate and fitted with a grid of **electrodes**.  
These electrodes detect **tongue contact** patterns during speech.

### Advantages

- Provides **spatiotemporal data** on tongue–palate contact.
    
- Allows **real-time visualization** of articulation.
    

### Limitations

- Requires **custom fabrication**, time-consuming and expensive.
    
- Measures only **contact patterns**, not tongue motion off the palate.
    
- May **interfere with speech** production.
    

### Studied organs

- **Tongue** (upper surface)
    
- Hard palate
    


# Dynamic measurements

## Force sensors

![[capteurforce_palais.png]]  
![[capteurForce_mesure.png]]

### Principle

**Force sensors** (strain gauge-based) measure the pressure exerted by the tongue on the palate or other structures.  
The electrical resistance of the sensor changes with mechanical deformation.

### Advantages

- Provides **quantitative** measures of articulatory strength.
    
- Reveals aspects of **fine motor control** in speech.
    

### Limitations

- **Bulky sensors** may **disturb speech**.
    
- **Calibration** is complex and subject-specific.
    

### Studied organs

- **Tongue**
    
- Palate
    

## Electromyography (EMG)

![[uniteMotrice_principe.png]]  
![[nappe_electrode.png]]

### Principle

**Electromyography** records the **electrical activity** of muscles during contraction.  
Each **motor unit** (motoneuron + related muscle fibers) produces an action potential recorded by electrodes.

### Methods

- **Surface EMG:** electrodes placed on the skin.
    
- **Intramuscular EMG:** needle electrodes inserted directly into the muscle.
    

### Advantages

- Measures **muscle activation** intensity and timing.
    

### Limitations

- May record signals from **neighboring muscles** (crosstalk).
    
- **Invasive** for intramuscular recordings.
    
- May **disturb speech**

### Studied organs

- **Tongue**.
    


# Experimental paradigms

## Tongue Perturbation Experiment

![[tonguePerturbExpe.png]]

### Principle

A robotic device gently pulls the tongue forward during speech production. **EMG** recordings measure the muscular response.

![[mesures_reponse_perturb_langue.png]]  
![[EMG_speech_nSpeech_rest_volun.png]]

### Results

- During speech → a **compensatory reflex** occurs: the tongue returns to its original position.
    
- Without speech → **no significant reflex activation**.
    
- Therefore, the reflex is **specifically triggered during speech production** (Ito et al., _Scientific Reports_, 2024) -> à confirmer...!
    


# Summary table

| Technique                     | Studied Organ(s)     | Principle                                     | Advantages                       | Limitations                            | Typical Applications                         |
| ----------------------------- | -------------------- | --------------------------------------------- | -------------------------------- | -------------------------------------- | -------------------------------------------- |
| **EMA / EMMA**                | Tongue, lips, jaw    | Electromagnetic sensors tracking 3D positions | High precision, dynamic tracking | Invasive, expensive                    | Articulatory kinematics, *research*          |
| **Ultrasound**                | Tongue               | Ultrasound echoes                             | Non-invasive, real time          | Sensitive to head motion, bone shadows | Speech therapy, *research*                   |
| **Endoscopy**                 | Vocal folds          | Direct camera observation                     | Real-time visualization          | Invasive, uncomfortable                | Phoniatrics, diagnosis, *clinical*           |
| **Transillumination**         | Vocal folds          | Light transmission measurement                | Simple, non-invasive             | Binary signal only                     | Glottal opening detection, *research*        |
| **Electroglottography (EGG)** | Vocal folds          | Impedance between electrodes                  | Non-invasive, continuous         | No imaging, morphology-dependent       | Voice analysis, *research*                   |
| **Electropalatography (EPG)** | Tongue / palate      | Electrodes on custom palate                   | Real-time contact visualization  | Custom fabrication required:expensive  | Articulatory studies, *research*, *clinical* |
| **Force sensors**             | Tongue, palate, lips | Pressure measurement                          | Quantitative data                | Speech disturbance, calibration        | Motor control research, *research*           |
| **Electromyography (EMG)**    | Tongue               | Electrical muscle activity                    | Reveals motor control            | Invasive, signal contamination         | Neuromotor studies, *research*               |
