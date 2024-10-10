import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import sys
import time

### CHECKLIST ### 
ChecklistValues = {
    "Pygame Window":False,
    "Player Sprite":False}
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
      + (" • " + "\n • ".join(UncompletedEntries) if UncompletedEntries else "None")
      + "\n\n\033[1;32mCompleted Tasks:\033[37;0m\n" 
      + (" • " + "\n • ".join(CompletedEntries) if CompletedEntries else "\033[1mNONE\033[0m"))

Checklist()