#! usr/bin/env python3
# main.py

from config import *
import IO
import pygame
from pygame.locals import *
import structures



def main():
    while True:
        # building the screen
        pygame.init()
        screen = pygame.display.set_mode(SCR_SIZ)
        pygame.display.set_caption("BLOCK CRUSH")
        font55 = pygame.font.Font(None, 55)
        text55 = font55.render("ENTRE TO START", True, (0, 255, 0))
        # start menu
        while True:
            screen.fill(BCG_COL)
            screen.blit(text55, (SCR_SIZ[X] / 2 - 100, SCR_SIZ[Y] / 2 - 22))
            # exit
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    return END, bullet
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return END, bullet
                    if event.key == K_RETURN:
                        break
            else:
                pygame.display.update()
                pygame.time.wait(LOAD_TIME)
                continue
            break

        blocks = []
        for i in range(5 - 1):
            for j in range(13 - 1):
                blocks.append(structures.Block((SCR_SIZ[X] * ((j + 1) % 13) / 13, SCR_SIZ[Y] * 0.1 * (i + 1))))
        status, bullet = IO.display(PRC, bullet=structures.Bullet(INIT_P_BLL), blocks=blocks)
        if status == END:
            pygame.quit()
        if IO.display(status, bullet=bullet) != RDO:
            break
        
if __name__ == "__main__":
    main()