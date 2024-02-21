# Import necessary modules
import pygame
from Cannon import Cannon
from CannonBall import CannonBall
from SpaceShip import SpaceShip

# Initialize Pygame modules
pygame.init()

# Set window dimensions
height = 500
width = 800

# Set up game window
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cannon Game")

# Load game images
cannon_Img = pygame.image.load("Cannon.png")
cannonBall_Img = pygame.image.load("CannonBall.png")
spaceShip_Img = pygame.image.load("SpaceShip.png")

# Lists to store game objects
gameObj = []
enemies = []

# Movement directions for enemies
directions = ['Left', 'Right', 'Down']

# Initialize cannon object
cannon = Cannon(cannon_Img, width/2, (height/2)+125)
gameObj.append(cannon)

# Velocities for different objects
cannon_vel = 10
cannonBall_vel = 8
spaceShip_vel = 5

# Number of cannonballs and maximum allowed
numBalls = 0
maxBalls = 8

# Index for cannon object in gameObj
cannonIndex = 0

# Time delay for firing cannonballs
timeSinceFire = 0
cooldown = 5

# Function to add enemies to the list
def spawnEnemies():
    total = 10
    x, y = 225, 50
    for _ in range(total):
        if _ % 5 == 0 and _ != 0:
            x, y = 225, y + (spaceShip_Img.get_height() * 1.5)
        if _ % 5 != 0:
            x += spaceShip_Img.get_width()
        saucer = SpaceShip(spaceShip_Img, x, y)
        enemies.append(saucer)

# Function to update positions and movements of enemies
def moveEnemy():
    for enemy in enemies:
        if way == directions[0]:
            enemy.x = enemy.moveLeft(win, spaceShip_vel)
        elif way == directions[1]:
            enemy.x = enemy.moveRight(win, spaceShip_vel)
        elif way == directions[2]:
            enemy.y = enemy.moveDown(win, spaceShip_vel)

# Function to check collision between cannonballs and enemies
def enemyCollision():
    global numBalls
    for i in range(len(gameObj)):
        if i != cannonIndex:
            for j in range(len(enemies)):
                if gameObj[i].rect.colliderect(enemies[j].rect):
                    del gameObj[i]
                    del enemies[j]
                    numBalls -= 1
                    return

# Function to clean up cannonballs going out of bounds
def cleanupBalls():
    i = 1
    while i < len(gameObj):
        if gameObj[i].rect.center[1] < -5:
            del gameObj[i]
        else:
            i += 1
    return len(gameObj) - 1

# Function to determine distance between two points
def distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# Main game loop
while True:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        break

    if keys[pygame.K_SPACE]:
        if timeSinceFire == 0 and numBalls < maxBalls:
            timeSinceFire = 5
            ball = CannonBall(cannonBall_Img, gameObj[cannonIndex].rect.midtop[0] - 10,
                              gameObj[cannonIndex].rect.midtop[1] - 50)
            gameObj.append(ball)
            numBalls += 1

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        win.fill((0, 0, 0))
        cannon.x = cannon.moveLeft(win, cannon_vel)

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        win.fill((0, 0, 0))
        cannon.x = cannon.moveRight(win, cannon_vel)

    launchBalls()
    moveEnemy()
    enemyCollision()
    blitGameObjImages()
    blitEnemies()
    updateGameObjRects()
    updateEnemyRect()
    numBalls = cleanupBalls()

    if timeSinceFire > 0:
        timeSinceFire -= 1

    pygame.display.update()

pygame.quit()
