import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 372005520 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 47
    alpha = 1 - p
    a = 2*x/t**2
    loc = a.mean()+0.5
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
