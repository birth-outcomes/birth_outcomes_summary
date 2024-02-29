# Causal diagrams: Conditioning, D-seperation rules, time-varying treatments and table 2 fallacy

`````{admonition} Executive summary
:class: info

### Paths

A **backdoor path** is a non-causal path between the treatment and outcome that will exist if:
* If you haven't conditioned for confounders
* If you condition on a collider (which opens a backdoor path)

Whether or not a path will be open or blocked is described using D-seperation rules, which essentially just explain that associations will be present if either of the above are true, or if one node causes the other.

Conditioning on a variable means you are examining the relationship between the treatment and outcome within levels of the conditioning variable, using either: sample restriction, stratification, adjustment, matching. 

Ideally, you want to identify a minimal set of covariates to condition on that (a) block all back-door paths, and (b) don't open closed paths.

### Time-varying treatment

If you have time-varying treatment (takes different values over time), then you will have other time-varying components (e.g. time-varying confounding). If there is treatment-confounder feedback (i.e. earlier treatment impacts value of later confounder), then you will need to use a special type of method to adjust for confounders, referred to as G-methods.

### Table 2 fallacy

Since you have designed the study to appropriate control for confounding for your relationship of interest - between a given treatment/exposure and outcome - the other variables included may have residual confounding or other biases that affect their associations, and it is important that these effect estimates are not presented (or are explained) - otherwise this is called 'Table 2 fallacy'.
`````

## Conditioning

**Conditioning** on a variable means examining the relationship between A and Y within levels of the conditioning variable, using either:
* Sample restriction
* Stratification
* Adjustment
* Matching

Other terms like "adjusting" or "controlling" suggest a misleading interpretation of the model.

When you condition on something, you draw a box around it on the DAG.

Scenarios where we may want to condition...

**(1) To control for confounding**. A back door path is a connection between A and Y that doesn't follow the path of the arrows - for example, along the path of a confounder. If we condition on the variable in that path (i.e. control for confounding), then we close that back door path and remove the non-causal association.
* If we don't do this, we will get **confounding bias** (where a common cause of A and Y is not blocked).

**(2) To open a path blocked by a collider**.
* **Collider bias** = conditioning on common effects
* **Selection bias** = type of collider bias where the common effect is selection into the study - occurs when a common effect is conditioned on such that there is now a conditional association between A and Y
* **Berkson's bias** = type of selection bias in which selection of cases into the study depends on hospitalisation, and the treatment is another diase, or a cause of another disease, which also results in hospitalisation

**(3) To remove part of the causal effect** by conditioning on a mediator.

[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)

### Minimal set of covariates

We want to identify a minimal set of covariates that:
1. Blocks all backdoor paths.
2. Doesn't inadvertenly open closed pathways by conditioning on colliders or descendents.

[[source]](https://med.stanford.edu/content/dam/sm/s-spire/documents/WIP-DAGs_ATrickey_Final-2019-01-28.pdf)

## Causal structures where we expect to see associations

### Structural sources of seperation

The **structural sources** of association are:
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

There is another source of association: **chance**. May be association even if none of above are true. Chance is not a structural source of association. **Increasing our sample size, chance associations should disappear (whilst structural remain and become sharper)**.

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## D-seperation rules

**Path** is any route through graph (can follow arrow direction or not). Paths can be **blocked or open**, which is according to the **D-seperation rules**. We use D-seperation to decide whether two variables are D-seperated, where D stands for directional.

You will be able to see that all D-separation says is that - as above - two variables **would be associated** if:
* One causes the other,
* They share common causes
* They have a common effect and we condition on the common effect...

Another summary:
* Path is blocked only if (a) containins non-collider that been conditioned on, or (b) collider that not been conditioned on.
* Two variables are D-seperated if all paths between them are blocked.
* Two variables are marginally or unconditionally independent if they are D-seperated without conditioning on all the variables
* Two variables are conditionally independent if they are D-seperated after conditioning

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### D-seperation rule 1: If there are no variables being conditioned on, a path is blocked if and only if two arrowheads on the path collide at some variable on the path

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### D-seperation rule 2: Any path containing non-collider that has been conditioned on is blocked.

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### D-seperation rule 3: A collider that has been conditioned on does not block a path.

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

### D-seperation rule 4: Collider with descendent that has been conditioned on does not block a path.

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Faithfulness

Faithfulness is the result of opposite effects of exactly equal magnitude - e.g. if aspirin caused stroke for half of poppulation and prevented it in the other half, then causal dag is correct (as aspirin affects stroke) but no association is observed (as they cancel each other out). In that case, we say the joint distribution of the data is not faithful to the causal DAG.

These perfect cancellations are rare and we don't expect them to happen in practice, so we can safetly say lack of D-seperation means non-zero association. So - 
* **D-seperation = statistical independence**
* **All paths blocked = no association**

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Time-varying treatments and confounders

A time-varying treatment one that can take different values over time - (e.g. whether or not receive medicine, or dose of medicine, at multiple different timepoints) - as opposed to fixed treatments that do not vary over time (e.g. whether took vitamin D at time of conception).

Example: EPO used to treat anemia, dose is based on haemoglobin level, which itself depends on disease severity.

````{mermaid}
  flowchart LR;

    l("L: Haemoglobin"):::white;
    a("A: EPO"):::white;
    y("Y: Death"):::white;
    u("U: Disease severity"):::white;

    l --> a;
    a --> y;
    u --> y;
    u --> l;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

To show that we have **time-varying** components, we refer to:
* L and A at timepoint K (e.g. week 0)
* Y, L and A at timepoint K+1 (e.g. week 1)
* Y at timepoint K+2 (e.g. week 2)

Actual study includes many more weeks but for most purposes, two time points are enough to represent the main features of the causal structure when there is time varying treatment. These will often be two arbritary time points (K and K+1) (rather than 0 and 1).

You'll notice that a consequence of the time-varying treatment is time-varying confounder and outcome. A confounder is time-varying when it can take different values at different timepoint, and confound at different timepoints.

With the example below, the minimal set of variables you'd need to condition for would be L0 and L1 (wouldn't need to for U as doing for L0 and L1 blocks the backdoor paths)

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

However, if there is **treatment-confounder feedback**, then conventional adjustment methods - even if closing all back door paths - will still not be able to yield an unbiased estimate.

Our DAG above was incomplete - in this scenario, treatment at timepoint K will impact the confounder (levels of haemoglobin) at timepoint K+1. This is referred to as **treatment-confounder feedback** - when the later confounder is impacted by prior treatment.

We'll get a biased estimate if we condition on the Ls, as conditioning on L<sub>K+1</sub> will open a path that was previously blocked: A<sub>K</sub> to L<sub>K+1</sub> to U to Y<sub>K</sub>. Hence, we have introduced selection bias.

If the time-varying confounder also affects the outcome (e.g. L<sub>K+1</sub> --> Y<sub>K+2</sub>), it will be impossible to estimate the total effect of the treatment.

We need other methods to handle these settings: **G-methods**.

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

[[HarvardX PH559x]](https://learning.edx.org/course/course-v1:HarvardX+PH559x+2T2020/home)

## Presenting results

'Causal models are typically designed to test an association between a **single exposure and an outcome**. The additional independent variables in a model (often called “covariates”) **serve to control for confounding**. The observed associations between these covariates and the outcome have not been subject to the same approach to control of confounding as the exposure' (i.e. they themselves have not been corrected for confounding - *and they shouldn't and didn't have to be*). 'Therefore, **residual confounding and other biases often heavily influence these associations**.'

'This situation is known as “**Table 2 fallacy**,” a term arising from the practice of presenting effect estimates for all independent variables in “Table 2”.' It is strongly recommended that these effect estimates are **not presented**.[[Lederer et al. 2018]](https://doi.org/10.1513/AnnalsATS.201808-564PS)

Hartig 2019 discusses how this may not be practical in some fields (they give example of ecology) where you rarely have a clear target variable/hypothesis, but suggest instead that's important to explicitly state/seperate reasonablly controlled varaibles from possibly confounded variables.[[source]](https://theoreticalecology.wordpress.com/2019/04/14/mediators-confounders-colliders-a-crash-course-in-causal-inference/)

## Example cases

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