import pandas as pd
import numpy as np
import scipy.stats as stat
from scipy.stats import norm


chat_id = 372005520 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t = 47
    alpha = 1 - p
    a = 2*x/t**2
    # stat.erlang.ppf(p, n, loc=0, scale=1/n).
    loc = a.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    n=len(x)
    return loc - stat.erlang.ppf(1 - alpha / 2,n,loc=0, scale=1/n ), \
           loc - stat.erlang.ppf(alpha / 2,n,loc=0, scale=1/n)
