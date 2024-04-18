# Target trial emulation

`````{admonition} Executive summary
:class: info

**Target trial emulation** involves outlining your imaginary ideal RCT, and using that to inform study design, to help prevent avoidable biases like:
* **Immortal time bias** - when you ignore variation in timing of treatment initiation
* **Lead time bias** - when you detect a disease earlier than you otherwise would have in practice
* **Selection bias** - when people in study systematically differ from population of interest

It also helps identify relevant causal questions and confounders.

To design your target trial protocol you should outline the:
* Eligibility criteria
* Treatment strategies
* Treatment assignment
* Outcomes
* Causal estimand
* Start and end of follow-up
* Statistical analysis

When emulating the target trial, you should ensure that the following are aligned at **time zero**: eligibility criteria met, treatment strategies assigned, follow-up started.
`````

## Introduction

'**Target trial emulation** is a **framework** for designing and analysing observational studies that aim to estimate the causal effect of interventions. For each causal question on an intervention, one can imagine the randomized trial (the “target trial”) that could have been conducted to answer that question. This target trial should be explicitly specified in a target trial protocol'. This then informs design of the observational study. [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

Target trial emulation is recommended as the standard approach for causal observational studies that investigate interventions. Reasons for this include...

### Bias

It **improves the quality of these observational studies by preventing avoidable biases**. ' Although many practitioners worry about confounding in observational studies, the effect of these “self-inflicted” biases is often much more severe.' [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

Examples:
* **Immortal time bias (ITB)** - 'occurs when there is variation in timing of treatment initiation from cohort entry and time-to-treatment is misclassified or ignored', meaning that a cohort is followed during times in which outcomes cannot occur. [[Agarwal et al. 2018]](https://doi.org/10.1177%2F1073274818789355) 

    Example from [Egom 2014](http://dx.doi.org/10.1056/NEJMc1408400#SA1):

![Immortal Time Bias example](../images/immortal_time_bias.png)

* **Lead time bias** - 'when a disease is detected by a screening or surveillance test at an earlier time point than it would have been if it had been diagnosed by its clinical appearance' [[Rollinson and Sabel 2007]](https://doi.org/10.1016/B978-0-8151-4385-7.50009-6)

    Example by [Mcstrother - Own work, CC BY 3.0](https://commons.wikimedia.org/w/index.php?curid=15703636):

![Lead time bias example](../images/Lead_time_bias.svg.png)

* **Selection bias** - 'occurs when individuals or groups in a study differ systematically from the population of interest leading to a systematic error in an association or outcome' [[Catalogue of Bias Collaboration]](https://catalogofbias.org/biases/selection-bias/)

A recent review of observational studies found that:
* 57% of observational studies suffer from immortal time bias
* 44% suffer from depletion of susceptibles/prevalent user selection bias.' [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

### Relevant causal questions

Target trial emulation 'forces investigators to ask causal questions about interventions, leading to findings that are directly useful in decision-making'.

> Example: *'Many observational studies have investigated the causal effect of BMI on outcomes. BMI is not an intervention; patients cannot be randomized to have a certain BMI—a certain BMI can only be achieved through a particular intervention, such as diet, physical exercise, bariatric surgery, or medications (e.g., semaglutide or tirzepatide). These observational studies thus lose the vital information on how a patient attained a different BMI level. Each of the interventions may lower BMI by the same amount but may have completely different causal effects on the outcome. Therefore, the association between BMI and outcomes becomes an amalgamation of each of these interventions, which makes the association difficult to interpret.*'

'The fact that the causal effect of biomarkers cannot be directly studied does not necessarily mean that the target trial emulation is restrictive—the investigator just needs to reformulate the question in terms of an intervention, just as has been performed to research biomarker targets in real randomized trials.' [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

### Identify confounders

> Example: *'Suppose that an investigator is interested in estimating the causal effect of living donor kidney transplantation versus deceased donor kidney transplantation on graft and recipient survival. Which confounders should the investigator adjust for: donor characteristics, recipient characteristics, or both?*
> 
> *When donor and recipient characteristics are imbalanced, the investigator may be inclined to adjust for both in the observational analysis. Fortunately, thinking about the target trial provides the solution. In a randomized trial, the investigator randomizes recipients to a kidney transplant from a living donor or a deceased donor. Consequently, the recipients in both groups have similar characteristics. However, living donors will not have characteristics similar to deceased donors in this randomized trial. The potential lower quality of kidneys from deceased donors is part of the treatment.*
> 
> *The observational analysis should therefore only adjust for recipient characteristics to emulate this randomization and not for donor characteristics.'* [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

### Guides required data and analysis

'The required data and statistical analysis logically flow from the specifications in the research question.' [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

## How to design your target trial protocol

You should include the following protocol elements. This table is adapted from [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152). The example is 'for an observational study aiming to estimate the causal effect of renin-angiotensin system inhibitors versus calcium channel blockers on outcomes in patients with advanced CKD'.

| Protocol element | Description | Target Trial | Subsequent observational study | Comments |
| --- | --- | --- | --- | --- |
| **Eligibility criteria** | **Who will be included in this study?** | - Age 18+<br>- Under nephrologist care<br>- CKD G4 (i.e., eGFR <30 ml/min per 1.73 m2)<br>- No history of kidney transplantation<br>- No use of RASi or CCB in previous 180 d between January 2007 and December 2016 | Same as target trial | Observational study could be tempted to include all individuals on treatment or with outcome in follow-up - but this would be incorrect, as eligibility criteria determine who is enrolled in a trial, and information from follow-up could **never** determine eligibility<br><br>Will often need to **compromise** in observational study if can't get all data required to determine eligibility
| **Treatment strategies** | **Which precise treatment strategies or interventions will eligible individuals receive?** | 1. Initiate RASi (ACEi or ARB) only<br>2. Initiate CCB only | Same as target trial | In practice, more likely "initiate RASi only and always use during follow-up" - should capture that nauance. Important to be specific as guides follow-up and analysis, including whether need to adjust for time-varying confounding |
| **Treatment assignment** | **How will eligible individuals be assigned to the treatment strategies?** | Randomization, no blinding | Eligible individuals are assigned at baseline to the treatment strategy that their data are consistent with. To emulate randomization, we adjust for the following baseline confounders: age, sex, eGFR, systolic and diastolic blood pressure, medical history (heart failure, arrhythmia, peripheral vascular disease, cerebrovascular disease, ischemic heart disease, diabetes mellitus, hyperkalemia, AKI), medication use (β-blocker, thiazide diuretic, potassium-sparing diuretic, statin), and health care use (the total number of hospitalizations in previous year) | Individuals will be randomly assigned to one of the treatment strategies in the target trial<br><br>Appropriate emulation of randomization requires sufficient adjustment for all baseline confounders, which need to be measured before treatment assignment. The difficulty is to obtain enough data on confounders to remove residual confounding. |
| **Outcomes** | **What outcomes will be measured during follow-up?** | 1. Kidney replacement therapy (dialysis or kidney transplantation) 2. All-cause mortality 3. Major adverse cardiovascular events (composite of cardiovascular death, nonfatal myocardial infarction, nonfatal stroke) | Same as target trial. Kidney replacement therapy is registered in the Swedish renal registry; all-cause/cardiovascular mortality is identified from the Swedish death registry; hospitalizations for myocardial infarction or stroke are identified through ICD-10 codes in the national patient registry | Outcome data may often be missing<br><br>In observational data, outcomes usuallly not assessed blindly and systematically, so this can lead to bias (e.g. if you get more measurements when you're sicker - which you can addresss by comparing number of measurements - but not by restricting to patients with certain number of measurements, since randomised trial wouldn't have known that at baseline, and this would lead to selection bias) |
| **Causal estimand** | **Which causal estimand will be estimated with the observational data?** | **Intention-to-treat effect** (analyse in randomised groups regardless of whether complete or switch treatment)<br><br>**Per protocol effect** (only analyses people who strictly adhered to protocol - and excludes people who didn't complete or switched treatment) | Per protocol effect (effect of receiving treatment strategy as specified in protocol) | Randomised trials are commonly effect of being randomised (intention-to-treat effect) and effect of receiving treatment as per protocol (per protocol effect). Observational studies are not randomised so you can only estimate per protocol effects, **never** intention-to-treat (despire investigators often using that term) |
| **Start and end of follow-up** | **When does follow-up start and when does it end?** | Starts at randomization and ends at occurrence of end point, administrative censoring or 5 yr of follow-up | Starts at medication initiation (filled prescription) and ends at occurrence of end point, administrative censoring or 5 yr of follow-up | Target trial starts at randomization and finishes at reaching an end point, administrative censoring, or 5 years of follow-up<br><br>Observational starts when (1) patient eligible and (2) patient data congruent with start of treatment. There isn't clear time for when "do not initiate" treatment begins - solution is to analyse question in sequential trials, which uses idea that patients in "do not initiate treatment" group can be allocated to strategy at any point in time when are eligible. When interested in patients who "always use during follow-up", would need to censor (stop follow-up) when discontinue assigned treatment |
| **Statistical analysis** | **Which statistical analyses will be used to estimate the causal estimand?** | Intention-to-treat analysis, non-naïve per protocol analysis | Per protocol analysis: Hazard ratios are estimated using Cox regression while adjusting for baseline confounders with inverse probability of treatment weighting. Weighted cumulative incidence curves are estimated using the Aalen–Johansen estimatora | Includes methods to adjust for confounding, how missing data are dealt with, and which methods were used to obtain effect estimates |

[[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)

## How to use this to inform your observational study

'To ensure that the target trial protocol properly emulates the design of a randomized trial, it is a key to align the following three components **at time zero** (often also referred to as baseline) in the observational study:
1. Eligibility criteria are met, that is, all included patients meet the specified inclusion and exclusion criteria.
2. Treatment strategies are assigned.
3. Follow-up is started, that is, we start counting outcomes.

Note that these three components are naturally aligned in randomized trials at the moment of randomization.' 

Observational study design options:
* Active comparator, new user (ACNU) design
* Clone censor weight design
* Sequential trial design [[Fu 2023]](https://doi.org/10.1681/ASN.0000000000000152)
