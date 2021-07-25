#!/bin/python3
import numpy as np
import os
import pytz
import time

from datetime import datetime

def load_data(filename) -> np.ndarray:
    return np.genfromtxt(filename,
                         usecols=(0, 2, 4),
                         encoding=None,
                         delimiter=',',
                         dtype=None,
                         case_sensitive=True,
                         autostrip=True,
                         replace_space=' ',
                         names=True,
                        )

def load_all_data() -> np.ndarray:
    """load the downloaded cvs files and return as numpy arrays"""
    for filename in os.scandir('data'):
        print("Processing: ", filename.name)
        raw_data += load_one_day_data(filename)
        
        return raw_data

def load_one_day_data(date: str) -> np.ndarray:
    """For a given date (format: "YYYYMMDD") starting from 2001/06/21,
    return the numpy arrays of the daily electricity load data."""

    for filename in os.scandir('data'):
        if date in filename.name:
            raw_data = load_data(filename)

    return raw_data

def process_data(raw_data: np.ndarray) -> np.ndarray:
    processed_data = np.zeros([np.shape(raw_data)[0], 3], dtype=object)
    # normalize the EDT and EST timezones to UTC 
    utc = pytz.utc
    eastern = pytz.timezone('US/Eastern')

    for idx, row in enumerate(raw_data):
        load_datetime = datetime.strptime(row[0].replace('"',''),  "%m/%d/%Y %H:%M:%S")
        load_datetime_eastern=eastern.localize(load_datetime, is_dst = None)
        load_datetime_utc = datetime.utcfromtimestamp(time.mktime(load_datetime.timetuple()))
        processed_data[idx] = [load_datetime_utc, row[1].replace('"', ''), row[2]]
    
    return processed_data


# perform normalization
def normalize_multi_feature(X):
    """ Normalizes the features in X
    
    returns a normalized version of X where
    the mean value of each feature is 0 and the standard deviation
    is 1. This is often a good preprocessing step to do when
    working with learning algorithms.
    """
    mu = np.zeros(len(X))
    sigma = np.zeros(len(X))
    for i, feature in enumerate(X.transpose()):
        if i == 0: continue
        mu_ = np.mean(feature)
        sigma_ = np.std(feature)
        mu[i] = mu_
        sigma[i] = sigma_
        X[:, i] = ((feature - mu_) / sigma_).T
        
    return X, mu, sigma

def gradient_descent_multi(X, y, theta, alpha, iterations):
    m = len(y)
    J_history = []
    for i in range(iterations):
        # here it won't work for datetime and strings
        theta = theta - ((alpha / m) * X.transpose() @ (X @ theta - y))
        J_history.append(float(cost_function(X, y, theta)))
    return theta, J_history

if __name__ == "__main__":
    raw_data_20011225 = load_one_day_data("20011225")
    processed_data = process_data(raw_data_20011225)
    X = processed_data[:,:3]    # input_feature
    y = processed_data[:, :-1]  # target
    # X, mu, sigma = normalize_multi_feature(X)
    
    alpha = 0.01
    iterations = 1500
    initial_theta = np.zeros(np.shape(processed_data))
    theta, J_history = gradient_descent_multi(X, y, initial_theta, alpha, iterations)
    