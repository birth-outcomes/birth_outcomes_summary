# HIE proposal 1: predicting HIE

I have included several examples of proposals, which all revolve around an example of a focus. This focus was simply based on what was most frequently discussed at our meeting earlier in Spring 2024. This focus was the problem of **infants who would have benefitted from having a caesarean**, and who go on to have **hypoxic ischaemic encephalopathy**, and then potentially further complications (for example, cerebral palsy).

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

## Aims and objectives

Predicting the occurence of HIE.

## Inclusion and exclusion criteria

Inclusion criteria:
* Infants born at or beyond 35 weeks of gestation
* Singleton pregnancies

## Outcome

The outcome is infants experiencing HIE. My current recommendation on measuring this would be to follow the protocol defined by the Neonatal Data Analysis Unit and the Department of Health and use either:
* Diagnosis of NE or HIE (severe, moderate, grade 2 or grade 3)
* Therapeutic hypothermia for 2 or more consecutive days{cite}`gale_brain_2017`

## Research design

Machine learning model with various maternal, antenatal and labour characteristics - including:
* Information derived from the fetal heart rate traces.
* Method of delivery (as a predictor in the model).

## Limitations

<mark>why can't we just include whether they had a caesarean as a predictor in the model... explain why that's a limited strategy...</mark>
