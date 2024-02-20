# Treatment Paradox

`````{admonition} Executive summary
:class: info

A **treatment paradox** is when we have a predictor with a strong relationship with the outcome which, when present, triggers a treatment to be delivered. For example, we don't see a relationship between outcomes and time to wait for a caesaraen, as when the situation is worse, the infants will be delivered more quickly.
`````

## What is a treatment paradox?

A **treatment paradox** (or "intervention effect", or "treatment use in a validation study") is 'when a strong prognostic factor of an adverse outcome triggers an effective treatment, thus reducing incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will appear to have a poorer prognostic performance than it actually has.' This can lead to an underestimation of adverse outcomes for people with that prognostic factor.

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