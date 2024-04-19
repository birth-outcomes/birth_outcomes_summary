# HIE proposal 1: predicting HIE

## Paradigm and framing of research problem

### Causal inference

This is **not predictive research**. In a predictive research study, your aim is to predict an outcome with the best accuracy, and although you may be interested in how those predictions were made, you don't made whether those are true relationships or not between the predictor and outcome.[[Ramspek et al. 2021]](https://link.springer.com/article/10.1007/s10654-021-00794-w)

We are interested in the **true relationships** between predictors and the outcome. As such, in design of the study, one of our primary concerns is to account for the impact of treatment on relationships (referred to as the intervention effect or treatment paradox). This is when a predictor is: (a) related to the outcome, and (b) triggers an effective treatment that prevents the outcome. The consequence of this is that predictors can appear to have a poorer prognostic performance that they actually do in reality, leading to underestimation of adverse outcomes.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8) [[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

In the case of HIE, an example is an abnormal CTG, which is indicative of high risk of HIE having occurred, and triggers a caesarean. With our focus being more broadly on any adverse neonatal outcomes, this would become a wider range of observations and characteristics before or during labour, which would trigger the decision to do an elective or emergency caesarean.

### Using the "language of causal inference" to describe our research problem

There are three "languages" for causality: potential outcomes (counterfactuals), graphs, and structural equation models. I will describe our research problem using the former two.

We want to identify pregnancies at high risk of HIE, whilst accounting for the effect that treatment use has on these relationships. 

We want to understand the effectiveness of caesarean section in preventing adverse neonatal outcomes.

Causal models are designed to test the relationship between a signle exposure and outcome whilst controlling for confounding - so it's important to be aware that the other associations found between the covariate and outcome have not been through the same process to control for confounding in their relationship, and so their relationships may still be influenced by residual bias and confounding. This is referred to as Table 2 fallacy.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

As such, if using causal models, we really only have one focus - and so it doesn't answer the broader question causally - and instead focusses on specific questions, like -
* What is the effectiveness of this treatment on this outcome
* What is the impact of this specific variable on the outcome

Hence, if we build a causal model, it doesn't necessarily show true relationships between risk factors and the outcome. In fact, [Leder et al. 2018](https://doi.org/10.1513/AnnalsATS.201808-564PS) even caution against sharing those effect estimates for the other covariates in the model - whilst [Hartig 2019](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/) suggests that you make it explicitly clear which variables are reasonaly controlled and which are possibly confounded.

<mark>explain why we can view it as being treatment - outcome as focus, and not just treatment as a confounder of predictor - outcome</mark>
* Because its what we hope to learn - in making our prediction model, we're trying to understand who needs treatment
* BUT IS IT? DO WE HAVE TO? think about IPTW - there, treatment is treated more like a confounder. do you still say it like tretment - outcome? have a look at examples.

<mark>add coutnerfactual description of problem</mark>

<mark>add DAG</mark>

---

## Methods

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
