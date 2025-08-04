import json
def coding_instruct_prompt(idea):
    try:
        with open('analysis/results.json', 'r') as f:
            analysis_results = json.load(f)
    except FileNotFoundError:
        print("analysis/results.json not found, running without dataset analysis")
        analysis_results = {}
    return f"""
Your task is to generate a detailed, clear, and concise prompt that instructs another LLM (the instruct LLM)
to write a high-quality Python script for a model training pipeline based on the research idea: '{idea}' and the dataset information provided below
Write a Python script `run_pipeline.py` for a model training pipeline based on the idea '{idea}'. Load the dataset with:
```python
import numpy as np
try:
    data = np.load('pect_ndt_full_dataset.npz')
    X_train = data['X_train']
    y_train = data['y_train']
    X_valid = data['X_valid']
    y_valid = data['y_valid']
except FileNotFoundError:
    print("Dataset file not found")
    exit(1)
```
Analyze dataset features base on result {analysis_results}, missing values, and imbalance (noting 'good' vs. 'crack' classes).
Determine task (classification/regression) from 'idea or dataset.
Choose model: deep learning (e.g., neural network) if specified in '{idea}', else machine learning (e.g., Random Forest).
Preprocess: impute missing values (e.g., median), scale features (StandardScaler for ML, MinMaxScaler for DL), handle imbalance (e.g., SMOTE or class weights).
Configure model with reasonable hyperparameters (e.g., NN with 2x64-unit layers, RF with 100 trees).
Train on X_train, y_train, validate on X_valid, y_valid (DL: 50 epochs, early stopping; ML: optional 5-fold CV).
Compute metrics: classification (accuracy, F1, ROC-AUC), regression (MSE, R2). Save metrics and hyperparameters in 'result/results.json'.
analyze detailed dataset to choose the loss function . For instance,if the dataset is imbalance , focal loss will be suitable
Use libraries like scikit-learn, TensorFlow, PyTorch, imbalanced-learn. Ensure modularity, no random data/seeds.
＃requirement 
you must follow the coding style and structure of the provided code snippet and follow the content of idea
you impossible use the random  data if loading data failed
you should generate detailed prompt, not code
Ensure code dont have any note because the generated code quite long and complex 

"""