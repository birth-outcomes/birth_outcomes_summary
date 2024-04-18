# Finding a focus

`````{admonition} Executive summary
:class: info

* **Outcome** - neonatal and/or maternal; which outcomes; how measure the outcomes
* **Treatment/intervention** - which interventions; how many interventions; whether include subsequent interventions (if outcome not immediately after birth)
* **Focus** - linked with outcome and treatment chosen (e.g. if focus on earlier caesareans v.s. later, or on people who did not receive caesarean but maybe should have, or if focus is to identify women in whom assisted deliveries would be unsuccessful) - or other characteristics (e.g. a focus on inequalities)
* **Methodological considerations** - timing; analysis of cardiotocograph data; treatment paradox; variables included
* Working with clinicians and parents
`````

In it's broadest sense, the end-goal of this project is to lead us towards producing a tool to provide live, real-time, data-driven risk assessment during labour. This means using machine learning to avoid adverse neonatal outcomes. This is a tool for which the effectiveness could be evaluated, to ascertain whether it helps support decision making by the care providers and mother during labour, to help identify when and which interventions and delivery methods would most reduce risk of poor maternal or neonatal outcomes.

However, this is a complex problem with lots of moving parts, and requires that we identify a clearer research focus. Some things to consider...

## Outcome

> Whether you focus on **neonatal and/or maternal** outcomes
> 
> **Which outcomes** you choose to focus on.
> * Neonatal examples include:
>   * Neonatal encephalopathy (NE), and specific types, like hypoxic ischaemic encephalopathy (HIE)
>   * Choroioamnionitis (intra-aminotic infection)
>   * Death
>   * Indicators of poor health - umbilical cord pH, Apgar, resuscitation, meconium-stained amniotic fluid, transfer to neonatal care services
> * Maternal outcomes include vaginal tearing or episiotomy, blood clots, and urinary or anal incontinence
> 
> **Outcome measurement** - some outcomes are quite clear cut, but others are harder to define, and may use proxy measures or combinations of measures

## Treatment/Intervention

> **Which interventions** you choose to focus on. These could be specific **interventions during labour or delivery types**.
> * Examples of type of delivery include:
>   * Unassisted vaginal delivery
>   * Assisted vaginal delivery - ventouse (vacuum cup) or forceps
>   * C-section - elective or emergency
>   * Vaginal birth after C-section
> * Examples of treatments or other interventions during labour include:
>   * Gas and air (Enotox)
>   * Pethidine injections
>   * Epidural
>   * Remifentanil
>   * Water birth
>   * TENS machine
>   * Artifical rupture of the membranes
>   * Oxytocin drip/syntocinon
>   * Episiotomy
>
> How you compare these - e.g. compare **two** delivery pathways, or compare **multiple** delivery pathways
>
> If the outcome is not immediately after birth, whether you focus on **subsequent treatments** - for example, magnesium sulfate and cooling for infants with HIE.

## Focus

Choice of **treatment** and **outcome** are ultimately both about defining the focus of the project. Examples:
> * Comparing outcomes from labours with similar characteristics except that there was an **earlier or later** decision to do a caesarean
> * Identifying infants who **did not receive caesareans** but who would have benefited
> * Reducing risk of **unecessary caesarean** sections - with inherent maternal complications like infection, bleeding and bladder damage.
> * Identifying women in whom **forceps or ventouse deliveries would be unsuccessful** and reduce the risk of traumatic assisted vaginal deliveries which lead to adverse neonatal outcomes

This can be related not just to treatment and outcome, but also to the other characteristics included in the analysis, and how they are dealt with. Examples:

> * Focus on **inequalities** in a particular treatment/outcome. Death and disability in pregnancy are much higher in disadvantaged groups. For example, stillbirth is up to four times higher in black than white women in the UK.

The focus **may be necessitated by available data and sample sizes**. For example, if you hoped to focus on HIE but there were too few cases in the dataset, you might switch to a more general indicator of adverse outcomes (e.g. admission to neonatal unit), and so your focus shifts to being on admission to a unit rather than specifically on HIE.

## Methodological considerations

**Timing** will be important with regards to the choice to intervene and the outcome. The risk-benefit ratio is dynamic and changes during labour depending on how the labour progresses and how events unfold. For example, caesareans are safer earlier in labour than later.

How **cardiotocograph data** is analysed and incorporated as a predictor is also complex, with a wide range of methods used in the literature, as explored in https://github.com/birth-outcomes/ctg_exploratory and https://github.com/birth-outcomes/fhrma_python. For example:

> * Generating a set of parameters that describe the signal (clinically relevant or others), and the chosen method for that analysis
> * Transforming the signal, such as into an image using continuous wavelet transformation, and the chosen parameters

The **treatment paradox** is another important consideration, as explored [on this page](../risk_factors/treatment_paradox.md). This exists as the indicators for a poor outcome (e.g. abnormal cardiotocograph, gestational age) will trigger an effect treatment (caesarean), which then biases the observed relationship between the indicators and outcome. This is important to us - we are not just interested in prediction - but in the true relationships between variables. Hence, **causal inference methodologies** should be used within this work. Another reason to use these methods is to help us deal with **omitted variable bias**, as its highly likely that the clinical datasets we can access are missing important variables. There are a range of possible methods, including but not limited to...

> **Conventional methods:**
> * (Principal) Stratification
> * Matching
> * Inverse probability of treatment weighting (IPTW)
> * Multivariable regression
> 
> **G-methods:**
> * G-computation (/ parametric G-formula / G-standardisation / standardisation / outcome regression)
> * Marginal structure models
> * G-estimation
> 
> **Methods to address unobserved confounding:**
> * Instrumental variables
> * Regression discontinuity (RD)
> * Interrupted time series (ITS)
> * Difference in differences (DiD)
> 
> **Other methods:**
> * Marginal, asymmetric conditional, and causal SHAP values
> * Synthetic control
> * Matrix completion
> * Causal discover
> * Double machine learning
> * Causal forests
> * Structural estimation

Another methodological consideration is **what variables** are included. This will depend on our chosen focus. Things to consider here include -

> **Which variables** are considered, which depends on the relationship you focus on, and your analysis method - e.g.
> * Some may just have **one** (e.g. instrumental variable studies)
> * Could look at **minimally important set of variables**
> * Some studies use a really **wide range**
> 
> Examples of variables include:
> * Suspected fetal growth restriction (FGR proxy is number of antenatal scans)
> * Previous CS
> * Parity (number, or nulliparity vs multiparity)
> * Antepartum haemorrhage
> * Body mass index
> * Maternal age
> * Maternal ethnicity
> * Gestational age at delivery
> * Induction of labour
> * Analgesia - epidural use
> * Oxytocin use
> * Maternal pyrexia
> * Abnormal FHR
> * Meconium-stained amniotic fluid
> * Single unsupported mother
> * Highest antenatal blood pressure
> * Duration of labour
> * Fetal size on scan (if done)

## Working with clinicians and parents

For any chosen study design and focus, involvement of clinicians, as well as public and patient involvement, will be important.
* Clinicians - e.g. how acceptable a live tool would be, and how co-production could be used to inform design
* Public and patient involvement - e.g. parents of infants who experienced adverse outcomes (short or long-term)