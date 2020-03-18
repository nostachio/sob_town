"""Travel.

Defines functions used for travel.
"""
import random
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
    print("See Frontier Town Adventure Book pp. 19-22 for the rolling chart.")
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
