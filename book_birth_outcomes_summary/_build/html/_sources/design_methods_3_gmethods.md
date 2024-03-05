# Methods #3: G-methods

`````{admonition} Executive summary
:class: info

G-methods address intermediate confounding, i.e. treatment-confounder feedback.

**G-computation**
* Also known as **parametric G-formula**, **G-standardisation**, **standardisation** or **outcome regression**
* Predict outcomes in counterfactual populations that assume all had treatment or not, and compare

Marginal structure models

G-estimation

`````

## G-methods

G-methods are a family of methods that **address intermediate confounding, i.e. treatment-confounder feedback**, which is when a confounder is affected by prior exposure status. They do so by taking the by 'taking the observed distribution of intermediate confounders (in the population as well as over time) into account, instead of holding them constant; in other words, they estimate **marginal effects rather than conditional effects**'. [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) They were developed by James Robins. [[source]](https://stats.stackexchange.com/questions/612029/what-is-the-difference-between-the-g-formula-g-estmation-g-computation-and-g-m)

## G-computation

### Terminology

Names for this method:
* **G-computation**
* **Parametric G-formula**
* **G-standardisation**
* **Standardisation** [[Vansteelandt and Keiding 2011]](https://doi.org/10.1093/aje/kwq474)
* **Outcome regression** [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)

There has been some debate around terminology. As quoted from [Vansteelandt and Keiding 2011](https://doi.org/10.1093/aje/kwq474):
> *'The term standardization is revealing and rather well-known to epidemiologists and therefore, in our opinion, is the terminology of choice. The term G-computation has so far been mostly reserved to refer to standardization of the effects of time-varying exposures; potentially the term “G-standardization” as nomenclature for “standardization with respect to generalized exposure regimens” would have been more enlightening. Despite the essential equivalence of G-computation for point exposures and standardization with the total population as the reference, we believe that the developments from the causal inference literature add to the literature on standardization. They give a precise meaning to standardized effect measures in terms of counterfactuals, provide insight into the delicate differences between conditional and marginal epidemiologic effect measures, and suggest novel standardization techniques that combine precision with robustness against model misspecification and extrapolation.'*

### About the method

G-computation involves using a statistical model (e.g. predict) to predict **potential** outcomes (counterfactuals - with and without exposure).[[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267) 

````{mermaid}
  flowchart LR;

    X("Binary treatment (X)"):::white;
    Y("Outcome (Y)"):::white;
    W("Confounder (W)"):::white;

    X --> Y;
    W --> X;
    W --> Y;
  
    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

Key steps:
1. **Fit model on observed data** - regression model with Y as outcome and X and W as predictors (perhaps also with polynomials and/or interactions if there are multiple control variables)
2. Make identical copy of observed data, but just **replace** outcome so all X=1.
3. Create another where all to X=0.
4. Use our fitted model to **predict outcomes** in the two counterfactual datasets [[source]](https://marginaleffects.com/vignettes/gcomputation.html) [[Batten 2023]](https://causallycurious.com/posts/standardization/standardization) [[source]](http://www.statslab.cam.ac.uk/~qz280/talk/ssrmp-2020/slides.pdf)
5. Estimate the **Average treatment effect (ATE)** - this is the mean difference (+ 95% CI) in the predicted outcomes between the two groups.[[Batten 2023]](https://causallycurious.com/posts/standardization/standardization)  It essentially describes the average effect, at a population level, of moving an entire population from untreated to treated.[[Chatton et al. 2020]](https://doi.org/10.1038/s41598-020-65917-x)

For **average treatment effect on the treated (ATT)**:
* This is the average effect of treatment on those subjects who ultimately received the treatement [[Chatton et al. 2020]](https://doi.org/10.1038/s41598-020-65917-x)
* To calculate ATT, use **only the treated units in steps 2 and 3**. 'The control units are still used to fit the model in 1, but only the treated units are used to compute the predicted values.' [[source]](https://stats.stackexchange.com/questions/613569/estimating-and-interpreting-the-att-with-regression-adjustment-and-marginal-effe)

You could also compute **average treatment effect on the untreated (ATU).** [[Wang et al. 2017]](https://doi.org/10.1186/s12874-016-0282-4)

To get standard errors, you can use bootstrapping or the delta method. [[source]](https://stats.stackexchange.com/questions/613569/estimating-and-interpreting-the-att-with-regression-adjustment-and-marginal-effe)

### G-computation vs. IPTW

'Standardization models the outcome, whereas inverse probability weighting models the treatment'.  If we were to do IPW and standardisation '**without using any models** (i.e. non-parametrically) then we would expect both methods to give the exact same result'. [[Batten 2023]](https://causallycurious.com/posts/standardization/standardization)

However, we expect them to differ if we use **models** to estimate them since some degree of misspecification is inescapable in models, 'but misspecification in the treatment model (IP weighting) and outcome model (standardisation) will not generally result in the same magnitude and direction of bias in the effect estimate'.

'Both IP weighting and standardization are estimators of the **g-formula**, a general method for causal inference first described in 1986... We say that standardization is a **plug-in g-formula** estimator because it simply replaces the conditional mean outcome in the g-formula by its estimates. When those estimates come from parametric models, we refer to the method as the **parametric g-formula**. Because here we were only interested in the average causal effect, we estimated parametrically the conditional mean outcome.'

'Often there is no need to choose between IP weighting and the parametric g-formula. When both methods can be used to estimate a causal effect, **just use both methods**. Also, whenever possible, use **doubly robust methods** that combine models for treatment and for outcome in the same estimator'. [[Hernán and Robins 2024]](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)

<mark>why is standardisation a g-method and not iptw if they're equivalent?</mark>

### Doubly robust estimators

'Some authors have proposed combinations of G-computation and propensity scores to improve the estimation of the marginal causal effect. These methods are known as doubly robust estimators (DRE) because they require the specification of both the outcome (for GC) and treatment allocation (for PS) mechanisms to minimise the impact of model misspecification'. [[Chatton et al. 2020]](https://doi.org/10.1038/s41598-020-65917-x)

## Marginal structural models

'**Marginal structural models** aim to make the exposed and unexposed groups exchangeable in terms of confounders by weighting each observation (commonly using inverse probability of treatment weighting) so that the distribution of confounders is similar in both groups. An ATE can then be calculated by a simple comparison or unadjusted regression model.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

'marginal structural models (MSMs) were designed to estimate marginal quantities (i.e., not conditional on other covariates). The parameters of a MSM can be consistently estimated using two classes of estimators: the g-computation algorithm [4] and the inverse-probability of treatment weighting (IPTW) [5]. G-computation is often seen as a viable alternative to IPTW because gcomputation produces more efficient (i.e. small standard errors) and more stable estimates in parametric settings and can better handle heterogeneity involving timevarying exposure and confounding'. [[Wang et al. 2017]](https://doi.org/10.1186/s12874-016-0282-4)

See https://academic.oup.com/ckj/article/15/1/14/6358134 = [[Chesnaye et al. 2022]](https://doi.org/10.1093%2Fckj%2Fsfab158)

<mark>is this all also called "inverse probability weighting of marginal structural models?</mark>

## Augmented inverse probability weighting

## G-estimation of structural nested models

'**G-estimation** of structural nested models (SNM) predicts the counterfactual outcome at each time point given no exposure from that point onwards, conditional on prior values of the exposure and confounders.' [[Igelström et al. 2022]](https://doi.org/10.1136/jech-2022-219267)

'SNM are outcome models meant to handle time-varying effect measure modification (something that is technically difficult to define). But they are pretty straightforward in the single time-point setting. An additive SNM has two parameters, the effect of a when V=0 and the effect of a when V=1 (if V is binary). So, the structural nested model is a model we might assume for how the additive effect of A on Y varies by V.'[[source]](https://stats.stackexchange.com/questions/612029/what-is-the-difference-between-the-g-formula-g-estmation-g-computation-and-g-m)
