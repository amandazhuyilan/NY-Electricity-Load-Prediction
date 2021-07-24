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

    print("Loaded ", len(os.listdir('data')), "csv files")
    print("Loaded ", raw_data)
    return raw_data

def process_data(raw_data: np.ndarray) -> np.ndarray:
    processed_data = np.zeros([np.shape(raw_data)[0], 3], dtype=object)
    utc = pytz.utc
    eastern = pytz.timezone('US/Eastern')

    for idx, row in enumerate(raw_data):
        load_datetime = datetime.strptime(row[0].replace('"',''),  "%m/%d/%Y %H:%M:%S")
        load_datetime_eastern=eastern.localize(load_datetime, is_dst = None)
        load_datetime_utc = datetime.utcfromtimestamp(time.mktime(load_datetime.timetuple()))
        processed_data[idx] = [load_datetime_utc, row[1].replace('"', ''), row[2]]
    
    return processed_data

if __name__ == "__main__":
    raw_data_20011225 = load_one_day_data("20011225")
    process_data(raw_data_20011225)
    # load_all_data()
