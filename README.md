# Water Potability Prediction Using LightGBM

## Overview

This project focuses on predicting the potability of water using the LightGBM algorithm. It is a classification problem where the goal is to determine whether a given water sample is potable (drinkable) or not, based on various features.

## Project Structure

- **Data**: The dataset includes various attributes such as pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, and Turbidity, which are used to predict water potability.
- **Model**: LightGBM, a gradient boosting framework, is employed to build and train the classification model.
- **Pipeline**: The project includes steps for data preprocessing, model training, and evaluation to ensure accurate predictions.
  
## DVC ML Pipeline

## Features

- **Gradient Boosting Decision Tree**: Leverages the power of ensemble learning to improve prediction accuracy.
- **Binary Classification**: Determines whether the water is potable (1) or not potable (0).
- **Evaluation Metrics**: Uses binary log loss as the evaluation metric to assess model performance.

## Installation

To get started, clone the repository and install the necessary dependencies using the provided requirements file.

```sh
git clone https://github.com/iguptashubham/water-potability-prediction-using-LightGBM.git
cd water-potability-prediction-using-LightGBM
pip install -r requirements.txt
```
