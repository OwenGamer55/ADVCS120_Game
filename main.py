import pygame
import sys
import time

print("Hi")

"""
Checklist:
"""

Pygame_window = False
ChecklistEntries = [Pygame_window]
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