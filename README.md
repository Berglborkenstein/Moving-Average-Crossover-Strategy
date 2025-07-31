# Moving Average Crossover Strategy

This project implements a simple moving average crossover trading strategy using historical price data. Generates buy and sell signals based on when the long and short-term moving averages cross over.

## Strategy Overview

The strategy works as follows:
- **Buy Signal**: When the short-term moving average crosses **above** the long-term moving average.
- **Sell Signal**: When the short-term moving average crosses **below** the long-term moving average.

This strategy is often used to capture trends in the market while reducing noise from short-term fluctuations.

## Structure

backtest.py - Defines functions to calculate returns and performance metrics
main.py - Calculates the buy and sell signals using historical data, producing a plot marking all the buy and sell points
plot.png - Example plot produced showing the buy and sell points relative to the stocks price
