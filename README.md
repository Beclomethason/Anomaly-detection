<<<<<<< HEAD
# Anomaly-detection
Cobblestone assignment
=======
# Efficient Data Stream Anomaly Detection

## Description
A Python-based project to detect anomalies in real-time data streams, simulating patterns and seasonal variations.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

 Installation
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
## efficient Data Stream Anomaly Detection
## Overview
This project implements a real-time anomaly detection system for data streams using a rolling Z-score algorithm. It identifies unusual data points in streaming data, such as revenue, and visualizes them in real-time. The system is highly configurable and can process data from simulations or real-world datasets in CSV format.

## Features
## Real-Time Detection: Identifies anomalies in a data stream using a rolling Z-score algorithm.
Customizable Parameters: Users can adjust the rolling window size and Z-score threshold for optimal performance.
Real-Time Visualization: Visualizes data streams with anomalies marked in real-time.
CSV Support: Processes real-world data from CSV files, supporting single or multiple columns.
Error Handling: Robust error handling and validation for input data.
Unit Tests: Ensures reliability with tests for anomaly detection and data processing.
Algorithm Explanation
The project uses a Rolling Z-Score algorithm to detect anomalies:

A rolling window tracks the most recent data points.
The mean and standard deviation of the rolling window are computed.
A data point is flagged as an anomaly if it deviates from the mean by more than a user-defined threshold (e.g., 3 standard deviations).
This algorithm is lightweight, efficient, and suitable for real-time data streams.

Installation
Prerequisites
Python 3.x (tested with Python 3.10+)
Minimal external libraries (see requirements.txt).
## Install Dependencies
## Run the following command to install required libraries:
```pip install -r requirements.txt```
## code run 
   ```python src/main.py --file data/clean_data.csv --column revenue --window_size 50 --threshold 3.0```
>>>>>>> 328a5b3 (Initial commit)
