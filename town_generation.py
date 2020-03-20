"""Generation.

These functions are used to generate a town.
"""
import random


town_type_array = {2: "Town Ruins",
                   3: "Haunted Town",
                   4: "Plague Town",
                   5: "Rail Town",
                   6: "Standard Frontier Town",
                   7: "Standard Frontier Town",
                   8: "Standard Frontier Town",
                   9: "Mining Town",
                   10: "River Town",
                   11: "Mutant Town",
                   12: "Outlaw Town",
                   }
possible_town_locations = ["Blacksmith",
                           "Frontier Outpost",
                           "Church",
                           "Doc's Office",
                           "General Store",
                           "Smuggler's Den",
                           "Gambling Hall",
                           "Guard House",
                           "House of Healing",
                           "Mutant Quarter",
                           "Sheriff's Office",
                           "Shrine",
                           "Street Market",
                           "Swordsmith",
                           "Tavern",
                           "Village Market",
                           "Indian Trading Post",
                           "Saloon Post",
                           ]


def town_spaces(town_size):
    """Define the number of spaces for a town of a particular size."""
    if town_size == "small":
        spaces_available = 4
    if town_size == "medium":
        spaces_available = 6
    if town_size == "large":
        spaces_available = 8
    return spaces_available


def town_type():
    """Determine town type by rolling 2d6 against a table."""
    die_1 = random.randrange(1, 6)
    die_2 = random.randrange(1, 6)
    dice_total = die_1 + die_2
    print("Town type:")
    print("Dice rolled: ", die_1, " and ", die_2, ", ", dice_total)
    town_type_name = town_type_array[dice_total]
    print("The town type is " + town_type_name)
    print()
    print()
    return town_type_name


def town_special_effects(town_type_name):
    """Create special text to display in interface for each town type."""
    text = []
    if town_type_name == "Mining Town":
        text.append("Well Supplied: Everything at the General Store is $25\
        less (to a minimum of $25)")
        text.append("Rich Local Deposits: The mines in this area are booming. \
        During the next Adventure, while in the Mines, any time a hero finds g\
        old, they gain +$10 extra, and any time a hero finds Dark Stone, they \
        gain 1 extra shard.")
        text.append("VOID ACTIVITY: The massive boom of local mining has uncov\
        ered countless new portals, releasing all manner of creatures and evil\
         to find their way to the surface!  When rolling to see if there is a \
         TOWN EVENT, roll an extra die.  Either roll may trigger a TOWN EVENT \
         (or both).")
        text.append("PURCHASE DARK STONE: Heroes may purchase DARK STONE shard\
        s for $150 each.")
        text.append("MINING TOOLS: Additional items available at the GENERAL \
        STORE.")
    if town_type_name == "Haunted Town":
        text.append("ANGRY GHOSTS")
        text.append("BREAKING THE CURSE")
        text.append("BUY CURSED ARTIFACTS")
    if town_type_name == "Outlaw Town":
        text.append("LAWLESS")
        text.append("Scum and Villainy")
        text.append("Rescue a Kidnapping Victim")
        text.append("Highly Illegal Ammo")
    if town_type_name == "Town Ruins":
        text.append("Rubble and Ruin")
        text.append("Help to Rebuild")
        text.append("Search the Rubble")
    if town_type_name == "Rail Town":
        text.append("Fresh Supplies")
        text.append("Hustle and Bustle")
        text.append("Rail Travel")
        text.append("Send a telegraph")
        text.append("Rob the train")
    if town_type_name == "Plague Town":
        text.append("Keep Your Distance")
        text.append("The Plague")
        text.append("Tend to the Sick")
        text.append("Experimental Medical Supplies")
    if town_type_name == "Mutant Town":
        text.append("Distrust")
        text.append("Something in the Water")
        text.append("Go to Work on the Cut")
        text.append("Railworker Supplies")
    if town_type_name == "River Town":
        text.append("Wealthy Town")
        text.append("River Travel")
        text.append("Find work on the Docks")
        text.append("Black Market Alley")
    if town_type_name == "Standard Frontier Town":
        text.append("None")
    return text


def town_location_adjustment(town_type_name):
    """Make a list of required locations."""
    mandatory_town_locations = []
    if town_type_name == "Mining Town":
        mandatory_town_locations.append("General Store")
        possible_town_locations.remove("General Store")
    if town_type_name == "Outlaw Town":
        mandatory_town_locations.append("Smuggler's Den")
        possible_town_locations.remove("Smuggler's Den")
        possible_town_locations.remove("Sheriff's Office")
    if town_type_name == "Plague Town":
        mandatory_town_locations.append("Doc's Office")
        mandatory_town_locations.append("Church")
        possible_town_locations.remove("Church")
        possible_town_locations.remove("Doc's Office")
    if town_type_name == "Mutant Town":
        mandatory_town_locations.append("Mutant Quarter")
        possible_town_locations.remove("Mutant Quarter")
        possible_town_locations.remove("Frontier Outpost")
    if town_type_name == "River Town":
        mandatory_town_locations.append("Street Market")
        mandatory_town_locations.append("Gambling Hall")
        possible_town_locations.remove("Street Market")
        possible_town_locations.remove("Gambling Hall")
    return mandatory_town_locations, possible_town_locations


def locations_destroyed():
    """Find out if any locations need to be destroyed."""
    print("How many spaces need to be destroyed?")
    while True:
        try:
            spaces = int(input())
        except ValueError:
            print("Please enter a number from 1 to 8.")
            continue
        if spaces < 0 or spaces > 8:
            print("Please enter a number from 0 to 8.")
            continue
        else:
            break
    # add input validation
    return spaces


def location_assignment(starting_spaces, destroyed_spaces,
                        mandatory_town_locations, possible_town_locations):
    """Assign a location to each space."""
    locations = mandatory_town_locations
    available_spaces = starting_spaces - destroyed_spaces
    locations.append(random.sample(possible_town_locations, (available_spaces
                     - len(locations))))
    for d in range(0, destroyed_spaces):
        locations.append(["Destroyed"])
    return locations


def generate_town(town_size, town_type):
    """Generate the town."""
    destroyed_spaces = locations_destroyed()
    if town_type == "River Town":
            town_size += 1
    mandatory_town_locations, possible_town_locations =\
        town_location_adjustment(town_type)
    assigned_locations = location_assignment(town_spaces(town_size),
                                             destroyed_spaces,
                                             mandatory_town_locations,
                                             possible_town_locations)
    return assigned_locations
