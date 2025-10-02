To develop a scalable, explainable, and fair AI pipeline that predicts the presence and severity of allergic diseases using clinical and allergen-specific IgE chip test data from the Allergen Chip Challenge (ACC) dataset.

## Objectives
1. Data Engineering & Preprocessing

    - handle missing values
    - standardize features
    - encode categorical_variables consistently

2. Feature Selection and Dimensionality Reduction

    - apply statistical filtering
    - use regularization
    - compare with tree-based feature importance

3. Model Development

    - train baseline ML models
    - extend to advanced models
    - tackle 2 prediction tasks:
        - presence of allergy (Allergy_Present)
        - severity of allergy (Severe_Allergy)

4. Explainanility and Interpretability

    - use SHAP/LIME
    - generate feature attribution visualizations/dashboard

5. Fairness and Bias Analysis

    - evaluate subgroup performance
    - quantify disparities in accuracy/recall
    - explore rebalancing techniques

6. Pipeline Engineering and Reusability

    - implement modular, OOP-based architecture:
    data_loader -> preprocessor -> feature_selector -> model_trainer -> evaluator -> visualizer
    - ensure pipeline scalability for other healthcare datasets

7. Deployment Prototype

    - build a simple flask app:
        - input: patient features
        - output: predicted allergy presence, severity and explanation


## Dataset
download the dataset from: (https://www.data.gouv.fr/datasets/allergen-chip-challenge/)