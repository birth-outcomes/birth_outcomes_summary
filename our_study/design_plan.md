# Research proposal: Machine learning to avoid adverse neonatal outcomes

## Finding a focus

In it's broadest sense, the end-goal of this project is to lead us towards producing a tool to provide live, real-time, data-driven risk assessment during labour. This could support decision making by the care providers and mother during labour, to help identify when and which interventions and delivery methods would most reduce risk of poor maternal or neonatal outcomes.

However, this is a complex problem with lots of moving parts, and requires that we identify a clearer research focus. Some things to consider...

### Outcome

> Whether you focus on **neonatal and/or maternal** outcomes
> 
> **Which outcomes** you choose to focus on. Neonatal examples include:
> * Neonatal encephalopathy (NE)
> * Hypoxic ischaemic encephalopathy (HIE)
> * Choroioamnionitis
> * Mortality<mark>finish</mark>
> 
> Maternal outcomes include:
> * Vaginal tearing or episiotomy
> * Blood clots
> * Urinary or anal incontinence
> 
> **Outcome measurement** - some outcomes are quite clear cut, but others are harder to define. For example, HIE might be defined based on:
> * Diagnostic code for HIE
> * Receiving treatment for cooling
> 
> But those decisions will then be based on a number of factors (which many studies specifically focus on) like:
> * pH
> * <mark>finish</mark>

### Treatment/Intervention

> Whether you focus on comparing **two or multiple** treatment/delivery pathways
> 
> Whether you focus on **type of delivery and/or other treatments that can be given during delivery**
> 
> **Which outcomes** you then choose to focus on. Examples of type of delivery include:
> * Unassisted vaginal delivery
> * Assisted vaginal delivery - ventouse (vacuum cup) or forceps
> * C-section - elective or emergency
> * Vaginal birth after C-section
> 
> Examples of treatments or other interventions during labour include:
> * Gas and air (Enotox)
> * Pethidine injections
> * Epidural
> * Remifentanil
> * Water birth
> * TENS machine
> * Artifical rupture of the membranes
> * Oxytocin drip/syntocinon
> * Episiotomy
> 
> If the outcome is not immediately after birth, whether you focus on **subsquent treatments** with examples like:
> * Magnesium sulfate and cooling for infants with HIE

### Focus

Choice of **treatment** and **outcome** are ultimately both about defining the focus of the project. Examples:
> * Identifying infants who **did not receive caesareans** but who would have benefited
> * Reducing risk of **unecessary caesarean** sections - with inherent maternal complications like infection, bleeding and bladder damage.
> * Identifying women in whom **forceps or ventouse deliveries would be unsuccessful** and reduce the risk of traumatic assisted vaginal deliveries which lead to adverse neonatal outcomes

This can be related not just to treatment and outcome, but also to the other characteristics included in the analysis, and how they are dealt with. Examples:

> * Focus on **inequalities** in a particular treatment/outcome. Death and disability in pregnancy are much higher in disadvantaged groups. For example, stillbirth is up to four times higher in black than white women in the UK.

### Methodological considerations

Timing
* Cross-sectional v.s. more live
* Rapdily changing
* 'The risk-benefit ratio is dynamic and changes during labour depending on how the labour progresses and how events unfold.' (the research bid)
* Timing is important... e.g. caesarean safer earlier in labour than later<mark>finish</mark>

FHR
* How process, complexities<mark>finish</mark>
* link to our repository

Treatment paradox, causal inference
* prediction v.s. causation and why this is a concern of ours
* Using information from FHR and complexities in that...
* Bias in predictions...<mark>finish</mark>
* Produce DAGs 
* Target trial emulation
* methods

## Example: Caesarean section and hypoxic ischaemic encephalopathy

Here, I have focussed on one example (simply as it was the most discussed at our meeting earlier in the year). This is the problem of infants who would have benefitted from having a caesarean, and who go on to have hypoxic ischaemic encephalopathy, and then potentially further complications (for example, cerebral palsy).

### Introduction

Preventative adverse neontal outcomes (in particular, HIE).

Intervention: caesarean.

Want more evidence to support decisions on who to intervene with. Worry of people not intervening and leading to poor outcomes (HIE).

Problem: treatment paradox. Prognostic --> caesarean. Alters relationship. Hence, just predicting who gets HIE will be unreliable. You can make a good prediction model, but would need to have no interest in how that prediction was made. If you're interested in true relationships, and what actually determines outcome, then treatment paradox is a problem. Hence, causal inference.

Caesarean --> HIE

Measured confounders

Unmeasured confounders

## Step 1

SAMueL-1: Identify variation in propensity to thrombolyse between hospitals, and demonstrate which patients were treated differently by which hospitals.

Similar approach here - identify variation in propensity to do caesarean between hospitals, and demonstrate who it varies for.
* Doesn't just have to be between hospitals - can do for other variables like time of day
* You could describ this as us "identifying an instrumental variable" - something that impacts decision to treat but not outcomes - and this is because it enables us to escape the treatment paradox

## Step 2

SAMueL-2: Look at association with outcomes

Here, likewise would look at outcomes. A few options of how do this.

Instruemntal variable added to DAG. Explain why that works.

<mark>if you're not doing 2sls, is it still instrumental variable methodology?</mark>

<mark>first, just start with trying to give a clear explanation of how you would do it with instrumental variable methods</mark>

## Rough ideas

To **demonstrate existence of the treatment paradox** (by comparison to models that are causal), and to allow comparability to other studies:
* **Prediction model (association)** - can we predict HIE

To actually **explore the proposed research question**:
* **Causality (intervention)** - what is the causal relationship between caesarean and HIE?
* **Counterfactuals** - what would have happened if we had done or not done the caesarean?

We should:
* Reporting predictive accuracy of all models
* Being explicitly clear which variables in a model were considered in design of the causal model (to avoid Table 2 fallacy)

## Design ideas

### From Mike's email + Steve's comments - Research questions - 

1. How well can we predict poor outcomes during labour? Poor outcomes are defined as:
    * APGAR < 7
    * Use of neonatal ventilation
    * NICU admission
    * Use of neonatal cooling (as a surrogate of risk of HEI)
    * Infant death

2. Can we predict the likely effect of intervention (CS) when predicted outcome is poor?
    * This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations.
    * We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.

3. As research question (2) but examine timing of intervention. There is no simple way to define timing, but possibilities include:
    * The presence of multiple (𝑘) risk factors.
    * Length of labour, or length of Stage-II labour.
    * Cervical dilation (Steve: This is the standard method of determining the length of labour. The time from the start is really variable and inaccurate)
    * Contraction rate/force (Steve: Unfortunately, we cannot determine the force of contraction, only the timing which is really important for any changes in the fetal heart rate)

4. How acceptable would such a system be to clinicians? How can co-production be used to inform design?

5. (Final stage): How effective is such a tool at changing practice and outcomes? (Trial)

Notes: * All ML models will also employ an explainability model such as SHAP (SHaply Additive exPlanations). When heightened risk is predicted, this will show clinicians what is making the ML model predict high risk.

## Rough notes from meeting

Can’t use outcomes in classical way because of treatment paradox. May need to reformulate, as this is not a prediction question. In women in labour, is there a way we can predict whose going to need something that allows us to act more effectively. Dave Right statistician screening for down syndrome example – all previous ranked top five predicting down syndrome and so on – doesn’t necessarily tell you best way, as those five together may predict less well than one of those and others, its more complex than that. You’re trying to produce an instrument that allows you to behave differently. 

If definition of problem is avoiding fetal injury, is what is needed a more subtle instrument, or having experts who know what they’re doing. 

**Exclude delivery by caessarean** (i.e. only look at untreated) - this is what they did in the Cambridge data - although...
* Still subject to influence due to forcep delivery and so on – but potentially less issue
* Takes out highest risk groups

Doing a **clinical trial**

**Incorporating human opinion** - Judea Pearl, causal inference, would say you cannot tell these things from the data alone. Statisticians are used to only answer from data alone, other things non data, but humans are good at recognising patterns that data isn’t. E.g. a first thing cant be caused by second. But statistics can’t handle. He says you take models through experts of describing what are potential causal routes through here and model them under different conditions. If you expert is right about this causing this, then can predict effect size of this causing this. Gives you a way around this problem – not just relying on data. In stroke, want to be able say causally about link between thrombolysis and outcomes.

When the clinician thinks the baby is in trouble, what tells you whether it really is or isn’t – that narrows it down to a smaller group where intervention produces less of paradox.
* majority of sections for fetal distress are not true distress – its abnormal ctg but no fetal compromise
* correct – define of group not to be worried about

No treatment would be no low outcomes. We have better outcomes as experts intervene. The question is not is the child fine. The question is whether they would’ve been fine if hadn’t intervened, and we don’t know that. Looking for marginal improvement, thing has to be better than expert, and that’s a big ask

Another way around paradox is how in stroke, say different units do different things, and helps them understand, as propensity to give ceassarean differs between hospitals, and that may allows us to dig into it
* issue will be is that it will be between clinician rather than site
* will still be site difference in rates even when account for socioeconomic and stuff, so there must be something