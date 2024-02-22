# Causal inference

# Notes from HarvardX course

https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2023/home

In 1970s, women began to receive oestrogren after menopause. Some studies in 1975/6 found that women receiving oestrogen had higher risk of diagnosis with endometrical cancer than women not receiving them. Why? Possibilities include...
1. Oestrogens cause cancer
2. Oestrogens can cause uterine bleeding, so women receive a uterine exam, during which the cancer (which is often silent, asymptomatic, and otherwise not diagnosed) is noticed and diagnosed - this phenomenon is called **ascertainment bias**

How do we decide which explanation is right?

* Yale researchers restricted the data analysis to women with uterine bleeding (regardless of whether they were on oestrogens), since they should all have the same likelihood of uterine exams and existing cancer being diagnosed. If there still an association, oestrogen causative.
* Boston researchers argued we would find association even in women who bleed and even if they don't cause cancer, and so that this approach would still have ascertainment bias.

Explanation one.
````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;

    a --> u;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Explanation two.
````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::white;

    a --> c;
    u --> c;
    c --> y;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Restrict analysis to women who bleed. If association still found, must be path of A --> U --> Y. Boston argued could still exist.
* Conditioning on C blocks path A-C-Y
* However, we still have path of A-C-U-Y, and C is collider on that path, so when condition on C, it becomes open (and conditioning on C is what we do when we restrict analysis to bleeders)

So Boston were right. 

````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::black;

    a --> c;
    u --> c;
    c --> y;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

What can you do then? You can design study where C-Y doesn't exist as you require all women to be screened for cancer frequently regardless of whether they bleed. If no association between A and Y, then we know there is no causal effect of A on U. If you still found association, then A must cause U.

````{mermaid}
  flowchart LR;

    a("A: Oestrogens"):::white;
    u("U: Cancer (unmeasured)"):::white;
    y("Y: Cancer (diagnosed)"):::white;
    c("C: Uterine bleeding"):::white;

    a --> c;
    u --> c;
    u --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````


### Example: HIV and ART

Randomised controlled trials of new antiretroviral therapy (ART) for HIV found it was effective and reduced morality by more than half.

Observational of clinical data to look at real world effect of ART did not detect much benefit for new combination therapies - no increased survival among those taking ART. What was wrong with the studies?

They were adjusting for lots of confounders - e.g. CD4 count - and yet could not eliminate the bias. Some people say there must be lots of unmeasured confounding. However, the more time-varying confounders were adjusted for, the more biased the effect estimate seemed to be. The problem was treatment-confounder feedback - the value of CD4 count was impacted by earlier treatment - in this case, the bias was in the opposite direction.

There is a way to identify whether the bias is due to incomplete adjustment for confounding or for incorrect adjustment for time-varying confounders - and that is to use G-methods to adjust for the time-varying confounders. When they used G-methods, the effect estimates were much closer to the ARTs.

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub><br>ART"):::white;
    
    lk("L<sub>K</sub><br>CD4 count"):::black;
    u("U<br>Immuno-suppression status"):::white;
    yk1("Y<sub>K+1</sub><br>Mortality"):::white;
    lk1("L<sub>K+1</sub><br>CD4 count"):::black;
    ak1("A<sub>K+1</sub><br>ART"):::white;
    yk2("Y<sub>K+2</sub><br>Mortality"):::white;
    
    lk --> ak;
    u --> lk; 
    u --> yk1;
    u --> lk1;
    lk1 --> ak1;
    u --> yk2;
    ak --> lk1;
    
    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

<mark>look more into methods of conditioning for things and confound adustment methods</mark>

## Causal SWIGs

### Example: EPO

EPO treats aneamia for people with serious kidney disease. In 2000s, the US were using much more EPO than doctors in Europe. Patients with end-stage renal disease need dialysis one or a few times a week, so have to spend a few hours in those facilities. In US, many of those are run by for-profit companies. Each pateint was paid fixed amount per dialysis session plus cost of EPO. However, the facilies bought EPO at a discount and charged government full price, and so more EPO used meant more profit, incentivising patients to be given higher doses of EPO. Patients in Europe receiving less EPO were not doing worse than the US patients. In fact, very high doses of EPO might be harmful and increase risk of cardiovascular disease, but no large randomised trials of EPO dosing in patients with end-stage renal disease, so conducted observational studies.

One of these was to perform a study that uses G-methods to adjust for time-varying confounding (for which there is alot in this situation as current EPO dose affects future haemoglobin values) and they estimated the mortality risk that would have been obesrved if all patients had received low dose, medium dose or high doses, and estimated no mortality differences.

After this was published, they realised the analysis was not helpful for doctors who had to decide how much EPO to give. In fact, their sophisticated analysis was quite naive.

# Notes from R

https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html

Causal DAGs are mathematically grounded, but they are also consistent and easy to understand. Thus, when we’re assessing the causal effect between an exposure and an outcome, drawing our assumptions in the form of a DAG can help us pick the right model without having to know much about the math behind it.

Chains and forks are open pathways, so in a DAG where nothing is conditioned upon, any back-door paths must be one of the two. In addition to the directed pathway to cardiac arrest, there’s also an open back-door path through the forked path at unhealthy lifestyle and on from there through the chain to cardiac arrest: [IMAGE] We need to account for this back-door path in our analysis. There are many ways to go about that–stratification, including the variable in a regression model, matching, inverse probability weighting–all with pros and cons. But each strategy must include a decision about which variables to account for. Many analysts take the strategy of putting in all possible confounders. This can be bad news, because adjusting for colliders and mediators can introduce bias, as we’ll discuss shortly. Instead, we’ll look at minimally sufficient adjustment sets: sets of covariates that, when adjusted for, block all back-door paths, but include no more or no less than necessary. That means there can be many minimally sufficient sets, and if you remove even one variable from a given set, a back-door path will open. Some DAGs, like the first one in this vignette (x -> y), have no back-door paths to close, so the minimally sufficient adjustment set is empty (sometimes written as “{}”). Others, like the cyclic DAG above, or DAGs with important variables that are unmeasured, can not produce any sets sufficient to close back-door paths.

For the smoking-cardiac arrest question, there is a single set with a single variable: {weight}. Accounting for weight will give us an unbiased estimate of the relationship between smoking and cardiac arrest, assuming our DAG is correct. We do not need to (or want to) control for cholesterol, however, because it’s an intermediate variable between smoking and cardiac arrest; controlling for it blocks the path between the two, which will then bias our estimate (see below for more on mediation).

Controlling for intermediate variables may also induce bias, because it decomposes the total effect of x on y into its parts. Depending on the research question, that may be exactly what you want, in which case you should use mediation analysis, e.g. via SEM, which can estimate direct, indirect, and total effects.

# Notes from Lederer and wordpress

## Confounders

### What is a confounder?

Traditionally, a **confounder** has been defined as any third variable that (a) associates with the predictor/exposure, (b) causes the outcome, and (c) doesn't reside in the causal pathway between the exposure and outcome. It is recommended that confounders are selected based on **prior knowledge**, rather than based on variables identified from the data.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

### Causal models

'Causal models can be represented visually using **directed acyclic graphs (DAGs)**. A DAG is a graph in which **unidirectional** arrows are used to represent known causal effects (on the basis of prior knowledge). Although investigators often feel some discomfort in deciding what causal effects do and do not exist on the basis of prior knowledge, the advantage of this approach is that it makes these assumptions explicit (and hence transparent). In fact, all other methods of controlling for confounding involve implicit assumptions about causal effects, which are not transparent to the reader.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 

#### Examples

Smoking is a **confounder** for the causal relationship between exercise and lung cancer. When we control for smoking, it closes the "back-door path", and the association between exercise and lung cancer is no longer observed.

'In a fully developed DAG with many paths, control of a small number of variables (a “minimum set” of confounders) will often close all back-door paths. We recommend using this approach in causal inference studies. DAGitty.net offers authors a simple interface with which to construct DAGs and identify back-door paths and minimum sets of confounders'.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 

````{mermaid}
  flowchart LR;

    ex("Exercise");
    lung("Lung cancer");
    smoking("Smoking");

    ex --> lung;
    smoking --> ex;
    smoking --> lung;
````

A **mediator** 'is a variable that lies along the causal path... between the exposure and disease'. They are of interest as they are the 'causes and mechanisms of disease'. Example: Some of the causal effect of exercise on lung cancer risk is mediated by immune function.

A path that includes a mediator is often called an **indirect effect** or indirect causal path. In contrast, the arrow directly connecting exercise and lung cancer represents the **direct causal effect** of exercise on lung cancer not due to changes in immune function.

'Control of a mediator (through adjustment or other means) will close the indirect causal path, preventing or limiting the ability to observe an association between the exposure and outcome (if indeed one exists). Mediators therefore require special attention (if they are to be examined at all) and should not be treated as confounders.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 

````{mermaid}
  flowchart LR;

    ex("Exercise");
    lung("Lung cancer");
    immune("Immune function");

    ex --> immune;
    immune --> lung;
    ex --> lung;
````

A **collider** is a variable with two or more causes that lie within a pathway of interest.  When both the exposure and outcome are causes of the collider, one may be tempted to control for the collider. However, colliders naturally block back-door paths. Controlling for a collider will open the back-door path, thereby introducing confounding.

'To clarify, imagine that, in reality, shift work is not a cause of obstructive sleep apnea. If we encountered a sleepy person with obstructive sleep apnea, their sleep apnea would likely be the cause of their sleepiness, and therefore they would be less likely to be a shift worker. Conversely, if we encountered a sleepy shift worker, it is likely that shift work is the cause of their sleepiness rather than obstructive sleep apnea. We would therefore observe that sleep apnea occurs less commonly among shift workers and thus report an inverse association. This confounded association results from conditioning on a collider (in this case, by only examining sleepy people). The same bias would occur if we were to adjust for sleepiness using a regression model.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

````{mermaid}
  flowchart LR;

    shift("Shift work");
    apnea("Obstructive sleep apnea");
    sleepy("Sleepiness");

    shift --> apnea;
    apnea --> sleepy;
    shift --> sleepy;
````

Collider bias may also be present when neither the exposure nor the outcome is a direct cause of the collider variable. An example is **M-bias**.

' In this example, we are testing the causal association between chronic β-blocker use and the risk of developing ARDS. We might be tempted to adjust for the presence of auscultatory crackles at hospital admission, because: 1) heart failure leads to both chronic β-blocker therapy and crackles, and 2) pneumonia causes both ARDS and crackles. These relationships may lead us to believe that crackles is a confounder, whereas in reality it is not. Instead, crackles is a collider on the back-door path of chronic β-blocker therapy ← heart failure → crackles ← pneumonia → ARDS. Adjusting for the presence of crackles opens this back-door path, introducing confounding. Ignoring the presence of crackles would be the right thing to do.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

````{mermaid}
  flowchart TD;

    beta("Beta blocker use");
    ards("Acute respiratory distress syndrome (ARDS)");
    hf("Heart failure");
    pneu("Pneumonia");
    crackles("Crackles");

    hf --> beta;
    hf --> crackles;
    pneu --> crackles;
    pneu --> ards;
    beta --> ards;
````

### Variable selection methods

'P value–based and model-based variable selection methods (including forward, backward, and stepwise selection) should not be used for causal inference. These approaches ignore the causal structure underlying the hypothesis and therefore do not adequately control for confounding. Confounders and colliders are treated similarly. Methods relying on model fit or related constructs (such as r2, Akaike information criterion, and Bayesian information criterion) also have no relevance to causal inference. These methods rely heavily on the available data, in which causal relationships may or may not have been captured and may or may not be evident. Specification of the model and the arbitrary variables included in any particular model will drive observed associations with the outcome. Selection of variables that, when included in a model, change the magnitude of the effect estimate of the exposure of interest should not be used to identify confounders, for the reasons discussed above. Identification of multiple “independent predictors” (“winners”) through purposeful or automated variable selection is an unacceptable approach for testing causal associations. If the authors have hypotheses about each variable, then a separate model for each variable should be generated using one of the above preferred approaches. Alternatively, a prediction model could be developed, if prediction, rather than causal inference, is the goal of the analysis.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

### Other

Table 2 Fallacy
Causal models are typically designed to test an association between a single exposure and an outcome. The additional independent variables in a model (often called “covariates”) serve to control for confounding. The observed associations between these covariates and the outcome have not been subject to the same approach to control of confounding as the exposure. Therefore, residual confounding and other biases often heavily influence these associations. This situation is known as “Table 2 fallacy,” a term arising from the practice of presenting effect estimates for all independent variables in “Table 2” (20). We strongly caution authors to avoid presenting these effect estimates in the primary manuscript.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

Moreover, what I really liked about the Lederer paper is their discussion of the Table 2 fallacy. The paper recommends that variables included as confounders should NOT be discussed and not be presented in the regression table at all (this is typically Table 2 in a paper, thus the name), because they are themselves usually not corrected for confounding (and they shouldn’t or at least don’t have to be corrected for, see Pearl 2000 / discussion above). Sensible advice, but I think contrary to common practice in standard and SEM regression reporting in ecology. A cynical (but possibly accurate) explanation for why the Table 2 fallacy is the norm in ecology is that we rarely have a clear target variable / hypothesis, and thus we feel all variables that were used have to be discussed. A side effect is that this makes for the most boring result / discussion sections, where the effect of one variable after the other has to be discussed an interpreted. More importantly, however, each variable that is discussed as a causal effect must be controlled for confounding, or else we should make a clear distinction between the variables that are controlled, and those that aren’t. As I said, Lederer recommend not mentioning uncontrolled variables at all. I’m not sure if that is practical for ecology (as analyses are often semi-explorative), but I have recently been wondering about the option to separate reasonably controlled from possibly confounded variables by a bar or extra section in the regression table.[[source]](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/)

Causal Association, Causal Effect, and Claiming Causality
Readers may find it unusual that we are using the word “causal” to describe observed associations. When examining associations in observational causal inference studies, the intention is always to seek evidence to support (or refute) a true causal effect of the exposure on the outcome. Of course, we often cannot establish these causal effects from any single study. Yet, by acknowledging the intent, it is reasonable to use the label “causal association” (but not “causal effect”) to describe findings arising from an observational study.

We therefore caution authors that claims of causality should be avoided without substantial evidence of a true causal effect, as espoused by Bradford Hill (21) and further developed by John Ioannidis (22). It is reasonable to use the term “effect estimate” when referring to a causal association in an observational study, but assertions that an exposure has an “effect” or “impact” on the outcome, or that the exposure “protects against” or “promotes” the outcome, should not be made.

A Note on Methods to Control for Confounding
Investigators may control for confounding either in the design or analysis of a study. Randomization to exposure, use of an instrumental variable, weighted regression via propensity scores, adjustment using multivariable regression, stratification on a confounder, conditioning enrollment on a confounder (restriction), and matching on a confounder are common methods (4). We do not make recommendations for or against any of these methods.

[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## To read

Books
* Pearl J, Mackenzie D. The book of why: the new science of cause and effect. New York, NY: Basic Books; 2018. (17)
* Pearl J. Causality: models, reasoning, and inference. New York, NY: Cambridge University Press; 2009.
* Hernán MA, Robins JM. Causal Inference. Boca Raton: CRC Press; 2018 (Available from: https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

Articles
* Greenland S, Pearl J, Robins JM. Causal diagrams for epidemiologic research. Epidemiology 1999;10:37–48.
* Greenland S. Quantifying biases in causal models: classical confounding vs collider-stratification bias. Epidemiology 2003;14: 300–306. (9)
* Hernán MA, Hernández-Díaz S, Robins JM. A structural approach to selection bias. Epidemiology 2004;15:615–625. (11)
* Schisterman EF, Cole SR, Platt RW. Overadjustment bias and unnecessary adjustment in epidemiologic studies. Epidemiology 2009;20:488–495. (13)
* Morabia A. History of the modern epidemiological concept of confounding. J Epidemiol Community Health 2011;65:297–300. (12)
* Williamson EJ, Aitken Z, Lawrie J, Dharmage SC, Burgess JA, Forbes AB. Introduction to causal diagrams for confounder selection. Respirology 2014;19:303–311. (14)
* Hernán MA. The C-word: scientific euphemisms do not improve causal inference from observational data. Am J Public Health 2018;108:616–619.