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
import argparse
import logging

VERSION = "0.0.1"

# =============================================================================
# Initialize logger
# =============================================================================
def logger_setup():


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

    

if __name__ == "__main__":
    main()

