import numpy as np
import pandas as pd

def data_stream_simulation(size=1000, noise_level=0.1, anomaly_rate=0.01):
    """
    Simulates a data stream with seasonal patterns, noise, and anomalies.

    Args:
        size (int): Number of data points to generate.
        noise_level (float): Standard deviation of random noise.
        anomaly_rate (float): Proportion of anomalies in the data.

    Returns:
        np.ndarray: Simulated data stream.
    """
    t = np.linspace(0, 4 * np.pi, size)
    seasonal_pattern = np.sin(t)
    noise = np.random.normal(0, noise_level, size)
    data = seasonal_pattern + noise

    anomalies = np.random.choice([0, 1], size=size, p=[1-anomaly_rate, anomaly_rate])
    data += anomalies * np.random.uniform(3, 6, size)

    return data

def load_real_data(filepath):
    """
    Load data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        np.ndarray: Loaded data stream.
    """
    try:
        df = pd.read_csv(filepath)
        return df['value'].to_numpy()  # Assuming the data is in a column named 'value'
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
