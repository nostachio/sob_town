"""Display.

Functions related to displaying the town.
"""
import os


def display_town(locations, town_text, type, events):
    """Display the town."""
    os.system('clear')
    print()
    print(type)
    print()
    print(events)
    print()
    print("Locations:")
    print()
    for i in locations:
        print('\n'.join(map(str, i)))
    print("Campsite (always present, does not take a location)")
    print("")
    print("Special Rules:")
    for t in town_text:
        print(t)
    return
