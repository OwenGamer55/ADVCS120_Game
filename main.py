import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import time

### CHECKLIST ### 
ChecklistValues = {
    "Pygame Window":False,
    "Player Sprite":False,
    "Active Keyboard Listener":False,
    "Sprite Movement (Left & Right)":False,
    "Sprite Collision":False,
    "Sprite Gravity":False,
    "Sprite Jump":False,
    "Tetris Grid (10 x 24)":False,
    "Tetris Sprites":False,
    "Tetris Interactions (Separating Inputs)":False,
    "Tetris Rotates":False,
    "Tetris Block Descent":False,
    "Tetris Speed Up":False,
    "Tetris Points":False,
    "Tetris Preview":False,
    "Tetris Line Clear":False,
    "Tetris Line Clear Fall":False,
    "Tetris Sudden Fall (Down Button)":False,
    "Player Destroy Block":False,
    "Player Shovel Sprite":False,
    "Player Shovel Ability Delay":False,
    "Tetris Sudden Fall Kill Prevention":False,
    "Tetris Isolated Block(s) Fall":False,
    "Frame Limit (60FPS)":False,
    "Player Death Animation":False,
    "Game Pause":False,
    "Game Menu":False,
    "Game Title & Title Screen":False,
    "Gameplay Pause After Player Death":False,
    "Timer To Next Bottom Layer Removal":False,
    "Player Death From Bottom Layer Removal":False,
    "Game Music":False,
    "Title Music":False}
### CHECKLIST ###

CompletedEntries = []
UncompletedEntries = []

def Checklist():
    for entry, status in ChecklistValues.items():
        if status:
            CompletedEntries.append(entry)
        elif not status:
            UncompletedEntries.append(entry)
    print("\033[1;31mUncompleted Tasks:\033[37;0m\n" 
      + (" • " + "\n • ".join(UncompletedEntries) if UncompletedEntries else "\033[1mNONE\033[0m")
      + "\n\n\033[1;32mCompleted Tasks:\033[37;0m\n" 
      + (" • " + "\n • ".join(CompletedEntries) if CompletedEntries else "\033[1mNONE\033[0m"))

Checklist()