#! usr/bin/env python3
# ball.py

from config import *

local_logger=loggerSet(name='structure',filename='structureLog.txt')

class Bullet:
    def __init__(self, p_components, v_components=INIT_V, r=BLL_R):
        if len(p_components) != len(v_components):
            local_logger.warning('DIMENSION OF P AND V IS NOT EQUAL')
        self.dimension = min(len(p_components), len(v_components))
        self.p = Vector([p_components[i] for i in range(self.dimension)])
        self.v = Vector([v_components[i] for i in range(self.dimension)])
        self.r = r

    def move(self):
        self.p = self.p.addVecInstance(self.v)

    def reflect(self, normal_vec):
        # NOTE: normal_vec has to be an instance of Vector class
        # unitizing the normal vector
        normal_vec = normal_vec.mulVecInstance(1 / normal_vec.absVecValue())
        # if v is along n, you do not have to change v
        if self.v.dotProductValue(normal_vec) < 0:
            # new v = v - 2(n*v)n, so first calculating 2(n*v)n as sub
            sub = normal_vec.mulVecInstance(2 * self.v.dotProductValue(normal_vec))
            # new v = v + (-sub)
            self.v = self.v.subVecInstance(sub)
    
class Paddle:
    def __init__(self, p_components, size=PDL_SIZ, colour=PDL_COL):
        # p at centre of the rectangle
        self.p = Vector(p_components)
        # rectangle size
        self.size = PDL_SIZ
        # colour
        self.colour = colour
        
        
class Block:
    def __init__(self, p_components, colour=BLC_COL, radius=BLC_R):
        self.p = Vector(p_components)
        self.colour = colour
        self.r = radius


def perpendicularFoot(point, edges):
    # NOTE: input: point is an instance of Vector class
    # NOTE: input: edges is a list of instances of Vector class
    # NOTE: output: returns an instance of Vector class to show the position vector
    # direction vector of the line
    n = edges[1].addVecInstance(edges[0].invVecInstance())
    # unitizing n
    n = n.mulVecInstance(1 / n.absVecValue())
    # foot = a + ((a - p)*n)n
    foot = edges[0].addVecInstance(n.mulVecInstance(edges[0].subVecInstance(point).dotProductValue(n)))
    return foot
   


if __name__ == "__main__":
    bullet = Bullet([1, 1], [1, 1])
    paddle = Paddle((10, 10))
