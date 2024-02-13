# Diagnostic codes for HIE

`````{admonition} Executive summary
:class: info

**Outcome:** Diagnosis of HIE in clinical records

**Specific to HIE?**
* For the HIE diagnosis code, yes. However, a French study found half of newborns with this code were not confirmed to have HIE from secondary datasets they linked with
* If using more general codes for NE, then no.

**Which infants with HIE?**
* Those who were diagnosed (not certain on factors that make this more or less likely). However, a French study found that 37% of infants identified to have HIE in a secondary dataset were not identified in the medical records with the HIE diagnosis code.

**Any other benefits or caveats not already mentioned?**
* NA

**Conclusion:** Potentially recommended. A French validation suggested half of infants coded with HIE were false positive, and that over a third of infants with HIE were not identified. Uncertain for English data, or for codes beyond ICD P91.6, but their findings make me cautious.
`````

## Diagnostic codes for HIE

Infants can be given a diagnosis of HIE or NE. In their project on brain injury from 2010 to 2015, the Neonatal Data Analysis Unit at Imperial use these diagnostic codes in the National Neonatal Research Dataset (NRRD) to identify HIE (or from therapeutic hypothermia). They used:
* Severe Hypoxic Ischaemic Encephalopathy (HIE)
* Severe Neonatal Encephalopathy
* Grade 3 Hypoxic Ischaemic Encephalopathy (HIE)
* Moderate Hypoxic Ischaemic Encephalopathy (HIE)
* Moderate Neonatal Encephalopathy
* Grade 2 Hypoxic Ischaemic Encephalopathy (HIE)

[[Gale et al. 2017]](https://assets.publishing.service.gov.uk/media/5a82446ced915d74e6236ad3/Report_on_brain_injury_occurring_during_or_soon_after_birth.pdf)

These diagnoses were from any Diagnosis field. The NRRD has patient diagnoses at admission to neonatal critical care, at discharge from neonatal care, and in neonatal critical care daily care data. These diagnoses are either **ICD** or **SNOMED CT**.[[source]](https://www.datadictionary.nhs.uk/data_sets/clinical_data_sets/national_neonatal_data_set/national_neonatal_data_set_-_episodic_and_daily_care.html)

### ICD-10 codes for HIE

P91.6 - Hypoxic ischaemic encephalopathy of a newborn

P21 - Birth asphyxia
* P21.0 - Severe birth asphyxia - Pulse less than 100 per minute at birth and falling or steady, respiration absent or gasping, colour poor, tone absent; Asphyxia with 1-minute Apgar score 0-3; White asphyxia
* P21.1 - Mild and moderate birth asphyxia - Normal respiration not established within one minute, but heart rate 100 or above, some muscle tone present, some response to stimulation; Asphyxia with 1-minute Apgar score 4-7; Blue asphyxia
* P21.9 - Birth asphyxia, unspecified

[[source]](https://icd.who.int/browse10/2019/en)

### SNOMED CT codes for HIE

* Hypoxic-ischemic coma
* Fetal hypoxia
* Hypoxia of brain
* Perinatal hypoxia

## Validation of diagnostic codes for HIE

A French study aimed to validate ICD-10 codes for moderate to severe HIE in hospital discharge databases through linkage of those data to a national population-based cohort of newborns with moderate and severe HIE. They found that:
* 67% of HIE cases were identified using the diagnostic code (P91.6)
* Half of the newborns encoded with P91.6 were not confirmed HIE

They state that this was consistent with previous validation studies showing poor performance of diagnosis codes for identifying newborn morbidities in healthcare administrative databases.[[Ego et al. 2024]](https://doi.org/10.1016/j.jpeds.2024.113950)

## Grades of HIE

### Grades on NHS records

NHS records can include a grade indicating the observed level of HIE - these are:
* None (code 0)
* Mild (code 1)
* Moderate (code 2)
* Severe (code 3)[[source]](https://www.datadictionary.nhs.uk/attributes/hypoxic_ischemic_encephalopathy_grade.html)

I'm not certain what the criteria for these grades are, and whether they might be to do with the Sarnat score or not...

### Sarnat score

In 1976, Sarnat and Sarnat published a study that included a 'staging system for the sequential evolution of clinical signs and EEG changes was intended to facilitate formulation of prognosis for neurologic outcome.' 'Modifications of the Sarnat Scoring System have been employed in the major trials of therapeutic hypothermia for neonatal hypoxic-ischemic encephalopathy (HIE) to identify neonates at highest risk for abnormal neurodevelopmental outcome'.[[Mrelashvili et al. 2020]](https://doi.org/10.1038%2Fs41390-020-01143-5)

The use of sarnat staging for HIE was:
* **Stage 1 (mild)**: hyperalertness, hyper‐reflexia, dilated pupils, tachycardia, absence of seizures;
* **Stage 2 (moderate)**: lethargy, hyper‐reflexia, miosis, bradycardia, seizures, hypotonia with weak suck and Moro;
* **Stage 3 (severe)**: stupor, flaccidity, small to mid position pupils that react poorly to light, decreased stretch reflexes, hypothermia and absent Moro. [[Cochrane Neonatal Group]](https://doi.org/10.1002%2F14651858.CD003311.pub3)

## Diagnosis of NE in NNAP

The National Neonatal Audit Programme includes a measure of encephalopathy in babies born at 35 weeks gestational age or above, within the first three full calendar days after birth.

Encephalopathy is categorised if the baby was admitted to neonatal care for at least 72 hours and the daily summaries from those 72 hours include two or more of the following neurological signs in the same daily data summary:
* **Abnormal tone**
* **Lethargic or comatose consciousness**
* **Convulsions**

These details were captured on BadgerNet in daily summary forms (forms are created for each baby for each calendar day where they are an inpatient on a neonatal unit).

[[source]](https://www.rcpch.ac.uk/sites/default/files/2019-02/NNAP%202018%20Audit%20Measures%20Guide%20v1.3%20FINAL.pdf)

In the 2019 NNAP report on data from 2018, there was 0.01% missing data. However, I imagine this assumes incompletion of tone and consciousness and convulsions means no encephalopathy, when actually it could be failure to complete record?

However, NE does not appear to be in the latest NNAP Audit Measures [[source]](https://www.rcpch.ac.uk/sites/default/files/2024-01/2024_nnap_audit_measures_guide_v1.0_0.pdf).

They don't have a measure specific to HIE - this just broadly tries to identify NE based on the broad definition of NE.

## Other considerations

Ford et al. 2007  looking at the accuracy of routinely collected hospital discharge data in Australia for identifying neonatal morbidity, and found the **procedures tended to be more accurately recorded than diagnoses**.[[Ford et al. 2007]](https://doi.org/10.1186/1472-6963-7-188)