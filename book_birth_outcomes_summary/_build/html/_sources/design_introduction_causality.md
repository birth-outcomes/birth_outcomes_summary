# The problem: prediction, causation and the treatment paradox

`````{admonition} Executive summary
:class: info

Predictive research aims to predict an outcome with the **best accuracy**. Explainability (e.g. SHAP) is about understanding why a model makes certain predictions. When making predictions, whether the direction of relationships (e.g. from SHAP values) is true/causal doesn't matter, as the goal is just to make the best predictions.

Etiological research aims to **uncover causal effects**. It involves finding an unbiased estimate of the effect of X on Y, by controlling for confounding factors that could bias the estimate. In causal inference, the true direction of relationships (and the counterfactual scenarios) are important. It typically starts with drawing a causal diagram.

A **treatment** paradox is when a prognostic factor (a) has a strong relationship with the outcome, and (b) when its present, triggers an effective treatment. It will mean that the prognostic factor will appear to have poorer performance than it actually has, and hence leading to underestimation of outcomes for people with that prognostic factor.
* A treatment paradox is relevant to causal inference studies (as its about the true relationship between the treatment and the outcome, rather than using the presence of treatment to help best predict the outcome).
* In our study, we are interested in the true relationship between ceasareans and HIE, and this is confounded by the presence of hypoxia, which can lead to HIE but also can trigger a caesarean, thereby creating a treatment paradox.
`````

## The difference between predictive and etiological research

### Types of research

Scientific research can be categorised into descriptive, predictive and etiological research.

**Descriptive research** aims to summarise the characteristics of a group (or person).[[Hamaker et al. 2020]](https://doi.org/10.1016/j.dcn.2020.100867)

**Predictive research** aims to predict an outcome with the **best accuracy**.[[Ramspek et al. 2021]](https://link.springer.com/article/10.1007/s10654-021-00794-w)  It doesn't matter whether predictors are causal or not - just focussed on best prediction. We're interested in associations (i.e. relationships aren't directional).[[source]](https://stats.stackexchange.com/questions/56909/what-is-the-relation-between-causal-inference-and-prediction)

**Etiological research** (or "explanatory" research) aims to uncover **causal effects** - i.e. **causal inference**. It is important that relationships are **directional**, as these directions are required to support interventional reasoning.[[source]](https://stats.stackexchange.com/questions/56909/what-is-the-relation-between-causal-inference-and-prediction)

### Causal inference

In etiogical research, we want an unbiased estimate of the effect of X and Y - i.e. estimate of the causal effect of an exposure on an outcome[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) When it comes to defining causality, pioneers in causal inference have come up with three definitions/languages, with the strengths of each listed:
1. **Counterfactuals** (also called **potential outcomes**) - good for articulating the inference for a small number of causes and effects
2. **Causal graphical models** - good for understanding the scientific problems
3. **Structural equation models** - good for fitting simultaneous models for the variables (espeically for abstract concepts)[[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)

#### Counterfacturals / Potential outcomes framework

To **define a causal effect**, we use the **potential outcomes framework** (also known as counterfactural or equivalent concepts approach[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) or Rubin or Neyman-Rubin causal model). This framework 'uses **mathematical notation** to describe **counterfactual outcomes** and can be used to describe the causal effect of an exposure on an outcome in statistical terms'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Some key terms in the potential outcomes framework:
* **Counterfactuals** are a comparison between what is and what might have been (e.g. treatment v.s. no treatment).
  * *For example, I know ingesting the poison killed John, because if John hadn't ingested the poison, I know he would have lived.* [No source]
  * 'The counterfactual outcomes of a specific individual can never be known, since we can never observe the same individual both exposed and unexposed under the same circumstances' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
* **Exposure (A)** = 'treatment, intervention or other variable that could have taken one of several counterfactual values'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
  * We are often focussed on **interventions** (i.e. variables that can be manipulated), as they fit well in the potential outcomes framework. Although other variables like age, race and gender can have causal effects, they do not fit as cleanly in the potential outcomes framework.[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) Rubin states that *"if you are not talking about an intervention, you can't talk about causality"* - i.e. we're defining causality using counterfactuals, which is about the counterfactual effects of the intervention[[source]](https://baselbiometrics.github.io/home/docs/trainings/20210202/1_Moffa.pdf)
* **Outcome (Y)**

'Potential outcomes refer to **all possible outcomes** that an individual could experience—both those which are observed (factual) and those which are not (counterfactual). Given a binary exposure and a binary outcome, the possible combinations of actual and counterfactual outcomes give rise to four causal types':
* '**‘Doomed’**: would have experienced the outcome regardless of exposure.'
* '**‘Causative’**: would have experienced the outcome if exposed, otherwise not.'
* '**‘Preventative’**: would have experienced the outcome if unexposed, otherwise not.'
* '**‘Immune’**: would not have experienced the outcome regardless of exposure status.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

There are various notations used, but some examples are:
* Potential outcome if exposed (Y<sup>a=1</sup>) or not exposed (Y<sup>a=0</sup>)
* Expected value of continuous outcome (E(Y)) or probability of binary outcome(P(Y=1))
* Conditional expectation - expected value of Y given that another variable C is 1 (E(Y|C=1)) - i.e. expected values conditional on C / within levels of C / holding C constant. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

#### Individual v.s. average

Causal inference for an individual (generating **individual causal effects**) is generallly impossible in health and social sciences (as you can't go back in time and not give them the outcome) - instead, causal inference focusses on **average causal effect** when comparing groups of individuals.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)

#### Terminology

Terminology can vary. Lederer et al. 2018 recommend that, by acknowledging the intent, it is reasonable to use the labels:
* **Causal association**
* **Effect estimate**

But not:
* Causal effect
* Exposure has an 'effect' or 'impact' on outcome
* Exposure 'protects against' or 'promotes' outcome

As these make claims of causality that should be avoided without substantial evidence of a true causal effect.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

### Confusion and controversy around causality

Why?
* Causally unrelated variables can be highly correlated
* Results may be reported in a way that is careful to avoid referring to any causal relationships, but it will often still naturally be read and interpreted as causal
* Even if there is a causal relationship, sometimes the direction is unclear - would need to carefully examine the temporal relationships between the variables[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/x4UMR/confusion-over-causality)

In practice, prediction and causation are commonly **conflated**. A review of observational studies found that 26% (46 / 180) observational cohort studies conflated between etiology and prediction -
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

In the language of causal inference:
* Treatment is a mediator
* We are interested in the bottom arrow - the direct causal effect of the exposure on the outcome - i.e. effect not due to mediator
````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    exp("Exposure"):::white;
    treat("Treatment"):::white;
    out("Outcome"):::white;

    %% Produce the figure
    exp --> treat;
    treat --> out;
    exp --> out;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
````

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

## Choosing between prediction and causality

### Sometimes we're interested in both

Many problems will require a **combination of prediction and causation**.
* "Pure forecasting task" - e.g. just want to predict whether or not it will rain, and don't care why/what caused the rain
* "Pure causation task" - e.g. performing a rain dance presumed to save dying crops, only if it actually causes rain
* Combination of the two - e.g. if planning assignment of fire inspectors across a city, should (a) predict will establishment will be in violation of fire codes, and (b) estimate causal effect on establishment's behaviour of receiving an inspection or not

Beck et al. 2018 also argue that **prediction remains relevant even if you're only interested in understanding causal effects**. Explanations that invoke causal mechanisms always make predictions - specifically, predictions about what will happen under an intervention. 'Whether they do so explicitly or not, that is, causal claims necessarily make predictions; thus it is both fair and arguably useful to hold them accountable for the accuracy of the predictions they make.' They therefore argue that the **predictive performance of models and of explanations** is important to include (e.g. R<sup>2</sup>, MAE, RMSE, AUC, accuracy, recall, F1).[[Beck et al. 2018]](https://doi.org/10.31219/osf.io/u6vz5)

### The ladder of causality

Judea Pearl proposed the '**Ladder of Causality**' to categorise different levels of causal thinking, with increasing levels of difficulty.

| Level | Typical activity | Typical questions | Examples |
| --- | --- | --- | --- |
| **Association** | Seeing | What is?<br>How would seeing X change my belief in Y? | What does a symptom tell me about a disease?<br>What does a survey tell us about the election results? |
| **Intervention** | Doing | What if?<br>What if I do X? | What if I take aspirin, will my headachbe be cured?<br>What if we ban cigarettes? |
| **Counterfactuals** | Imagining, retrospection | Why?<br>Was it X that caused Y?<br> What if I had acted differently? | Was it aspirin that stopped my headache?<br>Would Kennedy be alive had Oswald not shot him?<br>What if I had not been smoking the past two years? |

[[source]](https://cacm.acm.org/magazines/2019/3/234929-the-seven-tools-of-causal-inference-with-reflections-on-machine-learning/fulltext?mobile=false)

Difference between interventions and counterfactuals in this hierarchy:
* With interventions, you ask what will happen on average if you perform an action.
* With counterfactuals, you ask what would have happened if you had performed a different action.
* These two queries are mathematically distinct as they require different levels of information to be answered (counterfactuals need more information to be answered)'.[[source]](https://stats.stackexchange.com/questions/379799/difference-between-rungs-two-and-three-in-the-ladder-of-causation)

## Our study - are we interested in prediction or causation?

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

### Current recommendation

On the surface, you may assume we just want to predict outcomes, but (a) we're interested in causal relationships - hence why we're so concerned by the treatment paradox, and (b) the application of making treatment decisions requires understanding of counterfactuals.

To **demonstrate existence of the treatment paradox** (by comparison to models that are causal), and to allow comparability to other studies:
* **Prediction model (association)** - can we predict HIE

To actually **explore the proposed research question**:
* **Causality (intervention)** - what is the causal relationship between caesarean and HIE?
* **Counterfactuals** - what would have happened if we had done or not done the caesarean?

We should:
* Reporting predictive accuracy of all models
* Being explicitly clear which variables in a model were considered in design of the causal model (to avoid Table 2 fallacy)