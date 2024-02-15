# Accounting for a treatment paradox

This page aims to answer the question: **How do you design a study that accounts for the treatment paradox?**

## Exclude treated individuals

Excluding individuals who received treatment will provide 'correct estimates of performance in the (untreated) target population if treatment use is associated with other prognostic factors' - but it will 'decrease the effective sample size' (which could cause you to not see an effect if you don't have the power).[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

In their simulation study, Pajouheshnia et al. 2017 find that excluding treated individuals resulted in calibration measures that appeared to reflect those of the untreated target population in most scenarios. However, when treatment allocation ws dependent on an individual’s risk, it resulted in a loss of information about calibration in high risk individuals. As treatment allocation became increasingly associated with an individual’s risk across scenarios, this method yielded lower estimates for discrimination than observed in the untreated set, due to the selective exclusion of high-risk individuals, and consequently a narrower case-mix. In the presence of a strong unmeasured predictor of the outcome associated with treatment use, exclusion of treated individuals resulted in an underestimation of the performance of the model. In addition, in all scenarios the precision of estimates of both the observed:expected ratio and c-index (area under the ROC curve) decreased due to the reduction in effective sample size.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

## Inverse probability weighting

Inverse probability weighting (IPW) is a method that is used to balance data where there is non-random treatment use, so it instead resembles use in an RCT. It is used when we want to estimate a causal association between an exposure and outcome whilst accounting for the influence of confounders.

Method:
1. Fit "treatment propensity model" on validation data - this is a regression model where the outcome is treatment use, and the predictors are variables that might predict treatment use, including the predictors of the prognostic model being evaluated.
2. Used that model to estimate the probability that each patient in the validation set receives a treatment.
3. Weight each individual by the inverse of their probability of the actual treatment received. This will produce a distribution of risks in the validation set that resembles what would have been seen had treatments been randomly allocated
4. If you then exclude the treated individuals after deriving weights, the resulting validation set should resemble the untreated target population

Limitations:
* Exclusion of treated individuals will mean a smaller sample size
* Practical non-positivity violates assumptions. This is when there is a risk strata where no subjects receive treatment - e.g. if have contraindication for treatment, or when guidelines already recommend that individuals above a certain probability threshold should receive treatment. This can lead to individuals receiving extreme weights, resulting in biased and imprecise estimates of model performance
* Incorrect specification of the treatment propensity model (e.g. unmeasured confounders) can also cause issues

Variants of IPW can be applied - e.g. weight truncation, which aims to improve performance when assumptions are violated.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

In their simulation study, Pajouheshnia et al. 2017 find that IPW alone did not improve calibration (compared to when we did nothing to account for the treatment paradox), but IPW followed by the exclusion of treated individuals provided correct estimates for calibration. IPW alone or followed by the exclusion of treated individuals improved estimates of the c-index in all scenarios where the assumptions of positivity and no unobserved confounding were met. In scenario 4, where treatment allocation was determined by a strict risk-threshold and thus the assumption of positivity was violated, IPW was ineffective, and resulted in the worst estimates of discrimination across all methods. In addition, the extreme weights calculated in scenario 4 led to very large standard errors. In scenarios 13–15, the presence of an unobserved confounder led to the failure of IPW to provide correct estimates of the c-index. Weight truncation at the 98% percentile increased precision, but was less effective in correcting of the c-index for the effects of treatment.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

'Although the use of IPW prior to the exclusion of treated individuals is a promising solution in data where treatments are non-randomly allocated, it should not be used when there are severe violations of the underlying assumptions, e.g. in the presence of non-positivity (where some individuals had no chance of receiving treatment), or when there is an unobserved confounder, strongly associated with both the outcome and treatment use. There is thus a need to explore alternative methods to IPW to account for the effects of treatment use when validating a prognostic model in settings with non-random treatment use.'[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

## Propensity scores

Propensity scores are 'the probability of a treatment being assigned to an individual based on observed pre-treatment variables. One can designate propensity scores to each individual in the study taking into account the multiway interactions with other predictors (on which the decision to treat was based). Such a model provides risk estimates for an individual taking into account the probability of requiring treatment.'

Limitations:
* It requires a prior knowledge of the propensity score
* It has limited clinical applicability for making decisions on whether to treat.

'A related option is to take into account each participant's propensity score by using it to define a weight for the contribution of that particular participant towards the logistic model analysis and development of the prognostic model. Women who received little or no treatment (and hence less treatment effect) should carry more weight than those who had a high probability of being treated.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

## Incorporation of treatment as a predictor in the model

Another method is to include treatment use as a predictor in the prognostic model.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) In practice, you won't be able to input "they have been treated or not" for the as-yet untreated patients - but you could use the model to estimate outcomes in scenarios where they are or are not treated.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

You could just add the indicator on top of the prognostic model, keeping the original coefficients fixed.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8) However, if there is an interaction between the effectiveness of treatment and having a predictor (e.g. more effective in those with predictor), then the model will need to account for/incorporate this interaction.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812) Instead therefore, the model could be entirely refitted with the addition of an indicator term for treatment, with the inclusion of interaction terms where anticipated.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

Limitations:
* Failure to correctly specify any interactions between treatment and other predictors in the validation set could mean that the effects of treatment are not completely taken into account[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)
* The addition of a term for treatment to the model that is to be validated may improve the performance beyond that of the original model due to the inclusion of additional predictive information[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)
* Not possible if everyone in the study had the same intervention (but in that case, it is likely that  unexpected findings are not due to a treatment paradox)[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)
* With this approach, 'differentiating treatment from predictor effects becomes difficult. We could adjust for the interaction between ‘decision to treat’ as a predictor and each of the other prognostic factors in the model; however, when many predictors are involved, or when ‘decision to treat’ is based on multiple predictors, this approach becomes complex. In such situations, extremely large sample sizes are needed for the reliable assessment of interactions.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

Due to the limitations, Pajouheshnia et al. 2017 do not recommend this approach.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

## Use treatment as the outcome

When starting a treatment is likely to prevent an adverse outcome, those who received the treatment could also be considered to have experienced the outcome.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

For example, 'in women with early-onset pre-eclampsia, if a large proportion of women are delivered at an early preterm gestation (before 34 weeks), then delivery itself could be considered as an outcome (replacing complications that would have occurred in the absence of delivery). In the absence of a standardised protocol for decision to deliver at early preterm gestation, such an approach could help to overcome the limitations in the model as a result of delivery preventing the occurrence of an adverse outcome.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

## Recalibration

**Don't yet understand:** 'The incidence of the predicted outcome may vary between development and validation data sets. If this is the case, the predictions made by the model will not, on average, match the outcome incidence in the validation data set [22]. As discussed in section 2.1, use of an effective treatment in a validation data set will lead to fewer outcome events and thus a lower incidence than there would have been had the validation set remained untreated. One approach to account for this would be to recalibrate the original model using the partially treated validation data set. In a logistic regression model, a derivative of the incidence of the outcome is captured by the intercept term in the model, and thus a simple solution would seem to be to re-estimate the model intercept using the validation data set [23, 24]. In doing this, the average predicted risk provided by the recalibrated model should then be equal to the (observed) overall outcome frequency in the validation set. Further details of this procedure are given in Table ​Table1.1. Where treatment has been randomly allocated, intercept recalibration should indeed account for the risk-lowering effects, provided that the magnitude of the treatment effect does not vary depending on an individual’s risk and thus is constant over the entire predicted probability range. In non-randomized settings, where treatment use by definition is associated with participant characteristics, a simple intercept recalibration is unlikely to be sufficient due to interactions between treatment use and patient characteristics that are predictors in the model. However, although recalibration may seem a suitable solution for modelling the effects of treatment, when applying recalibration, concerns should also be raised over the interpretation of the estimated performance of the model. Differences in outcome incidence between the development data set and validation data set may not be entirely attributable to the effects of treatment use. By recalibrating the model to adjust for differences in treatment use and effects, we simultaneously adjust for differences in case-mix between the development and validation set. As the aim of validation is to evaluate the performance of the original prognostic model, in this case in a treatment-naïve sample, recalibration may actually lead to an optimistic impression of the accuracy of predictions made by the original model in the validation set. For example, if the validation set included individuals with a notably greater prevalence of comorbidities and thus were more likely to develop the outcome, recalibration prior to validation could mask any inadequacies of the model when making predictions in this subset of high-risk individuals.'[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)

Due to the limitations, Pajouheshnia et al. 2017 do not recommend this approach.[[Pajouheshnia et al. 2017]](https://doi.org/10.1186%2Fs12874-017-0375-8)


## The existence of fully standardised care with no variation in treatment (or accounting for clinician differences with multi-level models)

This is a scenario where there is complete collinearity between the predictor and the treatment, where the presence of a particular predictor will always guarantee the presence of a particular treatment.

However, that requires no variation in treatment - that the same medications and dosages are always provided at the same treatment thresholds at the same times. This is not realistic. With the example of management of early-onset pre-eclampsia, such as the commencement of anti-hypertensives and magnesium sulphate, this is somewhat standardised by guidelines [e.g. from the National Institute for Health and Care Excellence (NICE) in the UK], but the threshold for commencing treatment varies between clinicians and centres. Furthermore, the response from a specific antihypertensive and dosage varies between individual patients.

This limits the applicability of such a strategy, although one could consider the use of multilevel models to allow for any differences between clinicians and treatment centres.'[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859)

Steer 2016 comments that 'such models rarely take into account all of the relevant factors (e.g. the coexistence of a modulating pathology such as an autoimmune disorder) or the social and emotional circumstances and preferences of the mother and her family.'[[Steer 2016]](https://doi.org/10.1111/1471-0528.13860)

## Predictor substition

You could remove all the predictors upon which the decision to treat is based on, and substitute them with alternative predictors. However, this can prevent you from including meaningful predictors in the model, and other predictors are potentially correlated with the predictors used to make treatment decisions.[[Cheong-See et al. 2016]](https://doi.org/10.1111/1471-0528.13859) Hence, this is not recommended.