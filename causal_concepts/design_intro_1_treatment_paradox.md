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
