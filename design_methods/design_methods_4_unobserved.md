# Methods #4: Methods for unobserved confounding

`````{admonition} Executive summary
:class: info

Addressing unobserved confounding:
* Instrumental variables
* Regression discontinuity (RD)
* Interrupted time series (ITS)
* Difference in differences (DiD)
`````

## Addressing unobserved confounding

'The above methods rely on an assumption of no unmeasured confounding (ie, conditional exchangeability), which is often not plausible in observational study designs. The following methods attempt to address unmeasured confounding, subject to certain unprovable assumptions, by exploiting some assignment mechanism (akin to randomisation in an RCT) that determines exposure status but is thought to be unrelated to any unobserved confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Instrumental variables

### What is an instrumental variable?

An **instrumental variable (IV)** is a variable that satisfies the following assumptions:
1. It **causes variation in the exposure/treatment** (i.e. relevance assumption - it is correlated with X, an endogenous explanatory variable)
2. It is **unrelated to the outcome**
3. As it is unrelated to the outcome, is is therefore **unrelated to unmeasured confounders** (unmeasured differences in characteristics that affect outcomes) (i.e. **exogeneity** assumption - it is an exogneous variable) [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026)[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) [[source]](https://towardsdatascience.com/instrumental-variables-a-practical-explanation-1a583408a5b9)

This is illustrated below:
````{mermaid}
  flowchart LR;

    iv("Instrumental variable"):::white;
    e("Exposure/treatment"):::white;
    o("Outcome"):::white;
    u("Unmeasured confounders"):::white;

    iv --> e;
    e --> o;
    u --> o;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Due to these characteristics, instrumental variables enable us to mimic randomisation to treatment. [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026) In fact, **randomisation to treatment** in an RCT is an example instrumental variable (it meets the above assumptions).

````{mermaid}
  flowchart LR;

    iv("RCT randomisation to treatment"):::white;
    e("Exposure/treatment"):::white;
    o("Outcome"):::white;
    u("Unmeasured confounders"):::white;

    iv --> e;
    e --> o;
    u --> o;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Two-stage least squares (2SLS)

You can use the two-stage least squares (2SLS) method to estimate the causal effect, using instrumental variables for individual-level data.

1. **Regress exposure (${x}$) on instrumental variable (G) to produce $\hat{x}$ (estimate of exposure independent of confounders)**
2. **Regress outcome (Y) on $\hat{x}$**. Here, $\hat{x}$ is replacing the actual value of the problematic predictor, ${x}$. [BSc Medical Sciences]

The 'groups being compared differ only in likelihoods of treatment, as opposed to a division into pure treatment and control groups'. Hence, this 'method estimates an incremental or "marginal" effect of treatment only over the range of variation in treatment across the IV groups'. [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026)

'IV analysis estimates a local average treatment effect (LATE) among 'compliers' - individudals whose exposure status is affected by the instrument. This group cannot be precisely identified, and the LATE may therefore sometimes be of limited practical or policy relevance'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

### Assumptions of instrumental variable analysis

(1) **Instrumental variable assumptions**(as above)

(2) **Homogeneity assumption** - the association between the instrumental variable and the exposure is homogenous (same for everyone in the population), or the effect of the exposure on the outcome is homogenous [BSc Medical Sciences]

### Example: Mendelian randomisation

Disease association with non-genetic risk factors are often confounded - for example:
````{mermaid}
  flowchart LR;

    e("Drinking alcohol"):::green;
    o("Lung cancer"):::green;
    c("Smoking"):::white;

    e --> o;
    c --> e; c --> o;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Genotype-phenotype associations are much less likely to be confounded. They are aetiological associations (causing or contributing to disease/condition development). 

If we know of a gene closely linked to the phenotype without direct effect on the disease, it can often be reasonably assumed that the gene is not itself associated with any confounding factors - a phenomenon called **Mendelian randomization**. Genetic variants (G) should influence the exposure (X) but should not be directly associated with confounders (U) or the outcome (Y).

We can then identify the causal relationship between X and Y - if it doesn't cause Y, then G should be independent of Y. This is the same logic as we use for an RCT (where G would be randomisation to treatment).
 
````{mermaid}
  flowchart TD;

    con:::outline;
    subgraph con["If X doesn't cause Y..."]
      G:::white;
      X:::white;
      Y:::white;
      U:::white;
    end

    G --> X;
    U --> X;
    U --> Y;

    uncon:::outline;
    subgraph uncon["If X causes Y..."]
      G2("G"):::white;
      X2("X"):::white;
      Y2("Y"):::white;
      U2("U"):::white;
    end

    G2 --> X2;
    U2 --> X2;
    U2 --> Y2;
    X2 --> Y2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef outline fill:#FFFFFF;
````

[BSc Medical Sciences]

### Example: Effect of intensive treatment on mortality in patients with acute myocardial infarction

Example from [McClellan et al. 1994](https://doi.org/10.1001/jama.1994.03520110039026): Want to determine the effect of more intensive treatments (e.g. catheterisation and revascualisation) on mortality in elderly patients with acute myocardial infarction. They use distance from hospital as an 'instrumental variable to account for unobserved case-mix variation (selection bias) in observational Medicare claims data' [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026)

Why is distance an instrumental variable?
* Intensive treatment only performed at certain hospitals
* Comparing treatments and outcomes between patients treated at different hospitals risks selection bias, 'because physician and patient decisions that influence treatment choice may ALSO influence choice of hospital to go to - e.g. AMI patients who appear to be better candidates for catheterisation may be disproportionately admitted to catheterisation hospitals' [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026)
* Distance from hospital (specifically, differential distance to hospital providing intensive treatment):
   * **Affects** probability of receiving intensive treatment
   * **Does not affect** patient characteristics
* Hence, distance from hospital can be used as an instrumental variable [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) - it meets the IV assumptions:
    1. Causes variation in whether receive intensive treatment
    2. Unrelated to mortality
    3. Unrelated to unmeasured confounders (like the physician and patient decisions)

````{mermaid}
  flowchart LR;

    treat("<b>Intensive treatment</b><br>(e.g. catheterisation)"):::green;
    mortality("<b>Mortality</b>"):::green;
    hosp("<b>Hospital</b> attended<br>(i.e. whether it<br>offers the treatment)"):::white;
    dist("<b>Differential distance</b> to<br> hospital providing<br>intenstive treatment"):::white;
    decisions("Physician and patient<br><b>decisions</b>"):::white;

    dist --> hosp;
    decisions --> hosp;
    hosp --> treat;
    treat --> mortality;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

First, checked for presence of selection bias (i.e. whether hospital type affects treatment intensity - and therefore whether simple comparisons of treatments and outcomes across hospital types are valid). Then, as was present, used IV methods to estimate effect of intensive treatment on mortality. **Differential distance approximately randomises patients to different likelihoods of receiving intensive treatments**, uncorrelated with health status.
* First, compared two groups of apx. equal size - patients near to catheterisation hospital (differential distance <= 2.5 miles) and patients far from them (> 2.5 miles). This evidenced assumption that distribution of health status in AMI patients is independent of differential distance, and illustrates IV method, estimating the 'average effect of invasive treatment for all patients who are marginal from the standpoint of the near-far IVs - those who undergo catheterisation in the relatively near group and not in the relatively far group - if the two groups are balanced and if catheterisation is the only treatment that differs between the groups'
* Then used more general IV estimation netchniques with wide range of differential distance groups, and account for small remaining observable differences between differential-distance groups [[McClellan et al. 1994]](https://doi.org/10.1001/jama.1994.03520110039026)

### Example: SAMueL

This doesn't suffer with problem as above, as here, we're assuming that all patients would simply go to their closest unit.

You could test that assumption, although we don't have the data.

````{mermaid}
  flowchart LR;

    treat("<b>Thrombolysis</b><br>(e.g. catheterisation)"):::green;
    out("<b>Stroke outcome</b>"):::green;
    con("NIHSS<br>Pre-stroke disability<br>Atrial fibrillation"):::white;
    hosp("Hospital propensity<br>to thrombolyse"):::white;

    hosp --> treat;
    treat --> out;
    con --> treat;
    con --> out;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Example: Neonatal

We could apply the same logic as in SAMueL - although we anticipate this might be more influenced by patient choice on where they want to give birth - in which case, would you use some kind of distance measure as above?

````{mermaid}
  flowchart LR;

    treat("<b>Caesarean</b>"):::green;
    out("<b>HIE</b>"):::green;
    con("Confounders"):::white;
    hosp("Hospital propensity<br>to do caesarean"):::white;
    choice("Physician and patient choice of hospital<br>(e.g. better candidates for caesarean<br>may be sent to hospitals with more propensity?)"):::white;
    dist("Hospital distance measure"):::white;

    choice --> hosp;
    dist --> hosp;
    hosp --> treat;
    treat --> out;
    con --> treat;
    con --> out;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

### Variants

'**Three-Stage Least Squares (3SLS)** - this method is an extension of the 2SLS method and is used when there are more than two endogenous variables in the model. The 3SLS method is based on the idea that the endogenous variables are correlated with each other, and therefore, the coefficients of these variables need to be estimated simultaneously.' [[source]](https://fastercapital.com/content/Econometric-Techniques--Understanding-Tinbergen-s-Statistical-Innovations.html)

## Regression discontinuity (RD)

<mark>read this</mark> https://dimewiki.worldbank.org/Regression_Discontinuity

'RD methods can be used when the **exposure status** (wholly or partly) is determined by some **continuous variable exceeding some arbitrary threshold** (called the forcing variable).'

'If the relationship between the forcing variable and the outcome is otherwise continuous, any discontinuity or jump in the relationship can be attributed to the exposure.'

'RD estimates a LATE among the individuals who fall just above or just below the threshold. As with
IV analysis, bias can occur if the forcing variable is connected
to the outcome through a back-door path or any other pathway
besides the exposure.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Interrupted time series (ITS)

'ITS studies compare the **trend over time in a population-level outcome before and after an exposure** is introduced. Assuming that the trend would have been unchanged if the intervention was not introduced, a change in trend at the point of introduction (in terms of level and/or slope) can be attributed to the exposure.'

'ITS can be regarded as a special case of IV or RD, with time being the instrument or forcing variable. ITS addresses time-invariant confounding but can be biased if other events that influence the outcome happen at the same time as the exposure'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

## Difference in differences (DiD)

'DiD studies measure the **change in a population-level outcome before and after an intervention** is introduced, compared with a **comparison group where the intervention is never introduced**. This is similar to RD and ITS, but attempts to control for changing time trends, by using a comparison group to represent the counterfactual outcome trend in the exposed.'

'DiD also addresses time-invariant confounding but requires assuming that there would have been no difference in trend between the groups in the absence of the intervention (the ‘parallel trends’ assumption).' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)