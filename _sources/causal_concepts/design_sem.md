# Structural equation modelling

`````{admonition} Executive summary
:class: info

Structural Equation Modelling (SEM) is a statistical technique to model hypothesised relationships among variables, and these can be causal models if certain criteria are met.

SEM involves visualising the hypothesised model, translating the DAG to a path statement, assessing fit statistics, improving model fit using modification indices, and so on.

`````

## Introduction to structural equation modelling

'**Structural Equation Modelling (SEM)** is a statistical technique to model hypothesised relationships among variables.' We first specify these relationships, based on subject matter expertise, either:
* Graphically
* By listing a set of functions - *hence "structural"*

Variables can be:
* **Manifest** (observed) or **latent** (unobserved)
* **Exogenous** (have no cause themselves, but affect others) or **endogenous** (values are caused by other variables)

Relationships between variables can be one of:
* Correlational / bidrectional
* Isolated / conditionally independent
* Causal / unidirectional

In a graphical model, representations include:
* Ovals = latent variables
* Rectangles = manifest variables
* Single or double headed arrows indicate nature of relationship [[Madhanagopal and Amrhein 2019]](https://support.sas.com/resources/papers/proceedings19/3240-2019.pdf)

![Example of an SEM graphical model](../images/sem_madhanagopal_2019.png)

## Structural causal models 

**Structural Causal Models (SCM)** were proposed by Judea Pearl. They integrate SEM and graphical models to aid understanding of causal relationships. SEMs are mainly 'used to confirm a model rather than to explore a phenomenon'. SEMs can be interpreted as causal models if they meet the conditions:
1. Structure is **valid representation of reality**
2. Relationships are **directed and acyclic**
    * Directed acyclic gropus are a subset of graphical models, where relationships must be directional 
3. **Variables, conditioned on their parents, are independent of their ancestores**
    * See example below - soccer is ancestor of heatstroke - this conditoin is met if soccer only causes heatstroke via dehydration - and is not met if soccer effects heat stroke directly or through another mediating variable (I think, if not included)

````{mermaid}
  flowchart LR;

    soccer("Soccer"):::white;
    dehy("Dehydration"):::white;
    heat("Heatstroke"):::white;

    soccer --> dehy;
    dehy --> heat;

    classDef white fill:#FFFFFF, stroke:#FFFFFF
    classDef black fill:#FFFFFF, stroke:#000000
````

4. There are **no "back doors"** from cause to effect [[Madhanagopal and Amrhein 2019]](https://support.sas.com/resources/papers/proceedings19/3240-2019.pdf)

## Covariance matrix

'The fundamental unit of information in an SEM is the covariance matrix of the model variables.' 

'An ‘Under-Identified’ model is a model in which it is not possible to estimate all the model parameters because there are too few unique elements. A ‘Just-Identified’ model is a model in which the number of unique covariance elements equals the number of parameters being estimated. An ‘Over-Identified’ model is a model in which the number of unique covariance parameters is greater than the number of parameters being estimated. The difference is the degrees of freedom available for hypothesis tests. The total number of estimated parameters in the model should always be lower than fundamental unit of information in the data; i.e. the model should be over-identified.' [[Madhanagopal and Amrhein 2019]](https://support.sas.com/resources/papers/proceedings19/3240-2019.pdf)

## Path statement

Each of the single headed arrows in the diagram 'represents a hypothesised dependency. For each of these paths,' we 'estimate a path coefficient and test whether the coefficient statistically differs from zero'. [[Madhanagopal and Amrhein 2019]](https://support.sas.com/resources/papers/proceedings19/3240-2019.pdf)

## Fit statistics

We assess goodness of fit, and can explore model modifications to improve fit, by:
1. 'Increasing the number of paths (i.e. allowing the corresponding coefficients to be estimated)
2. Reducing the number of paths (i.e. constraining the corresponding coefficients to zero)' [[Madhanagopal and Amrhein 2019]](https://support.sas.com/resources/papers/proceedings19/3240-2019.pdf)
