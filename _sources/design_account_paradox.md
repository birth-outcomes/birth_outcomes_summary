# Accounting for a treatment paradox

`````{admonition} Executive summary
:class: info

There are several proposed methods for accounting for a treatment paradox.

Might be suitable for us:
* ?

As yet unsure:
* Excluding treated individuals
* Inverse probability weighting
* Propensity scores
* Use of treatment as the model outcome
* Recalibration
* The existence of fully standardised care with no variation in treatment (or variation that you can account for)
* Marginal structure models

Unsuitable:
* Predictor substitution
* Incorporation of treatment as a predictor
`````

<mark>to read</mark>

* https://doi.org/10.1002/sim.2712 - Putter H, Fiocco M, Geskus RB. Tutorial in biostatistics: competing risks and multi-state models. Stat Med 2007;26:2389–430.
* https://doi.org/10.1002/sim.7913 - Sperrin M, Martin GP, Pate A, et al. Using marginal structural models to adjust for treatment drop-in when developing clinical prediction models. Stat Med 2018;37:4142–54.
* Wei Xin Chan, Limsoon Wong, Accounting for treatment during the development or validation of prediction models, Journal of Bioinformatics and Computational Biology, 10.1142/S0219720022710019, 20, 06, (2022).
* Barbra A. Dickerman, Issa J. Dahabreh, Krystal V. Cantos, Roger W. Logan, Sara Lodi, Christopher T. Rentsch, Amy C. Justice, Miguel A. Hernán, Predicting counterfactual risks under hypothetical treatment strategies: an application to HIV, European Journal of Epidemiology, 10.1007/s10654-022-00855-8, 37, 4, (367-376), (2022).
* Lijing Lin, Matthew Sperrin, David A. Jenkins, Glen P. Martin, Niels Peek, **A scoping review of causal methods enabling predictions under hypothetical interventions**, Diagnostic and Prognostic Research, 10.1186/s41512-021-00092-9, 5, 1, (2021). <mark>read this one first, recent and lots of methods, and also references and explains some like Pajouheshina's proposal of censoring followed by reweighting using inverse probability censoring weights</mark>
    * To correctly aid such decision-making, one needs answers to ‘what-if’ questions. As an example, suppose we are interested in statin interventions for primary prevention of CVD and we would like to predict the 10-year risk of CVD with or without statin interventions at an individual level. The methods used to derive CPMs do not allow for the correct use of the model in answering such ‘what-if’ questions, as they select and combine covariates to optimize predictive accuracy, not to predict the outcome distribution under hypothetical interventions [12, 13]. Nevertheless, end-users often mistakenly compare the contribution of individual covariates (in terms of risk predictions) and seek causal interpretation of model parameters [14]. Within a potential outcomes (counterfactual) framework, an emerging class of causal predictive models could enable ‘what-if’ queries to be addressed, specifically calculating the predicted risk under different hypothetical interventions. This enables targeted intervention, allows correct communication to patients and clinicians, and facilitates a preventative healthcare system.
    * We aimed to identify the main methodological approaches, their underlying assumptions, targeted estimands, and potential pitfalls and challenges with using the method. Finally, we aimed to highlight unresolved methodological challenges.
* Nan van Geloven, Sonja A. Swanson, Chava L. Ramspek, Kim Luijken, Merel van Diepen, Tim P. Morris, Rolf H. H. Groenwold, Hans C. van Houwelingen, Hein Putter, Saskia le Cessie, Prediction meets causal inference: the role of treatment in clinical prediction models, European Journal of Epidemiology, 10.1007/s10654-020-00636-1, 35, 7, (619-630), (2020).
* Barbra A. Dickerman, Miguel A. Hernán, Counterfactual prediction is not only for causal inference, European Journal of Epidemiology, 10.1007/s10654-020-00659-8, 35, 7, (615-617), (2020).
* Matthew Sperrin, Glen P. Martin, Rose Sisk, Niels Peek, Missing data should be handled differently for prediction than for description or causal explanation, Journal of Clinical Epidemiology, 10.1016/j.jclinepi.2020.03.028, 125, (183-187), (2020).
* Rose Sisk, Lijing Lin, Matthew Sperrin, Jessica K Barrett, Brian Tom, Karla Diaz-Ordaz, Niels Peek, Glen P Martin, Informative presence and observation in routine health data: A review of methodology for clinical risk prediction, Journal of the American Medical Informatics Association, 10.1093/jamia/ocaa242, 28, 1, (155-166), (2020).
* Pajouheshnia R, Schuster NA, Groenwold RH, Rutten FH, Moons KG, Peelen LM. Accounting for time-dependent treatment use when developing a prognostic model from observational data: A review of methods. Statistica Neerlandica. 2020;74(1):38–51. Available from: https://onlinelibrary.wiley.com/doi/abs/10.1111/stan.12193.
* Using marginal structural models to adjust for treatment drop-in when developing clinical prediction models - https://doi.org/10.1002/sim.7913
* https://arxiv.org/abs/2308.13026 - Assessing model performance for counterfactual predictions
    * estimating and evaluating counterfactual prediction models is challenging because one does not observe the full set of potential outcomes for all individuals.
* https://www.criticalcare.theclinics.com/article/S0749-0704(23)00011-8/abstract - Making the Improbable Possible: Generalizing Models Designed for a Syndrome-Based, Heterogeneous Patient Landscape
* https://arxiv.org/abs/2209.06101 - Evaluating individualized treatment effect predictions: a model-based perspective on discrimination and calibration assessment

## Methods that might be suitable for us

## As yet unsure

### Exclude treated individuals

Excluding individuals who received treatment can provide 'correct estimates of performance in the (untreated) target population'.

Limitations:
* Will 'decrease the effective **sample size**' (which could cause you to not see an effect if you don't have the power). This, for example, leads to 'the precision of estimates of both the observed:expected ratio and c-index (area under the ROC curve) decreased due to the reduction in effective sample size'.
* Results in loss of information about **high risk individuals**, if treatment allocation was dependent on risk (and so very few were untreated), with the discriminative ability of the model worsening with the exclusion of high-risk individuals and consequently narrower case mix.
* 'In the presence of a strong **unmeasured predictor of the outcome associated with treatment use**, exclusion of treated individuals resulted in an underestimation of the performance of the model.'

[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Inverse probability weighting

Inverse probability weighting (IPW) is a method that is used to **balance data where there is non-random treatment use, so it instead resembles use in an RCT**. It is used when we want to estimate a causal association between an exposure and outcome whilst accounting for the influence of confounders.

Method:
1. Fit "treatment propensity model" on validation data - this is a regression model where the outcome is treatment use, and predictors are variables that might predict treatment use, including the predictors of the prognostic model being evaluated.
2. Used that model to **estimate the probability that each patient in the validation set receives a treatment**.
3. **Weight each individual by the inverse of their probability of the actual treatment received. This will produce a distribution of risks in the validation set that resembles what would have been seen had treatments been randomly allocated**
4. Another step you can take is to excluded the treated individuals after deriving weights, so that the resulting validation set should resemble the untreated target population

Limitations:
* Incorrect specification of the treatment propensity model (e.g. unmeasured confounders) can also cause issues
* Practical non-positivity violates assumptions. This is when there is a **risk strata where no subjects receive treatment** - e.g. if have contraindication for treatment, or when guidelines already recommend that individuals above a certain probability threshold should receive treatment. This can lead to individuals receiving **extreme weights**, resulting in biased and imprecise estimates of model performance
* Exclusion of treated individuals will mean a smaller sample size

**Variants** of IPW can be applied - e.g. weight truncation, which aims to improve performance when assumptions are violated.

**Simulation study illustrates some of limitations:** In their simulation study, Pajouheshnia et al. 2017 find that **IPW alone did not improve calibration** (compared to when we did nothing to account for the treatment paradox), but IPW followed by the **exclusion of treated individuals** provided correct estimates for calibration. IPW alone or followed by the exclusion of treated individuals improved estimates of the c-index in all scenarios where the assumptions of positivity and no unobserved confounding were met. In scenario 4, **where treatment allocation was determined by a strict risk-threshold and thus the assumption of positivity was violated, IPW was ineffective, and resulted in the worst estimates of discrimination across all methods**. In addition, the extreme weights calculated in scenario 4 led to very large standard errors. In scenarios 13–15, the presence of an unobserved confounder led to the failure of IPW to provide correct estimates of the c-index. Weight truncation at the 98% percentile increased precision, but was less effective in correcting of the c-index for the effects of treatment.

'Although the use of IPW prior to the exclusion of treated individuals is a promising solution in data where treatments are non-randomly allocated, it **should not be used when there are severe violations of the underlying assumptions, e.g. in the presence of non-positivity (where some individuals had no chance of receiving treatment), or when there is an unobserved confounder, strongly associated with both the outcome and treatment use.** There is thus a need to explore alternative methods to IPW to account for the effects of treatment use when validating a prognostic model in settings with non-random treatment use.'

[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Propensity scores

<mark>how does this differ to IPW?</mark>

Propensity scores are 'the **probability of a treatment being assigned to an individual** based on observed pre-treatment variables. One can designate propensity scores to each individual in the study taking into account the multiway interactions with other predictors (on which the decision to treat was based). Such a model provides risk estimates for an individual taking into account the probability of requiring treatment.'

Limitations:
* It requires a prior knowledge of the propensity score
* It has limited clinical applicability for making decisions on whether to treat.

'A related option is to take into account each participant's propensity score by using it to define a weight for the contribution of that particular participant towards the logistic model analysis and development of the prognostic model. Women who received little or no treatment (and hence less treatment effect) should carry more weight than those who had a high probability of being treated.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

### Use treatment as the outcome

When starting a treatment is likely to prevent an adverse outcome, those who received the treatment could also be considered to have experienced the outcome.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

For example, 'in women with early-onset pre-eclampsia, if a large proportion of women are delivered at an early preterm gestation (before 34 weeks), then delivery itself could be considered as an outcome (replacing complications that would have occurred in the absence of delivery). In the absence of a standardised protocol for decision to deliver at early preterm gestation, such an approach could help to overcome the limitations in the model as a result of delivery preventing the occurrence of an adverse outcome.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

### The existence of fully standardised care with no variation in treatment (or variation that you can account for)

This is a scenario where there is complete collinearity between the predictor and the treatment, where the presence of a particular predictor will **always** guarantee the presence of a particular treatment.

However, that requires no variation in treatment - that the **same medications and dosages are always provided at the same treatment thresholds at the same times**. This is not realistic. With the example of management of early-onset pre-eclampsia, such as the commencement of anti-hypertensives and magnesium sulphate, this is somewhat standardised by guidelines [e.g. from the National Institute for Health and Care Excellence (NICE) in the UK], but the **threshold for commencing treatment varies between clinicians and centres**. Furthermore, the **response from a specific antihypertensive and dosage varies between individual patients**.

This limits the applicability of such a strategy, although one could consider the use of multilevel models to allow for any differences between clinicians and treatment centres.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

Steer 2016 comments that 'such models rarely take into account all of the relevant factors (e.g. the coexistence of a modulating pathology such as an autoimmune disorder) or the social and emotional circumstances and preferences of the mother and her family.'[[Steer 2016]](https://doi.org/10.1111/1471-0528.13860)

### Recalibration

**Don't yet understand:** 'The incidence of the predicted outcome may vary between development and validation data sets. If this is the case, the predictions made by the model will not, on average, match the outcome incidence in the validation data set [22]. As discussed in section 2.1, use of an effective treatment in a validation data set will lead to fewer outcome events and thus a lower incidence than there would have been had the validation set remained untreated. One approach to account for this would be to recalibrate the original model using the partially treated validation data set. In a logistic regression model, a derivative of the incidence of the outcome is captured by the intercept term in the model, and thus a simple solution would seem to be to re-estimate the model intercept using the validation data set [23, 24]. In doing this, the average predicted risk provided by the recalibrated model should then be equal to the (observed) overall outcome frequency in the validation set. Further details of this procedure are given in Table ​Table1.1. Where treatment has been randomly allocated, intercept recalibration should indeed account for the risk-lowering effects, provided that the magnitude of the treatment effect does not vary depending on an individual’s risk and thus is constant over the entire predicted probability range. In non-randomized settings, where treatment use by definition is associated with participant characteristics, a simple intercept recalibration is unlikely to be sufficient due to interactions between treatment use and patient characteristics that are predictors in the model. However, although recalibration may seem a suitable solution for modelling the effects of treatment, when applying recalibration, concerns should also be raised over the interpretation of the estimated performance of the model. Differences in outcome incidence between the development data set and validation data set may not be entirely attributable to the effects of treatment use. By recalibrating the model to adjust for differences in treatment use and effects, we simultaneously adjust for differences in case-mix between the development and validation set. As the aim of validation is to evaluate the performance of the original prognostic model, in this case in a treatment-naïve sample, recalibration may actually lead to an optimistic impression of the accuracy of predictions made by the original model in the validation set. For example, if the validation set included individuals with a notably greater prevalence of comorbidities and thus were more likely to develop the outcome, recalibration prior to validation could mask any inadequacies of the model when making predictions in this subset of high-risk individuals.'[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

Due to the limitations, Pajouheshnia et al. 2017 do not recommend this approach.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

### Marginal structure models

<mark>to add</mark>

'Marginal structural models “subtract” the effect of both current and future treatment use, appropriately adjusting for the association between treatment drop-in and risk factor progression postbaseline. Importantly, MSMs estimate the difference in risk for a patient who receives treatment under different regimes (ie, the causal effect of treatment under the counterfactual framework). In contrast, the aforementioned modeling techniques described cannot be used in this way since they do not explicitly consider counterfactuals.16 In practice, CPMs are often used in a counterfactual manner,17 so if such an interpretation were possible, this would be useful.'

## Unsuitable methods for our study

### Predictor substition

You could **remove all the predictors upon which the decision to treat is based on**, and substitute them with alternative predictors.

Limitations:
* Can prevent you from including meaningful predictors in the model
* Other predictors may be correlated with the predictors used to make treatment decisions.

[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

### Incorporation of treatment as a predictor in the model

Another method is to include treatment use as a predictor in the prognostic model.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) In practice, you won't be able to input "they have been treated or not" for the as-yet untreated patients - but you could use the model to estimate outcomes in scenarios where they are or are not treated.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

You could just add the indicator on top of the prognostic model, keeping the original coefficients fixed.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8) However, if there is an interaction between the effectiveness of treatment and having a predictor (e.g. more effective in those with predictor), then the model will need to account for/incorporate this interaction.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) Instead therefore, the model could be entirely refitted with the addition of an indicator term for treatment, with the inclusion of interaction terms where anticipated.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

Limitations:
* Failure to correctly specify any interactions between treatment and other predictors in the validation set could mean that the effects of treatment are not completely taken into account[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)
* The addition of a term for treatment to the model that is to be validated may improve the performance beyond that of the original model due to the inclusion of additional predictive information[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)
* Not possible if everyone in the study had the same intervention (but in that case, it is likely that  unexpected findings are not due to a treatment paradox)[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)
* With this approach, 'differentiating treatment from predictor effects becomes difficult. We could adjust for the interaction between ‘decision to treat’ as a predictor and each of the other prognostic factors in the model; however, when many predictors are involved, or when ‘decision to treat’ is based on multiple predictors, this approach becomes complex. In such situations, extremely large sample sizes are needed for the reliable assessment of interactions.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

Due to the limitations, Pajouheshnia et al. 2017 do not recommend this approach.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)