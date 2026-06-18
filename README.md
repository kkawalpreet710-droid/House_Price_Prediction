# House Price Prediction

A machine learning project that predicts house prices based on property features such as area, number of rooms, location amenities, and furnishing status.

## Project Overview

Real estate buyers and sellers often rely on guesswork to estimate a property's fair value.
This project builds and compares regression models to predict house prices accurately,
and identifies which features influence price the most.

## Dataset

- **Source:** [Kaggle — Housing Prices Dataset](https://www.kaggle.com/datasets/yasserh/housing-prices-dataset)
- **Size:** 545 rows, 14 columns
- **Target column:** `price`

## Project Structure
HousePricePrediction/
├── analysis.ipynb       # Main Jupyter Notebook with all tasks
├── Housing.csv          # Dataset

## Tasks Completed

- **Task 1** — Data loading and exploration
- **Task 2** — Data cleaning and encoding
- **Task 3** — Model building and evaluation (Linear Regression vs Random Forest)
- **Task 4** — Visualizations (price distribution, correlation heatmap, actual vs predicted)
- **Task 5** — Insights and summary

## Models Used

|      Model              |                  Result                  |
| Linear Regression       | Better performer on this dataset         |
| Random Forest Regressor | Compared against Linear Regression       |

## Key Findings

- **Area** and **bathrooms** are the strongest predictors of house price
- **Air conditioning** and **number of stories** also significantly influence price
- **Unfurnished** properties tend to sell for lower prices
- Linear Regression outperformed Random Forest, likely due to the linear nature of the data and relatively small dataset size

## Tools & Libraries

- Python 3
- Pandas
- Scikit-learn
- Matplotlib
- Seaborn 

