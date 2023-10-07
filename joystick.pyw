# Autor : Samuel Vidal Roberto
# Data de criação ; 03/04/2023
# Descrição : aplicação simples para automação de mouse com uso de um joystick

import pygame
import pyautogui as pa
from math import ceil as c

pygame.joystick.init()

joys = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

print(joys)

x, y = pa.position()

v = 10

pygame.init()
pygame.time.Clock()

while True:
    x, y = pa.position()
    
    for events in pygame.event.get():
        
        
        if events.type == pygame.JOYBUTTONDOWN:
            if events.button == 2:
                v += 5
            if events.button == 0:
                v -= 5
            if events.button == 3:
                pa.click()
            if events.button == 4:
                
                x, y = pa.size()
                x = x/2
                y = y/2
            if events.button == 5:
                pygame.quit()
                exit()

            print(events)
        if events.type == pygame.JOYAXISMOTION:
            
            
            if events.axis == 1 and c(events.value) == -1.0:

                y = y - v
                
                pa.moveTo(x, y)
                
            elif events.axis == 1 and c(events.value) == 1.0:

                y = y + v
                
                pa.moveTo(x, y)
                
            elif events.axis == 0  and c(events.value) == 1.0:

                x = x + v
                
                pa.moveTo(x, y)
                
            elif events.axis == 0 and c(events.value) == -1.0:

                x = x - v
                
                pa.moveTo(x, y)
                
            
            
            

            else:
                pass

            #pa.move_to()"""
    
