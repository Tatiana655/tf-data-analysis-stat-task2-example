#import pandas as pd
import numpy as np

from scipy.stats import chi2


chat_id = 372005520 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 47
    alpha = 1 - p
    n = len(x)
    sum_x_2 = sum([e ** 2 for e in x])
    q_l = chi2(2 * n).ppf(q=alpha / 2)
    q_r = chi2(2 * n).ppf(q=1 - alpha / 2)
    return np.sqrt(sum_x_2 / q_r / t), np.sqrt(sum_x_2 / q_l / t)
