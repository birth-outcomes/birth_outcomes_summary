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

A **treatment paradox** (or "**intervention effect**", or "**treatment use** in a validation study") is 'when a **strong prognostic factor of an adverse outcome triggers an effective treatment**.

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

**Lack of generalisability** - the aim of predictive models will often be to help guide decisions to treat on future patients (i.e. they have not yet received any treatments). **Models trained on treated patients will offer poor/biased performance, underestimating risk, which can be attributed to treatment use in the validation data.**[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

The impact of treatment use depends on various factors...
* Strength of effect of treatment on outcome - e.g.
  * If weak effect, then impact will be small[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)
  * When a strong prognostic factors triggers an effective treatment, it reduces incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will **appear to have a poorer prognostic performance than it actually has.** This can lead to an **underestimation of adverse outcomes for people with that prognostic factor**. [[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518) This leads to a lack of **generalisability**.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)
* Proportion of individuals receiving treatment
* Underlying pattern of treatment use
* Whether treatment is allocated randomly or based on individual risk profile or based on strict treatment guidelines - e.g.
  * If high-risk individuals are selectively treated, this will have a large impact - '**distribution of observed risks will become narrower**, due to the risk-lowering effects of treatment in the high-risk individuals,  making it **more difficult for the model to discriminate** between individuals who will or will not develop the outcome, and the calibration in high-risk individuals will be most greatly affected'[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Is this relevant to obstetrics?

Absolutely! In fact, obstetric examples are quite commonly cited in papers about the treatment paradox, and there are a few papers focused on this, such as the paper by [Cheong-See et al. 2016](http://dx.doi.org/10.1111/1471-0528.13860) - '**Prediction models in obstetrics: understanding the treatment paradox and potential solutions to the threat it poses**'.

They describe clinicians use "probabilitic reasoning" to identify high risk pregnancies (based on clinical history and tests) - and how there is potential benefit for data-driven prediction/prognostic models providing individualised risk estimates are relevant in helping identify pregnancies at risk of adverse outcomes, to help guide clinical management and targeted interventions - as we are hoping to explore in this project.

They describe common statistical challenges - which are relevant to us also:
* The ascertainment of a suitable sample size - this is likely to be a problem, particularly if we choose a specific endpoint like HIE
* The choice of candidate predictors
* Reliable measurement of the outcome and predictors
* The identification of important predictors and their functional form
* Internal validation, potentially including bootstrap resampling and cross-validation, as well as shrinkage for potential over-optimism in model performance.
* Lack of external validation (many obstetric models perform well when internally validated but few have been externally validated using a population seperate from development) - *see end of page for a few extra notes on this*
* Lack of evaluation of the impact of models on clinician behaviour and patient outcomes
* **Handling of interventions in the prediction model** [[Cheong-See et al. 2016]](http://dx.doi.org/10.1111/1471-0528.13860)

See examples below...

### Examples

**Intrapartum fever leads to metabolic acidosis, but also triggers a caesarean section.** Because of this:
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

**Fetal compromise would lead to poor outcomes, but it also triggers quicker delivery (e.g. caesarean)** (as in the NICE 2011 Caesarean guidance).
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

**High blood pressure leads to poor outcome, but also triggers effective treatment (antihypertensive, delivery)**. A recent model for adverse outcomes in women with pre-eclampsia did not identify high blood pressure as a predictor. This may be due to the treatment paradox, as 'women with high blood pressure are likely to receive effective interventions (antihypertensive or delivery)' - and this effective treatment means they are unlikely to develop the outcome.
* 'If blood pressure is truly a predictor of high(er) risk in untreated patients, effective intervention will make it look like a poor predictor during the development of a model in treated patients. This problem frequently jeopardises obstetric modelling, altering the true predictor–outcome association and the natural outcome rate (incidence).'
* 'In pre-eclampsia, a prediction model without blood pressure risks overlooking patients with high blood pressure, and may actually underestimate the outcome risks (as an important predictor is missed).' [[Cheong-See et al. 2016]](http://dx.doi.org/10.1111/1471-0528.13860)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    bp("High blood pressure"):::white;
    adverse("Adverse outcomes"):::white;
    treat("Treatment (antihypertensive<br>or delivery)"):::white;

    %% Produce the figure
    bp --> adverse;
    treat --> adverse;
    bp --> treat;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
````


**Other examples** (not detailed):
* Epidural, pyrexia (fever), and birth outcomes
* Pre-term birth, tocolytics, and birth outcomes[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859) (tocolytics are drugs used to slow/stop contractions, typically given to women in pre-term labour)


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

We could demonstrate the **existence** of this paradox as they do in [Uffen et al. 2021](https://doi.org/10.1136%2Fbmjopen-2020-046518) - in which the aim of their study was to 'evaluate the existence of a treatment paradox by determining the influence of baseline qSOFA on treatment decisions within the first 24 hours after admission' - with patients with particularly values of qSOFA have higher odds of receiving intensive therapy, fast antibiotic administration, or vasopressic therapy.

## How do we deal with the treatment paradox?

In their paper, [Cheong-See et al. 2016](https://doi.org/10.1111/1471-0528.13859) convene 'a panel of experts in pre-eclampsia and prognostic research, to explore the potential solutions in the development of a valid prediction model for adverse maternal or fetal outcomes' - addressing this very problem! They panel had 24 members including 'obstetricians, statisticians, clinical epidemiologists, and researchers'. It had a particular focus on the treatment paradox, as they developed a prediction model for the [PREP study (Thnagaratinam et al. 2017)](https://doi.org/10.3310/hta21180). The methods they identified are described in the table below. [[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

**How does this relate to causal inference?** Ultimately, our interest is in understanding the true relationships between variables, which is also the focus of causal inference studies. However, it is important to be aware that in causal inference, you are focussed on understanding the causal effect of an exposure or treatment on an outcome, whilst controlling for confounders for that relationship. If you create a model that includes those confounders, the effect estimates between the confounders and the outcome are still at risk of being impacted by residual confounding or bias, as we did not go through the process for their relationship, and only for the primary relationship of interest. Therefore, some of those methods fall under the banner of "causal inference", and could be designed in such a way that you would be estimating the causal effect between an exposure and an outcome, but it does not mean that you are finding causal effects between all variables and the outcome (which is often the focus below - having a multivariable model that accounts for treatment use - that is still a prediction model).

| Method | Description | Limitations | Possible for us? | Related causal inference technique (or at least, my understanding!) |
| --- | --- | --- | --- | --- |
| Standardisation of treatment | If the predictor is deterministic of treatment (i.e. everyone with this predictor *definitely* receives treatment - complete colinearity between predictor and treatment), then this resolves the paradox, as we can interpret that e.g. normal blood pressure = no anti-hypertensives. | This requires fully standardised care (same medication, same dose, same treatment thresholds). However, you can deal with this statistically using a multi-level model to account for differences between clinicians and treatment centres | Yes - although not true in practice, as decision to intervene (caesarean) and timing of that intervention varies between clinicians and hospitals - could deal with statistically | Multivariable regression - with the hospital/clinician included as a predictor<br><br>Instrumental variable analysis - where the hospital/clinician (a) cause variation in treatment, (b) are unrelated to outcome - and so can be used as an instrumental variable |
| Predictor substitution | Remove all predictors which are also used to guide treatment decisions | Often not possible as removes all the meaningful predictors | No | No equivalent |
| Treatment as a predictor | Include whether they were treated as a predictor | As the decision to treat may be influenced by other predictors in the model, this will make differentiating the effect of the treatment from the effect of the predictor very difficult. You can adjust for this interactivation, although that becomes very complex if there are multiple predictors that would prompt decision to treat, and require extremely large sample sizes for 'reliable assessment of interactions' | Yes - although limitation is significant | Multivariable regression - with treatment included as a predictor |
| Treatment as an outcome | If the treatment is likely to prevent an adverse outcome, then you can use treatment itself as the outcome, as it indicates they would've otherwise experienced an adverse outcome. | - | Yes - although, if I'm correct in understanding that there are many reasons why an emergency caesarean might be performed, this may not be specific enough? And that often, caesareans are performed and they think actually they shouldn't have been, and vice versa? | No equivalent |
| Propensity scores | Use propensity score (treatment probability) to account for 'multiway interactions with other predictors'. Either include in model, or use to weight contribution of participant towards the model (i.e. receiving no treatment --> less treatment effect --> more weight) | Limited clinical applicability as requires knowledge of a propensity score for clinicians to make a decision on whether to treat | Yes - although being aware of that limitation | Propensity score methods make up most of the conventional causal inference approaches - in this example, referencing inverse probability of treatment weighting (IPTW) |

Method and description and limitations based on [[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859), and relevant to us and link to causal inference based on my understanding of causal inference methodologies at this point.

## Other important considerations when designing an obstetric model

### Choice of population, predictors and outcomes

The panel in [Cheong-See et al. 2016](https://doi.org/10.1111/1471-0528.13859) not only discuss methods for dealing with the treatment paradox, but also around definition of the study sample, predictors and outcomes.

**Study sample**: Pre-eclampsia is multisystemic, different predictor groups associated with different outcomes, 'case mix impacts on the distribution of the predictors and the prevalence of the outcomes, and this in turn impacts on predictor–outcome associations, thereby influencing the accuracy of the model.'

**Outcomes:** More than one relevant outcome (e.g. eclampsia, abruption). As very few mothers will develop early-onset pre-eclampsia, these outcomes will occur at very low rates. This would not meet the suggested level of having 10-15 outcome events per predictor - and so, they recommend using composite outcomes and competing risk models.

They note that models are population-specific.

### External validation

This is mentioned above, but a few other comments are included below:
* 'Historically, the field of obstetrics has been successful in developing prediction models but has been poor in fully validating and thus implementing them effectively... Only two thirds of the papers [62.4%, 164/263] in a large systematic review of prognostic models in obstetrics were found to have presented their models in such a way that external validation would be feasible. This has been highlighted as a concern given the importance of validity in the development of such models.'[[Murphy et al. 2019]](https://doi.org/10.5772/intechopen.87311)
* 'Certain models can be too complex for routine clinical usage and this may lead to a reluctance on the part of the clinicians to accept them... It is also important that models which have been developed are also validated in a new population as otherwise it may not be possible to generalise them to a different cohort of patients. This is also known as impact analysis and this paper by Reilly et al. highlights that very few prediction models have undergone formal impact analysis or validation. This is essential in order for clinicians to know if the usage of such a model will have a positive or negative effect, i.e. is there a possibility that it will cause harm. The authors highlighted the benefit of having clinicians involved in the development and validation of such models before, during and after implementation.'[[Murphy et al. 2019]](https://doi.org/10.5772/intechopen.87311)
