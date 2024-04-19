# HIE proposal 2: caesarean v.s. vaginal

## Background

As in [research proposal 1](./research_proposal.md).

<mark>add some literature on causal inference</mark>

i.e. previous ones Missing: consideration of treatment paradox

## Aims and objectives

Comparing the incidence of HIE between similar patients who received an emergency caesarean versus those who had a vaginal delivery.

````{mermaid}
  flowchart LR;

    t("Non-elective<br>caesarean section"):::white;
    o("HIE"):::white;

    t --> o;

    classDef white fill:#FFFFFF, stroke:#FFFFFF;
    classDef black fill:#FFFFFF, stroke:#000000;
    classDef empty width:0px,height:0px;
    classDef green fill:#DDF2D1, stroke: #FFFFFF;
````

<mark>why can't we just include whether they had a caesarean as a predictor in the model</mark>

## Inclusion and exclusion criteria

Inclusion criteria:
* Received an emergency caesarean or had a vaginal birth
* Infants born at or beyond 35 weeks of gestation
* Singleton pregnancies

Exclusion criteria:
* Elective caesarean (as focussing on patients who began labour intending to have a vaginal delivery)

## Outcome

As in [research proposal 1](./research_proposal.md).

## Research design

<mark> add design </mark>

## Limitations

<mark>add</mark>

## Rough notes

### Investigate variation in use of emergency caesarean sections

There is not one right way to perform this analysis. However, a good starting point could be to replicate the methods used in [SAMueL-1](https://samuel-book.github.io/samuel-1/introduction/intro.html) (which focussed on variation in thrombolysis use between hospitals).

Here, we would:
* Model variation in use of emergency caesareans between hospitals so we can ask: *'What treatment would my patient receive at other hospitals?'*
* Model the delivery pathway, using clinical pathway simulation, so we can ask the question: *'What would happen to a hospital's use of and benefit from use of emergency caesarean sections, by changing key aspects of the pathway*, especially focussing on timing of the caesarean

<mark>add more detail on actual methods</mark>

However, this doesn't necessarily need to be just between hospitals - you can, for example, look at variation in use of emergency caesarean by:
* Time of day - Steve Thornton comments that "the time of day is important in the rate of delivery. More deliveries tend to happen at night naturally (perhaps because this was safer in long gone times as predators were not around). Also, nowadays because the inductions happen in the morning on the whole, this influences the timing of delivery"
* Weekday v.s. weekend

When look into timing of caesarean, there is no simple way to define timing, but possibilities include:
* The presence of multiple (𝑘) risk factors.
* Length of labour, or length of Stage-II labour.
* Cervical dilation (Steve: This is the standard method of determining the length of labour. The time from the start is really variable and inaccurate)
* Contraction rate/force (Steve: Unfortunately, we cannot determine the force of contraction, only the timing which is really important for any changes in the fetal heart rate)

### Looking at relationship between use of emergency caesarean and outcome of hypoxic ischaemic encephalopathy

Could do SAMueL-2. <mark>explain how they did it</mark>

Could look into causal inference methologies.
* The first step we did on variation could be described as us trying to identify instrumental variables
* <mark>Go into detail of some based on obstetric studies and worked examples. Provide links to those pages.</mark>
* <mark>add dag</mark>
* for causal models, should be being explicitly clear which variables in a model were considered in design of the causal model (to avoid Table 2 fallacy)
* should be reporting predictive accuracy of all models (with reference)
* Mike's ideas - 'This step will likely require the natural experiment of comparing between units with high and low intervention rates, using matched cohorts of labours (or conditioning machine model on a propensity score for likelihood of a mother having a CS). Using machine learning we can estimate a teams’ propensity to use CS; this score allows comparison of different units with different populations. We will also use expert opinion and literature review to build qualitative causal models. These will be articulated using Directional Acyclic Graphs (DAGs), and will inform any machine learning.'

You can demonstrate the existence of the treatment paradox by comparison of models designed to account for it, to those that are not.
