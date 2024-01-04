# Air Quality Analysis README

## Overview

This repository contains a Python script for analyzing air quality data in India using the Pandas library. The script performs three main tasks:

1. **Task 1:** Year-wise list of the top 10 cities in India with the most air pollution based on the RSPM (Respirable Suspended Particulate Matter) levels.

2. **Task 2:** Year-wise list of the top 10 states in India with the most air pollution. The air quality index (AQI) is calculated using the concentrations of SO2, NO2, RSPM, and SPM (Suspended Particulate Matter).

3. **Task 3:** Month-wise air quality analysis for Delhi in the year 2021.

## Data

The analysis uses air quality data stored in a CSV file ('data.csv'). The data is loaded into a Pandas DataFrame, and additional columns are created to facilitate the analysis.

## Tasks and Functions

### Task 1

The script identifies the top 10 cities each year based on their RSPM levels. The results are displayed using the Pandas DataFrame.

### Task 2

The script calculates the AQI for each data point using the concentrations of SO2, NO2, RSPM, and SPM. It then identifies the top 10 states with the highest mean AQI for each year.

### Task 3

The script extracts and analyzes the monthly air quality of Delhi in the year 2021. The results are displayed using the Pandas DataFrame.

## Functions

The script defines several functions to calculate the sub-indices (SI, NI, RPI, and SPI) and the overall AQI. These functions are applied to the DataFrame to derive the air quality indices.

## How to Run

1. Ensure you have Python installed on your system.
2. Install the required libraries using `pip install pandas`.
3. Place the air quality data CSV file ('data.csv') in the same directory as the script.
4. Run the script using `python script_name.py` in your terminal.


## How the code works?
The provided Python script utilizes the Pandas library to analyze air quality data in India from a CSV file. It performs three main tasks: first, it identifies and displays the top 10 cities in India with the highest air pollution each year based on RSPM levels. Second, it calculates the Air Quality Index (AQI) for each state using sub-indices derived from concentrations of SO2, NO2, RSPM, and SPM, then lists the top 10 states with the highest mean AQI for each year. Lastly, the script analyzes and displays the monthly air quality of Delhi in the year 2021. 