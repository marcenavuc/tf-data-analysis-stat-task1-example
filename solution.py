import pandas as pd
import numpy as np
from scipy.optimize import minimize


chat_id = 351730666 # Ваш chat ID, не меняйте название переменной


def solution(x: np.array) -> float:
    a = x / 10
    return np.mean(a) + 34
