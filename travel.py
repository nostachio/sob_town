"""Travel.

Defines functions used for travel.
"""
import random
import json
import textwrap
from end_of_adventure import ready


def travel_hazards(hero_number, town_size):
    """Determine how many travel hazards occur."""
    hazards = 0
    print()
    print()
    print("Let's see how many travel hazards you encounter on the way to the ",
          town_size, "town.")
    print()
    if town_size == "small":
        print("Small town: hazard on a 1, 2, or 3.")
        print()
        for hero in range(1, hero_number + 1):
            roll = random.randrange(1, 6)
            print("Hero ", hero, "rolled a ", roll)
            if roll < 4:
                print("Added a hazard.")
                hazards += 1
                print("There are now ", hazards, " hazards.")
    if town_size == "medium":
        print("Medium town: hazards equal to heroes.")
        print()
        hazards = hero_number
    if town_size == "large":
        print("Large town: one hazard for each hero plus an additional hazard\
              for each hero on a 1, 2, or 3.")
        print()
        hazards = hero_number
        for hero in range(1, hero_number + 1):
            roll = random.randrange(1, 6)
            print("Hero ", hero, "rolled a ", roll)
            if roll < 4:
                print("Added a hazard.")
                hazards += 1
                print("There are now ", hazards, " hazards.")
    print()
    print()
    print("There are ", hazards, " total hazards.")
    with open("travel_hazards.json") as travel_hazards_json:
        travel_hazards = json.load(travel_hazards_json)
    for hazard in range(0, hazards):
        tens_roll = random.randrange(1, 6)
        ones_roll = random.randrange(1, 6)
        hazard_roll = str(tens_roll) + str(ones_roll)
        print("Hazard Chart roll:", hazard_roll)
        print('*' * 80)
        print(textwrap.fill(travel_hazards[hazard_roll]['title'], 80))
        print()
        print(textwrap.fill(travel_hazards[hazard_roll]['flavor_text'], 80))
        print()
        print(textwrap.fill(travel_hazards[hazard_roll]['effect_text'], 80))
        print('*' * 80)
        print("There are ", (hazards - hazard) - 1, " hazards left.")
        ready()
    return


def travel_to_town():
    """Deal with traveling to town."""
    print("How many heroes are there?")
    while True:
        try:
            heroes = int(input())
        except ValueError:
            print("Please enter a number from 1 to 6.")
            continue
        if heroes < 1 or heroes > 6:
            print("Please enter a number from 1 to 6.")
            continue
        else:
            break
    print("What size town are you going to? [small/medium/large]")
    while True:
        size = str(input())
        if size != "small" and size != "medium" and size != "large":
            print("Please enter only small, medium, or large.")
            continue
        else:
            break
    travel_hazards(heroes, size)
    return size
