import tkinter as tk
import random

# Game constants
GAME_WIDTH = 600
GAME_HEIGHT = 400
SNAKE_SIZE = 10
SNAKE_SPEED = 100
FOOD_SIZE = 10
BACKGROUND_COLOR = "black"
SNAKE_COLOR = "green"
FOOD_COLOR = "red"

# Initialize game variables
snake = [(100, 100), (90, 100), (80, 100)]  # Initial snake position
direction = "Right"  # Initial direction
food = (0, 0)  # Initial food position
score = 0

# Create the main window
window = tk.Tk()
window.title("Snake Game")
window.resizable(False, False)

# Create the canvas
canvas = tk.Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT, bg=BACKGROUND_COLOR)
canvas.pack()
