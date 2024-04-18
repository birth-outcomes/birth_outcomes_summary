# Introduction to causal study design and methods

This page describes how to design a causal inference study, and provides a brief overview of the possible methods you could use within your study.

The gold standard method for inferring causality is randomisation - e.g. randomising patients to receive a treatment or not. This is because it removes confounding - it removes the common cause of the treatment and outcome, since the only cause of treatment was randomisation.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) When we are using **observational data**, there are a variety of possible methods for causal effect estimation.

## Identifying the focus of the research

The first step will be to clearly specify your **research question**. You can do so using the counterfactuals approach, directed acyclic graphs, or structural equation models. When you do this, you need to identify a **single exposure and outcome**, for which you want to estimate a causal effect. The exposure is a variable that can take one of several counterfactual values. It will often be a treatment or intervention.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

You **cannot** be focussed on the relationship of **several** different variables with the outcome! This is because we design our study around identifying the true causal relationship between those two variables, but any other variables included in modelling or so on will still be vulnerable to residual confounding or biases, as we haven't designed the study around them. The reporting of the relationships of those other variables with the outcome is known as **Table 2 fallacy**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## Methods for causal effect estimation

<mark>write summary</mark>