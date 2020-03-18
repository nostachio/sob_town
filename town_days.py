"""Days.

Defines functions for each day in town.
"""
import random
import sys

# add dragon switch
town_event_table = \
    {2:
    """VOID TWISTER:
    A Void Twister sweeps through the town, annihilating it in a flash!
    Livestock, buildings, and people are swept away right before your
    eyes and it's coming toward you!

    Every hero must make an Agility 5+ or Strength 5+ to avoid or resist
    the powerful pull of the twister!  If failed, the Hero is swept away,
    broken and battered - they are killed.  The town is destroyed and the
    town stay is over.""",
     3:
     """TOWN OVERRUN: The town is overrun with monsters, slaughtering people
     and razing buildings.  It's time to get out while you can!

     Each hero in town must roll a number of dice equal to the number of
     Dark Stone they currently carry.  For every roll of 1, that hero takes
     d6 wounds, ignoring Defense, as they are assaulted by monsters.
     Any hero KO'd by this is killed in the firey ruins of the town.
     The town is destroyed and the town stay is over.""",
     4: "FIRE: A fire has broken out, setting the town ablaze.\n\n\
     d3 random town locations burn to the ground in the fire and are \
     destroyed.",
     5: "THE FEVER: A terrible sickness spreads through town, causing Void \
     Boils and death.\n\nEach hero must make a Spirit 6+ test to avaid the \
     plague.  If successful, gain 10XP.  If failed, take d6+3 Wounds, \
     ignoring Defense.",
     6: "SPREADING FEAR: Fear Spreads through the town as the days grow dark \
     and the demonic attacks more frequent.\n\nOne Random Town Location \
     closes up shop and may not be visited for the rest of this town stay.  \
     The Camp Site dissipates (may no lonegr be used or visited) and the \
     Hotel doubles their current rate.",
     9: "INTENSE DREAD: A dark cloud on the horizon makes your soul sink as \
     you see a Void Twister in the distance wipe through a neighboring town!\
     \n\nEach hero must make a Cunning 6+ test.  If successful, gain 10XP.  \
     If failed, take d6+3 Sanity Damage, ignoring Willpower.  If no hero \
     passes this test, also add a Growing Dread card to the stack at the \
     start of the next adventure.",
     10: "THE END IS NIGH: The people are stocking up on supplies and \
     weapons, feeling like the next big attack could come at any time!\
     \n\nAll prices in town are +$50 due to the increasing demand.",
     12: "ROTTEN FROM WITHIN: It has become clear that the officials running \
     this town are twisted and tainted by their greed, and the very Dark \
     Stone they have been hearding!  When they see something they want, they \
     take it!\n\nRandomly choose a hero to be singled out by the corrupt \
     sheriff.  That hero must either hand over P Dark Stone or one item with \
     a Dark Stone icon to pay off the 'Law Man' and his mutated gang of \
     thugs.  If the hero has neither, the gang opens fire on them and they \
     must escape town.  They take 2d6 Wounds, ignoring Defense, and the town \
     stay is over.",
     }
daily_event_deck = ["No Event",
                    ]


def initialize_daily_event_deck():
    """Set deck to initial deck."""
    initialized_event_deck = daily_event_deck
    return initialized_event_deck


def day_in_town_end(event_table, days_since_last_event):
    """Check for town event."""
    roll = random.randrange(1, 6)
    print("Days since last event:", days_since_last_event)
    print("Town event roll is", roll)
    if roll <= days_since_last_event:
        days_since_last_event = 1
        print("A town event happens!")
        event_roll = random.randrange(2, 12)
        print("The event roll is", event_roll)
        if event_roll == 7 or event_roll == 8:
            event_roll = 6
        if event_roll == 11:
            event_roll = 10
        print(event_table[event_roll])
        print()
        input("Press enter when ready.")
    else:
        days_since_last_event += 1
    return days_since_last_event


def day_in_town_start(daily_event_deck):
    """Draw Daily events."""
    # if deck is empty, initialize deck
    print("Daily Event:")
    events = []
    events.append(random.sample(daily_event_deck, 1))
    # if rail town, draw a second event
    return daily_event_deck, events


def end_of_day_prompt(days_since_last_event):
    """Prompt before rolling end of day event."""
    print()
    quit = input("Press enter when the day is over.  Type quit to exit.")
    print()
    if quit == "quit":
        sys.exit
    days_since_last_event = day_in_town_end(town_event_table,
                                            days_since_last_event)
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
