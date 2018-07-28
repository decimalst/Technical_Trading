# Technical trading script
# Written 3/12/2017
# Author: Byron Lambrou
# Import external Libraries
import numpy as np
import quandl
# Supporting functions
from technical_function import *

#this isn't a real API key
quandl.ApiConfig.api_key = "abcdefghijk"
mydata = quandl.get("FRED/GDP", returns="numpy", start_date="2001-12-31", end_date="2005-12-31")

meanAvg = runningMeanFast(mydata.value, len(mydata))