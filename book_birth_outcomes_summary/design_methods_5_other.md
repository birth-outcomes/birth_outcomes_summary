# Methods #4: Other

`````{admonition} Executive summary
:class: info

* SHAP variants
    * Marginal
    * Conditional (symmetric and asymmetric)
    * Causal
`````

This page details other methods that either don't fit into the prior three categories - or, that I have not realised would have fit into one of the prior categories!

## SHAP variants

### Marginal SHAP values

https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf

### Conditional SHAP values

**Symmetric and asymmetric**

https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf

SHAP values are usually symmetric, with no causal knowledge incorporated into their calculation. However, Frye et al. 2021(https://doi.org/10.48550/arXiv.1910.06358) proposed asymmetric Shapley values, which incorporate prior knowledge into the calculation. They 'can be tuned by the researcher to avoid splitting the Shapley feature effects uniformaly across related/correlated features - as is done in the symmetric case - and focus on the uniqute effect of a target feature after having conditioned on other pre-specified "causal" feature effects'.[[source]](https://github.com/nredell/shapFlex)

The shapFlex package offers two asymmetric options (marked as experimental):
* Asymmetric with weights of 0.5 - 'Agnostic causality. Similar to the symmetric algorithm. The difference is that, in the asymmetric algorithm, the entire set of causal effects is conditioned on as a group; the symmetric algorithm would condition on random subsets of the causal features.'
* Asymmetric with weights of 0.1 - 'Pure causality. The Shapley estimates for the causal targets are based on the actual/true/known feature values of the causal effects. Put another way, the estimates for the causal targets have been conditioned on the causal effects which decreases their magnitude. The Shapley estimates for the causal effects will then increase correspondingly to satisfy the Shapley property that the sum of the feature-level effects equals the model prediction.'

### Causal SHAP

https://proceedings.neurips.cc/paper/2020/file/32e54441e6382a7fbacbbbaf3c450059-Paper.pdf

https://towardsdatascience.com/casual-shap-values-a-possible-improvement-of-shap-values-4d4d62925b71