# The problem: prediction, causation and the treatment paradox

`````{admonition} Executive summary
:class: info

Predictive research aims to predict an outcome with the **best accuracy**. Explainability (e.g. SHAP) is about understanding why a model makes certain predictions. When making predictions, the direction of relationships (e.g. from SHAP values) doesn't matter, as the goal is just to make the best predictions.

Etiological research aims to **uncover causal effects**. It involves finding an unbiased estimate of the effect of X on Y, by controlling for confounding factors that could bias the estimate. In causal inference, the true direction of relationships (and the counterfactual scenarios) are important. It typically starts with drawing a causal diagram/

A **treatment** paradox is when a prognostic factor (a) has a strong relationship with the outcome, and (b) when its present, triggers an effective treatment. It will mean that the prognostic factor will appear to have poorer performance than it actually has, and hence leading to underestimation of outcomes for people with that prognostic factor.
* A treatment paradox is relevant to causal inference studies (as its about the true relationship between the treatment and the outcome, rather than using the presence of treatment to help best predict the outcome).
* In our study, we are interested in the true relationship between ceasareans and HIE, and this is confounded by the presence of hypoxia, which can lead to HIE but also can trigger a caesarean, thereby creating a treatment paradox.
`````

## The difference between predictive and etiological research

### Definitions

**Predictive research** aims to predict an outcome with the **best accuracy**. It doesn't matter whether predictors are causal or not - just focussed on best prediction. We're interested in associations (i.e. relationships aren't directional)

**Etiological research** aims to uncover **causal effects** - i.e. **causal inference**.
* We want an unbiased estimate of the effect of X and Y - i.e. estimate of the causal effect of an exposure on an outcome
* It is important that relationships are **directional**, as these directions are required to support interventional reasoning.
* The goal is to control for other variables in such a way that the effect size obtained matches that which we would find if the target predictor was manipulated in a controlled intervention (experience/RCT)
* To perform causal inference, we first start by drawing a **causal diagram**, which then guides methodological choices.
* Causal inference for an individual (generating individual causal effects) is general ly impossible in health and social sciences (as you can't go back in time and not give them the outcome) - instead, causal inference focusses on **average causal effect** when comparing groups of individuals.
* When we're talking about one thing causing another, this is based in counterfactuals. **Counterfactuals** (or equivalent concepts) are needed to define causal effects. Knowing the counterfactual outcomes can be referred to as knowing the outcomes under treatment and under no treatment. For example, I know ingesting the poison killed John, because if John hadn't ingested the poison, I know he would have lived.

[[Ramspek et al. 2021]](https://link.springer.com/article/10.1007/s10654-021-00794-w) [[source]](https://stats.stackexchange.com/questions/56909/what-is-the-relation-between-causal-inference-and-prediction)[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 

### Confusion

**These are commonly conflated**. The findings of etiological and predictive research can often get conflated when reported and interpreted - a review of observational studies found that 26% (46 / 180) observational cohort studies conflated between etiology and prediction.
* In causal studies, this was mainly due to selection of covariates based on their ability to predict **without taking causal structure into account**.
* In prediction studies, this was mainly due to **causal interpretation** of covariates included in a prediction model.

### Explainability v.s. causality

Explainability refers to being able to **understand why a model makes certain predictions**. The aim of explainable AI is to make ML models more transparent. It provides insights on:
* How a model makes predictions
* What features are most important
* How sensitive a model is to changes in the input

However, it cannot be used to infer causal relationships, since the findings may be biased by stratification or unmeasured confounders, or mediated by other factors in the causal pathway.[[Prosperi et al. 2020]](https://doi.org/10.1038/s42256-020-0197-y) If you wish to make claims about causality, you will need to build a casual model. Causal ML aims to **infer causal relationships** from observational data by estimating the effect of a specific variable on the outcome, while controlling for other confounding factors that could bias the estimate.[[source]](https://medium.com/@dahnert.sebastian/understand-the-difference-and-intersection-between-causal-ml-and-explainable-ai-65583132e704)

## How do you know whether you are interested in prediction or causation?

**Example:** A team have built an XGBoost model to predict whether customers will renew their subscription. They use SHAP values to understand how the model made its predictions. They notice a suprising finding: **users who report more bugs are more likely to renew. Is this a problem? It depends on their goal**

* If their goal is to **predict customer retention to estimate future revenue**, then this relationship is helpful for **prediction**, and it doesn't matter about the direction, as long as our predictions are good.

* However, if their goal is to **inform actions to help retain customers**, then it important to understand the true relationships between features and the outcomes, and the counterfactual scenarios if features were modified. In this case, the team are interested in **causation**. In order for the team to understand the causal relationships, they would need to use causal inference methods (causal diagrams, appropriate techniques to account for confounding).

**Why did this finding occur?** If the team are interested in causation, they could draw a causal diagram (simplified version below). In it, they notice that some features are influenced by unmeasured confounding. WIth the example above, **users who report more bugs are people who use the product more so encounter more bugs, but need the product more so are more likely to report**. Because they can’t directly measure product need, the correlation they end up capturing in the predict model between bugs reported and renewal combines a small negative direct effect of bugs faced and a large positive confounding effect from product need.


````{mermaid}
  flowchart LR;

    need("<b>Unmeasured</b><br>Product need"):::white;
    month("Monthly usage"):::white;
    face("<b>Unmeasured</b><br>Bugs faced"):::white;
    report("Bugs reported"):::white;
    ren("Did renew"):::important;


    month --> face; face --> report; face --> ren;
    need --> report;
    need --> month;
    need --> ren;
    month --> ren;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef important fill:#DDF2D1, stroke: #FFFFFF;
````

## The treatment paradox

A **treatment paradox** (or "intervention effect", or "treatment use in a validation study") is 'when a **strong prognostic factor of an adverse outcome triggers an effective treatment, thus reducing incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will appear to have a poorer prognostic performance than it actually has.**' This can lead to an **underestimation of adverse outcomes for people with that prognostic factor**.

In order for a treatment paradox to occur, two criteria must occur:
1. The prognostic factor has a strong relationship with the outcome
2. When the prognostic factor is present, it triggers an effective treatment

If you wanted to demonstrate the presence of a treatment paradox, you would need to demonstrate the two criteria above.[[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

The consequence of this is a lack of **generalisability**.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) The aim of predictive models will often be to help guide decisions to treat on future patients (i.e. they have not yet received any treatments). Models trained on treated patients will offer poor/biased performance, underestimating risk, which can be attributed to treatment use in the validation data.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Example of the treatment paradox in obstetrics

**Example 1: Intrapartum fever leads to metabolic acidosis, but it also triggers a ceasarean.**
* Due to this treatment paradox, you will find an unexpected negative (protective) relationship between intrapartum fever and metabolic acidosis
* If you include caesarean delivery in the model, you will find the expected positive relationship between intrapartum fever and metabolic acidosis

[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    fever("Intrapartum fever"):::white;
    cs("Ceasarean section"):::white;
    met("Metabolic acidosis"):::white;

    %% Produce the figure
    fever --> cs;
    cs --> met;
    fever --> met;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
````

**Example 2: Fetal compromise would lead to poor outcomes, but it also triggers quicker delivery (e.g. caesarean)** (as in the NICE 2011 Caesarean guidance).
* Due to this treatment paradox, you will find that babies born within 30 minutes will consistently contain a higher proportion of babies in poorer condition, but that this likely due to this disparity (treatment paradox), rather than being due to differences in speed of delivery.'[[source]](https://www.nice.org.uk/guidance/ng192/evidence/full-guideline-pdf-9071942942)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    comp("Compromised"):::white;
    quick("Quicker delivery"):::white;
    poor("Poor outcomes"):::white;

    %% Produce the figure
    comp --> quick;
    quick --> poor;
    comp --> poor;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
````

**Other examples** (not detailed):
* Epidural, pyrexia (fever), and birth outcomes
* Pre-term birth, tocolytics, and birth outcomes[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859) (tocolytics are drugs used to slow/stop contractions, typically given to women in pre-term labour)
* Pre-eclampsia, treatments (e.g. magnesium sulphate and parenteral antihypertensives), length of delivery, etc.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

## Our study: are we interested in prediction or causation?

We are interested in whether and when caesareans should be performed, to prevent the development of hypoxic ischaemic encephalopathy.

We could build a **predictive model**, where caesarean is included along various other predictors, with the outcome of predicting HIE. We might build an XGBoost model, for example, and use SHAP values to understand how the predictions were made. In doing so, we might notice **an unexpected relationship between HIE and caesarean (e.g. no effect)**. Is this a problem? It depends on our goal.

* If our goal is to **predict infants with HIE so we can estimate the likely prevalence** then it doesn't matter, as we're just interested in making a good prediction.

* However, if our goal is to understand **whether we should be doing those ceasareans**, then this is very important, as we are interested in whether doing a caesarean has a causal relationship with HIE.

If we drew a causal diagram (simplified), we might see that the relationship is confounded by hypoxia - e.g. if infants are experiencing hypoxia, and a caesarean is performed, and then are less likely to have HIE. This is an example of a **treatment paradox**, where we have performed the treatment (caesrean) due to presence of a prognostic factor (hypoxia, indicated by abnormal FHR) for the outcome (HIE).

````{mermaid}
  flowchart LR;

    L_sen("Sentinal event"):::white;
    L_fhr("Abnormal FHR"):::white;
    U("Hypoxia"):::white;
    A("Caesarean"):::important;
    Y("Hypoxic ischaemic<br>encephalopathy (HIE)"):::important;
    Empty[ ]:::empty;
    Mod("Timing of caesarean"):::white;
    
    L_sen --> U; L_sen --> A;
    Mod --> Empty;
    A --- Empty; Empty -->|?| Y;
    U --> L_fhr; L_fhr --> A; U --> Y;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef important fill:#DDF2D1, stroke: #FFFFFF;
````