# -*- coding: utf-8 -*-
# # This script tests PyMC3 which I have found to be a bit tricky to install and
# run correctly, especially on Windows.

import sys
import numpy as np
import pymc as pm
import arviz as az
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("seaborn-darkgrid")
print("Running on PyMC v{}".format(pm.__version__))

np.random.seed(123)

if __name__ == "__main__":

    drug = (
        101,
        100,
        102,
        104,
        102,
        97,
        105,
        105,
        98,
        101,
        100,
        123,
        105,
        103,
        100,
        95,
        102,
        106,
        109,
        102,
        82,
        102,
        100,
        102,
        102,
        101,
        102,
        102,
        103,
        103,
        97,
        97,
        103,
        101,
        97,
        104,
        96,
        103,
        124,
        101,
        101,
        100,
        101,
        101,
        104,
        100,
        101,
    )
    placebo = (
        99,
        101,
        100,
        101,
        102,
        100,
        97,
        101,
        104,
        101,
        102,
        102,
        100,
        105,
        88,
        101,
        100,
        104,
        100,
        100,
        100,
        101,
        102,
        103,
        97,
        101,
        101,
        100,
        101,
        99,
        101,
        100,
        100,
        101,
        100,
        99,
        101,
        100,
        102,
        99,
        100,
        99,
    )

    y1 = np.array(drug)
    y2 = np.array(placebo)
    y = pd.DataFrame(
        dict(
            value=np.r_[y1, y2],
            group=np.r_[["drug"] * len(drug), ["placebo"] * len(placebo)],
        )
    )

    y.hist("value", by="group", figsize=(12, 4))

    μ_m = y.value.mean()
    μ_s = y.value.std() * 2

    with pm.Model() as model:
        group1_mean = pm.Normal("group1_mean", mu=μ_m, sigma=μ_s)
        group2_mean = pm.Normal("group2_mean", mu=μ_m, sigma=μ_s)

    σ_low = 1
    σ_high = 10

    with model:
        group1_std = pm.Uniform("group1_std", lower=σ_low, upper=σ_high)
        group2_std = pm.Uniform("group2_std", lower=σ_low, upper=σ_high)

    with model:
        ν = pm.Exponential("ν_minus_one", 1 / 29.0) + 1

    plt.figure()
    with model:
        az.plot_kde(np.random.exponential(30, size=10000), fill_kwargs={"alpha": 0.5})
    plt.savefig("kde.png")

    with model:
        λ1 = group1_std**-2
        λ2 = group2_std**-2

        group1 = pm.StudentT("drug", nu=ν, mu=group1_mean, lam=λ1, observed=y1)
        group2 = pm.StudentT("placebo", nu=ν, mu=group2_mean, lam=λ2, observed=y2)

    dot = pm.model_to_graphviz(model)
    dot.format = "png"
    dot.render("graphviz.gv")

    with model:
        diff_of_means = pm.Deterministic(
            "difference of means", group1_mean - group2_mean
        )
        diff_of_stds = pm.Deterministic("difference of stds", group1_std - group2_std)
        effect_size = pm.Deterministic(
            "effect size",
            diff_of_means / np.sqrt((group1_std**2 + group2_std**2) / 2),
        )

    if sys.platform.startswith("win"):
        print("Warning: Temporarily disabling test on windows.")
        sys.exit(0)

    with model:
        # For this test script, we do not do much sampling. This is not enough
        # for real work!
        trace = pm.sample(
            tune=200, draws=100, chains=2, cores=2, return_inferencedata=True
        )

    plt.figure()
    with model:
        pm.plot_posterior(
            trace,
            var_names=[
                "group1_mean",
                "group2_mean",
                "group1_std",
                "group2_std",
                "ν_minus_one",
            ],
            color="#87ceeb",
        )
    plt.savefig("posteriors.png")

    with model:
        print(
            az.summary(
                trace,
                var_names=["difference of means", "difference of stds", "effect size"],
            )
        )
