# Causal inference

Once have built up understanding around this, **integrate as appropriate with the treatment paradox pages** (as that is the reason for reading around this, since the concepts and methologies are related to the treatment paradox).

## Directed acyclic graphs

* Nodes
* Arrows (directed edges)
* Drawing a box around a node indicates that we are conditioning on that node

# TO SORT

# Notes from HarvardX course

https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2023/home

In 1970s, women began to receive oestrogren after menopause. Some studies in 1975/6 found that women receiving oestrogen had higher risk of diagnosis with endometrical cancer than women not receiving them. Why? Possibilities include...
1. Oestrogens cause cancer
2. Oestrogens can cause uterine bleeding, so women receive a uterine exam, during which the cancer (which is often silent, asymptomatic, and otherwise not diagnosed) is noticed and diagnosed - this phenomenon is called **ascertainment bias**

How do we decide which explanation is right?

* Yale researchers restricted the data analysis to women with uterine bleeding (regardless of whether they were on oestrogens), since they should all have the same likelihood of uterine exams and existing cancer being diagnosed. If there still an association, oestrogen causative.
* Boston researchers argued we would find association even in women who bleed and even if they don't cause cancer, and so that this approach would still have ascertainment bias.

We'll return to this later.

Directed acyclic graph (or "causal graphs" or "DAGs") (directed due to arrow direction, and acyclic as you can't go round in a circle)
* Nodes
* Arrows i.e. directed edges. They indicate direction of causality

**How do you know what to include?**

DAGs are causal DAGs if, when two variables share a cause, that cause is also in the graph. This is known as the **causal markov condition**.

Gave example of RCT investigating aspirin causing stroke. Do you also need to include other variables that cause stroke (e.g. high blood pressure, coronrary heart disease, diet, genes)? No, because they didn't cause why people got Aspirin, as it was an RCT, so we don't need to include them in the graph. A causal DAG in this case is just Aspirin --> Stroke.

````{mermaid}
  flowchart LR;

    asp("Aspirin");
    str("Stroke");

    asp --> str;
````

If it were observational, using electronic medical records, comparing people who received Apirin or not. Here, people who have coronary heart disease are more likely to receive aspirin, so have to include. If we excluded it, it would not be a causal DAG.

````{mermaid}
  flowchart LR;

    asp("Aspirin");
    str("Stroke");
    chd("Coronary heart disease")

    asp --> str;
    chd --> asp;
    chd --> str;
````

**When should you draw arrows**

When you believe something causes something else. However, if our expert knowledge is insufficient for us to rule out a direct effect of variable D on variable E, we should draw an arrow from D to E on the causal DAG.

**Why draw?**

They're helpful becausal they are both (a) qualitative causal models, and (b) statistical models. We can draw the graph using our expert knowledge, and we're also building a statistical model without realising it. This is because causal effect implies association, and no causal effect implies independent.This is important as biases are associations, and we can use causal graphs to conceptualise biases and identify them.

Example:
* Based on our expert knowledge, we believe smoking causes lung cancer.
* We expect smoking and lung cancer to be **associated** if there is a causal effect, and **independent** if there is not 
* There will be an association if the proportion of individuals with cancer differs between smokers and non-smokers. Equivalent, is that they are associated if having information about smoking helps us to better predict lung cancer

So, if we use expert knowledge to draw causal graph, we are drawing statistical model saying they are associated or independent.

````{mermaid}
  flowchart LR;

    cig("Smoking");
    lung("Lung cancer");

    cig --> lung;
````

#### Inclusion of mediators

<mark> i don't understand the explanation given below </mark>

We could include lung cell damage, as it is one of the mediators of this relationship. However, we **don't need to include mediators**, when our goal is to estimate the effect of smoking on lung cancer. (It would be pretty impossible to cause all mediators normally anway, as we don't have information on them).

If we do **include mediators, our question is then about conditional independence** - is the relationship between smoking and lung cancer **conditional** on lung cell damage. We can do this by restricting analysing to subset of individuals with particular level of cell damage, which we would represent in the DAG using a square box around cell damage. In the subset with cell damage, we check for association between smoking and lung cancer.

According to the graph, effect of smoking is entirely mediated through cell damage - so learning they are a smoker should provide no additional information with respect to risk of developing lung cancer.
* If someone with cell damage has 10% chance of cancer, being a smoker shouldn't change that number
* If someone without cell damage has 1% chance of cancer, being a smoker (without damage) shouldn't change that number
* In this case, it would be no conditional association between smoking and lung cancer, for all levels of cell damage

So if no direct arrow from smoking to lung cancer, we are saying there is no association between smoking and lung cancer conditioned on lung cell damage, even though smoking has a causal effect on lung cancer.

Note: Arrows on causal graphs are not deterministic - i.e. doesn't mean every smoker will see cell damage - as some will never, and some non-smokers will develop it.

````{mermaid}
  flowchart LR;

    cig("Smoking");
    lung("Lung cancer");
    cell("Lung cell damage");

    cig --> cell;
    cell --> lung;
````

````{mermaid}
  flowchart LR;

    cig("Smoking");
    lung("Lung cancer");
    cell("Lung cell damage");

    cig --> lung;
    cig --> cell;
    cell --> lung;
````

Another example...

Causal DAG representing belief that aspirin can only reduce risk of stroke through reduction of platelet aggregation

````{mermaid}
  flowchart LR;

    asp("Aspirin"):::white;
    plat("Platelet aggregation"):::white;
    stroke("Stroke"):::white;

    asp --> plat;
    plat --> stroke;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Causal DAG representing finding that aspirin is associated with stroke, conditionally on platelet aggregation (i.e. find association even when condition)

````{mermaid}
  flowchart LR;

    asp("Aspirin"):::white;
    plat("Platelet aggregation"):::white;
    stroke("Stroke"):::white;

    asp --> plat;
    plat --> stroke;
    asp --> stroke;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Causal DAG representing finding that aspirin is not associated with stroke (unconditionally).

#### Confounding: causal structures with common causes

We expect to see association between yellow fingers and lung cancer even if there is no causal effect. This association is a **bias** - specifically, there is **confounding**, and is referred to as us expecting to see that yellow fingers is marginally (unconditionally) associated with death.

````{mermaid}
  flowchart LR;

    cig("Smoking"):::white;
    lung("Lung cancer"):::white;
    yellow("Yellow fingers"):::white;

    cig --> lung;
    cig --> yellow;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Our goal in causal inference is to eiliminate bias due to confounding.

If we condition on smoking, expect to see no association between yellow fingers and lung cancer - i.e. they are **not associated conditional on smoking**.

````{mermaid}
  flowchart LR;

    cig("Smoking"):::black;
    lung("Lung cancer"):::white;
    yellow("Yellow fingers"):::white;

    cig --> lung;
    cig --> yellow;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Summary: We existance of a shared cause of treatment and outcome to result in bias.

#### Selection bias: causal structures with common effects

If genetic factor doesn't have causal effect on environmental factor (as in graph), then we **don't expect to see an association** - they are **independent**. The environmental factor is distributed in the population independently of genetics. Learning an individual has a genetic factor should provide no additional information on environmental exposure.

````{mermaid}
  flowchart LR;

    gene("Genetic factor"):::white;
    env("Environmental factor"):::white;
    cancer("Cancer"):::white;

    gene --> cancer;
    env --> cancer;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

The common effect cancer is a **collider** as two arrows collide with it. A collider blocks the flow of association along the path they lie on.

Above was the unconditional/marginal association. We can look at whether genes and environment are associated conditional on cancer. We can just look at people who developed cancer, and see if proportion exposed to environment is different depending on genetic.

As the cancer is caused by gene or environment, if they have cancer and not genetic, they're more likely to have environment - not because genetic protects against environmental factor, but because something must have caused it. Hence, we expect an **inverse association** between the genetic and environmental factor when we condition on cancer. There is a conditional association between A and Y within levels of L. In this case, it is an inverse association. This is a **biased effect estimate**.

In this case, when a component of the association is due to selecting a subset of the population (e.g. just looking at cancer patients), we say there is a **selection bias**.

We can **induce** selection bias by conditioning on the downstream consequence of a collider - e.g. if cancer is collider, and surgery is consequence of cancer, if we condition on surgery, we expect to see inverse association between genetic and environment conditional on surgery (just as we did for the collider cancer).

Summary: We expect conditioning on a common effect of treatment and outcome to result in bias.

In the graph, when you condition on cancer, draw black box

````{mermaid}
  flowchart LR;

    gene("Genetic factor"):::white;
    env("Environmental factor"):::white;
    cancer("Cancer"):::black;

    gene --> cancer;
    env --> cancer;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

#### Summary

Causal structures where we expect to see an association (i.e. structural sources of association):
* Cause and effect
* Common causes (confounding)
* Conditioning on common effects (conditioning on collider)

````{mermaid}
  flowchart LR;

    a:::white;
    b:::white;
    c:::white;
    d:::white;
    e:::white;
    f:::white;
    g:::white;
    h:::black;

    a --> b;

    c --> d;
    c --> e;

    f --> h;
    g --> h;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

There is another source of association: **chance**. May be association even if none of above are true. Chance is not a structural source of association. Increasing our sample size, chance associations should disappear (whilst structural remain and become sharper).

#### Names

````{mermaid}
  flowchart LR;

    a("A (parent)"):::white;
    b("B (child)"):::white;
    c("C (grandparent)"):::white;
    d("D"):::white;
    e("E (grandchild)"):::white;

    a --> b;
    c --> d; d --> e;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

#### Paths

**Path** is any route through graph (can follow arrow direction or not). Paths can be **blocked or open**, which is according to the **D-seperation rules**.

We use D-seperation to decide whether two variables are D-seperated, where D stands for directional.

D-seperation rules:

**RULE ONE.** If there are no variables being conditioned on, a path is blocked if and only if two arrowheads on the path collide at some variable on the path

Path from A to Y is **open**:
````{mermaid}
  flowchart LR;

    a("A"):::white;
    b("B"):::white;
    y("Y"):::white;
    
    a --> b; b--> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Path from A to Y is **blocked**:
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::white;
    d("D"):::white;
    
    a --> l; y --> l; l --> d;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Definition of collider is path-specific. L is collider on path A to Y, but on on path A to D. 

**RULE TWO.** Any path containing non-collider that has been conditioned on is blocked.

Path from A to Y is **blocked**:
````{mermaid}
  flowchart LR;

    a("A"):::white;
    b("B"):::black;
    y("Y"):::white;
    
    a --> b; b--> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

**RULE THREE.** A collider that has been conditioned on does not block a path.

Path from A to Y is **open**:
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::black;
    
    a --> l; y--> l;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

**RULE FOUR.** Collider with descendent that has been conditioned on does not block a path.

Path from A to Y is **open**:
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::white
    d("D"):::black;
    
    a --> l; y--> l; l --> d;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

**SUMMARY** Path is blocked only if (a) containins non-collider that been conditioned on, or (b) collider that not been conditioned on.

Two variables are D-seperated if all paths between them are blocked.

Two variables are marginally or unconditionally independent if they are D-seperated without conditioning on all the variables

Two variables are conditionally independent if they are D-seperated after conditioning

you will be able to see that all D-separation says is that two variables **would be associated** if:
* one causes the other,
* they share common causes
* they have a common effect and we condition on the common effect.


#### Faithfulness

Faithfulness is the result of opposite effects of exactly equal magnitude - e.g. if aspirin caused stroke for half of poppulation and prevented it in the other half, then causal dag is correct (as aspirin affects stroke) but no association is observed (as they cancel each other out). In that case, we say the joint distribution of the data is not faithful to the causal DAG.

These perfect cancellations are rare and we don't expect them to happen in practice, so we can safetly say lack of D-seperation means non-zero association. So - 
* **D-seperation = statistical independence**
* **All paths blocked = no association**

#### Oestrogens and uterine cancer

Returning to example from start.

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

#### Why do DAG?

* Helps identify problems in study design and guide data analysis
* More precise and efficient than writing many pages of assumptions

# Notes from R

https://cran.r-project.org/web/packages/ggdag/vignettes/intro-to-dags.html

Causal DAGs are mathematically grounded, but they are also consistent and easy to understand. Thus, when we’re assessing the causal effect between an exposure and an outcome, drawing our assumptions in the form of a DAG can help us pick the right model without having to know much about the math behind it.

Chains and forks are open pathways, so in a DAG where nothing is conditioned upon, any back-door paths must be one of the two. In addition to the directed pathway to cardiac arrest, there’s also an open back-door path through the forked path at unhealthy lifestyle and on from there through the chain to cardiac arrest: [IMAGE] We need to account for this back-door path in our analysis. There are many ways to go about that–stratification, including the variable in a regression model, matching, inverse probability weighting–all with pros and cons. But each strategy must include a decision about which variables to account for. Many analysts take the strategy of putting in all possible confounders. This can be bad news, because adjusting for colliders and mediators can introduce bias, as we’ll discuss shortly. Instead, we’ll look at minimally sufficient adjustment sets: sets of covariates that, when adjusted for, block all back-door paths, but include no more or no less than necessary. That means there can be many minimally sufficient sets, and if you remove even one variable from a given set, a back-door path will open. Some DAGs, like the first one in this vignette (x -> y), have no back-door paths to close, so the minimally sufficient adjustment set is empty (sometimes written as “{}”). Others, like the cyclic DAG above, or DAGs with important variables that are unmeasured, can not produce any sets sufficient to close back-door paths.

For the smoking-cardiac arrest question, there is a single set with a single variable: {weight}. Accounting for weight will give us an unbiased estimate of the relationship between smoking and cardiac arrest, assuming our DAG is correct. We do not need to (or want to) control for cholesterol, however, because it’s an intermediate variable between smoking and cardiac arrest; controlling for it blocks the path between the two, which will then bias our estimate (see below for more on mediation).

Controlling for intermediate variables may also induce bias, because it decomposes the total effect of x on y into its parts. Depending on the research question, that may be exactly what you want, in which case you should use mediation analysis, e.g. via SEM, which can estimate direct, indirect, and total effects.

# Notes from Lederer and wordpress

## Causality

'Causal inference is the examination of causal associations to estimate the causal effect of an exposure on an outcome.'[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 'Assume we look at the effect of a target variable (something that could be manipulated = predictor) on another variable (the outcome = response) in the presence of other (non-target) variables. The goal of a causal analysis is is to control for these other variables, in such a way that we obtain the same effect size for the target variable that we would if the target predictor was manipulated in a controlled intervention (= experiment).'[[source]](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/)

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