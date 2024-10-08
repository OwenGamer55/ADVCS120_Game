import pygame
import sys
import time

print("Hi")

"""
Checklist:
"""

ChecklistEntries = ["Pygame_window"]
CompletedEntries = []
UncompletedEntries = []
Pygame_window = False


def Checklist():
    for entry in ChecklistEntries:
        if entry:
            CompletedEntries.append(entry)
        elif not entry:
            UncompletedEntries.append(entry)
    print(UncompletedEntries)

Checklist()