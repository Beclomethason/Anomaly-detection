import unittest
from anomaly_detection import AnomalyDetector

class TestAnomalyDetector(unittest.TestCase):
    def test_detection(self):
        detector = AnomalyDetector(window_size=3, threshold=2)
        data = [1, 1, 1, 10]  # Last point is an anomaly
        for value in data:
            result = detector.detect(value)
        self.assertTrue(result)

    def test_no_anomaly(self):
        detector = AnomalyDetector(window_size=3, threshold=2)
        data = [1, 1, 1, 1]
        for value in data:
            result = detector.detect(value)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
