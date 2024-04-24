# Focus of the research

:::{toctree}
:hidden:
:caption: Things to consider

self
2_treatment_paradox
:::

:::{toctree}
:hidden:
:caption: Previous studies

3_examples_risk
4_examples_intervene
:::

:::{toctree}
:hidden:
:caption: Example research proposals

5_proposal_1
6_proposal_2
references
:::

`````{admonition} Executive summary
:class: info

The aim of this research is currently quite broad. There are several things to consider when clarifying the focus of this work.

**Outcome** - neonatal and/or maternal; conditions, interventions and/or clinical observations; number of outcomes and whether seperate or composite; how outcomes are measured; expert feedback.

**Treatment/intervention** - which interventions, how many you compare, whether you also include treatments after birth.

**What we hope to learn** - e.g. timing of caesarean, where caesarean was needed, where caesarean was not needed, where forceps or ventouse deliveries would be unsuccessful, understanding inequalities.

**Methods** - considering the timing of events; which predictors we include; how we analyse cardiotocograph data; how we identify risk factors; how we assess intervention effectiveness.
`````

## Stated aim of this research

As stated in the protocol for the ethics application, the ultimate aim of this project is to produce a tool that provides live, real-time, data-driven risk assessment during labour, using machine learning to avoid adverse neonatal and maternal outcomes. Key components of this work are:
1. Identifying an appropriate method of analysis for the **cardiotocograph data**
2. Identifying **risk factors** (maternal characteristics during labour, and risk factors that develop during labour) that influence maternal and neonatal outcomes
3. Identifying when **intervention** during labour would beneficial (as that is the natural recommendation you would be making off the back of such a tool)

Supporting this is the fact that:
* Reliable methods of interpreting CTG in labour have not yet been developed
* Current studies of risk factors for adverse outcomes do not use live data to predict outcomes during labour, and to modify the pre-labour risk [Protocol]

## Outcome

Given the broad stated aim of this project, there are a range of possibile choices for the outcome.

> Whether you focus on **neonatal and/or maternal** outcomes
> 
> The **type of outcome** you focus on...
> * **Conditions** - e.g. NE, HIE, pre-eclampsia
> * **Interventions** - e.g. transfer to neonatal care services, resuscitation, mode of delivery (spontaneous, vacuum, forceps, caesarean), whether rotation is needed
> * **Clinical observations** - e.g. chorioamnionitis, perinatal death (antenatal and intrapartum), Apgar (1-, 5-, 10-minute), meconium-stained amniotic fluid, vaginal tearing or episiotomy, blood clots, and urinary or anal incontinence
>
> **How many** outcomes you focus on...
> * **One** outcome
> * **Several** seperate outcomes
> * A **composite** of several outcomes (which could even combine neonatal + maternal outcomes, and different types of outcome)
>
> How the chosen outcome/s are **measured** - as some will be quite simple, but others may be harder to define, and require proxy measures or a combination of indicators for that one outcome. This requires careful thought for each outcome.
>
> These decisions could also involve **expert feedback** which could be quite structured (such as in previous studies, with steering committees and Delphi studies to form consensus opinions)

In this book, I have often focussed on HIE as an example. This is simply because of our meeting in January (which largely had revolved around HIE). However, we might not be interested in HIE if - 
* **We are actually interested in a broader range of outcomes**, or
* **There are too few HIE cases** as HIE is a fairly rare outcome. Depending on the criteria used to identify cases, and depending on the size of our dataset, there is a possibility that we have too few cases of HIE for us to use it as an endpoint To contextualise this...
    * The reported incidence of NE ranges from about 2 to 6 per 1000 live births, and the incidence of HIE ranges from about **1 to 8 per 1000** live births, although these figures have several limitations.[[Kurinczuk et a. 2010]](https://doi.org/10.1016/j.earlhumdev.2010.05.010)
    * [[Törn et al. 2023]](https://doi.org/10.1111/1471-0528.17533) - using data from Swedish national health and quality registers from **2009 to 2015, 0.0008% had mild HIE diagnosis(n=414, whilst n=504661 had no HIE)**
    * [[Leith et al. 2024]](https://doi.org/10.1016/j.annepidem.2023.11.011) - using US dataset of **836,216 births, of which 376 (0.00045%) had a diagnosis of HIE**
    * [[Odd et al. 2017]](https://doi.org/10.3233/NPM-16152) - using Bristol dataset of 14,000 births. In the training set, had **6712 births, of which 130 (0.01%) had HIE**

If looking at a broader outcome (and not with the intention of it being an indicator for HIE), this has **implications** for the predictors you should include, and any DAGs, and ultimately what your research question and focus is all about. For example:
* If a particular treatment/intervention/process is used as the outcome, then you'd need to think carefully about what that outcome represents - i.e. **all the possible reasons for receiving that intervention** - so they are appropriately included and considered in the model.
* If a particular condition is used as the outcome, then you'd need to think carefully about what is influencing the relationships between predictors and the outcome - this might often be about the influence of intervention via caesarean section, but **other treatments** might commonly be used that influence relationships as well.

I have not done alot of research into broader outcomes. However, whilst looking into HIE, I have come across examples of papers looking more broadly at outcomes, and examples include:
* **Maternal and perinatal complications** - Maternal complication = maternal death, neurological, hepatic, cardiorespiratory, renal or haematological complications, or delivery before 34 weeks. Perinatal complications by discharge = perinatal or infant mortality, bronchopulmonary dysplasia, necrotising enterecolitis, intraventricular haemorrhage, cystic periventricular leukomalacia, retionpathy of prematury, or HIE. [[Thangaratinam et al. 2017]](https://doi.org/10.1186/s12916-017-0827-3)
* **Adverse pregnancy outcome** - Composite of: hypertensive disorders of pregnancy, LGA, neonatal hypoglycaemia, shoulder dystocia, fetal death, neonatal death, bone fracture, nerve palsy. [[Cooray et al. 2020]](http://dx.doi.org/10.1136/bmjopen-2020-038845)
* **Adverse neonatal outcome** - 5-min Apgar <7, or composite of 5-minute Apgar score <7, resuscitation by intubation and/or perinatal death. [[Steer et al. 2023]](https://doi.org/10.1111/1471-0528.17531)
* **Adverse pregnancy outcomes** - delivery by elective or emergency caesarean section,pre-eclampsia, gestational hypertension, small-for-gestational-age, stillbirth, neonatal death and neonatal unit admission for at least 48 hours. [[Syngelaki et al. 2022]](https://doi.org/10.1002/uog.26036)

## Treatment/Intervention

We are often concerned about interventions - either in the context of accounting for treatment use when identifying risk factors for adverse outcomes, or in making recommendations about changes in risk when an intervention occurs. Things to consider here include...

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

## What do we hope to learn?

We have talked about a range of possible things that we might hope to learn from analysis of the sorts of outcome listed above. Examples have included:
* Comparing outcomes from labours with similar characteristics except that there was an **earlier or later** decision to do a caesarean
* Identifying infants who **did not receive caesareans** but who would have benefited
* Reducing risk of **unecessary caesarean** sections - with inherent maternal complications like infection, bleeding and bladder damage.
* Identifying women in whom **forceps or ventouse deliveries would be unsuccessful** and reduce the risk of traumatic assisted vaginal deliveries which lead to adverse neonatal outcomes
* Focus on **inequalities** in a particular treatment/outcome. Death and disability in pregnancy are much higher in disadvantaged groups. For example, stillbirth is up to four times higher in black than white women in the UK.

## Methods

**Timing** will be very important in this research. Things to consider will include...

> How you **model** the evolving risks during labour, and subsequently how you **analyse** data feeding into the model (e.g. analysing CTG data in 15 minute windows, and rerunning predictions)
>
> How you account for timing when assessing **interevention** effectiveness. The risk-benefit ratio is dynamic and changes during labour depending on how the labour progresses and how events unfold (e.g. caesareans are safer earlier in labour than later).

Another methodological consideration is **what variables** are included. This will depend on our chosen focus. Things to consider here include -

> **Which variables** are considered, which depends on the relationship you focus on, and your analysis method. Examples include:
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

How **cardiotocograph data** is analysed and incorporated as a predictor is also complex, with a wide range of methods used in the literature, as explored in https://github.com/birth-outcomes/ctg_exploratory and https://github.com/birth-outcomes/fhrma_python. For example:

> * Generating a set of parameters that describe the signal (clinically relevant or others), and the chosen method for that analysis
> * Transforming the signal, such as into an image using continuous wavelet transformation, and the chosen parameters

How we account for **treatment use** when identifying risk factors is another important factor [explored on the subsequent page](./2_treatment_paradox.md)

Finally, how we assess **intervention effectiveness**. When making recommendations about whether or not to intervene, we are focussed on the true causal relationship between the intervention and the outcome, which necessitates that we consider the use of [causal inference techniques](../causal_concepts/1_predict_vs_causal.md)

## Working with clinicians and parents

For any chosen study design and focus, involvement of clinicians, as well as public and patient involvement, will be important.
* Clinicians - e.g. how acceptable a live tool would be, and how co-production could be used to inform design
* Public and patient involvement - e.g. parents of infants who experienced adverse outcomes (short or long-term)