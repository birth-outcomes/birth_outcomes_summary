# HIE Proposal #2

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

#### As in SAMUeL-1

There is not one right way to perform this analysis. However, a good starting point could be to replicate the methods used in [SAMueL-1](https://samuel-book.github.io/samuel-1/introduction/intro.html) (which focussed on variation in thrombolysis use between hospitals). For this, we would be - for example - comparing the incidence of HIE between similar patients who received an emergency caesarean versus those who had a vaginal delivery.

Here, we would:
* Model variation in use of emergency caesareans between hospitals so we can ask: *'What treatment would my patient receive at other hospitals?'*
* Model the delivery pathway, using clinical pathway simulation, so we can ask the question: *'What would happen to a hospital's use of and benefit from use of emergency caesarean sections, by changing key aspects of the pathway*, especially focussing on timing of the caesarean

However, this doesn't necessarily need to be just between hospitals - you can, for example, look at variation in use of emergency caesarean by:
* Time of day - Steve Thornton comments that "the time of day is important in the rate of delivery. More deliveries tend to happen at night naturally (perhaps because this was safer in long gone times as predators were not around). Also, nowadays because the inductions happen in the morning on the whole, this influences the timing of delivery"
* Weekday v.s. weekend

When look into timing of caesarean, there is no simple way to define timing, but possibilities include:
* The presence of multiple (𝑘) risk factors.
* Length of labour, or length of Stage-II labour.
* Cervical dilation (Steve: This is the standard method of determining the length of labour. The time from the start is really variable and inaccurate)
* Contraction rate/force (Steve: Unfortunately, we cannot determine the force of contraction, only the timing which is really important for any changes in the fetal heart rate)

Mike's ideas - 'This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations. We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.'

#### Using causal inference methods

Would recommend we explore a selection of methods to answer the same problem.

<mark>summarise options, give IV example, how to convert sam1 to IV</mark>
