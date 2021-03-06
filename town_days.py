"""Days.

Defines functions for each day in town.
"""
import random
import sys
import textwrap
import json


def initialize_daily_event_deck():
    """Set deck to initial deck."""
    with open("daily_events.json") as daily_event_deck_json:
        initialized_event_deck = json.load(daily_event_deck_json)
    return initialized_event_deck


def day_in_town_end(days_since_last_event):
    """Check for town event."""
    roll = random.randrange(1, 6)
    print("Days since last event:", days_since_last_event)
    print("Town event roll is", roll)
    if roll <= days_since_last_event:
        days_since_last_event = 1
        print("A town event happens!")
        event_roll = random.randrange(2, 12)
        print("The event roll is", event_roll)
        print('*' * 80)
        with open("town_events.json") as town_events_table:
            event_table = json.load(town_events_table)
        for x in range(0, len(event_table)):
            if event_roll in event_table[x]["roll"]:
                print(textwrap.fill(event_table[x]["title"], 80))
                print()
                print(textwrap.fill(event_table[x]["flavor_text"], 80))
                print()
                print(textwrap.fill(event_table[x]["effect_text"], 80))
                print()
                break
        # print(textwrap.dedent(event_table[event_roll]))
        print('*' * 80)
        input("Press enter when ready for the next day.")
    else:
        days_since_last_event += 1
    return days_since_last_event


def draw_daily_event(daily_event_deck, town_type):
    """Draw a daily event."""
    if len(daily_event_deck) == 0:
        daily_event_deck = initialize_daily_event_deck()
    event = random.sample(daily_event_deck, 1)
    if town_type != "Standard Frontier Town" and \
            event[0]['title'] == "Just another day on the frontier":
        with open("town_type.json") as town_type_json:
            town_type_table = json.load(town_type_json)
        event_roll = random.randrange(1, 6)
        for x in town_type_table[0]:
            if town_type_table[x]['name'] == town_type:
                event_chart = town_type_table[x]['town_type_daily_events']
                for y in event_chart[0]:
                    if event_chart[y]['roll'] == event_roll:
                        event = event_chart[y]
    return event[0], daily_event_deck


def day_in_town_start(daily_event_deck, town_type):
    """Draw Daily events."""
    print("Daily Event:")
    events = []
    new_event, daily_event_deck = draw_daily_event(daily_event_deck, town_type)
    events.append(new_event)
    if town_type == "Rail Town":
        new_event, daily_event_deck = draw_daily_event(daily_event_deck,
                                                       town_type)
        events.append(new_event)
    return daily_event_deck, events


def end_of_day_prompt(days_since_last_event):
    """Prompt before rolling end of day event."""
    print("If a hero is Wanted or Most Wanted, be sure to roll as per the\
     card")
    print()
    quit = input("Press enter when the day is over.  Type quit to exit.")
    if quit == "quit":
        sys.exit
    days_since_last_event = day_in_town_end(days_since_last_event)
    return days_since_last_event
#
# Set darkness tracker on 1 on Days Since Last Event
#
# OMG this went late and we need to be done
# No travel hazards, small standard town, 4 locations, each hero chooses 1.
#
#
# Time in town (repeat until all heroes have left town)
# Draw Daily Event Card
# Just Another Day cards drawn in a non-standard town cause a roll on the
# town's Event Chart
# Stay in Hotel or Campsite
# Hotel: pay $10
# Campsite: roll on the Campsite Hazard chart
# Choose location to visit (may include the campsite)
# Roll on the location's event chart
# Do your business
# End of day
# Roll a d6.
# If the roll is higher than Days Since Last Event position, move the counter
# up one.
# If the roll is lower or equal to Days Since Last Event position, move the
# counter back to 1 and roll on the Town Event Chart
# If any heroes leave town, remove them from the town board.
