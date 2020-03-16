"""Town Generator.

Generates a town for Shadows of Brimstone using the rules found in the
Frontier Town Adventure Book.
"""


import random
import os

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
town_event_table = ["VOID TWISTER: A Void Twister sweeps through the town, annihilating it in a flash!  Livestock, buildings, and people are swept away right before your eyes and it's coming toward you!\n\nEvery hero must make an Agility 5+ or Strength 5+ to avoid or resist the powerful pull of the twister!  If failed, the Hero is swept away, broken and battered - they are killed.  The town is destroyed and the town stay is over.",
                    "DRAGON ATTACK: A massive Dragon sweeps over the village, annihilationg it in a flash of fire and death!  Livestock, buildings, and people are incinerated before your eyes... and it's coming towards you!\n\nEvery Hero in town must make an Agility 5+ or Cunning 5+ test to evade the burning flames of the Dragon!  If failed, the hero is caught in the inferno and turned to ash (killed)!  The town is destroyed and the town stay is over.",
                    "TOWN OVERRUN: The town is overrun with monsters, slaughtering people and razing buildings.  It's time to get out while you can!\n\nEach hero in town must roll a number of dice equal to the number of Dark Stone they currently carry.  For every roll of 1, that hero takes d6 wounds, ignoring Defense, as they are assaulted by monsters.  Any hero KO'd by this is killed in the firey ruins of the town.  The town is destroyed and the town stay is over.",
                    "FIRE: A fire has broken out, setting the town ablaze.\n\nd3 random town locations burn to the ground in the fire and are destroyed.",
                    "THE FEVER: A terrible sickness spreads through town, causing Void Boils and death.\n\nEach hero must make a Spirit 6+ test to avaid the plague.  If successful, gain 10XP.  If failed, take d6+3 Wounds, ignoring Defense.",
                    "SPREADING FEAR: Fear Spreads through the town as the days grow dark and the demonic attacks more frequent.\n\nOne Random Town Location closes up shop and may not be visited for the rest of this town stay.  The Camp Site dissipates (may no lonegr be used or visited) and the Hotel doubles their current rate.",
                    "INTENSE DREAD: A dark cloud on the horizon makes your soul sink as you see a Void Twister in the distance wipe through a neighboring town!\n\nEach hero must make a Cunning 6+ test.  If successful, gain 10XP.  If failed, take d6+3 Sanity Damage, ignoring Willpower.  If no hero passes this test, also add a Growing Dread card to the stack at the start of the next adventure.",
                    "THE END IS NIGH: The people are stocking up on supplies and weapons, feeling like the next big attack could come at any time!\n\nAll prices in town are +$50 due to the increasing demand.",
                    "ROTTEN FROM WITHIN: It has become clear that the officials running this town are twisted and tainted by their greed, and the very Dark Stone they have been hearding!  When they see something they want, they take it!\n\nRandomly choose a hero to be singled out by the corrupt sheriff.  That hero must either hand over P Dark Stone or one item with a Dark Stone icon to pay off the 'Law Man' and his mutated gang of thugs.  If the hero has neither, the gang opens fire on them and they must escape town.  They take 2d6 Wounds, ignoring Defense, and the town stay ",
                    ]


def ready():
    """Clear screen after user input."""
    print()
    input("Press enter when ready to go on.")
    print()
    os.system('clear')
    return


def darkstone_corruption():
    """Print out darkstone corruption text."""
    print("Darkstone corruption.")
    print("For each darkstone or item with a darkstone icon, roll a d6.")
    print("For each 1, 2, or 3 rolled, take a corruption hit.")
    print("Save using willpower or corruption resistance as normal.")
    ready()
    return


def recovery():
    """Print out recovery text."""
    print("Any heroes that were knocked out or passed out at the end of the \
    mission:")
    print("Roll on the Injury or Madness chart as appropriate.")
    ready()
    return


def restore():
    """Print out restore text."""
    print("All heroes are restored to full health and sanity.")
    print("All heroes are set to one grit.")
    ready()
    return


def status_removal():
    """Print status removal text."""
    print("Discard anything that lasts for an adventure such as:")
    print("Auras, Bullets, status effects, concussions, etc.")
    ready()
    return


def mission_pass_fail():
    """Print adventure consequences reminder."""
    print("Apply any rewards for success or penalies for failures of the \
    mission.")
    ready()
    return


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


def town_spaces(town_size):
    """Define the number of spaces for a town of a particular size."""
    if town_size == "small":
        spaces_available = 4
    if town_size == "medium":
        spaces_available = 6
    if town_size == "large":
        spaces_available = 8
    return spaces_available

# Complete any travel hazards (See Frontier Town Adventure Book p19-22)


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
    locations = []
    available_spaces = starting_spaces - destroyed_spaces
    for i in mandatory_town_locations:
        locations.append(i)
    locations.append(random.sample(possible_town_locations, (available_spaces
                     - len(locations))))
    for d in range(0, destroyed_spaces):
        locations.append(["Destroyed"])
    return locations


def end_of_adventure():
    """Print out all text for end of adventure."""
    darkstone_corruption()
    recovery()
    restore()
    status_removal()
    mission_pass_fail()
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


def display_town(locations, town_text, type):
    """Display the town."""
    os.system('clear')
    print()
    print(type)
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


def day_in_town_start(event_deck):
    """Draw Daily events."""
    
    return


def day_in_town_end(event_table, days_since_last_event):
    """Check for town event."""
    roll = random.randrange(1, 6)
    print("Days since last event:", days_since_last_event)
    print("Town event roll is", roll)
    if roll <= days_since_last_event:
        print("A town event happens!")
        event_roll = random.randrange(2, 12)
        print("The event roll is", event_roll)
        print(event_table[event_roll])
    return


def main():
    """Run it all."""
    os.system('clear')
    end_of_adventure()
    size = travel_to_town()
    type = town_type()
    locations = generate_town(size, type)
    text = town_special_effects(type)
    display_town(locations, text, type)
    return


main()
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
