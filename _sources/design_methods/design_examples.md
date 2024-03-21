# Examples of studies that account for the treatment paradox

https://www.sciencedirect.com/science/article/pii/S0167629617307609

## Commentary on prognostic models in obstetrics

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

## Are there examples of studies of neonatal outcomes that have attempted to account for the treatment paradox?

### Thangaratinam et al. 2017

**Model:** Development and validation of Prediction models for Risks of complications in Early-onset Pre-eclampsia.[[Thangaratinam et al. 2017]](https://doi.org/10.1186/s12916-017-0827-3)

This is a prediction model for pre-eclampsia that has been successfully validated. In a 2016 commentary in the British Journal of Obstetrics and Gynaecology (BJOG)[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859), they examined this model to identify what made it succesful and highlighted:
* Large sample size
* Standardisation of treatment or intervention
* Consideration of the initiation of treatment being an outcome itself - i.e. "when starting a treatment is likely to prevent an adverse outcome, those who received the treatment could also be considered to have experienced the outcome"[[Murphy et al. 2019]](https://doi.org/10.5772/intechopen.87311)

### Helenius et al. 2019

<mark> don't quite understand </mark>

Study using data from the National Neonatal Research Database (NRRD) investigating whether birth in a non-tertiary hospital or transfer within 48 hours are associated with poor outcomes when compared with birth in a tertiary setting. A "tertiary" setting is one that provides specialist care. Their hypothesis was that mortality and severe brain injury would be higher in transferred infants compared with non-transferred infants born in tertiary hospitals.

They use propensity score matching to create matched groups for comparison with near identical distributions of background and potential confounder variables. 

Paper: https://doi.org/10.1136/bmj.l5678

Supplementary: https://www.bmj.com/content/bmj/suppl/2019/10/16/bmj.l5678.DC1/helk050424.ww1.pdf

Responses: https://www.bmj.com/content/367/bmj.l5678/rapid-responses

### Examples to look at

* https://doi.org/10.1111/cdoe.12634 - Caesarean delivery and early childhood caries: Estimation with marginal structural models in Brazilian pre-schoolers - Ladeira et al. 2021
* https://bmjopen.bmj.com/content/bmjopen/10/11/e038845.full.pdf - Protocol for development and validation of a clinical prediction model for adverse pregnancy outcomes in women with gestational diabetes - Cooray et al. 2020
    * Addressing the treatment paradox (in this case with insulin) is a challenge in prediction modelling studies. The traditional approach has been to accept predictions in the context of current care. However, this does not remove the possibility that a potentially useful model may appear to perform poorly due to the confounding effect of the judicious application of effective interventions to individual’s whom clinicians subjectively assess to be at high risk of the outcome of interest.
    * Two solutions to address the problem of treatment paradox in prediction modelling studies have been advocated.50
        * First, the use of treatments suspected to confound the predictor-outcome relationship can be set as a **predictor** in the final model.
        * Second, the use of such effective treatments can be included within a composite **outcome** to be predicted.
    * For this study, both approaches were considered but deemed **inappropriate**. For the former, the inclusion of the requirement for insulin therapy as a predictor is not possible as this information is not available at the intended moment of prediction—the time of GDM diagnosis, usually around 24 to 28 weeks gestation. For the later, inclusion of the requirement for insulin therapy within the composite outcome would impair its interpretability as this outcome occurs at a significantly higher frequency than the other component outcomes (31% vs approximately 10% based on our prior work).44 This is likely to lead to a less meaningful composite that is primarily driven by the need for insulin therapy and no longer predicts what we want (adverse pregnancy outcomes). While many promising novel approaches have been proposed in the statistical literature, such as multistate modelling or marginal structural models for ‘treatment drop-ins’,51 52 at time of writing all are primarily based on empirical data and are yet to be applied to clinical prediction problems.
    * The three possible results from the **sensitivity analysis** to evaluate the effect of including the decision to treat with insulin will be informative and may be interpreted as follows. If the sensitivity analyses find that the inclusion of the decision to treat with insulin within the outcome:
        1. Positively affects model performance, then this suggests the presence of treatment paradox, that is, pregnancy complications are more likely to occur in the absence of insulin therapy;
        2. Has no significant effect on model performance then this suggests that the model is robust with predictive performance not affected by the decision to treat, that is, the absolute risk of adverse pregnancy outcomes for an individual woman with GDM is not affected by insulin therapy;
        3. Negatively affects model performance, then this would suggest that adverse pregnancy outcomes are more likely to occur in women treated with insulin, and thus imply more ‘severe’ GDM or a harmful effect for this treatment. (unlikely)
    * The effect of treatment with insulin will be further evaluated using an IPTW algorithm to weight women according to their propensity of having been treated and transformation of the logistic model into a multinomial model. This multinomial model will have four categories depending on the occurrence of the composite pregnancy outcome and whether the women have received treatment with insulin or not.
* https://doi.org/10.1093%2Finthealth%2Fihz111 - Adverse infant outcomes associated with caesarean section delivery in India - Gondwe et al. 2020
* https://doi.org/10.1093%2Fpch%2Fpxz051 - Caesarean section and neonatal survival and neurodevelopmental impairments in preterm singleton neonates - Lodha et al. 2020
* https://doi.org/10.1111/aogs.13214 - Propensity score method for analyzing the effect of labor induction in prolonged pregnancy - Pyykönen et al. 2017
* https://doi.org/10.1016/j.ejogrb.2015.09.011 - Elective repeat cesarean delivery compared with trial of labor after a prior cesarean delivery: a propensity score analysis - Kok et al. 2015
* https://jamanetwork.com/journals/jamapediatrics/fullarticle/2792041 - Developmental Outcomes for Children After Elective Birth at 39 Weeks’ Gestation - Lindquist et al. 2022
* https://doi.org/10.1186%2Fs12887-018-1324-3 - Mode of delivery and short-term infant health outcomes: a prospective cohort study in a peri-urban Indian population - Gondwe et al. 2018
* https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755743/ - Mode of delivery, type of labor, and measures of adiposity from childhood to teenage: Project Viva - Mueller et al. 2021
* https://doi.org/10.1111/cdoe.12634 - Caesarean delivery and early childhood caries: Estimation with marginal structural models in Brazilian pre-schoolers

### Other

**Incorporation of treatment in the model:** 'In the prediction of metabolic acidosis in neonates (example 1) there could be an intervention effect present owing to cesarean delivery. An unexpected finding was observed for the relation between intrapartum fever and metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]). Upon inclusion of cesarean delivery in the model, intrapartum fever was positively related to metabolic acidosis (OR 1.08 [95% CI 0.86–1.34]), which was in line with expectations.'[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

**Including an alternative outcome not impacted by treatment paradox:** By including abnormal CTG as a neonatal outcome (alongside stillbirth, early neonatal death, mean birthweight, incidence of small-for-gestational age, neonatal unit admission, and composite of Apgar5<7, pH<7 or neonatal encephalopathy).[[Bhatia et al. 2019]](https://doi.org/10.1111/aogs.13671)