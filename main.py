#! usr/bin/env python3
# main.py

from config import *
import IO
import pygame
from pygame.locals import *
import structures

local_logger = loggerSet(name='main', filename='mainLog.txt', fileWritingMode='a')

def main():
    while True:
        # start menu
        if IO.startmenu() == END:
            return 


        # placements of blocks
        blocks = []
        for i in range(5 - 1):
            for j in range(13 - 1):
                blocks.append(structures.Block((SCR_SIZ[X] * ((j + 1) % 13) / 13, SCR_SIZ[Y] * 0.1 * (i + 1))))


        # game start
        status, bullet = IO.display(PRC, bullet=structures.Bullet(INIT_P_BLL), blocks=blocks)


        # after game
        # in case of end
        if status == END:
            pygame.quit()
            return
        if IO.display(status, bullet=bullet) == RDO:
            pass
        else:
            pygame.quit()
            break
        
if __name__ == "__main__":
    main()