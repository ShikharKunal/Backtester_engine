
# Backtester Engine

This repository contains a backtesting engine designed for a static threshold strategy. The engine allows for the simulation of trading strategies based on predefined thresholds, calculating the Profit and Loss (PnL) at each timestamp. The codebase is organized into several key components as outlined below.

## Components

### 1. [backtesting.py](./backtesting.py)

The `backtngting.py` file containg the core `Backtester` class which handles the backtesting logic. The class takes a dataset and threshold values as arguments and calculates the PnL for each timestamp based on the implemented strategy.

#### Features

- **Initialization**: Takes in the dataset and threshold values (long, short, and liquidate) as arguments.
- **Static Threshold Strategy**: Determines trading positions (long, short, or neutral) based on the given alpha values and thresholds.
- **Apply Strategy**: Applies the static threshold strategy to the dataset, ensuring positions are updated correctly.
- **Calculate PnL**: Computes the PnL for each timestamp by simulating trades according to the strategy.
- **Run Backtest**: Runs the complete backtest process.
- **Get PnL**: Returns the final PnL after the backtest.

### 2. [optimisation.ipynb](./optimisation.ipynb)

The `optimisation.ipynb` notebook provides a step-by-step guide to running the `Backtester` class on a given dataset, `asset_1.csv`, and finding the PnL using default threshold values. Additionally, the notebook includes code to optimize the threshold values for maximizing PnL.

#### Sections

- **Running the Backtester**: Demonstrates how to use the `Backtester` class with default arbitrary threshold values on the provided dataset.
- **Optimization**: Contains code to find the optimal set of threshold values that yield the maximum PnL. This involves iterating through different threshold combinations and evaluating their performance.
