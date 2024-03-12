# Causal inference

As on the last page, etiological research aims to **uncover causal effects**. It involves finding an unbiased estimate of the effect of X on Y, by controlling for confounding factors that could bias the estimate.
This is an estimate of the causal effect of an exposure on an outcome[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 

## Terminology

Terminology can vary. Lederer et al. 2018 recommend that, by acknowledging the intent, it is reasonable to use the labels:
* **Causal association**
* **Effect estimate**

But not:
* Causal effect
* Exposure has an 'effect' or 'impact' on outcome
* Exposure 'protects against' or 'promotes' outcome

As these make claims of causality that should be avoided without substantial evidence of a true causal effect.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## Average causal effect

Causal inference for an individual (generating **individual causal effects**) is generallly impossible in health and social sciences (as you can't go back in time and not give them the outcome).

Instead, causal inference focusses on **average causal effect** when comparing groups of individuals.[[source]](https://hummedia.manchester.ac.uk/institutes/methods-manchester/docs/CausalInference.pdf)

## Languages for causality

When it comes to talking about and defining causality, pioneers in causal inference have come up with three languages.

| Language | Pioneers | Strengths | Limitations |
| --- | --- | --- | --- |
| Using **potential outcomes / counterfactuals** | 1923 Neyman (statistics); 1973 Lewis (philosophy); 1974 Rubin (statistics); 1986 Robins (epidemiology); [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Good for articulating the inference for a small number of causes and effects [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)<br>Easy to add additional assumptions [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Not as convenient if the system is complex [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) |
| Using **graphs** | 1921 Wright (genetics); 1988 Pearl (computer science “AI”); 1993 Spirtes, Glymour, Scheines (philosophy). [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Good for understanding the scientific problems [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)<br>Easy to visualise the causal assumptions [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Difficult for statistical inference because model is non-parametric [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) (i.e. doesn't make explicit assumptions about functional form of underlying population distribution... inference more challenging as no predefined functional forms) |
| Using **structural equations** | 1921 Wright (genetics); 1943 Haavelmo (econometrics); 1975 Duncan (social sciences); 2000 Pearl (computer science). [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Good for fitting simultaneous models for the variables (espeically for abstract concepts)[[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)<br>Bridge between graphs and counterfacturals.<br>Easy to operationalise[[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) | Danger to be confused with regression [[Zhao 2022]](https://www.statslab.cam.ac.uk/~qz280/teaching/causal-2023/notes-2021.pdf) |

### More on: Counterfacturals / Potential outcomes framework

To **define a causal effect**, we use the **potential outcomes framework** (also known as counterfactural or equivalent concepts approach[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) or Rubin or Neyman-Rubin causal model). This framework 'uses **mathematical notation** to describe **counterfactual outcomes** and can be used to describe the causal effect of an exposure on an outcome in statistical terms'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

Some key terms in the potential outcomes framework:
* **Counterfactuals** are a comparison between what is and what might have been (e.g. treatment v.s. no treatment).
  * *For example, I know ingesting the poison killed John, because if John hadn't ingested the poison, I know he would have lived.* [No source]
  * 'The counterfactual outcomes of a specific individual can never be known, since we can never observe the same individual both exposed and unexposed under the same circumstances' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
* **Exposure (A)** = 'treatment, intervention or other variable that could have taken one of several counterfactual values'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
  * We are often focussed on **interventions** (i.e. variables that can be manipulated), as they fit well in the potential outcomes framework. Although other variables like age, race and gender can have causal effects, they do not fit as cleanly in the potential outcomes framework.[[source]](https://www.coursera.org/learn/crash-course-in-causality/lecture/Lgb6O/hypothetical-interventions) Rubin states that *"if you are not talking about an intervention, you can't talk about causality"* - i.e. we're defining causality using counterfactuals, which is about the counterfactual effects of the intervention[[source]](https://baselbiometrics.github.io/home/docs/trainings/20210202/1_Moffa.pdf)
* **Outcome (Y)**

'Potential outcomes refer to **all possible outcomes** that an individual could experience—both those which are observed (factual) and those which are not (counterfactual). Given a binary exposure and a binary outcome, the possible combinations of actual and counterfactual outcomes give rise to four causal types':
* '**‘Doomed’**: would have experienced the outcome regardless of exposure.'
* '**‘Causative’**: would have experienced the outcome if exposed, otherwise not.'
* '**‘Preventative’**: would have experienced the outcome if unexposed, otherwise not.'
* '**‘Immune’**: would not have experienced the outcome regardless of exposure status.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

There are various notations used, but some examples are:
* Potential outcome if exposed (Y<sup>a=1</sup>) or not exposed (Y<sup>a=0</sup>)
* Expected value of continuous outcome (E(Y)) or probability of binary outcome(P(Y=1))
* Conditional expectation - expected value of Y given that another variable C is 1 (E(Y|C=1)) - i.e. expected values conditional on C / within levels of C / holding C constant. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
