#!/usr/bin/env python3
# =============================================================================
# filenams  : ESP32_parser.py
# Purpose   : parsing the data from ESP32 log file to time series csv file
# Author    : JohnsonCL Chen (johnson35762@gmail.com)
# =============================================================================

# =============================================================================
# Import required modules
# =============================================================================
import os
import matplotlib.pyplot as plt
import argparse
import logging
import scipy
import numpy as np

VERSION = "0.0.1"
FILE_NAME = "adc_value_sample.log"
# =============================================================================
# Initialize logger
# =============================================================================
def logger_setup():
    """setup logger"""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    return logger

def plotter_data_from_file(file_name: str):
    """plotter the data from file"""
    logger = logger_setup()
    logger.info(f"plotter_data_from_file: {file_name}")
    if not os.path.exists(file_name):
        logger.error(f"file not found: {file_name}")
        return
    with open(file_name, "r") as f:
        data = [line.strip() for line in f.readlines()]
    logger.info(f"read data from file: {file_name}")
    logger.info(f"data: {data}")
    data = [line.split(": ") for line in data]
    x = []
    y = []
    for element in data:
            x.append(int(element[0]))
            y.append(int(element[1]))

    mean_y = scipy.ndimage.uniform_filter1d(y, size=30)
    mean_y = np.pad(mean_y, (0, len(y) - len(mean_y)), 'constant')
    
    logger.info(f"mean y (padded): {mean_y}")
    logger.info(f"x: {x} \n")
    logger.info(f"x: {x} \n")
    logger.info(f"y: {y} \n")
    plt.grid(True)
    plt.plot(x,y, label = "raw")
    plt.plot(x, mean_y, label = "mean")
    plt.title("ESP32 ADC value")
    plt.xlabel("Time")
    plt.ylabel("ADC value")
    plt.show()

# =============================================================================
# argument parser setup
# =============================================================================
def parse_options(version: str = "0.0.1"):
    """argparser setup for ESP32_parser.py"""
    description = "parse ESP32 logged data to time series csv file"

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {version}")
    parser.add_argument("-i", "--input", type=str, help="input file name")
    parser.add_argument("-d", "--datatype", type=str, help="data type")
    parser.add_argument("-h", "--help", action="help", help="show this help message and exit")
    options = parser.parse_args()
    return parser, options
    
    
def main():
    plotter_data_from_file(FILE_NAME)
    

if __name__ == "__main__":
    main()

