# Our study

> Research proposal: Machine learning to avoid adverse neonatal outcomes

## Finding a focus

In it's broadest sense, the end-goal of this project is to lead us towards producing a tool to provide live, real-time, data-driven risk assessment during labour. This is a tool for which the effectiveness could be evaluated, to ascertain whether it helps support decision making by the care providers and mother during labour, to help identify when and which interventions and delivery methods would most reduce risk of poor maternal or neonatal outcomes.

However, this is a complex problem with lots of moving parts, and requires that we identify a clearer research focus. Some things to consider...

### Outcome

> Whether you focus on **neonatal and/or maternal** outcomes
> 
> **Which outcomes** you choose to focus on.
> * Neonatal examples include:
>   * Neonatal encephalopathy (NE), and specific types, like hypoxic ischaemic encephalopathy (HIE)
>   * Choroioamnionitis (intra-aminotic infection)
>   * Death
>   * Indicators of poor health - umbilical cord pH, Apgar, resuscitation, meconium-stained amniotic fluid, transfer to neonatal care services
> * Maternal outcomes include vaginal tearing or episiotomy, blood clots, and urinary or anal incontinence
> 
> **Outcome measurement** - some outcomes are quite clear cut, but others are harder to define, and may use proxy measures or combinations of measures

### Treatment/Intervention

> Whether you focus on comparing **two or multiple** treatment/delivery pathways
> 
> Whether you focus on **type of delivery and/or other treatments that can be given during delivery**
> 
> **Which outcomes** you then choose to focus on. Examples of type of delivery include:
> * Unassisted vaginal delivery
> * Assisted vaginal delivery - ventouse (vacuum cup) or forceps
> * C-section - elective or emergency
> * Vaginal birth after C-section
> 
> Examples of treatments or other interventions during labour include:
> * Gas and air (Enotox)
> * Pethidine injections
> * Epidural
> * Remifentanil
> * Water birth
> * TENS machine
> * Artifical rupture of the membranes
> * Oxytocin drip/syntocinon
> * Episiotomy
> 
> If the outcome is not immediately after birth, whether you focus on **subsequent treatments** - for example, magnesium sulfate and cooling for infants with HIE.

### Focus

Choice of **treatment** and **outcome** are ultimately both about defining the focus of the project. Examples:
> * Comparing outcomes from labours with similar characteristics except that there was an **earlier or later** decision to do a caesarean
> * Identifying infants who **did not receive caesareans** but who would have benefited
> * Reducing risk of **unecessary caesarean** sections - with inherent maternal complications like infection, bleeding and bladder damage.
> * Identifying women in whom **forceps or ventouse deliveries would be unsuccessful** and reduce the risk of traumatic assisted vaginal deliveries which lead to adverse neonatal outcomes

This can be related not just to treatment and outcome, but also to the other characteristics included in the analysis, and how they are dealt with. Examples:

> * Focus on **inequalities** in a particular treatment/outcome. Death and disability in pregnancy are much higher in disadvantaged groups. For example, stillbirth is up to four times higher in black than white women in the UK.

### Methodological considerations

**Timing** will be important with regards to the choice to intervene and the outcome. The risk-benefit ratio is dynamic and changes during labour depending on how the labour progresses and how events unfold. For example, caesareans are safer earlier in labour than later.

How **cardiotocograph data** is analysed and incorporated as a predictor is also complex, with a wide range of methods used in the literature, as explored in https://github.com/birth-outcomes/ctg_exploratory and https://github.com/birth-outcomes/fhrma_python. For example:

> * Generating a set of parameters that describe the signal (clinically relevant or others), and the chosen method for that analysis
> * Transforming the signal, such as into an image using continuous wavelet transformation, and the chosen parameters

The **treatment paradox** is another important consideration, as explored [on this page](../causal_concepts/design_intro_1_treatment_paradox.md). This exists as the indicators for a poor outcome (e.g. abnormal cardiotocograph, gestational age) will trigger an effect treatment (caesarean), which then biases the observed relationship between the indicators and outcome. This is important to us - we are not just interested in prediction - but in the true relationships between variables. Hence, causal inference methodologies should be used within this work. This enables us to account for the treatment paradox when comparing outcomes in people with similar characteristics who received a caesarean or not, or received one earlier. There are a range of possible methods, including but not limited to...

> **Conventional methods:**
> * (Principal) Stratification
> * Matching
> * Inverse probability of treatment weighting (IPTW)
> * Multivariable regression
> 
> **G-methods:**
> * G-computation (/ parametric G-formula / G-standardisation / standardisation / outcome regression)
> * Marginal structure models
> * G-estimation
> 
> **Methods to address unobserved confounding:**
> * Instrumental variables
> * Regression discontinuity (RD)
> * Interrupted time series (ITS)
> * Difference in differences (DiD)
> 
> **Other methods:**
> * Marginal, asymmetric conditional, and causal SHAP values
> * Synthetic control
> * Matrix completion
> * Causal discover
> * Double machine learning
> * Causal forests
> * Structural estimation

Another methodological consideration is **what variables** are included. This will depend on our chosen focus. Things to consider here include -

> **Which variables** are considered, which depends on the relationship you focus on, and your analysis method - e.g.
> * Some may just have **one** (e.g. instrumental variable studies)
> * Could look at **minimally important set of variables**
> * Some studies use a really **wide range**
> 
> Examples of variables include:
> * Suspected fetal growth restriction (FGR proxy is number of antenatal scans)
> * Previous CS
> * Parity (number, or nulliparity vs multiparity)
> * Antepartum haemorrhage
> * Body mass index
> * Maternal age
> * Maternal ethnicity
> * Gestational age at delivery
> * Induction of labour
> * Analgesia - epidural use
> * Oxytocin use
> * Maternal pyrexia
> * Abnormal FHR
> * Meconium-stained amniotic fluid
> * Single unsupported mother
> * Highest antenatal blood pressure
> * Duration of labour
> * Fetal size on scan (if done)

## Example: Caesarean section and hypoxic ischaemic encephalopathy

Here, I have focussed on one example (simply as it was the most discussed at our meeting earlier in the year). This is the problem of infants who would have benefitted from having a caesarean, and who go on to have hypoxic ischaemic encephalopathy, and then potentially further complications (for example, cerebral palsy).

---

### Introduction

<mark>set scene, provide context, what is of interest, what do we already know, what has not adequately been answered</mark>

### Aims and objectives

Identifying when emergency caesareans helped prevent severe hypoxic ischaemic encephalopathy, compared with vaginal delivery.

````{mermaid}
  flowchart LR;

    t("Non-elective<br>caesarean section"):::white;
    o("Hypoxic ischaemic<br>encephalopathy"):::white;

    t --> o;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Research type (predictive or etiological (causal))

Our aim is uncover true relationships between variables. It is not just to predict an outcome with the best accuracy. Hence, causal research methodologies should be considered.

One reason for this is the **treatment paradox**.<mark>finish</mark>

file:///home/amy/Documents/birth_outcomes_summary/_build/html/causal_concepts/design_intro_1_treatment_paradox.html

Another is **omitted variable bias**.<mark>finish... we'll measure many but that's also lots that we know we won't</mark>

All ML models will also employ an explainability model such as SHAP (SHaply Additive exPlanations). When heightened risk is predicted, this will show clinicians what is making the ML model predict high risk. However, explainability is not the same as causation.<mark>finish</mark>

### Treatment

Emergency caesarean section, as opposed to vaginal birth.

Exclusion: Elective caesarean (as interested in patients who begin with vaginal labour then transition to caesarean)

### Outcome

<mark>add sentinel event alternative as highlighted by steve</mark>

Hypoxic ischaemic encephalopathy - defined as by [Neonatal Data Analysis Unit and the Department of Health](file:///home/amy/Documents/birth_outcomes_summary/_build/html/outcomes/neo_out_background.html#neonatal-data-analysis-unit-and-the-department-of-health) as:
* Diagnosis of NE or HIE (severe, moderate, grade 2 or grade 3)
* Therapeutic hypothermia for 2 or more consecutive days

It's worth being aware that these diagnosis or treatment decisions will have been based on data - e.g. cooling guidelines:
* Apgar, need for resuscitation, low pH, high base deficit
* Altered state of consciousness (lethargy, stupor or coma, and one of: clinical seizures, abnormal reflexes, hypotonia, weak/absent suck)
* 30 minute aEEG with one of: normal background with some seizure activity, moderately abnormal activity, suppressed activity, or continuous seizure activity

### Research design

#### Investigate variation in use of emergency caesarean sections

There is not one right way to perform this analysis. However, a good starting point could be to replicate the methods used in [SAMueL-1](https://samuel-book.github.io/samuel-1/introduction/intro.html) (which focussed on variation in thrombolysis use between hospitals).

Here, we would:
* Model variation in use of emergency caesareans between hospitals so we can ask: *'What treatment would my patient receive at other hospitals?'*
* Model the delivery pathway, using clinical pathway simulation, so we can ask the question: *'What would happen to a hospital's use of and benefit from use of emergency caesarean sections, by changing key aspects of the pathway*, especially focussing on timing of the caesarean

<mark>add more detail on actual methods</mark>

However, this doesn't necessarily need to be just between hospitals - you can, for example, look at variation in use of emergency caesarean by:
* Time of day - Steve Thornton comments that "the time of day is important in the rate of delivery. More deliveries tend to happen at night naturally (perhaps because this was safer in long gone times as predators were not around). Also, nowadays because the inductions happen in the morning on the whole, this influences the timing of delivery"
* Weekday v.s. weekend

When look into timing of caesarean, there is no simple way to define timing, but possibilities include:
* The presence of multiple (𝑘) risk factors.
* Length of labour, or length of Stage-II labour.
* Cervical dilation (Steve: This is the standard method of determining the length of labour. The time from the start is really variable and inaccurate)
* Contraction rate/force (Steve: Unfortunately, we cannot determine the force of contraction, only the timing which is really important for any changes in the fetal heart rate)

#### Looking at relationship between use of emergency caesarean and outcome of hypoxic ischaemic encephalopathy

Could do SAMueL-2. <mark>explain how they did it</mark>

Could look into causal inference methologies.
* The first step we did on variation could be described as us trying to identify instrumental variables
* <mark>Go into detail of some based on obstetric studies and worked examples. Provide links to those pages.</mark>
* <mark>add dag</mark>
* for causal models, should be being explicitly clear which variables in a model were considered in design of the causal model (to avoid Table 2 fallacy)
* should be reporting predictive accuracy of all models (with reference)
* Mike's ideas - 'This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations. We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.'

You can demonstrate the existence of the treatment paradox by comparison of models designed to account for it, to those that are not.

## Working with clinicians and parents

For any chosen study design and focus, involvement of clinicians, as well as public and patient involvement, will be important.

Clinicians -
* mike - how acceptable would such a system be to clinicians? How can co-production be used to inform design?

Parents -
* public and patient involvement
