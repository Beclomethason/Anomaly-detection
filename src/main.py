import argparse
from data_processing import load_and_preprocess
from anomaly_detection import AnomalyDetector
from visualization import real_time_visualization

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Efficient Data Stream Anomaly Detection")
    parser.add_argument("--file", type=str, required=True, help="Path to real data CSV file")
    parser.add_argument("--column", type=str, default="revenue", help="Column name for anomaly detection")
    parser.add_argument("--window_size", type=int, default=50, help="Rolling window size for anomaly detection")
    parser.add_argument("--threshold", type=float, default=3.0, help="Z-score threshold for anomaly detection")

    args = parser.parse_args()

    # Load and preprocess the data
    data = load_and_preprocess(args.file, args.column)
    if data is None:
        exit("Failed to load data. Exiting.")

    # Initialize the anomaly detector
    detector = AnomalyDetector(window_size=args.window_size, threshold=args.threshold)

    # Visualize anomalies in real time
    real_time_visualization(data, detector)
