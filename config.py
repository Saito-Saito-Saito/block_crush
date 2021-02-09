#! usr/bin/env python3
# config.py

from logging import getLogger, StreamHandler, FileHandler, DEBUG, INFO, WARNING, ERROR, CRITICAL, Formatter
from math import *



### LOGGER SETUP
DEFAULT_LOG_ADDRESS = 'log.txt'
DEFAULT_LOG_FORMAT = Formatter('%(asctime)s - %(levelname)s - logger:%(name)s - %(filename)s - L%(lineno)d - %(funcName)s - %(message)s')

def loggerSet(name='default', *, level=DEBUG, filehandler=None, streamhandler=None, filehandlerLevel=DEBUG, streamhandlerLevel=WARNING, fileWritingMode='w', filename=DEFAULT_LOG_ADDRESS, filehandlerFormat=DEFAULT_LOG_FORMAT, streamhandlerFormat=DEFAULT_LOG_FORMAT):
    logger = getLogger(name)
    logger.setLevel = level

    # file handler
    fhandler = filehandler or FileHandler(filename, mode=fileWritingMode)
    fhandler.setLevel(filehandlerLevel)
    fhandler.setFormatter(filehandlerFormat)
    logger.addHandler(fhandler)

    # stream handler
    shandler = streamhandler or StreamHandler()
    shandler.setLevel(streamhandlerLevel)
    shandler.setFormatter(streamhandlerFormat)
    logger.addHandler(shandler)

    return logger


local_logger=loggerSet('config',filename='configLog.txt')



### CALCULATION CLASS AND FUNCTIONS
DIMENSION = 2

class Vector:
    def __init__(self, components, logger=None):
        self.components = components
        self.dimension = len(components)
        self.logger = logger or local_logger
        
    def invVecInstance(self):
        return Vector([-self.components[i] for i in range(self.dimension)])

    def absVecValue(self):
        ans = 0
        for i in range(self.dimension):
            ans += self.components[i]** 2
        return sqrt(ans)


    def addVecInstance(self, addition):
        # NOTE: input: addition must be an instance of Vector class
        # NOTE: output: returns an instance of Vector class
        if self.dimension != addition.dimension:
            self.logger.warning('DIMENSION IS NOT EQUAL')
        dimension = min(self.dimension, addition.dimension)
        return Vector([self.components[i] + addition.components[i] for i in range(dimension)])
        
    def subVecInstance(self, subtraction):
        # NOTE: input: subtraction has to be an instance of Vector class
        # NOTE: output: returns an instance of Vector class
        if self.dimension != subtraction.dimension:
            self.logger.warning('DIMENSION IS NOT EQUAL')
        return self.addVecInstance(subtraction.invVecInstance())

    def mulVecInstance(self, multiplier):
        # NOTE: output: returns an instance of Vector class 
        return Vector([multiplier * self.components[i] for i in range(self.dimension)])
        
    def dotProductValue(self, product):
        # NOTE: input: product have to be an instance of Vector class
        if self.dimension != product.dimension:
            self.logger.warning('DIMENSION IS NOT EQUAL')
        dimension = min(self.dimension, product.dimension)
        ans = 0
        for i in range(dimension):
            ans += self.components[i] * product.components[i]
        return ans

class ZeroVector(Vector):
    def __init__(self, dimension, logger=None):
        self.dimension = dimension
        self.components = [0] * dimension
        self.logger = local_logger

def distance(point1, point2):
    # NOTE: input: point1 and point2 have to be instances of Vector class
    return point1.subVecInstance(point2).absVecValue()


# game status
OVR = 0
PRC = 1
WIN = 2
END = -1
RDO = -2

X = 0
Y = 1

SCR_SIZ = (500, 600)
DEADLINE = SCR_SIZ[Y] * 0.8


BLL_R = 10
BLC_R = 15
PDL_SIZ = (50, 20)

RED = 0
GRN = 1
BLU = 2

BCG_COL = [0, 0, 0]
BLL_COL = (255, 255, 255)
PDL_COL = (122, 122, 122)
BLC_COL = (122, 122, 0)

INIT_V = (2, 2)
INIT_P_BLL = (100, 300)

LOAD_TIME = 6


if __name__ == "__main__":
    vec = Vector((0, 1, 1))
    print(vec.invVecInstance().components)
    print(vec.subVecInstance(Vector((2, 1, 1))).components)
    
    