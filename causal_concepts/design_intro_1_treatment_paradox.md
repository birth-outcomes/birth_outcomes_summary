# The treatment paradox

`````{admonition} Executive summary
:class: info

A **treatment paradox** is when a prognostic factor:
* (A) Has a **strong relationship** with the outcome, and
* (B) When its present, **triggers an effective treatment**

It will mean that the prognostic factor will appear to have **poorer performance** than it actually has, and hence leading to **underestimation of outcomes** for people with that prognostic factor. For example, may find an unexpected protective relationship between two factors that actually have a harmful relationship.

A treatment paradox is relevant to causal inference studies (as its about the true relationship between the treatment and the outcome, rather than using the presence of treatment to help best predict the outcome).

`````

## What is a treatment paradox?

A **treatment paradox** (or "intervention effect", or "treatment use in a validation study") is 'when a **strong prognostic factor of an adverse outcome triggers an effective treatment**.

In other words, if we wanted to demonstrate the presence of a treatment paradox, we would need to meet two criteria:
1. The prognostic factor has a **strong relationship with the outcome**
2. When the prognostic factor is present, it **triggers an effective treatment** [[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

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

## Why does it matter?

When a strong prognostic factors triggers an effective treatment, it reduces incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will **appear to have a poorer prognostic performance than it actually has.** This can lead to an **underestimation of adverse outcomes for people with that prognostic factor**. [[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518) This leads to a lack of **generalisability**.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) The aim of predictive models will often be to help guide decisions to treat on future patients (i.e. they have not yet received any treatments). **Models trained on treated patients will offer poor/biased performance, underestimating risk, which can be attributed to treatment use in the validation data.**[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

**Example: Intrapartum fever leads to metabolic acidosis, but also triggers a caesarean section.** Because of this:
* We find an **unexpected negative (protective)** relationship between intrapartum fever and metabolic acidosis
* If we include caesarean delivery in the model, we would expect to find a **positive (harmful)** relationship between intrapartum fever and metabolic acidosis [[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

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
* Due to this treatment paradox, you will find that babies **born within 30 minutes will consistently contain a higher proportion of babies in poorer condition**, but that this likely due to this disparity (treatment paradox), rather than being due to differences in speed of delivery.'[[source]](https://www.nice.org.uk/guidance/ng192/evidence/full-guideline-pdf-9071942942)

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

## Treatment paradox for caesarean and HIE

In our case, we have a treatment paradox as indicators of poor outcome (e.g. abnormal fetal heart rate (FHR), gestational age) will trigger an effective treatment (caesarean). Hence, if we fit a prediction model where those indicators were used to predict risk of HIE, the relationship between the indicators and outcome will be biased by the selection to receive treatment which helps prevent the outcome, e.g.
* Protective relationship between abnormal FHR and HIE, even though abnormal FHR is an indicator that there is likely something wrong
* Protective relationship between gestational age and HIE, even though we know later gestational age makes sentinal events that lead to hypoxia more likely, but masked by the fact that it also makes selection for caesarean section more likely

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    ind("Indicators of HIE<br>(e.g. abnormal FHR,<br>gestational age)"):::white;
    csection("Caesarean section"):::white;
    poor("Hypoxic ischaemic encephalopathy"):::white;

    %% Produce the figure
    ind --> csection;
    csection --> poor;
    ind --> poor;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
````

## How do we deal with the treatment paradox?

Our concern here is that we are interested in the true causal relationships at play, and not just in predicting HIE. If we were just interested in predicting HIE, it wouldn't matter that gestational age appears protective. However, if you then concluded that indivudals with a later gestational age would benefit less from a caesarean, (we anticipate) that that would be a incorrect and harmful conclusion. Therefore, we are **interested in causal inference, and not in prediction**.

## Commentary on prognostic models in obstetrics

**This commentary introduces some of the problems facing prediction mdoels in obstetrics - ending on the note of how they handle interventions in the prediction model** (the paper then continues on to focus on the treatment paradox).

'Historically, the field of obstetrics has been successful in developing prediction models but has been poor in fully validating and thus implementing them effectively... Only two thirds of the papers [62.4%, 164/263] in a large systematic review of prognostic models in obstetrics were found to have presented their models in such a way that external validation would be feasible. This has been highlighted as a concern given the importance of validity in the development of such models.'[[Murphy et al. 2019]](https://doi.org/10.5772/intechopen.87311)

'Certain models can be too complex for routine clinical usage and this may lead to a reluctance on the part of the clinicians to accept them... It is also important that models which have been developed are also validated in a new population as otherwise it may not be possible to generalise them to a different cohort of patients. This is also known as impact analysis and this paper by Reilly et al. highlights that very few prediction models have undergone formal impact analysis or validation. This is essential in order for clinicians to know if the usage of such a model will have a positive or negative effect, i.e. is there a possibility that it will cause harm. The authors highlighted the benefit of having clinicians involved in the development and validation of such models before, during and after implementation.'[[Murphy et al. 2019]](https://doi.org/10.5772/intechopen.87311)

'Obstetrics focuses on the early identification of pregnancies at risk of adverse outcomes to plan targeted intervention. Clinicians often use probabilistic reasoning, intuitively based on clinical history and tests, to assess the risk of complications in a mother or fetus; however, they need to be aware of false-positive and false-negative test results in their clinical decision-making.

Prediction models (also known as prognostic models) provide individualised risk estimates for clinically important outcomes in patients with a particular disease or condition. Derived using statistical models, they include multiple predictors, such as age, previous history, and, increasingly, biomarkers. Although clinicians’ intuition has a place and a role in prediction, it has been shown that statistical prediction models give more accurate prognosis than clinicians can achieve working on their own. As in other clinical fields, the development and use of prediction models in obstetrics has limitations.

In the development phase there are many statistical challenges, including:
* The ascertainment of a suitable sample size
* The choice of candidate predictors
* Reliable measurement of the outcome and predictors
* The identification of important predictors and their functional form
* Internal validation, potentially including bootstrap resampling and cross-validation, as well as shrinkage for potential over-optimism in model performance.

Most, if not all, models perform well when they are internally validated; however, the use of prediction models has been hampered by a distinct lack of research into the external validation of prediction models distant from the specific population that they were developed in, and the assessment of models on the behaviour of doctors and on patient outcomes. Another issue that limits clinical use... is the handling of interventions in the prediction model.'[[source]](https://doi.org/10.1111/1471-0528.13859)
