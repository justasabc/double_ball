#!usr/bin/python
# encoding: utf-8
"""
file: version.py
This file contains version info of this app.
"""

__all__ = ['__app__','__version__','version','app_name']

__app__ = "Double Ball History Data Queryer"
__version__ = "0.1.0"
__author__ = "zunlin ke, justasabc"
__copyright__ = "(C) 2014 justasabc. GNU GPL 3."
__contributors__ = ['justasabc','zunlin ke']

def app_name():
	return __app__

def version():
	return __version__


