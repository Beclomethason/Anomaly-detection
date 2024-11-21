import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def real_time_visualization(data, detector):
    """
    Displays a real-time plot of the data stream with anomalies marked.

    Args:
        data (iterable): Data stream.
        detector (AnomalyDetector): Instance of the anomaly detector.
    """
    fig, ax = plt.subplots()
    x, y = [], []
    anomalies_x, anomalies_y = [], []

    def update(frame):
        value = data[frame]
        x.append(frame)
        y.append(value)

        if detector.detect(value):
            anomalies_x.append(frame)
            anomalies_y.append(value)

        ax.clear()
        ax.plot(x, y, label="Data Stream")
        ax.scatter(anomalies_x, anomalies_y, color="red", label="Anomalies")
        ax.set_title("Real-Time Anomaly Detection")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        ax.legend()

    ani = FuncAnimation(fig, update, frames=len(data), repeat=False)
    plt.show()
