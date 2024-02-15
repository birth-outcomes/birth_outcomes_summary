# Treatment Paradox

## Rationale

'Obstetrics focuses on the early identification of pregnancies at risk of adverse outcomes to plan targeted intervention. Clinicians often use probabilistic reasoning, intuitively based on clinical history and tests, to assess the risk of complications in a mother or fetus; however, they need to be aware of false-positive and false-negative test results in their clinical decision-making. Prediction models (also known as prognostic models) provide individualised risk estimates for clinically important outcomes in patients with a particular disease or condition.1 Derived using statistical models, they include multiple predictors, such as age, previous history, and, increasingly, biomarkers. Although clinicians’ intuition has a place and a role in prediction, it has been shown that statistical prediction models give more accurate prognosis than clinicians can achieve working on their own.2 As in other clinical fields, the development and use of prediction models in obstetrics has limitations.3 In the development phase there are many statistical challenges, including: the ascertainment of a suitable sample size; the choice of candidate predictors; reliable measurement of the outcome and predictors; the identification of important predictors and their functional form; and internal validation, potentially including bootstrap resampling and cross-validation, as well as shrinkage for potential over-optimism in model performance.4 Most, if not all, models perform well when they are internally validated; however, the use of prediction models has been hampered by a distinct lack of research into the external validation of prediction models distant from the specific population that they were developed in, and the assessment of models on the behaviour of doctors and on patient outcomes. Another issue that limits clinical use, and which is the focus for this commentary, is the handling of interventions in the prediction model.'[[source]](https://doi.org/10.1111/1471-0528.13859)

'When the direction of a predictor–outcome relation is well-established in both the literature and in clinical experience, it is easy to identify unexpected (or incorrect) findings. Things become complicated when there is no pre-existing knowledge and it is unknown what direction is to be expected. Then, one has to make assumptions on the relation, and therefore it is called an unexpected finding rather than an incorrect finding. A more subtle unexpected finding occurs when the direction of a predictor–outcome association is as expected, but the magnitude of the effect is larger or smaller than expected.'[[source]](https://doi.org/10.1503/cmaj.120812)

## What is a treatment paradox?

A **treatment paradox** (or "intervention effect", or "treatment use in a validation study") is 'when a strong prognostic factor of an adverse outcome triggers an effective treatment, thus reducing incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will appear to have a poorer prognostic performance than it actually has.' This can lead to an underestimation of adverse outcomes for people with tthat prognostic factor.

In order for a treatment paradox to occur, two criteria must occur:
1. The prognostic factor has a strong relationship with the outcome
2. When the prognostic factor is present, it triggers an effective treatment

The presence of a treatment paradox is well-recognised in obstetrics. If you wanted to demonstrate the presence of a treatment paradox, you would need to demonstrate the two criteria above.[[Uffen et al. 2021]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

The consequence of this is a lack of **generalisability**.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) The aim of predictive models will often be to help guide decisions to treat on future patients (i.e. they have not yet received any treatments). Models trained on treated patients will offer poor/biased performance, underestimating risk, which can be attributed to treatment use in the validation data.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

## The treatment paradox for neonatal outcomes

### Example 1:

'In the prediction of metabolic acidosis in neonates, there could be an intervention effect present owing to cesarean delivery. An unexpected finding was observed for the relation between intrapartum fever and metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]). Upon inclusion of cesarean delivery in the model, intrapartum fever was positively related to metabolic acidosis (OR 1.08 [95% CI 0.86–1.34]), which was in line with expectations.'[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    fever("Intrapartum fever")
    cs("Ceasarean section")
    met("Metabolic acidosis")

    %% Produce the figure
    fever --> cs;
    cs --> met;
    fever --> met;
````

### Example 2:

Pre-eclampsia is hypothesised to cause cerebral palsy. It is also associated with higher risk of medically indicated (ordered by the physician) pre-term birth - and pre-term birth is also associated with higher risk of cerebral palsy.

You could adjust for pre-term birth or gestational age like a confounding variable. However, pre-term birth is a intermediate between pre-eclampsia and cerebral palsy, and not a common cause of both. Therefore, this adjustment (overadjustment) takes away from the detrimental effect of pre-elcampsia, mediated through pre-term birth - attenuating the effect or event reversing it.

In an early study, pre-eclampsia was found to be protective in pre-term infants and detrimental for those born later. However, we expect pre-eclampsia to be detrimental for all infants. This finding could be as the analysis seperated out pre-term births and later births, closing the causal path between pre-eclampsia and cerebral palsy via pre-term birth.[[Williams et al. 2018]](https://doi.org/10.1038/s41390-018-0071-3)


````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    eclam("Pre-eclampsia")
    preterm("Preterm birth")
    cp("Cerebral palsy")

    %% Produce the figure
    eclam --> preterm;
    preterm --> cp;
    eclam --> cp;
````

However, it's likely more complex. In a more realistic directed acyclic graph (DAG) below, chorioamnionitis is added. It is another cause of pre-term birth and cerebral palsy.

Gestational age, as a shared effect of pre-eclampsia and chorioamnionitis, acts as a **collider**. This is the opposite of a confounder (where a common cause of exposure and outcome is not controlled for) - instead, a collider is when the exposure and outcome (or factors causing) each influence a common third variable, and that variable is controlled for in the design. Controlling for a collider can result in a distorted association betwene the exposure and outcome, when actually none exists.

In this model, if we look in a group of pre-term infants:
* Babies born to mothers with pre-eclampsia will be less likely to have chorioamnionitis and vice versa
* The effect of pre-eclampsia will be compared with the effect of chorioamnionitis on cerebral palsy, and will falsy appear to be protective - the estimated direct causal effect of pre-eclampsia on the outcome will be biased (through the effect of chorioamnionitis)

Hence, although widely used, conditioning on gestational at birth in studies of prenatal exposures and their relationship to postnatal outcomes may not reduce but actually lead to bias through overadjustment and faulty comparisons, and generate counterintuitive results and apparent changes of effect in different groups of patients.[[Williams et al. 2018]](https://doi.org/10.1038/s41390-018-0071-3)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    chor("Chorioamnionitis")
    eclam("Pre-eclampsia")
    preterm("Preterm birth")
    cp("Cerebral palsy")

    %% Produce the figure
    chor --> preterm;
    eclam --> preterm;
    chor --> cp;
    preterm --> cp;
    eclam --> cp;
````

### Example 3:

In the NICE 2011 Caesarean guidance, they state how there is a treatment paradox in that 'babies who are delivered the quickest are likely to be the ones who are most compromised and therefore more likely to have poorer ourcomes. As a result, samples of babies born within 30 minutes will consistently contain a higher proportion of babies in poorer condition. Thus, differences in findings between groups might reflect this disparity, rather than being due to differences in speed of delivery.'[[source]](https://www.nice.org.uk/guidance/ng192/evidence/full-guideline-pdf-9071942942)

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    comp("Compromised")
    quick("Quicker delivery")
    poor("Poor outcomes")

    %% Produce the figure
    comp --> quick;
    quick --> poor;
    comp --> poor;
````

### Other examples:

From our meeting (not super clear on this) -

````{mermaid}
  flowchart LR;

    %% Define the nodes and subgraphs
    epi("Epidural")
    fever("Pyrexia (fever)")
    adverse("Adverse outcome")

    %% Produce the figure
    epi --> fever;
    epi --> adverse;
    fever --> adverse;
````

From our meeting - relationship between caesarean and outcome - don't see relationship with longer wait for caesarean, as when things are worse, you do it more quickly.

Tocolytic effectiveness may mask the predictive accuracy of prognostication in pre-term birth.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859) Tocolytics are drugs used to slow/stop contractions, typically given to women in pre-term labour.

Pre-eclampsia is a condition that causes high blood pressure during pregnancy and after labour, and it is a common cause of adverse outcomes. Delivery reduces probability of maternal complications, but prolonged delivery is usually desirable for fetus. Treatments with known effectiveness (e.g. magnesium sulphate and parenteral antihypertensives) minimise the risk of eclampsia and intracerebral haemorrhage.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)