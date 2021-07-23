#!/bin/python3

import numpy as np
import os

def load_all_data():
    """load the downloaded cvs files and return as numpy arrays"""
    for filename in os.scandir('data'):
        print("Processing: ", filename.name)
        raw_data = np.recfromcsv(filename,
                                 delimiter=',',
                                 case_sensitive=True,
                                 deletechars='',
                                 replace_space=' ')
    print("Loaded ", len(os.listdir('data')), "csv files")
    print("Loaded ", raw_data)
    return raw_data

if __name__ == "__main__":
    load_all_data()
