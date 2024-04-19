# <center>Birth outcomes</center>

## Why did I make this book?

We are designing a research project focussed around the prevention of adverse outcomes during labour. I developed this book to further our understanding around this topic and help guide design of the project. In particular, it is to help guide our thinking around the following...

:::{admonition} Issue 1: Outcome choice and measurement
:class: warning

Which adverse neonatal outcomes should we focus on? If we focus on hypoxic ischaemic encephalopathy, how do we measure it? If we anticipate there being too few cases, what then should we focus on?
:::

:::{admonition} Issue 2: Accounting for treatment use when identifying risk factors
:class: warning

There are prognostic factors that are associated with an increased risk of adverse outcomes but also trigger an effective intervention (caesarean section), creating a treatment paradox. This biases observed relationships between risk factors and the outcome - so it is very important that study design accounts for this
:::

:::{admonition} Issue 3: Intervention effectiveness
:class: warning

If we want to assess the effectiveness of an intervention, it requires that we use causal inference methodologies. These are introduced and explored in this book.
:::

There is a further issue - how we **process and use cardiotocograph data** - but that is explored further in seperate repositories [here](https://github.com/birth-outcomes/ctg_exploratory) and [here](https://github.com/birth-outcomes/fhrma_python).

## Section overview

**Background** - Context of key topics (e.g. stages of pregnancy and labour, interventions during labour, introduction to neonatal encephalopathy)

**Causal inference** -
* **Introduction and core concepts:** Introduces causal inference, differentiates it from prediction, goes over the theree "languages", and details about DAGs, estimands, assumptions and target trials.
* **Methods:** Describes key methods for causal inference.

**Outcomes** - Identifying which adverse outcomes to focus on, and how best to measure these - in particular, identifying cases of hypoxic ischaemic encephalopathy.

**Study design** -
* **Risk factors:** Designing a study to identify risk factors of an adverse outcomes, with designing accounting for the effect of treatment use on relationships. Includes examples of existing studies.
* **Intervention effectiveness:** Designing a study to assess the effectiveness of interventions in preventing adverse outcomes. Includes examples of existing studies.

There is also an **Appendices** section, which contains some additional notes around various topics (some incomplete/older).

## Acknowledgements

Throughout this book, I have reused text and images from various publications and sources - these have been provided throughout. These references will be the source I acquired the information/image from - but they themselves may sometimes have been referencing other studies and authors. 

```{toctree}
:hidden:
:caption: Background

Background <background/encephalopathy>
```

```{toctree}
:hidden:
:caption: Causal Inference

Causal Inference <causal_concepts/1_predict_vs_causal>
```

```{toctree}
:hidden:
:caption: Outcomes

Outcomes <outcomes/summary>
```

```{toctree}
:hidden:
:caption: Study Design

Study Design <risk_factors/treatment_paradox>
```

```{toctree}
:hidden:
:caption: Appendices

Appendices <appendices/neo_out_enceph_treatment_outcomes>
```