"""Display.

Functions related to displaying the town.
"""
import os
import json


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


def get_town_details(town_type):
    """Display details for town type."""
    with open("town_type.json") as town_type_json:
        town_type_details = json.load(town_type_json)
    for x in range(0, len(town_type_details)):
        if town_type_details[x]['name'] == town_type:
            tags = town_type_details[x]['tags']
            flavor_text = town_type_details[x]['flavor_text']
            special_rules = town_type_details[x]['special_rules']
            extra_options = town_type_details[x]['extra_options']
    return tags, flavor_text, special_rules, extra_options


def print_town_details(tags, flavor_text, special_rules, extra_options):
    """Print details about the town."""
    print("Tags:", tags)
    print(flavor_text)
    for x in special_rules:
        print(x['title'])
        print(x['effect_text'])
        print()
    if len(extra_options) > 0:
        print("Extra Options:")
        print()
        for y in extra_options:
            print(y['title'])
            print(y['text'])
            print()


def display_town(locations, town_text, type, events):
    """Display the town."""
    os.system('clear')
    print(type)
    tags, flavor_text, special_rules, extra_options = get_town_details(type)
    print_town_details(tags, flavor_text, special_rules, extra_options)
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
