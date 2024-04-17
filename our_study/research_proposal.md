# HIE proposal 1: predicting HIE

I have included several examples of proposals, which all revolve around an example of a focus. This focus was simply based on what was most frequently discussed at our meeting earlier in Spring 2024. This focus was the problem of **infants who would have benefitted from having a caesarean**, and who go on to have **hypoxic ischaemic encephalopathy**, and then potentially further complications (for example, cerebral palsy).

---

## Introduction

Neonatal encephalopathy (NE) refers to brain disease, damage or malfunction in late pre-term or term infants (born at or beyond 35 weeks). It is characterised by 'challenges initiating and maintaining respiration, reduced tone and reflexes, seizures, and impaired levels of consciousness'.{cite}`molloy_neonatal_2023,quirke_cohesion_2024` The cause of NE is often difficult to identify, with careful phenotyping using a range of measurements and examinations required to differentiate between posisble causes. Morover, there may not just be one cause, but several factors that lead to NE.{cite}`molloy_neonatal_2023` The possible causes of NE include: hypoxia ischaemia, neonatal stroke, infection, intracranial haemorrhage, congenital brain anomalies, as well as neurometabolic, genetic and epigenetic factors.{cite}`quirke_cohesion_2024,austin_guidelines_2021`

Hypoxia ischaemia is the most common cause of NE. This is when there has been restricted blood flow to tissues ("ischaemia"), meaning that tissues that have low/insufficient oxygen levels ("hypoxia").{cite}`klabunde_ischemia_2023` This type of NE is referred to as hypoxic ischaemic encephalopathy (HIE), but was often previously referred to as birth/perinatal asphyxia.{cite}`bliss_hypoxic-ischaemic_nodate` The current treatment for infants with suspected HIE is therapeutic hypothermia. This must be started within six hours of birth,{cite}`parmentier_magnetic_2022` and involves cooling of the infant's head or whole body to reduce their body temperature to 33-36.5°C for 48 to 72 hours.{cite}`allen_hypoxic_2011` Potential consequences of moderate/severe HIE include mortality, and the development of cerebral palsy, epilepsy, and intellectual disability.{cite}`shim_which_2021,torn_outcomes_2023`

There are several risk factors associated with HIE. These include maternal and pregnancy characteristics which indicate that a delivery is at higher risk of HIE occuring, as well as observations during labour which indicate HIE may have occured/is more likely to have occurred. Risk factors for HIE during labour include: decreased fetal movement; abnormal fetal heart rate or contractions patterns; severe maternal cramping, maternal high blood pressure, or vaginal bleeding. However, in some cases (particularly infants with mild to moderate HIE), there may not be any obvious signs or symptoms of HIE during labour or at the time of birth.{cite}`hie_help_center_hypoxic-ischemic_nodate`

If a clinician suspects that HIE is likely, they may choose to perform an emergency caesarean section, based on the rationale that if an infant is truly experiencing HIE, sooner delivery would reduce the severity of HIE by reducing the length of time that the infant experiences hypoxia ischaemia. However, in the United States, a third of malpractice claims in obstetrics are related to neurological injuries in neonates, with factors leading to these including that clinicians have failed to account for risk factors known before birth, and failure to identify or act on (or delays in acting on) identified risk factors during birth like abnormal fetal heart rate, fetal distress, and malpresentation.{cite}`leith_predictive_2024`

### Existing studies

There have been some studies that have created predictive models for HIE which incorporate a wide range of known risk factors. The rationale/hope of these studies is that the development of models that can combined information on risk to generate an overall estimate of risk, can then help clinicians identify high-risk pregnancies and plan delivery accordingly to hopefully prevent HIE.

Odd et al. 2017{cite}`odd_hypoxic-ischemic_2017` use a logistic regression model to predict cases of HIE (i.e. infants who need resuscitation and had NE symptoms). It is based on data from over 14,000 infants in a Bristol cohort study, with half used for training and half for validation. In the training set (n=6712), 130 infants had HIE (0.01%). The model includes a range of maternal, antepartum and intrapartum characteristics - although it does not include the delivery method. However, they do estimate the number of elective caesareans that would be required to prevent one case of HIE in different antenatal risk groups.{cite}`odd_hypoxic-ischemic_2017`

Leith et al. 2024{cite}`leith_predictive_2024` use a logistic regression model to predict cases of HIE (i.e. presence of HIE diagnostic code) in a US dataset of 836,216 births - of which, 376 (0.00045%) had a diagnosis of HIE. The model includes a range of maternal, antepartum and intrapartum characteristics - including the delivery type (with predictors including forceps, vacuum, elective C-section, emergency C-section, and intrapartum C-section).{cite}`leith_predictive_2024`

Abnormal fetal heart rate is an important indicator which we'd hope to include in our analysis, but is not included in Odd et al. 2017{cite}`odd_hypoxic-ischemic_2017`, and is included via identification of an ICD code for fetal heart rate abnormality in Leith et al. 2024{cite}`leith_predictive_2024`. There is a study by Eden et al. 2018{cite}`eden_fetal_2017` which includes more detailed information on fetal heart rate. They used fetal heart rate, baseline variability, accelerations, decelerations and uterine activity - in combination with other maternal, obstetrical and fetal risk factors - to produce a risk score. This score was to distinguish between infants with intrapartum neurological injury and subsequent cerebral palsy, and control term infants who had a normal fetal tracing on admission.{cite}`eden_fetal_2017`

---

## Focus

### Initial aim

Broadly speaking, what we're hoping to do is:
1. Predict risk of HIE (using multivariable models)
2. Assess effectiveness of caesarean section in preventing occurence or development of HIE - identifying who best to intervene for and when

However, it is likely we won't be able to specifically focus on HIE due to sample size, and we will likely need to look at more general outcomes...

### Outcomes

If we were to focus just on HIE, my recommendation would be to follow the protocol defined by the Neonatal Data Analysis Unit and the Department of Health and use either:
* Diagnosis of NE or HIE (severe, moderate, grade 2 or grade 3)
* Therapeutic hypothermia for 2 or more consecutive days{cite}`gale_brain_2017`

I would recommend checking the number of infants meeting this criteria - but I think it highly likely this will be insufficient for analysis, and so it will likely need to be one of the more general outcomes, such as:
* Transfer to neonatal care services
* Need to resuscitation

Although these are relevant to identifying HIE, if we use them as the outcome, we would need to explicitly state that the model is predicting that outcome, and *not* HIE.

### Likely actual aim of analysis

Specific to the chosen outcome - for example:
1. Predict risk of transfer to neonatal care services
2. Assess effectiveness of caesarean section in preventing transfer to neonatal care services

### Existing studies

<mark>refer to relevant studies - as this is not just about HIE now</mark>

---

## Paradigm and framing of research problem

### Causal inference

This is **not predictive research**. In a predictive research study, your aim is to predict an outcome with the best accuracy, and although you may be interested in how those predictions were made, you don't made whether those are true relationships or not between the predictor and outcome.[[Ramspek et al. 2021]](https://link.springer.com/article/10.1007/s10654-021-00794-w)

We are interested in the **true relationships** between predictors and the outcome. As such, in design of the study, one of our primary concerns is to account for the impact of treatment on relationships (referred to as the intervention effect or treatment paradox). This is when a predictor is: (a) related to the outcome, and (b) triggers an effective treatment that prevents the outcome. The consequence of this is that predictors can appear to have a poorer prognostic performance that they actually do in reality, leading to underestimation of adverse outcomes.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8) [[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

In the case of HIE, an example is an abnormal CTG, which is indicative of high risk of HIE having occurred, and triggers a caesarean. With our focus being more broadly on any adverse neonatal outcomes, this would become a wider range of observations and characteristics before or during labour, which would trigger the decision to do an elective or emergency caesarean.

### Using the "language of causal inference" to describe our research problem

<mark>explain why we can view it as being treatment - outcome as focus, and not just treatment as a confounder of predictor - outcome</mark>
* Because its what we hope to learn - in making our prediction model, we're trying to understand who needs treatment
* BUT IS IT? DO WE HAVE TO? think about IPTW - there, treatment is treated more like a confounder. do you still say it like tretment - outcome? have a look at examples.

<mark>add coutnerfactual description of problem</mark>

<mark>add DAG</mark>

---

## Methods

## Inclusion and exclusion criteria

Inclusion criteria:
* Infants born at or beyond 35 weeks of gestation
* Singleton pregnancies

# ROUGH NOTES 1

Would recommend we explore a selection of methods to answer the same problem.

<mark>add notes from my piece of paper, front and back</mark>

<mark>add thing about optional extra of demonstrating the treatment paradox exists (?) or maybe not</mark>

<mark>look at the other research proposal documents and consider whether they could actually just be incorporated here</mark>

# ROUGH NOTES 2

## Research design

Machine learning model with various maternal, antenatal and labour characteristics - including:
* Information derived from the fetal heart rate traces
* Method of delivery (as a predictor in the model) - included due to the treatment paradox - as we might find unexpected protective relationships between the risk factor and the outcome otherwise, as they result in an intervention and then improved outcomes

Demonstrate existence of treatment paradox similar to [Uffen et al. 2021](https://doi.org/10.1136%2Fbmjopen-2020-046518) <mark>write out method based on theirs</mark>

qsofa was tool developed to identify patients at risk of disease or unwanted outcome. typically developed in partially treated populations. this means treatment paradox. biased underestimation of adverse outcomes when applied to treatment naive.

the qsofa has strong prognostic and in treated population.

to test they:

* looked at prognostic accuracy of qsofa for mortality
    * sensitivity and specificty and AUROC

* analysis relationship between positive qsofa, or abnormal parameters within qsofa, and intensity of therapy (five different therapies)
    * binary logistic regression analyses - qsofa as binary covariate, therapy as outcome - seperate regressions per therapy then combined - including age and cci as confoudners in model

An illustrative example of the risks of ignoring the treatment paradox in prognostic models can be found in the field of obstetrics.17 A retrospective study aimed to develop a **prediction model for adverse maternal outcomes** in suspected pre-eclampsia **failed to identify maternal hypertension as a risk factor for adverse outcome due to a treatment paradox**.13 In the study cohort, maternal hypertension was such a strong trigger for physicians to start an effective treatment that significantly less adverse events occurred. As a consequence, the statistical inference between maternal hypertension and adverse outcomes completely disappeared, and this well-known risk factor was not included in the prognostic model. However, ignoring a strong risk factor such as maternal hypertension in pre-eclampsia in new treatment-naïve patients would certainly lead to undertreatment and adverse outcomes. Although the treatment paradox effect in sepsis will probably be less strong than in pre-eclampsia, because sepsis is a far more heterogeneous syndrome with more heterogeneity in treatment effects, the results of our study support the presence of the effect.

## Limitations

* Including all confounders can introduce bias due to the presence of colliders and mediators

<mark>why can't we just include whether they had a caesarean as a predictor in the model... explain why that's a limited strategy...</mark>
