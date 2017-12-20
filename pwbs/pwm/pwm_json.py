#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""PAiP Web Module - JSON

This module creates function to read and write JSON.

NAME - PAiP Web Module - JSON
AUTHOR - Patryk Adamczyk <patrykadamczyk@paip.com.pl>
LICENSE - MIT
VERSION - v.0.0.0.3
"""
### Imports
import os
import json
### Functions

def read_json(filename):
    """Function to read data from json file
    Args:
        filename (object): File Name

    Returns:
        :obj:`str`: Returning Data from JSON file
    """
    dane = {}
    if os.path.isfile(filename):
        with open(filename, "r") as plik:
            dane = json.load(plik)
    return dane

def write_json(filename, data):
    """Function to write data to json file
    Args:
        filename (object): File Name
        data (object): Data

    Returns:
        :obj:`str`: Returning Data from JSON file
    """
    with open(filename, "w") as plik:
        json.dump(data, plik)
    return True

class JSON_IO(object):
    """JSON Input Output Class [Alternative to functions]

    Attributes:
        filename (object): File name
        data (object): data

    """
    def __init__(self, filename):
        """Init Method

        Constractor of class
        Args:
            filename (object): File name
        """
        self.filename = filename
        self.read()
    def read(self):
        """Reading File
        Returns:
            Data from file
        """
        self.data = read_json(self.filename)
        return self.data
    def write(self, newdata):
        """Writing to File
        Args:
            newdata: New Data which you want to be overwrite to file
        Returns:
            Data from file
        """
        write_json(self.filename, newdata)
        return self.read()
