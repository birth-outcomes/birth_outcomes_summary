# Study design in the context of the treatment paradox

Papers to make sure I have read and used:
* Prediction of neonatal metabolic acidosis in women with a singleton term pregnancy in cephalic presentation - Westerhuis et al. 2012 [[source]](https://doi.org/10.1055/s-0031-1284226)
* Predicting pre-eclampsia: dealing with both complex models and complex variables - Steer 2016 [[source]](https://doi.org/10.1111/1471-0528.13860)
* Prediction models in obstetrics: understanding the treatment paradox and potential solutions to the threat it poses - Cheong-See et al. 2016 [[source]](https://doi.org/10.1111/1471-0528.13859)
* Accounting for treatment use when validating a prognostic model: a simulation study - Pajouheshnia et al. 2017[[source]](https://doi.org/10.1186%2Fs12874-017-0375-8)
* Prediction of Caesarean Delivery - Murphy et al. 2019 [[source]](https://www.intechopen.com/chapters/67863)

## The treatment paradox

### What is a treatment paradox?

A **treatment paradox** (or "intervention effect", or "treatment use in a validation study") is 'when a strong prognostic factor of an adverse outcome triggers an effective treatment, thus reducing incidence of the outcome, and meaning that the prognostic factor that initiated the treatment will appear to have a poorer prognostic performance than it actually has.' This can lead to an underestimation of adverse outcomes for people with tthat prognostic factor.

In order for a treatment paradox to occur, two criteria must occur:
1. The prognostic factor has a strong relationship with the outcome
2. When the prognostic factor is present, it triggers an effective treatment

The presence of a treatment paradox is well-recognised in obstetrics. If you wanted to demonstrate the presence of a treatment paradox, you would need to demonstrate the two criteria above.[[source]](https://doi.org/10.1136%2Fbmjopen-2020-046518)

The consequence of this is a lack of **generalisability**.[[source]](https://doi.org/10.1503/cmaj.120812) The aim of predictive models will often be to help guide decisions to treat on future patients (i.e. they have not yet received any treatments). Models trained on treated patients will offer poor/biased performance, underestimating risk, which can be attributed to treatment use in the validation data.[[source]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### The treatment paradox for neonatal outcomes

#### Example 1:

'In the prediction of metabolic acidosis in neonates, there could be an intervention effect present owing to cesarean delivery. An unexpected finding was observed for the relation between intrapartum fever and metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]). Upon inclusion of cesarean delivery in the model, intrapartum fever was positively related to metabolic acidosis (OR 1.08 [95% CI 0.86–1.34]), which was in line with expectations.'[[source]](https://doi.org/10.1503/cmaj.120812)

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

#### Example 2:

Pre-eclampsia is hypothesised to cause cerebral palsy. It is also associated with higher risk of medically indicated (ordered by the physician) pre-term birth - and pre-term birth is also associated with higher risk of cerebral palsy.

You could adjust for pre-term birth or gestational age like a confounding variable. However, pre-term birth is a intermediate between pre-eclampsia and cerebral palsy, and not a common cause of both. Therefore, this adjustment (overadjustment) takes away from the detrimental effect of pre-elcampsia, mediated through pre-term birth - attenuating the effect or event reversing it.

In an early study, pre-eclampsia was found to be protective in pre-term infants and detrimental for those born later. However, we expect pre-eclampsia to be detrimental for all infants. This finding could be as the analysis seperated out pre-term births and later births, closing the causal path between pre-eclampsia and cerebral palsy via pre-term birth.[[source]](https://doi.org/10.1038/s41390-018-0071-3)


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

Hence, although widely used, conditioning on gestational at birth in studies of prenatal exposures and their relationship to postnatal outcomes may not reduce but actually lead to bias through overadjustment and faulty comparisons, and generate counterintuitive results and apparent changes of effect in different groups of patients.[[source]](https://doi.org/10.1038/s41390-018-0071-3)

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

#### Other examples:

Tocolytic effectiveness may mask the predictive accuracy of prognostication in pre-term birth.[[source]](https://doi.org/10.1111/1471-0528.13859) Tocolytics are drugs used to slow/stop contractions, typically given to women in pre-term labour.

Pre-eclampsia is a condition that causes high blood pressure during pregnancy and after labour, and it is a common cause of adverse outcomes. Delivery reduces probability of maternal complications, but prolonged delivery is usually desirable for fetus. Treatments with known effectiveness (e.g. magnesium sulphate and parenteral antihypertensives) minimise the risk of eclampsia and intracerebral haemorrhage.[[source]](https://doi.org/10.1111/1471-0528.13859)

## How do you design a study that accounts for the treatment paradox?

### Exclude treated individuals

Excluding individuals who received treatment will provide 'correct estimates of performance in the (untreated) target population if treatment use is associated with other prognostic factors' - but it will 'decrease the effective sample size' (which could cause you to not see an effect if you don't have the power).[[source]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Inverse probability weighting

### Recalibration

### Model treatment

[[source]](https://doi.org/10.1186%2Fs12874-017-0375-8)


## Plan of methods for us to consider

### (1) Inverse probability weighting followed by the exclusion of treated individuals


## Rough notes from papers

## Difficulties in study design

There are several possible causes for unexpected findings in prediction models. These include:
* Chance
* Misclassification of the predictor
* Selection bias
* Mixing of effects (confounding)
* Intervention effects
* Hetereogeneity[[source]](https://doi.org/10.1503/cmaj.120812)

'Obstetrics focuses on the early identification of pregnancies at risk of adverse outcomes to plan targeted intervention. Clinicians often use probabilistic reasoning, intuitively based on clinical history and tests, to assess the risk of complications in a mother or fetus; however, they need to be aware of false-positive and false-negative test results in their clinical decision-making. Prediction models (also known as prognostic models) provide individualised risk estimates for clinically important outcomes in patients with a particular disease or condition.1 Derived using statistical models, they include multiple predictors, such as age, previous history, and, increasingly, biomarkers. Although clinicians’ intuition has a place and a role in prediction, it has been shown that statistical prediction models give more accurate prognosis than clinicians can achieve working on their own.2 As in other clinical fields, the development and use of prediction models in obstetrics has limitations.3 In the development phase there are many statistical challenges, including: the ascertainment of a suitable sample size; the choice of candidate predictors; reliable measurement of the outcome and predictors; the identification of important predictors and their functional form; and internal validation, potentially including bootstrap resampling and cross-validation, as well as shrinkage for potential over-optimism in model performance.4 Most, if not all, models perform well when they are internally validated; however, the use of prediction models has been hampered by a distinct lack of research into the external validation of prediction models distant from the specific population that they were developed in, and the assessment of models on the behaviour of doctors and on patient outcomes. Another issue that limits clinical use, and which is the focus for this commentary, is the handling of interventions in the prediction model.'[[source]](https://doi.org/10.1111/1471-0528.13859)

### The treatment paradox

### Chance

We can see an unexpected predictor-outcome relationship due to chance, particularly if our sample size is small.[[source]](https://doi.org/10.1503/cmaj.120812)

### Misclassification

Unexpected findings can occur due to problems with the predictors - e.g.
* Measurement contains errors (e.g. some people coded as one outcome when they're the other)
* Predictor model incorrectly (e.g. categorised continuous variable, or linear transformation on non-linear predictor)
* Collinearity (when 2+ predictors are highly correlated) - although this one shouldn't affect predictive accuracy

Solutions: Redo measurement, model correctly, delete erroneous values, omit colinear variables or combine into single variable, or interpret in combination, or adopt a different model.

Example: Study predicting risk of metabolic acidosis in neonates, when thresholds for intrapartum fever were adjusted, an unexpected relationship with temperaturee disappeared.[[source]](https://doi.org/10.1503/cmaj.120812)

### Selection bias

If both predictor and outcome affect probability of selecting participant for inclusion.[[source]](https://doi.org/10.1503/cmaj.120812)

### Mixed effects (confounding)

'When 2 causes of a disease are mutually related, the observed effect of one can be mixed up with the effect of the other. In causal research, this phenomenon is referred to as confounding. Similarly, if 2 factors are mutually related (e.g., smoking and alcohol consumption) and one is causal for the outcome but the other is not, then exclusion of the causal factor would lead to the noncausal factor having a strong predictor effect unexpectedly.'[[source]](https://doi.org/10.1503/cmaj.120812)

### Intervention effects (i.e. treatment paradox)

'Predictor values may guide the decision to start a medical intervention. If effective, this intervention then lowers the probability of the outcome, thus attenuating the observed predictor–outcome relation. Similar to the mixing of effects, the overall observed relation is a combination of the direct effect of the predictor on the outcome and the indirect effect through the intervention. However, expectations of the direction of the predictor–outcome relation apply to the direct effect. Theoretically, the overall observed predictor–outcome relation could even be the reverse of the direct effect between predictor and outcome (in the case of an extremely effective intervention), thereby leading to an unexpected finding. Without further consideration, it seems unlikely that an intervention reduces the risk of the outcome to a level that is even lower than observed in a group who didn’t have the indication and therefore didn’t receive the intervention.'

'**The solution to deal with an unexpected finding due to an intervention effect would be to include the intervention in the prediction model**. Clearly, this is not possible if everyone in the study has the same intervention. In that case, it is likely that the unexpected finding actually has another cause than an intervention effect. If an intervention is equally effective in all patients, modelling the intervention effect doesn’t require an interaction between predictor and intervention in the model. If the intervention is more effective in, for example, those having the predictor, then an interaction between intervention and predictor is required (see Heterogeneity).'

'In the prediction of metabolic acidosis in neonates (example 1) there could be an intervention effect present owing to cesarean delivery. An unexpected finding was observed for the relation between intrapartum fever and metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]). Upon inclusion of cesarean delivery in the model, intrapartum fever was positively related to metabolic acidosis (OR 1.08 [95% CI 0.86–1.34]), which was in line with expectations.'[[source]](https://doi.org/10.1503/cmaj.120812)

### Heterogeneity

'The effect of a predictor may differ across subgroups of patients. This is referred to as a differential predictor effect, interaction, effect modification or heterogeneity of the predictor. When heterogeneity is not accounted for in the prediction model, the observed predictor effect is a (weighted) average of predictor effects within the different subgroups. If the predictor–outcome relations across subgroups are opposite, the direction of the observed relation depends on the proportional contributions of the subgroups.'

'In the prognostic model of metabolic acidosis in neonates (example 1), the effect of intrapartum fever on metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]) was unexpected. Alongside the impact of misclassifying the presence of fever (see Misclassification), this unexpected finding could also have been the result of an interaction between intrapartum fever and epidural analgesia among women who received epidural analgesia (OR 0.47 [95% CI 0.35–0.64]) versus women without epidural analgesia (OR 3.16 [95% CI 2.16–4.64]).'[[source]](https://doi.org/10.1503/cmaj.120812)

### Other stuff

'When the direction of a predictor–outcome relation is well-established in both the literature and in clinical experience, it is easy to identify unexpected (or incorrect) findings. Things become complicated when there is no pre-existing knowledge and it is unknown what direction is to be expected. Then, one has to make assumptions on the relation, and therefore it is called an unexpected finding rather than an incorrect finding. A more subtle unexpected finding occurs when the direction of a predictor–outcome association is as expected, but the magnitude of the effect is larger or smaller than expected.'[[source]](https://doi.org/10.1503/cmaj.120812)


As stated in the NICE 2011 Ceasarean guidance, when we are looking at neonatal outcomes, 'there is a treatment paradox: the babies who are delivered the quickest are likely to be the ones who are most compromised and therefore more likely to have poorer ourcomes. As a result, samples of babies born within 30 minutes will consistently contain a higher proportion of babies in poorer condition. Thus, differences in findings between groups might reflect this disparity, rather than being due to differences in speed of delivery.'[[source]](https://www.nice.org.uk/guidance/ng192/evidence/full-guideline-pdf-9071942942)

Prediction models in obstetrics: understanding the treatment paradox and potential solutions to the threat it poses - Cheong-See et al. 2016.[[source]](https://doi.org/10.1111/1471-0528.13859)
* 
* There is commentary by Phil Steer on this article[[source]](https://doi.org/10.1111/1471-0528.13860)

Another limiting factor for clinical usage and which was discussed in a commentary in the British Journal of Obstetrics and Gynaecology (BJOG) in 2016 is how interventions might be handled in a prediction model [38]. This commentary highlighted the issues, which face clinicians in validating obstetric prediction models in order to effectively implement them in clinical practice. They specifically examined the area of pre-eclampsia and noted that a phenomenon described as the treatment paradox can occur; a strong predictor of a common complication may trigger an effective treatment (e.g. commencement of anti-hypertensive therapy) at an early stage and this will then prevent the occurrence of a certain proportion of adverse outcomes. This may result in the predictor, which triggered the treatment initially appearing poorer in its predictive performance [39, 40]. The BJOG review [38] further examined a prediction model which has been successfully validated for the predicting pre-eclampsia (PREP model-Development and validation of Prediction models for Risks of complications in Early-onset Pre-eclampsia) [41] in order to ascertain what made it a successful process and highlighted certain factors which can aid validation. These included large sample size, standardisation of treatment or intervention, and the consideration to the initiation of treatment being an outcome itself, i.e. ‘When starting a treatment is likely to prevent an adverse outcome, those who received the treatment could also be considered to have experienced the outcome’. These factors may aid obstetricians in validation of prediction models going forward and in handling the treatment paradox.[[source]](https://www.intechopen.com/chapters/67863)

How studies try to deal with it:
* By including abnormal CTG as a neonatal outcome (alongside stillbirth, early neonatal death, mean birthweight, incidence of small-for-gestational age, neonatal unit admission, and composite of Apgar5<7, pH<7 or neonatal encephalopathy).[[source]](https://doi.org/10.1111/aogs.13671)

Mentions of it:
* In discussion: 'treatment paradox could mean that women are appropriately delivered on the basis of moderate deterioration in biochemical parameters before severe complications occur'.[[source]](https://doi.org/10.1016/S0140-6736(19)31963-4)

# Rough notes from meeting

## Broad aims

Using live labour data to predict who is likely to require caessarean, and reduce adverse effects for mother and baby. Combining data from fetus, parent, and CTG. Involves combining (a) risk factors during pregnancy, with (b) live risk factors during labour. Outcome of "X chance" of adverse outcome if don't go for caessarean or assisted delivery. Decision currently based on experience. Want some more objective evidence that can given women to help them understand and base risks on.

Can’t use outcomes in classical way because of treatment paradox. May need to reformulate, as this is not a prediction question. In women in labour, is there a way we can predict whose going to need something that allows us to act more effectively. Dave Right statistician screening for down syndrome example – all previous ranked top five predicting down syndrome and so on – doesn’t necessarily tell you best way, as those five together may predict less well than one of those and others, its more complex than that. You’re trying to produce an instrument that allows you to behave differently. 

spend 3 billion on care and 7.8 billion on claims.
* vast majority of delivers by caessarean or forceps are fine
* acting too late has risk of poor outcomes and of cerbral palsy
* most common legal composition is acute total collapse - babies heart rate suddenly drops from high, and if goes on for 10-15 min, baby usually has CP is survive, and basal ganglia damage

if definition of problem is avoiding fetal injury, is what is needed a more subtle instrument, or havgin experts who know what they’re doing. 


## Treatment paradox

Treatment paradox means you can’t use outcomes (eg baby died, bad apgar) because worse things are is more quickly you intervene. Classical example of when to do caessarean – longer wait outcome not worse, as when really bad you do quickly, and when not so bad you wait, so you end up with same level all along.

pyrexia in mother uncommon but can be bad outcome linked, but babies often born with normal blood gases, as infection is problem rather than acidosis. Majority of women with fever have fever due to epidural but those babies are fine, just hot. In cambridge data, epidural comes out as protective, but because thought to be pyrexia risk but was actually epidural.

## Design ideas

Judee Pearl, causal inference, would say you cannot tell these things from the data alone. Statisticians are used to only answer from data alone, other things non data, but humans are good at recognising patterns that data isn’t. E.g. a first thing cant be caused by second. But statistics can’t handle. He says you take models through experts of describing what are potential causal routes through here and model them under different conditions. If you expert is right about this causing this, then can predict effect size of this causing this. Gives you a way around this problem – not just relying on data. In stroke, want to be able say causally about link between thrombolysis and outcomes.

excluded delivery by caessarean in cambridge
* still subject to influence due to forcep delivery and so on – but potentially less issue
*  takes out highest risk groups

doing a trial

When the clinician thinks the baby is in trouble, what tells you whether it really is or isn’t – that narrows it down to a smaller group where intervention produces less of paradox.
* majoriy of sections for fetal distress are not true distress – its abnormal ctg but no fetal compromise
* correct – define of group not to be worried about

No treatment would be no low outcomes. We have better outcomes as experts intervene. The question is not is the child fine. The question is whether they would’ve been fine if hadn’t intervened, and we don’t know that. Looking for marginal improvement, thing has to be better than expert, and that’s a big ask

another way around paradox is how in stroke, say different units do different things, and helps them understand, as propensity to give ceassarean differs between hospitals, and that may allows us to dig into it
* issue will be is that it will be between clinician rather than site
* will still be site difference in rates even when account for socioeconomic and stuff, so there must be something