import numpy as np
drug_data=np.array([100,105,95,120,110,100,125,95,120])
placebo_data=np.array([85,96,112,108,99,123,105,100,111])
z=1.96

drug_μ=np.mean(drug_data)
placebo_μ=np.mean(placebo_data)

drug_σ=np.std(drug_data)
placebo_σ=np.mean(placebo_data)

drug_se=drug_σ/(len(drug_data)**0.5)
placebo_se=placebo_σ/(len(placebo_data)**0.5)

drug_ci=drug_μ+(z*drug_se)
drug_ci1=drug_μ-(z*drug_se)

print("the confidence intreval for drug is",drug_ci,',',drug_ci1)

placebo_ci=placebo_μ+(z*placebo_se)
placebo_ci1=placebo_μ-(z*placebo_se)

print("the confidence intreval for placebo is", placebo_ci,',',placebo_ci1)
