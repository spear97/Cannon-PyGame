# Cannon Game

This is a simple cannon game implemented in Python using the Pygame library. The game features a cannon that can shoot cannonballs at enemy spaceships. The objective is to destroy all the enemy spaceships while avoiding their attacks.

## Installation
1. Make sure you have Python installed.
2. Install the Pygame library:
   ```bash
   pip install pygame
   ```
3. Clone this repository:
   ```bash
   git clone <repository_url>
   cd cannon-game
   ```
4. Run the game:
   ```bash
   python cannon_game.py
   ```
## How to Play
- Controls:
  - Use `A` or `LEFT ARROW` to move the cannon left.
  - Use `D` or `RIGHT ARROW` to move the cannon right.
  - Press `SPACE` to fire cannonballs.
  - Press `ESC` to exit the game.
- Objective:
  - Destroy all enemy spaceships by shooting them with cannonballs.
  - Avoid getting hit by enemy attacks.

 ## Game Mechanics

 ### Cannon
 - The cannon is controlled by the player.
 - It can move left (`A` or `LEFT ARROW`) and right (`D` or `RIGHT ARROW`).
 - The cannon shoots cannonballs towards the enemy spaceships.
   
 ### CannonBalls
 - Cannonballs are fired by the cannon.
 - They move upwards and disappear if they reach the top of the screen.
 - Maximum of 8 cannonballs can exist at a time.
   
 ### Enemy Spaceships
 - Enemy spaceships move across the screen from left to right, then down.
 - The player must shoot cannonballs to destroy them.
 - Colliding with an enemy spaceship ends the game.
   
 ### Score
 - Score is determined by the number of enemy spaceships destroyed.
 - The game ends when the player's cannon collides with an enemy spaceship or when all enemy spaceships are destroyed.

 # Files
 - `cannon_game.py`: Main Python script containing the game logic.
 - `Cannon.py`: Class for the player-controlled cannon.
 - `CannonBall.py`: Class for the cannonballs fired by the cannon.
 - `SpaceShip.py`: Class for the enemy spaceships.
