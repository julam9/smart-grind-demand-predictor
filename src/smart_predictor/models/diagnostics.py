import matplotlib.pyplot as plt
import numpy as np

def plot_residuals(y_true, y_pred, dates=None, title="Residual Plot"):
    residuals = y_true - y_pred

    plt.figure()
    plt.scatter(y_pred, residuals)
    plt.axhline(0)
    plt.xlabel("Predicted")
    plt.ylabel("Residual")
    plt.title(title)
    plt.show()

def plot_residuals_over_time(y_true, y_pred, dates, title="Residuals Over Time"):
    residuals = y_true - y_pred

    plt.figure()
    plt.plot(dates, residuals)
    plt.axhline(0)
    plt.xlabel("Date")
    plt.ylabel("Residual")
    plt.title(title)
    plt.xticks(rotation=45)
    plt.show()