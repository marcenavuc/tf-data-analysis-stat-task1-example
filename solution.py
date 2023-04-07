import pandas as pd
import numpy as np
from scipy.optimize import minimize


chat_id = 351730666 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    p = len(x)
    diff_distances = np.abs(np.diff(x))
    a = (1/p) * np.sum(diff_distances) / 10
    return a