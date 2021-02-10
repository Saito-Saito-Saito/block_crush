#! usr/bin/env python3
# io.py

from config import *
import structures
import pygame
from pygame.locals import *
import sys

def startmenu():
    # building the screen
    pygame.init()
    screen = pygame.display.set_mode(SCR_SIZ)
    pygame.display.set_caption("BLOCK CRUSH")
        
    button = pygame.Rect(SCR_SIZ[X] / 2 - 100, SCR_SIZ[Y] / 2 - 50, 200, 100)
    font55 = pygame.font.Font(None, 55)

    # start menu
    while True:
        # displaying setting
        screen.fill(BCG_COL)
        pygame.draw.rect(screen, (255, 255, 255), button, 2)
        text55 = font55.render("START", True, (0, 255, 0))
        screen.blit(text55, (SCR_SIZ[X] / 2 - 65, SCR_SIZ[Y] / 2 - 15))

        # events
        for event in pygame.event.get():
            # exit
            if event.type == QUIT:
                pygame.quit()
                bullet = 0
                return END
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    bullet = 0
                    return END
                # start
                if event.key == K_RETURN:
                    break
            if event.type == MOUSEBUTTONDOWN:
                if button.collidepoint(event.pos):
                    break
        # in case of no events
        else:
            pygame.display.update()
            pygame.time.wait(LOAD_TIME)
            continue
        # in case of start
        pygame.quit()
        break


def display(status, bullet=structures.Bullet(INIT_P_BLL), blocks = [structures.Block((SCR_SIZ[X] * ((i + 1) % 5) / 5, SCR_SIZ[Y] * 0.3)) for i in range(4)]):
    # building the screen
    pygame.init()
    screen = pygame.display.set_mode(SCR_SIZ)
    pygame.display.set_caption("BLOCK CRUSH")
    font55 = pygame.font.Font(None, 55)
    font33 = pygame.font.Font(None, 33)
            

    paddle = structures.Paddle(pygame.mouse.get_pos())
    

    while True:
        # game over
        if bullet.p.components[Y] > DEADLINE and status == PRC:
            return OVR, bullet
        # game clear
        if len(blocks) == 0 and status == PRC:
            return WIN, bullet

        # background
        screen.fill(BCG_COL)

        # bullet
        bullet.move()
        pygame.draw.circle(screen, BLL_COL, bullet.p.components, BLL_R)

        # paddle
        paddle.p = Vector((pygame.mouse.get_pos()[X], SCR_SIZ[Y] * 0.8))
        pygame.draw.rect(screen, paddle.colour, (paddle.p.components[X] - paddle.size[X] / 2, paddle.p.components[Y] - paddle.size[Y] / 2, paddle.size[X], paddle.size[Y]))
        pygame.draw.circle(screen, paddle.colour, (paddle.p.components[X] - paddle.size[X] / 2, paddle.p.components[Y]), paddle.size[Y] / 2)
        pygame.draw.circle(screen, paddle.colour, (paddle.p.components[X] + paddle.size[X] / 2, paddle.p.components[Y]), paddle.size[Y] / 2)
        # bouncing on top
        if paddle.p.components[X] - paddle.size[X] / 2 <= bullet.p.components[X] <= paddle.p.components[X] + paddle.size[X] / 2 and paddle.p.components[Y] - paddle.size[Y] / 2 <= bullet.p.components[Y] + bullet.r <= paddle.p.components[Y] + paddle.size[Y] / 2:
            bullet.reflect(Vector((0, -1)))
        # bouncing on bottom
        if paddle.p.components[X] - paddle.size[X] / 2 <= bullet.p.components[X] <= paddle.p.components[X] + paddle.size[X] / 2 and paddle.p.components[Y] - paddle.size[Y] / 2 <= bullet.p.components[Y] - bullet.r <= paddle.p.components[Y] + paddle.size[Y] / 2:
            bullet.reflect(Vector((0, 1)))
        # bouncing on left
        if distance(bullet.p, paddle.p.addVecInstance(Vector((-paddle.size[X] / 2, 0)))) <= bullet.r + paddle.size[Y] / 2:
            bullet.reflect(bullet.p.subVecInstance(paddle.p.addVecInstance(Vector((-paddle.size[X] / 2, 0)))))
        # bouncing on right
        if distance(bullet.p, paddle.p.addVecInstance(Vector((paddle.size[X] / 2, 0)))) <= bullet.r + paddle.size[Y] / 2:
            bullet.reflect(bullet.p.subVecInstance(paddle.p.addVecInstance(Vector((paddle.size[X] / 2, 0)))))
        

        # blocks (in status PRC)
        if status == PRC:    
            for a_block in blocks:
                pygame.draw.circle(screen, a_block.colour, a_block.p.components, BLC_R)
                # bouncing
                if distance(bullet.p, a_block.p) < bullet.r + a_block.r:
                    bullet.reflect(bullet.p.addVecInstance(a_block.p.invVecInstance()))
                    blocks.remove(a_block)

        # bouncing at wall
        if bullet.p.components[X] > SCR_SIZ[X] - BLL_R:
            bullet.reflect(Vector((-1, 0)))
        if bullet.p.components[X] < BLL_R:
            bullet.reflect(Vector((1, 0)))
        if bullet.p.components[Y] < BLL_R:
            bullet.reflect(Vector((0, 1)))
        if bullet.p.components[Y] > SCR_SIZ[Y] - BLL_R:
            bullet.reflect(Vector((0, -1)))

        # OVR
        if status == OVR:
            text55 = font55.render("GAME OVER", True, (255, 0, 0))
            screen.blit(text55, (SCR_SIZ[X] / 2 - 100, SCR_SIZ[Y] / 2 - 22))
            button = pygame.Rect(SCR_SIZ[X] / 2 - 60, SCR_SIZ[Y] / 2 + 45, 120, 50)
            pygame.draw.rect(screen, (255, 255, 255), button, 2)
            text33 = font33.render("RESTART", True, (255, 0, 0))
            screen.blit(text33, (SCR_SIZ[X] / 2 - 50, SCR_SIZ[Y] / 2 + 60))
        # WIN
        if status == WIN:
            text55 = font55.render("YOU WIN", True, (0, 255, 0))
            screen.blit(text55, (SCR_SIZ[X] / 2 - 80, SCR_SIZ[Y] / 2 - 22))
            button = pygame.Rect(SCR_SIZ[X] / 2 - 60, SCR_SIZ[Y] / 2 + 45, 120, 50)
            pygame.draw.rect(screen, (255, 255, 255), button, 2)
            text33 = font33.render("RESTART", True, (0, 255, 0))
            screen.blit(text33, (SCR_SIZ[X] / 2 - 50, SCR_SIZ[Y] / 2 + 60))
            
            

        # exit
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return END, bullet
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    return END, bullet
                if event.key == K_RETURN and status != PRC:
                    return RDO
            if event.type == MOUSEBUTTONDOWN and status != PRC:
                if button.collidepoint(event.pos):
                    return RDO

        
        pygame.display.update()
        pygame.time.wait(LOAD_TIME)



if __name__ == "__main__":
    status, bullet = display(PRC)
    if status == END:
        pygame.quit
    else:
        display(status, bullet)
        