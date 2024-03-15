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

### Marginal structure models

<mark>to add</mark>

'Marginal structural models “subtract” the effect of both current and future treatment use, appropriately adjusting for the association between treatment drop-in and risk factor progression postbaseline. Importantly, MSMs estimate the difference in risk for a patient who receives treatment under different regimes (ie, the causal effect of treatment under the counterfactual framework). In contrast, the aforementioned modeling techniques described cannot be used in this way since they do not explicitly consider counterfactuals.16 In practice, CPMs are often used in a counterfactual manner,17 so if such an interpretation were possible, this would be useful.'
