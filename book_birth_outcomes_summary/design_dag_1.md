# Introduction to directed acyclic graphs (DAGs)

`````{admonition} Executive summary
:class: info

Causal diagrams (directed acyclic graphs - DAGs) are based on expert knowledge. They depict the causal relationships between nodes using directed arrows. They are used to illustrate/identify sources of bias, to indicate where associations/independence should be expected, and to help inform study design.

In a DAG, you can identify:
* **Confounders** - common cause both treatment and outcome
* **Mediators** - lie on causal path between variables, inclusion depends on whether you are interested in direct effect of treatment and outcome that doesn't pass through mediator
* **Colliders** - common effect of two other variables
* **Moderators** - change size or direction of relationship between variables

You start the diagram with your research question (i.e. two nodes whose relationship you are interested) and then add all **common** causes for those nodes, and for any other nodes you add to the graph.
`````

## Introduction to causal diagrams

### What are causal diagrams?

Causal diagrams - **directed acyclic graphs (DAGs)** - depict causal relationship between different variables. Two key components are **nodes** and **arrows**.

They are:
* **Directed** - as arrows have a single direction (unidirectional) that represents known causal effects (based on prior knowledge)
* **Acyclic** - as nodes cannot have a directed path from itself back to itself [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

Example:

````{mermaid}
  flowchart LR;

    asp("Aspirin"):::white;
    str("Stroke"):::white;

    asp --> str;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

### Naming conventions

There are naming conventions for particular components of the DAG:
* **A (or E)** = Exposure / Treatment / Intervention / Primary IV
* **Y (or D)** = Outcome
* **C** = Covariates / Confounders
* **U** = Unmeasured relevant variables

When letters are not used, the exposure and outcome will often be highlighted using a "?" on the arrow, or through coloured boxes or arrows.

Example:

````{mermaid}
  flowchart LR;

    A:::green;
    Y:::green;
    C:::white;
    U:::white;
    
    A -->|?| Y;
    C --> A;
    C --> Y;
    U --> A;
    U --> C;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Nodes can also be described as:
* **Ancestor** = direct cause (**parent**) or indirect cause (e.g. **grandparent**) of a variable
* **Descendent** = direct effect (**child**) or indirect effect (e.g. **grandchild**) of a variable [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### Why do we create causal diagrams?

We don't draw causal diagrams as an exact, accurate representation of the world - instead, we draw causal DAGs to help us think about possible sources of bias when making causal inferences.

* They make sure we illustrate and identify our sources of biases (assumptions)
    * More precise and efficient than writing pages of assumptions[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)
    * Although they are based on assumptions, so are analytic models.[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)
    * Although investigators often feel some discomfort in deciding what causal effects do and do not exist on the basis of prior knowledge, the advantage of this approach is that it makes these assumptions explicit (and hence transparent).[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 
* They indicate when associations or independence should be expected.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)
* They can help determine whether the effect of interest can be identified from available data, and help us clarify our study question[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf) - and to identify problems in the study design[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Key components

### Confounders

**Confounders** are variables that **cause BOTH the treatment/exposure and outcomes**. Informally, it occurs when there is an open backdoor path between the treatment/exposure and outcome, and you could say a confounder is a variable that - possibly together with other variables - can be used to block the backdoor path between the treatment and outcome. We included **measured and unmeasured** confounders in our DAG.

Example: smoking causes yellow fingers and lung cancer
* If we don't condition on it, we expect to see an association between yellow fingers and lung cancer (known as a **marginal/unconditional** association)
* If we do condition on smoking, we expect to see no association between yellow fingers and lung cancers (i.e. they are "**not associated conditional on** smoking)[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart TD;

    con:::outline;
    subgraph con["`**Conditional**`"]
      cig2("Smoking"):::black;
      lung2("Lung cancer"):::white;
      yellow2("Yellow fingers"):::white;
    end

    cig2 --> lung2;
    cig2 --> yellow2;

    uncon:::outline;
    subgraph uncon["`**Unconditional**`"]
      cig("Smoking"):::white;
      lung("Lung cancer"):::white;
      yellow("Yellow fingers"):::white;
    end

    cig --> lung;
    cig --> yellow;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef outline fill:#FFFFFF;
````

### Moderators

**Moderators** are variables that change the **size or direction** of the relationship between variables. These could also be referred to as effect modifiers or statistical interaction. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)
* They usually help you judge the external validity of your study by identifying the limitations of when the relationship between variables holds. [[source]](https://www.scribbr.co.uk/faqs/why-should-you-include-mediators-and-moderators-in-your-study/) 
* There has been some disagreement on how these should be included/notation within DAGs. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)[[Weinberg 2007]](https://pubmed.ncbi.nlm.nih.gov/17700243/)

````{mermaid}
  flowchart LR;

    A("A (treatment/exposure)"):::green;
    Y("Y (outcome)"):::green;
    Empty[ ]:::empty;
    Mod("Moderator"):::white;

    Mod --> Empty;
    A --- Empty;
    Empty -->|?| Y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Mediators

**Mediators** are variables that lie in the causal path between the two other variables (e.g. between exposure and outcome), and they tell you how or why an effect takes place.[[source]](https://www.scribbr.co.uk/faqs/why-should-you-include-mediators-and-moderators-in-your-study/)
* A path that includes a mediator is often called an **indirect effect** or indirect causal path
* In contrast, the arrow directly connecting the treatment and outcome represents the **direct causal effect** of the treatment on the outcome that is not due to changes in the mediator.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS) 
* If you do not have a direct arrow between the treatment and outcome, and only via the mediator, this implies that this is the only way in which the treatment can cause the outcome, and that if you know the mediator is present, knowing whether or not the treatment was present should have no impact on the outcome.

````{mermaid}
  flowchart LR;

    treat("Treatment"):::white;
    med("Mediator"):::white;
    out("Outcome"):::white;

    treat --> med;
    med --> out;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

You might condition on a mediator if you are interested in the **direct effect of treatment on outcome that doesn't pass through mediator**. Example: In racial disparity studies, will condition on mediators like socioeconomic, education, location (often though **matching** on these characteristics),  to allow you to isolate the unique effect of race that is not explainable by those pathways. [[source]](https://stats.stackexchange.com/questions/488048/dag-are-there-situations-where-adjusting-for-mediators-is-reasonable)

````{mermaid}
  flowchart LR;

    race("Race"):::white;
    outcome("Outcome"):::white;
    ses("Socioeconomic status"):::black;
    ed("Education"):::black;
    loc("Location"):::black;

    race -->|?| outcome;
    race --> ses; ses --> outcome;
    race --> ed; ed --> outcome;
    race --> loc; loc --> outcome;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

### Colliders

**Colliders** are descendents of two other variables - i.e. common effect - with two arrows from the parents pointing to ("colliding with") the descendent node. Colliders naturally block back-door paths. **Controlling for a collider will open the back-door path, thereby introducing confounding**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

Example: A genetic factor and an environmental factor causing cancer.
* Scenario #1: No conditioning - These are **independent** - i.e. genetic factor doesn't have causal effect on environmental factor - and so we don't expect to see an association between genetic and environment (unconditional/marginal association).
* Scenario #2: Condition on cancer - If we condition on cancer - such as by just selecting people who have cancer - we will find an **inverse association** between genetics and environment (as if cancer wasn't caused by one, it was by the other). This biased effect estimate is referred to as **selection bias**.
* Scenario #3: Condition on surgery - We can **induce** selection bias by conditioning on the downstream consequence of a collider - e.g. if cancer is collider, and surgery is consequence of cancer, if we condition on surgery, we expect to see inverse association between genetic and environment conditional on surgery (just as we did for the collider cancer).[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart TD;

    con_sur:::outline;
    subgraph con_sur["`**Condition on surgery**`"]
      gene3("Genetic<br>factor"):::white;
      env3("Environmental<br>factor"):::white;
      cancer3("Cancer"):::white;
      surgery3("Surgery"):::black;
    end

    gene3 --> cancer3;
    env3 --> cancer3;
    cancer3 --> surgery3;

    con_cancer:::outline;
    subgraph con_cancer["`**Condition on cancer**`"]
      gene2("Genetic<br>factor"):::white;
      env2("Environmental<br>factor"):::white;
      cancer2("Cancer"):::black;
      surgery2("Surgery"):::white;
    end

    gene2 --> cancer2;
    env2 --> cancer2;
    cancer2 --> surgery2;

    none:::outline;
    subgraph none["`**No conditioning**`"]
      gene("Genetic<br>factor"):::white;
      env("Environmental<br>factor"):::white;
      cancer("Cancer"):::white;
      surgery("Surgery"):::white;
    end

    gene --> cancer;
    env --> cancer;
    cancer --> surgery;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF;
````

Collider bias may also be present when neither the exposure nor the outcome is a direct cause of the collider variable. An example is **M-bias**. In this example...
* Focus: beta-blocker use and risk of ARDS
* Might be tempted to adjust for crackles as you might think its a confounder... 1) heart failure leads to both chronic β-blocker therapy and crackles, and 2) pneumonia causes both ARDS and crackles
* However, crackles is actually a collider on the **back-door path** of **chronic β-blocker therapy** ← heart failure → crackles ← pneumonia → **ARDS**. Adjusting for the presence of crackles opens this back-door path, introducing confounding. Ignoring the presence of crackles would be the right thing to do.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

````{mermaid}
  flowchart TD;

    beta("Beta blocker use"):::white;
    ards("Acute respiratory distress syndrome (ARDS)"):::white;
    hf("Heart failure"):::white;
    pneu("Pneumonia"):::white;
    crackles("Crackles"):::black;

    hf --> beta;
    hf --> crackles;
    pneu --> crackles;
    pneu --> ards;
    beta -->|?| ards;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

### Selection nodes

**Selection nodes** - by definition - are **always conditioned on**. This is because they reflect a restriction for inclusion such as:
* **Loss to follow-up** - e.g. if some people lost to follow-up (C1) and some remain to end (C0), our analysis is restricted to C0. This means that only individuals with certain values of C are included in the analysis, as we're essentially conditioning on it.
* **Inclusion/exclusion criteria for the study** - e.g. if only include men, then gender --> study enrollment

### Measurement error (mis-measured variables)

**Measurement error** is the degree to which we mismeasure a variable. If believe a variable is mismeasured, we have a node with a "*" that points from variable, with another representing measurement error.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) There are two types:
* **Non-differential error** - if error is not in exposure or outcome - this will bias the estimate of effect towards the null (so for small effects or studies with little power, it can make a true effect disappear)
* **Differential error** - if there is error in exposure and outcome - then, errors themselvse can be associated, opening a back-door path between exposure and outcome.[[source]](https://cran.r-project.org/web/packages/ggdag/vignettes/bias-structures.html)

Example: **Recall bias**. Does taking multivitamins in childhood help protect against bladder cancer later in life?
* Bias in outcome depends only on how well diagnosis of bladder cancer represents actually having it
* Bias in exposure depends on both (a) memory of vitamin uptake, and (b) bladder cancer, since they might have spent more time reflecting on what could have caused the illness
* If there is no effect of vitamins on bladder cancer, this dependency will make it seem as if vitamins are a **risk** for bladder cancer. If it is, in fact, **protective**, recall bias can reduce or even reverse the association.

````{mermaid}
  flowchart TD;

    me_diag("<b>Measurement error</b><br>in diagnosis"):::white;
    diag("Diagnosis of bladder cancer *"):::white;
    cancer("Bladder cancer"):::white;
    me_vit("<b>Measurement error</b><br>in vitamin uptake"):::white;
    mem_vit("Memory of<br>vitamin uptake *"):::white;
    vit("Childhood vitamin intake"):::white;

    me_diag --> diag;
    cancer --> diag;
    cancer --> me_vit;
    me_vit --> mem_vit;
    vit --> mem_vit;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

## How do you know what to include in your DAG?

### DAG completeness

A DAG is said to represent a complete causal structure between a treatment and outcome if:
* **Treatment and outcome** are presented
* **For any two nodes on the graph, all common causes** of those two nodes are represented
* All **selection variables** are represented (i.e. selection node) [[Rogers et al. 2022]](https://doi.org/10.1002/psp4.12894)

What do we mean by including common causes? Illustrating with an example...
* In **RCT** where people were randomised to receive Aspirin, we **don't need to include other variables** that can cause stroke (e.g. coronary heart disease (CHD)), as they didn't cause why people got aspirin.
* In an **observational study**, there will be other variables that would explain why people received aspirin (e.g. CHD), which we would need to include for it to be a causal DAG (i.e. **aspirin AND stroke BOTH caused by CHD**). [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

You don't need variables that **cause Y but not A** (although might include if for example you want to compare to other studies that did adjust for that variable).

````{mermaid}
  flowchart TD;

    ob:::outline;
    subgraph ob["`**Observational**`"]
      asp2("Aspirin"):::green;
      str2("Stroke"):::green;
      chd2("Coronary heart disease (CHD)"):::white;
    end

    asp2 --> str2;
    chd2 --> asp2;
    chd2 --> str2;

    rct:::outline;
    subgraph rct["`**RCT**`"]
      asp("Aspirin"):::green;
      str("Stroke"):::green;
    end

    asp --> str;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### How do you know when to include mediators?

* If we are interested in the **total effect of A on Y**, we don't need to specify the mechanisms through which A may affect Y (i.e. don't need any m ediators between A and Y)
* However, if we are interested in the **direct effect of A on Y** that doesn't pass through the mediator, then we should include it. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### When should you draw arrows?

The DAG is drawn based on **expert knowledge**, including arrows when you believe that something causes something else. If expert knowledge is **insufficient** for us to rule out a direct effect of E on D, then we should draw an arrow.

Arrows on causal graphs are **not deterministic** - i.e. doesn't mean every person with exposure will see outcome - as some will never, and some without outcome will develop it. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### Can you use variable selection methods?

No - it is important that these are based on expert knowledge. For causal inference, it is **NOT** recommended to choose included variables/relationships based on:
* P value-based and model-based **variable selection methods** (including forward, backward, and stepwise selection) - since they ignore the causal structure underlying the hypothesis and treat confounders and colliders similarly
* Use methods that **rely on model** fit or related constructs (e.g. R<sup>2</sup>, Akaike information criterion, and Bayesian information criterion) - since these rely heavily on the available data, in which causal relationships may or may not have been captured and may or may not be evident, and specification of model and arbitrary variables included will drive observed associations with outcome
* Use selection of variables that, when included in a model, change the magnitude of the effect estimate of the exposure of interest, to identify confounders
* Identify multiple 'independent predictors' through purposeful or automated variable selection

**If the authors have hypotheses about each variable, then a separate model for each variable should be generated** - or a prediction model could be developed, if prediction, rather than causal inference, is the goal of the analysis[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

## How do you create a DAG?

First, start with your **research question**. This should be A (treatment/exposure) and Y (outcome), identificated by letters, "?" or colours.

Then add the key components as detailed above...
* Measured confounders (L)
* Unmeasured confounders (U)
* Selection nodes
* Moderators
* Mediators
* Mismeasured variables

**Everytime you add a new node** to the DAG, you need to conside whether it has common causes with any other variables (its not just about common causes of A and Y). For example, if you believe measurement of Y is affected by whether person is on treatment, draw arrow from A to measurement error for Y.

There can often be **more than one appropriate DAG**, and alternate DAGs can make excellent sensitivity analyses.[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf) [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart LR;

    A("A (treatment/exposure)"):::green;
    Y("Y (outcome)"):::green;
    Empty[ ]:::empty;
    Mod("Moderator"):::white;
    M("Mediator"):::white;
    L("L (confounder)"):::white;
    U("U (unmeasured confounder)"):::white;
    C("C (selection node)"):::black;
    Y*("Y* (mismeasured outcome)"):::white;
    UY("U<sub>Y</sub> (measurement error for Y)"):::white;

    Mod --> Empty;
    A --- Empty; Empty -->|?| Y;
    A --> M; M --> Y;
    L --> A; L --> Y;
    U --> L; U --> Y;
    A --> C;
    L --> C;
    Y --> Y*;
    UY --> Y*;
    A --> UY;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````
