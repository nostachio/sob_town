"""Display.

Functions related to displaying the town.
"""
import os


def display_daily_events(events):
    """Display daily town events."""
    print('*' * 80)
    print("Daily Events")
    print('*' * 80)
    for x in range(0, len(events)):
        print(events[x]['title'])
        print(events[x]['flavor_text'])
        print(events[x]['effect_text'])
        print('*' * 80)



def display_town(locations, town_text, type, events):
    """Display the town."""
    os.system('clear')
    print()
    print(type)
    print()
    display_daily_events(events)
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
