# Other design considerations

Beyond the treatment paradox, there are other reasons why we might see unexpected relationships in prediction models.

## Chance

We can see an unexpected predictor-outcome relationship due to chance, particularly if our sample size is small.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

## Misclassification

Unexpected findings can occur due to problems with the predictors - e.g.
* Measurement contains errors (e.g. some people coded as one outcome when they're the other)
* Predictor model incorrectly (e.g. categorised continuous variable, or linear transformation on non-linear predictor)
* Collinearity (when 2+ predictors are highly correlated) - although this one shouldn't affect predictive accuracy

Solutions: Redo measurement, model correctly, delete erroneous values, omit colinear variables or combine into single variable, or interpret in combination, or adopt a different model.

Example: Study predicting risk of metabolic acidosis in neonates, when thresholds for intrapartum fever were adjusted, an unexpected relationship with temperaturee disappeared.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

'Physiological measurements used as predictors are not linear in relation to outcome, but are U- or inverted U-shaped. For example, we all appreciate the increased perinatal mortality associated with maternal hypertension, but fewer people know that hypotension accounts for 91% of excess perinatal deaths associated with non-average blood pressure, possibly related to suboptimal placental perfusion (Steer et al. BMJ 2004;329:1312–14). The World Health Organization currently labels a maternal haemoglobin concentration of less than 110 g/l in pregnancy as ‘anaemia’ (www.who.int/vmnis/indicators/haemoglobin.pdf), although optimum birthweight occurs with mid-pregnancy haemoglobin concentrations of 95–105 g/l (Steer et al. BMJ 1995;310:489–91), and the substantial increase in perinatal mortality associated with haemoglobin concentrations above 120 g/l during pregnancy, as a result of poor plasma volume expansion (Little et al. Am J Obstet Gynecol 2005;193:220–6), is often unappreciated. A high early pregnancy maternal haemoglobin concentration is strongly related to the subsequent development of hypertension (Murphy et al. Lancet 1986;1:992–5), and yet is often ignored. Obstetricians are often unfamiliar with the complex statistics required to deal with these non-linear relationships.'[[Steer 2016]](https://doi.org/10.1111/1471-0528.13860)

## Selection bias

If both predictor and outcome affect probability of selecting participant for inclusion.[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

## Mixed effects (confounding)

'When 2 causes of a disease are mutually related, the observed effect of one can be mixed up with the effect of the other. In causal research, this phenomenon is referred to as confounding. Similarly, if 2 factors are mutually related (e.g., smoking and alcohol consumption) and one is causal for the outcome but the other is not, then exclusion of the causal factor would lead to the noncausal factor having a strong predictor effect unexpectedly.'[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)

## Heterogeneity

'The effect of a predictor may differ across subgroups of patients. This is referred to as a differential predictor effect, interaction, effect modification or heterogeneity of the predictor. When heterogeneity is not accounted for in the prediction model, the observed predictor effect is a (weighted) average of predictor effects within the different subgroups. If the predictor–outcome relations across subgroups are opposite, the direction of the observed relation depends on the proportional contributions of the subgroups.'

'In the prognostic model of metabolic acidosis in neonates (example 1), the effect of intrapartum fever on metabolic acidosis (OR 0.86 [95% CI 0.68–1.08]) was unexpected. Alongside the impact of misclassifying the presence of fever (see Misclassification), this unexpected finding could also have been the result of an interaction between intrapartum fever and epidural analgesia among women who received epidural analgesia (OR 0.47 [95% CI 0.35–0.64]) versus women without epidural analgesia (OR 3.16 [95% CI 2.16–4.64]).'[[Schuit et al. 2013]](https://doi.org/10.1503/cmaj.120812)