# Additional DAG concepts

`````{admonition} Executive summary
:class: info

**D-seperation rules** determine whether paths will be open (expect associations) or blocked (independent), which are based on whether condition or not on confounders and colliders.

If you have **time-varying treatment** (takes different values over time), then you will have other time-varying components (e.g. time-varying confounding). If there is **treatment-confounder feedback** (i.e. earlier treatment impacts value of later confounder), then you will need to use a special type of method to adjust for confounders, referred to as **G-methods**.

Since you have designed the study to appropriate control for confounding for your relationship of interest - between a given treatment/exposure and outcome - the other variables included may have residual confounding or other biases that affect their associations, and it is important that these effect estimates are not presented (or are explained) - otherwise this is called '**Table 2 fallacy**'.
`````

## Paths

A **path** is any route through graph - it **doesn't have to follow** the direction of the arrows. Paths can be either be:
* **Open** paths - represent statistical associations between two variables
  * E.g. If don't condition on confounder, will be an open path, and see association with confounder
* **Blocked** (or "closed" paths) - represent the absence of associations 
  * E.g. An unconditioned collider should have no association [[Williams et al. 2018]](https://doi.org/10.1038/s41390-018-0071-3)

````{mermaid}
  flowchart TD;

    block:::outline;
    subgraph block["`**Path blocked at collider**`"]
      a("Treatment"):::green;
      y("Outcome"):::green;
      x("Collider"):::white;
    end

    a --> y;
    a --> x;
    y --> x;

    open:::outline;
    subgraph open["`**Path open at confounder**`"]
      a2("Treatment"):::green;
      y2("Outcome"):::green;
      x2("Confounder"):::white;
    end

    a2 --> y2;
    x2 --> a2;
    x2 --> y2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

The **target (causal) paths** are the directed paths from the exposure to the outcome which transmit the target effect. **Biasing paths** are non-directed open paths between the exposure and the outcome, which transmit bias for estimating the effect of the exposure on the outcome.[[source]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3733703/)

## D-seperation rules

### Rules

**D-seperation** rules are used to determine whether paths are **open or blocked** - i.e. whether variables will be **associated or independent**.

If **all paths are blocked** between two variables on the DAG, then they are **d-seperated** (i.e. not associated / statistical independence).[[source]](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-All-DAGs/) Otherwise, they are **d-connected**.[[source]](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3733703/)

When identified here, these are structural sources of association. Another cause of association - beyond it being a causal relationship - is by chance. However, increasing our sample size, chance associations should disappear (whilst structural remain and become sharper). [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

Rules:
1. If there are **no** variables being conditioned on
    * A path is only **blocked** if it contains a **collider**
    * A path is **open** if it does not contain a collider

2. Path is **blocked** if it contains a **non-collider** that **is** conditioned on

3. Path is **open** if **collider is** conditioned on

4. Path is **open** if **descendent** of collider **is** conditioned on.[[source]](https://sgfin.github.io/2019/06/19/Causal-Inference-Book-All-DAGs/)

### Examples of each rule

Rule 1: L to Y open
````{mermaid}
  flowchart LR;

    l("L"):::white;
    a("A"):::white;
    y("Y"):::white;

    l --> a;
    a --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Rule 1: L to A blocked
````{mermaid}
  flowchart LR;

    l("L"):::white;
    a("A"):::white;
    y("Y"):::white;

    l --> y;
    a --> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
    classDef outline fill:#FFFFFF
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Rule 2: A to Y blocked.
````{mermaid}
  flowchart LR;

    a("A"):::white;
    b("B"):::black;
    y("Y"):::white;
    
    a --> b; b--> y;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Rule 3: A to Y open.
````{mermaid}
  flowchart LR;

    a("A"):::white;
    y("Y"):::white;
    l("L"):::black;
    
    a --> l; y--> l;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

Rule 4: A to Y open.
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

## Faithfulness

Faithfulness is the result of **opposite effects of exactly equal magnitude** - e.g. if aspirin caused stroke for half of poppulation and prevented it in the other half, then causal dag is correct (as aspirin affects stroke) but **no association is observed (as they cancel each other out**). In that case, we say the joint distribution of the data is not faithful to the causal DAG. These perfect cancellations are **rare** and we don't expect them to happen in practice. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Time-varying treatments and confounders

### What is a time-varying treatment?

A **time-varying treatment** is treatment that can take different values over time - such as:
* Whether or not receive medicine at each timepoint
* Dose of medicine at each time point

This is as opposed to **fixed treatments** that do not vary over time (e.g. whether took vitamin D at time of conception).

We can represent this using two arbritary time points, K and K+1. Actual study includes many more weeks but for most purposes, two time points are enough to represent the main features of the causal structure when there is time varying treatment.

You'll notice that a consequence of the time-varying treatment is **time-varying confounder and outcome**. A confounder is time-varying when it can take different values at different timepoint, and confound at different timepoints.

Example: EPO used to treat anemia, dose is based on haemoglobin level at time of appointment (which itself depends on disease severity, but we've just represented that as a single timepoint). To show that we have **time-varying** components, we refer to:
* L and A at timepoint K (e.g. week 0)
* Y, L and A at timepoint K+1 (e.g. week 1)
* Y at timepoint K+2 (e.g. week 2)

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::white;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::white;
    u("U: Disease severity"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

### Treatment-confounder feedback

Our DAG above was incomplete - in this scenario, treatment at timepoint K will impact the confounder (levels of haemoglobin) at timepoint K+1. This is referred to as **treatment-confounder feedback** - when the later confounder is impacted by prior treatment.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home) This is also referred to as **intermediate confounding** - when a confoudner is affected by prior exposure/treatment status.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

When there is **treatment-confounder feedback**, then conventional adjustment methods, since:
In other words:
1. Confounding on an intermediate confounder blocks part of the effect of prior exposure/treatment.
2. Conditioning on an intermediate confounder can introduce collider bias, opening additional back-door paths between exposure/treatment and outcome.[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)
  * e.g. We'll get a biased estimate if we condition on the Ls, as conditioning on L<sub>K+1</sub> will open a path that was previously blocked: A<sub>K</sub> to L<sub>K+1</sub> to U to Y<sub>K</sub>. Hence, we have introduced selection bias.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

This means we will be unable to yield an unbiased estimate and, if the time-varying confounder also affects the outcome (e.g. L<sub>K+1</sub> --> Y<sub>K+2</sub>), it will be impossible to estimate the total effect of the treatment.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

We need other methods to handle these settings: **G-methods**. [[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)


````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::black;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::black;
    u("U: Disease severity"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    ak --> lk1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

## Presenting results from causal inference studies

'Causal models are typically designed to test an association between a **single exposure and an outcome**. The additional independent variables in a model (often called “covariates”) **serve to control for confounding**. The observed associations between these covariates and the outcome have not been subject to the same approach to control of confounding as the exposure' (i.e. they themselves have not been corrected for confounding - *and they shouldn't and didn't have to be*). 'Therefore, **residual confounding and other biases often heavily influence these associations**.'

'This situation is known as “**Table 2 fallacy**,” a term arising from the practice of presenting effect estimates for all independent variables in “Table 2”.' It is strongly recommended that these effect estimates are **not presented**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

Hartig 2019 discusses how this may not be practical in some fields (they give example of ecology) where you rarely have a clear target variable/hypothesis, but suggest instead that's important to explicitly state/seperate reasonablly controlled varaibles from possibly confounded variables.[[source]](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/)

## Minimal set of covariates

We want to identify a **minimal set of covariates** that:
1. Blocks all backdoor paths.
2. Doesn't inadvertenly open closed pathways by conditioning on colliders or descendents. [[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)

With the example below, the minimal set of variables you'd need to condition for would be **L0 and L1 - wouldn't need to for U** as doing for L0 and L1 blocks the backdoor paths.[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

````{mermaid}
  flowchart LR;

    ak("A<sub>K</sub>: EPO dose"):::white;
    ak1("A<sub>K+1</sub>: EPO dose"):::white;
    yk1("Y<sub>K+1</sub>: Death"):::white;
    yk2("Y<sub>K+2</sub>: Death"):::white;
    lk("L<sub>K</sub>: Haemoglobin"):::white;
    lk1("L<sub>K+1</sub>: Haemoglobin"):::white;
    u("U: Disease severity"):::white;

    ak --> yk1;
    u --> yk1;
    u --> lk;
    lk --> ak;
    lk --> ak1;
    ak --> ak1;
    u --> lk1;
    lk1 --> ak1;
    ak1 --> yk2;
    u --> yk2;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

## Example cases

These examples help demonstrate the utility of causal diagrams.

### Example: Oestrogen and endometrial cancer

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)