# HIE Proposal (intervention)

As in [HIE Proposal #1](./5_proposal_1.md), this is just an **example** of how we could design this study. Here, I am assuming a focus on **assessing the effectiveness of caesarean section as a intervention for HIE**.

## Introduction

As in [HIE Proposal #1](./5_proposal_1.md).

### Existing studies

<mark>summarise studies for HIE from previous studies section</mark>

### Causal inference

Causal models are designed to test the relationship between a sinhle exposure and outcome whilst controlling for confounding - so it's important to be aware that the other associations found between the covariate and outcome have not been through the same process to control for confounding in their relationship, and so their relationships may still be influenced by residual bias and confounding. This is referred to as Table 2 fallacy.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

As such, if using causal models, we really only have one focus - and so it doesn't answer the broader question causally - and instead focusses on specific questions, like -
* What is the effectiveness of this treatment on this outcome
* What is the impact of this specific variable on the outcome

Hence, if we build a causal model, it doesn't necessarily show true relationships between risk factors and the outcome. In fact, [Leder et al. 2018](https://doi.org/10.1513/AnnalsATS.201808-564PS) even caution against sharing those effect estimates for the other covariates in the model - whilst [Hartig 2019](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/) suggests that you make it explicitly clear which variables are reasonaly controlled and which are possibly confounded.

### Aim

Estimate the causal relationship between emergency caesarean section and HIE.

Represened as DAG:

````{mermaid}
  flowchart LR;

    t("Emergency<br>caesarean section"):::white;
    o("HIE"):::white;

    t --> o;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

<mark>add counterfactual description</mark>

## Methods

Inclusion and exclusion criteria and outcome as in [HIE Proposal #1](./5_proposal_1.md).

### Analysis

<mark>Mike's ideas - 'This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations. We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.'</mark>

#### As in SAMUeL-1

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

SAMueL-2 incorporates outcomes.<mark>i'm less clear on how it works</mark>

#### Instrumental variable analysis

Another example of a method we could look at is **instrumental variable analysis**. We first must identify an instrumental variable, which needs to meet the criteria:
* Cause variation in exposure (caesarean)
* Be unrelated to outcome (HIE)

Many of the variables listed above - **hospital attended, time of day, day of week** - may be good candidates.

For hospital attended though, if there are any concerns prior to labour, which are linked to outcome, which dictate where the person gives birth - although I'm not sure if this is definitely a true concern or not.

Example:

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

To perform this analysis, we would want to test the first assumption of instrumental variable analysis, which is the strength of the relationship between the instrumental variable and the exposure. We would then use the two-stage least squares (2SLS) method, which is regression based, and described further on the [instrumental variable page](../causal_methods/c1_instrumental_variable.ipynb)

There have been some papers suggesting methods for instrumental variable analysis that incorporate deep learning, to avoid the assumptions that come with regression like linearity and homogeneity.{cite}`hartford_deep_2017,xu_learning_2021` However, I am not confident in understanding the validity of these methods. Several criticisms (with responses from the authors) can be viewed for Xu et al. 2021.{cite}`xu_learning_2021`

### IPTW

mike - or condition model on propensity score for likelihood of mother to have caesarean)