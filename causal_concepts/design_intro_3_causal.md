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
