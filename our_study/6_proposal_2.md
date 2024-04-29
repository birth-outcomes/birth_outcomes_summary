# HIE Proposal (intervention)

As in [HIE Proposal #1](./5_proposal_1.md), this is just an **example** of how we could design this study. Here, I am assuming a focus on **assessing the effectiveness of caesarean section as a intervention for HIE**.

## Introduction

As in [HIE Proposal #1](./5_proposal_1.md).

### Existing studies

As far as I am aware, there have not been any observational studies estimating a causal relationship between caesarean use and HIE - although I have identified four studies that include outcomes that might be used to help indicate HIE occurred. These include: Apgar scores,{cite}`costa-ramon_its_2018,costa-ramon_long-run_2022,card_health_2018,jensen_can_2015` the need for assisted ventilation,{cite}`costa-ramon_its_2018,costa-ramon_long-run_2022,card_health_2018` umbilical cord pH,{cite}`costa-ramon_its_2018` and intensive care admission.{cite}`costa-ramon_its_2018,costa-ramon_long-run_2022,card_health_2018`

Of those studies, three used instrumental variable analysis. The instruments used were time of birth,{cite}`costa-ramon_its_2018` a combination of type of day (working or pre-leisure) and type of shift (normal or not),{cite}`costa-ramon_long-run_2022` and relative distance from hospitals with high or low caesarean section rates.{cite}`card_health_2018` One of these studies also used difference-in-differences analysis, comparing outcomes in sibling pairs where the older sibling was born by vaginal delivery and the young sibling was born by emergency caesarean or vaginal delivery.{cite}`costa-ramon_long-run_2022` The final study used a fuzzy regression discontinuity design, as trial results on the use of caesareans in breech births led to a sudden change in caesarean section rates for these births.{cite}`jensen_can_2015`

Beyond those studies, there are several other studies looking at the relationship of caesarean sections with other outcomes less relevant to HIE, including: subsequent fertility and maternal labour,{cite}`halla_cutting_2020` early childhood caries,{cite}`ladeira_caesarean_2021` maternal mental health,{cite}`tonei_mothers_2019` severe maternal morbidity,{cite}`chen_causal_2022` and BMI.{cite}`cavalcante_cesarean_2022`

Three of these studies using instrumental variable analysis, with instruments of day of week,{cite}`halla_cutting_2020` position of the baby in the womb,{cite}`tonei_mothers_2019` and the average number of the delivery cases in the surrounding area of a hospital (reflecting delivery volume with direct effect on outcomes).{cite}`chen_causal_2022` The final two studies used inverse probability of treatment weighting{cite}`cavalcante_cesarean_2022` and a marginal structural model.{cite}`ladeira_caesarean_2021`

### Causal inference

Causal models are designed to test the relationship between a single exposure and outcome whilst controlling for confounding - so it's important to be aware that the other associations found between the covariate and outcome have not been through the same process to control for confounding in their relationship, and so their relationships may still be influenced by residual bias and confounding. This is referred to as Table 2 fallacy.{cite}`lederer_control_2019`

As such, if using causal models, we really only have one focus - and so it doesn't answer the broader question causally - and instead focusses on specific questions, like (a) 'What is the effectiveness of this treatment on this outcome?', and (b) 'What is the impact of this specific variable on the outcome?'.

Hence, if we build a causal model, it doesn't necessarily show true relationships between risk factors and the outcome. In fact, Leder et al. 2018{cite}`lederer_control_2019` even caution against sharing those effect estimates for the other covariates in the model - whilst Hartig 2019{cite}`hartig_mediators_2019` suggests that you make it explicitly clear which variables are reasonaly controlled and which are possibly confounded.

### Aim

Estimate the causal relationship between emergency caesarean section and HIE.

## Methods

Inclusion and exclusion criteria and outcome as in [HIE Proposal #1](./5_proposal_1.md).

### DAG

My current attempt:

````{mermaid}
  flowchart LR;

    L_sen("Confounder (L)<br><b>Sentinal event</b>"):::white;
    L_fhr("Confounder (L)<br><b>Abnormal FHR</b>"):::white;
    U("Unmeasured confounder (U)<br><b>Hypoxia/Asphyxia</b>"):::white;
    A("Treatment (A)<br><b>Caesarean</b>"):::green;
    Y("Outcome (Y)<br><b>Hypoxic ischaemic<br>encephalopathy (HIE)</b>"):::green;
    age("Gestational age<br>BMI"):::white;
  
    age --> L_sen; age --> A;
    L_sen --> U; L_sen --> A;
    A --> Y;
    U --> L_fhr; L_fhr --> A; U --> Y;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Analysis

This section discusses some of the possible approaches to this analysis.

#### Option 1: As in SAMUeL-1

One possible avenue could be to replicate methods used in [SAMueL-1](https://samuel-book.github.io/samuel-1/introduction/intro.html). SAMueL-1 focussed on variation in thrombolysis use between hospitals, to ask the question *"What treatment would my patient receive at hospitals*"? They also then used clinical pathway simulation to ask the question "*What would happen to a hospital’s thrombolysis use of, and benefit from, thrombolysis by changing key aspects of the pathway?*" (e.g. pathway speed, stroke onset times, what majority of high-thrombolysing hospitals would do for patient). Whilst this is not explicitly assessing the effectiveness of interventions, it does teach us which patients low-thrombolysis units and high-thrombolysis units treat differently, assuming that perhaps they might be patients low-thrombolysis units should consider treating.

Applying this to HIE, we could - for example - model **variation in emergency caesarean** use **between hospitals**.
* This would involve comparing units with low and high caesarean rates and looking whether a similar patient would receive a caesarean at a different hospital. However, this may be difficult to interpret, particularly with no information on timing, which is often the key thing of interest (i.e. caesarean too late).
* **How do you incorporate timing of caesarean?** I'm not quite sure. Could you focus just on those who receive a caesarean, and see what factors influence time to receive it? However, we're not learning about intervention effectiveness from this but instead, reasons for time to treatment.
* **What do we learn?**
  * For SAMueL-1, you start in a scenario where there is a demand to increase thrombolysis use, and so seeing which patients are thrombolysed at high v.s. low thrombolysing units, tells you perhaps where the low thrombolysing units could focus.
  * However, do we want to learn that here? In this context, there is not a large demand for more caesareans. Instead, there is a case-by-case scenario where some rare (but expensive) cases intervene too late. There are also cases where caesareans are done unnecessarily.

There are other examples of variables that lead to variation in caesareans. This might be particularly relevant as our first dataset is **only two hospitals**. Other variables include:
* **Time of day** - "*What treatment would my patient receive at a different time of day?*". Steve Thornton comments that "the time of day is important in the rate of delivery. More deliveries tend to happen at night naturally (perhaps because this was safer in long gone times as predators were not around). Also, nowadays because the inductions happen in the morning on the whole, this influences the timing of delivery"
* **Day of week** - hence asking, "*What treatment would my patient receive on a different day of the week?*"

SAMueL-2 incorporates outcomes, although Mike would be better able to reflect on this (as I am not up to speed with how that analysis works).

> Parting remark: Is this appropriate to our context? Caesarean use is a very different context to thrombolysis use. Does it make sense to compare units (or time of day or day of week) with high or low use? Would we want the low use units/times to learn from the high use, or do we actually have issues in both?

#### Option 2: Instrumental variable analysis

Another example of a method we could look at is **instrumental variable analysis**. We first must identify an instrumental variable, which needs to meet the criteria:
* Cause variation in exposure (caesarean)
* Be unrelated to outcome (HIE)

If using an outcome of HIE, then hospital attended should be unrelated to the outcome, and could be used as an instrument (although this wouldn't be true for other outcomes). However, if maternal or pregnancy characteristics indicate a mother is high risk, this could potentially impact which hospital they are sent to, so it may not be perfect. There are lots of other possibilities though, such as variables used in the existing studies mentioned above, which were:
* Time of day
* Day of week
* Type of day
* Type of shift
* Relative distance from hospitals with high and low caesarean rates
* Position of the baby in the womb
* Average number of delivery cases in the surrounding area of a hospital.

Focussing on the example of time of day, our steps for this analysis would be:
1. Test the first assumption of instrumental variable analysis, which is the strength of the relationship between the instrumental variable and the exposure
2. Use two-stage least squares (2SLS) method, which is regression based, and described further on the [instrumental variable page](../causal_methods/c1_instrumental_variable.ipynb)

There have been some papers suggesting methods for instrumental variable analysis that incorporate deep learning, to avoid the assumptions that come with regression like linearity and homogeneity.{cite}`hartford_deep_2017,xu_learning_2021` However, I am not confident in understanding the validity of these methods. Several criticisms (with responses from the authors) can be viewed for Xu et al. 2021.{cite}`xu_learning_2021`

````{mermaid}
  flowchart LR;

    treat("<b>Caesarean</b>"):::green;
    out("<b>HIE</b>"):::green;
    con("Confounders"):::white;
    hosp("Instrumental variable<br>Time of day"):::white;
    hosp --> treat;
    treat --> out;
    con --> treat;
    con --> out;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

> Parting remark: This could be a good option - it is simple, commonly used, accounts for unobserved confounding, and we have a range of candidate instruments

#### Other options

In less detailed, I have listed some of the other options for causal analysis, and provided my current thoughts on their feasibility (although still learning on this, and so as we learn more, we might change thoughts on what is best from below). It excludes multivariable regression (as that is our "risk factors" page) and instrumental variables (as these are discussed above). When considering between these, it would be worth reflecting on the methods **strengths and limitations**, as touched on in the causal inference section of this book.

Conventional methods:
* **Stratification** - unlikely to be feasible (depending on number of confounders and sample size to be able to divide into those stratums)
* **Matching** - potentially feasible, as simply match groups using known characteristics
* **Inverse probability of treatment weighting** - potentially feasible, as simply balance the treated and untreated groups by weights them by their inverse probability of receiving a caesarean section

**G-methods:** We don't have time-dependent confounding (as if you intervene, that is the end of data collection, so we cannot have a feedback loop). Hence, not anticipating any of these to be relevant (although I might be wrong?):
* Marginal structural models
* G-computation
* G-estimation of structural nested models

For unobserved confounding:
* **Regression discontinuity** - unlikely to be feasible as we don't anticipate there being a sudden change in the caesarean section rates for infants with HIE
* **Interrupted time series** - not feasible
* **Difference in differences** - potentially feasible, such as by Costa-Ramón et al. 2022{cite}`costa-ramon_long-run_2022` who compare outcomes in sibling pairs where the older sibling was born by vaginal delivery and the young sibling was born by emergency caesarean or vaginal delivery.{cite}`costa-ramon_long-run_2022`
