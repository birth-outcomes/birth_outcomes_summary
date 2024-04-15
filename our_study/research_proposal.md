# Proposal example: caesarean and HIE

This is an example of a proposal - but this does not necessarily have to be our focus - it was simply based on what was most frequently discussed at our meeting earlier in Spring 2024. This focus was the problem of **infants who would have benefitted from having a caesarean**, and who go on to have **hypoxic ischaemic encephalopathy**, and then potentially further complications (for example, cerebral palsy).

## Introduction

Neonatal encephalopathy (NE) refers to brain disease, damage or malfunction in late pre-term or term infants (born at or beyond 35 weeks). It is characterised by 'challenges initiating and maintaining respiration, reduced tone and reflexes, seizures, and impaired levels of consciousness'.{cite}`molloy_neonatal_2023,quirke_cohesion_2024` The cause of NE is often difficult to identify, with careful phenotyping using a range of measurements and examinations required to differentiate between posisble causes. Morover, there may not just be one cause, but several factors that lead to NE.{cite}`molloy_neonatal_2023` The possible causes of NE include: hypoxia ischaemia, neonatal stroke, infection, intracranial haemorrhage, congenital brain anomalies, as well as neurometabolic, genetic and epigenetic factors.{cite}`quirke_cohesion_2024,austin_guidelines_2021`

Hypoxia ischaemia is the most common cause of NE. This is when there has been restricted blood flow to tissues ("ischaemia"), meaning that tissues that have low/insufficient oxygen levels ("hypoxia").{cite}`klabunde_ischemia_2023` This type of NE is referred to as hypoxic ischaemic encephalopathy (HIE), but was often previously referred to as birth/perinatal asphyxia.{cite}`bliss_hypoxic-ischaemic_nodate` The current treatment for infants with suspected HIE is therapeutic hypothermia. This must be started within six hours of birth,{cite}`parmentier_magnetic_2022` and involves cooling of the infant's head or whole body to reduce their body temperature to 33-36.5°C for 48 to 72 hours.{cite}`allen_hypoxic_2011` Potential consequences of moderate/severe HIE include mortality, and the development of cerebral palsy, epilepsy, and intellectual disability.{cite}`shim_which_2021,torn_outcomes_2023`

There are several risk factors associated with HIE. These include maternal and pregnancy characteristics which indicate that a delivery is at higher risk of HIE occuring, as well as observations during labour which indicate HIE may have occured/is more likely to have occurred. Risk factors for HIE during labour include: decreased fetal movement; abnormal fetal heart rate or contractions patterns; severe maternal cramping, maternal high blood pressure, or vaginal bleeding. However, in some cases (particularly infants with mild to moderate HIE), there may not be any obvious signs or symptoms of HIE during labour or at the time of birth.{cite}`hie_help_center_hypoxic-ischemic_nodate`

<mark>finish this bit</mark>

If a clinician suspects that HIE is likely, they can perform an emergency caesarean section, which can help reduce the severity of HIE by reducing the length of time that the infant experiences hypoxia ischaemia.
* Variation in clinician decision making
* Variation in caesarean use
* Deifficult to decide whether to use caesarean
* High rate of medical malpractice claims
* Tools to support decision making, consider risk

Examples of studies on risk of HIE
* Missing: inclusion of detailed CTG info
* Missing: consideration of treatment paradox

## Aims and objectives

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

## Research type (predictive or etiological (causal))

Our aim is uncover true relationships between variables. It is not just to predict an outcome with the best accuracy. Hence, causal research methodologies should be considered.

One reason for this is the **treatment paradox**.<mark>finish</mark>

file:///home/amy/Documents/birth_outcomes_summary/_build/html/causal_concepts/design_intro_1_treatment_paradox.html

Another is **omitted variable bias**.<mark>finish... we'll measure many but that's also lots that we know we won't</mark>

All ML models will also employ an explainability model such as SHAP (SHaply Additive exPlanations). When heightened risk is predicted, this will show clinicians what is making the ML model predict high risk. However, explainability is not the same as causation.<mark>finish</mark>

## Treatment

Emergency caesarean section, as opposed to vaginal birth.

Exclusion: Elective caesarean (as interested in patients who begin with vaginal labour then transition to caesarean)

## Outcome

<mark>add sentinel event alternative as highlighted by steve</mark>

Hypoxic ischaemic encephalopathy - defined as by [Neonatal Data Analysis Unit and the Department of Health](file:///home/amy/Documents/birth_outcomes_summary/_build/html/outcomes/neo_out_background.html#neonatal-data-analysis-unit-and-the-department-of-health) as:
* Diagnosis of NE or HIE (severe, moderate, grade 2 or grade 3)
* Therapeutic hypothermia for 2 or more consecutive days

It's worth being aware that these diagnosis or treatment decisions will have been based on data - e.g. cooling guidelines:
* Apgar, need for resuscitation, low pH, high base deficit
* Altered state of consciousness (lethargy, stupor or coma, and one of: clinical seizures, abnormal reflexes, hypotonia, weak/absent suck)
* 30 minute aEEG with one of: normal background with some seizure activity, moderately abnormal activity, suppressed activity, or continuous seizure activity

## Research design

### Investigate variation in use of emergency caesarean sections

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

### Looking at relationship between use of emergency caesarean and outcome of hypoxic ischaemic encephalopathy

Could do SAMueL-2. <mark>explain how they did it</mark>

Could look into causal inference methologies.
* The first step we did on variation could be described as us trying to identify instrumental variables
* <mark>Go into detail of some based on obstetric studies and worked examples. Provide links to those pages.</mark>
* <mark>add dag</mark>
* for causal models, should be being explicitly clear which variables in a model were considered in design of the causal model (to avoid Table 2 fallacy)
* should be reporting predictive accuracy of all models (with reference)
* Mike's ideas - 'This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations. We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.'

You can demonstrate the existence of the treatment paradox by comparison of models designed to account for it, to those that are not.

## References

```{bibliography}
```