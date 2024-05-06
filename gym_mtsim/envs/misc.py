import numpy as np


def make_log_normal_parameter(mean: float, stddev: float):
    mu = np.log(mean ** 2 / np.sqrt(mean ** 2 + stddev ** 2))
    sigma = np.sqrt(np.log1p((stddev / mean) ** 2))
    return mu, sigma

