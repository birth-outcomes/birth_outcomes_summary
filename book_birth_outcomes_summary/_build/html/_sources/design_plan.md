# Design plans

## Overall aim

Using live labour data to predict who is likely to require caessarean, and reduce adverse effects for mother and baby. Combining data from fetus, parent, and CTG. Involves combining (a) risk factors during pregnancy, with (b) live risk factors during labour. Outcome of "X chance" of adverse outcome if don't go for caessarean or assisted delivery. Decision currently based on experience. Want some more objective evidence that can given women to help them understand and base risks on.

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