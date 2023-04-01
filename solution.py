import pandas as pd
import numpy as np
from scipy.optimize import minimize


chat_id = 351730666 # Ваш chat ID, не меняйте название переменной


def likelihood_func(mu: float, x: np.array) -> float:
    n = len(x)
    return -n * np.log(mu) - np.sum(x) / mu


def solution(x: np.array) -> float:
    res = minimize(likelihood_func, x0=1, args=(x,), method='Nelder-Mead')
    return res.x[0]
