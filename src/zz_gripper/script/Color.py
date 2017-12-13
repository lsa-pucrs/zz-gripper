#!/usr/bin/env python
from enum import Enum

class Color(object):
	
	""" HSV Values """

	LOW_BLUE = [108, 100, 100]
	UPPER_BLUE = [128, 255, 255]
	LOW_RED = [169, 100, 100]
	UPPER_RED = [189, 255, 255]
	LOW_GREEN = [60, 100, 100]
	UPPER_GREEN = [80, 255, 255]
	LOW_ORANGE = [5, 100, 100]
	UPPER_ORANGE = [15, 255, 255]
	LOW_PURPLE = [140, 100, 100]
	UPPER_PURPLE = [160, 255, 255]
	LOW_YELLOW = [20, 100, 100]
	UPPER_YELLOW = [40, 255, 255]


	class __metaclass__(type):
		def __getattr__(self, name):
			return self.values.index(name)
	
