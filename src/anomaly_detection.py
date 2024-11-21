from collections import deque
import numpy as np

class AnomalyDetector:
    """
    Detects anomalies in a data stream using a rolling window and Z-score threshold.

    Attributes:
        window_size (int): Size of the rolling window.
        threshold (float): Z-score threshold for anomaly detection.
    """
    def __init__(self, window_size=50, threshold=3.0):
        self.window = deque(maxlen=window_size)
        self.threshold = threshold

    def detect(self, value):
        """
        Flags a value as an anomaly if it deviates significantly from the rolling mean.

        Args:
            value (float): Current data point.

        Returns:
            bool: True if value is an anomaly, False otherwise.
        """
        if len(self.window) < self.window.maxlen:
            self.window.append(value)
            return False  # Not enough data for decision

        mean = np.mean(self.window)
        std_dev = np.std(self.window)
        self.window.append(value)

        if std_dev == 0:  # Handle case of zero variance
            return False

        return abs(value - mean) > self.threshold * std_dev
