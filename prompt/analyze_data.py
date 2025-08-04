def analyze_dataset_prompt(data):
    """
    Generate a prompt for analyzing the PECT-NDT dataset (.npz format)
    """
    return f"""
**Instructions for Coder LLM: Analyze PECT-NDT Dataset and Save Results**

You are tasked with writing a Python script to analyze a preprocessed Pulsed Eddy Current Testing (PECT) dataset for Non-Destructive Testing (NDT) at `{data}`. The dataset is stored in a single `.npz` file and contains the following arrays:

###Information about the dataset:

This dataset consists of thousands of time-series signals collected from a grid scan over a large metal surface (such as a steel plate or pipeline). Each signal represents the electromagnetic response measured at a specific location when a pulsed eddy current is applied. The goal is to detect and characterize subsurface defects (such as corrosion or thinning) without damaging the material.

**How is the data structured?**

- Each signal is a 1D array of 500 time points, representing the voltage response over time at one scan position.
- The scan covers tens of thousands of positions, forming a 2D grid over the inspected surface.
- Signals from defect-free (good) regions and defective (corroded) regions are both included.
- Labels are provided to indicate whether each signal comes from a normal or defective area.
- 

NDT Dataset Structure:

- **X_train**: Training signals, shape `(15456, 500, 1)`  
  15,456 signals for model training, each with 500 time points.
- **y_train**: Training labels, shape `(15456,)`  
  Binary labels: 0 = good, 1 = defect.
- **X_valid**: Validation signals, shape `(10304, 500, 1)`  
  10,304 signals for model validation.
- **y_valid**: Validation labels, shape `(10304,)`  
  Binary labels for validation set.
- **X_scan**: All scan signals, shape `(25761, 500, 1)`  
  Complete set of measured signals from the entire scan area.
- **sX**: Scan dimension, value `160`  
  Number of scan positions along one axis.
- **samples**: Signal length, value `500`  
  Number of time points per signal.
- **Xc**: Corrosion (defect) signals, shape `(711, 500)`  
  711 signals identified as coming from defective areas.
- **Xg**: Good (non-defect) signals, shape `(25049, 500)`  
  25,049 signals from normal/healthy regions.
- **X_in_corr**: Spatial corrosion data, shape `(161, 160, 500)`  
  2D spatial grid (161 rows × 160 columns), each cell contains a 500-point signal.
  Represents the corrosion region with spatial structure preserved.

Total signals: 25,760 (711 defect + 25,049 good)
Training split: 15,456 signals
Validation split: 10,304 signals


###

All arrays retain their original shapes and are ready for direct use in deep learning or machine learning frameworks or scientific analysis.
this is the required code you must use when loading the dataset:
 ```python
 import numpy as np

data = np.load('raw_data.npz', allow_pickle=True)

X_train = data['X_train']        
y_train = data['y_train']        
X_valid = data['X_valid']        
y_valid = data['y_valid']        
X_scan = data['X_scan']          
sX = data['sX'].item()           
samples = data['samples'].item() 
Xc = data['Xc']                  
Xg = data['Xg']                  
X_in_corr = data['X_in_corr'] 
 ```

---
## Task

Write a Python script that:

1. **Loads the `.npz` dataset** and prints the shape and type of each array.

2. **Visualizes the dataset**:
you can visualize Histogram / KDE plots for each feature, Boxplots to spot outliers, Scatter plots or pairplots to observe relationships between features, Correlation heatmap to find redundant or strongly related features

3. **Calculates and saves comprehensive statistics** to `results.json` in `analysis/`:
   - Dataset information: shapes, types, and array descriptions
   - Label distribution for training and validation sets
   - Statistical analysis for each array:
     - Basic statistics (mean, std, min, max, median, constant features, outliers) for signal arrays, Identify missing values
     - Signal characteristics (peak values, signal ranges, etc.)
   - Path to the saved comparison plot

---

## Requirements
- Use only the provided `.npz` file (do not generate random data) and dont note because i want you analyze enought what i need and not complicated
- Ensure the comparison plot is saved as `.png` in `analysis/figures/`
- The `results.json` must contain comprehensive statistics but the visualization should be simple and clear
- Provide clear comments explaining the signal selection and plotting process
- you also need introduce prompt agent should generate code according this prompt
- Do **not** use random data or random seed and synthetic data; only analyze the provided `.npz` file
- Ensure `results.json` is well-structured and comprehensive for PECT-NDT data

"""