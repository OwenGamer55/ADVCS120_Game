import pygame
import sys
import time

"""
Checklist:
Pygame_window
"""

Pygame_window = False

ChecklistEntries = {Pygame_window:"Pygame Window"}
CompletedEntries = []
UncompletedEntries = []


def Checklist():
    for entry in ChecklistEntries:
        if entry:
            CompletedEntries.append(entry)
        elif not entry:
            UncompletedEntries.append(entry)
    print(UncompletedEntries)

Checklist()