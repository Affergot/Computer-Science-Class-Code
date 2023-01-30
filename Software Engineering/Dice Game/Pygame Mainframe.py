import random
import pygame

pygame.init()
##Initializes screen, sets size, caption, timer, font, and colors. 
##Also creates variables for white and black.
WIDTH = 600
HEIGHT = 800
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Yahtzee")
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 18)
background = (128, 128, 128)
white = (255, 255, 255)
black = (0, 0, 0)
numbers = [0, 0, 0, 0, 0,]
roll = False


class Dice:
    def __init__(self, x_pos, y_pos, number, key):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.number = number
        self.key = key
        self.die = ''
    ##Draw function that draws each die.    
    def draw(self):
        self.die = pygame.draw.rect(screen, white, [self.x_pos, self.y_pos, 100, 100], 0, 5)
        if self.number == 1:
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
        if self.number == 2:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 3:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
        if self.number == 4:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)
        if self.number == 5:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 50, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)    
        if self.number == 6:
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 20), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 20, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 80), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 50), 10)
            pygame.draw.circle(screen, black, (self.x_pos + 80, self.y_pos + 20), 10)


running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    ##Draws 5 Die at top of screen
    die1 = Dice(10, 50, numbers[0], 0)
    die2 = Dice(130, 50, numbers[1], 1)
    die3 = Dice(250, 50, numbers[2], 2)
    die4 = Dice(370, 50, numbers[3], 3)
    die5 = Dice(490, 50, numbers[4], 4)
    roll_button = pygame.draw.rect(screen, black, [160, 160, 280, 30])
    roll_text = font.render("Click To Roll", True, white)
    screen.blit(roll_text, (240, 165))
    die1.draw()
    die2.draw()
    die3.draw()
    die4.draw()
    die5.draw()
    ##Event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        ##Button rolls dice if clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if roll_button.collidepoint(event.pos):
                roll = True
    
    if roll: 
        for number in range(len(numbers)):
            numbers[number] = random.randint(1, 6)
        roll = False      
        
           
    pygame.display.flip()
pygame.quit()