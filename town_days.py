"""Days.

Defines functions for each day in town.
"""
import random
import sys
import textwrap
import game_data
# add dragon switch

# each card will be ["title", "flavor text", "effect"]
daily_event_deck = [
                    [
                     "Just another day on the frontier",
                     "It's just another day on the frontier of the wild west..\
                     . death and adventure around every corner!",
                     "No effect.",
                    ],
                    [
                     "Hangin'",
                     "As the sun burns overhead, an outlaw is marched out to\
                     the wooden gallows in front of the courthouse.  With the\
                     pull of a lever and the snap of a rope, one more soul\
                     goes to meet its maker as the crowd looks on.",
                     "All heroes in town may recover 1 grit.",
                    ],
                    [
                     "Strange lights overhead",
                     "A bad omen to be sure!",
                     "Any heroes that choose to stay at the camp site today\
                     may onle roll a single d8 on the Camp Site Hazard Chart\
                     instead of the normal 2d6.",
                    ],
                    [
                     "We found somethin'!",
                     "Buried in the sand!  Come take a look!  I ain't never\
                     seen nothing like it!",
                     "Each hero may make a Lore 4+ test to investigate.  Gain\
                     10 XP for every 4+ rolled.  If you roll any 1s, take d6\
                     horror hits.  If you roll at least one 6, you also\
                     discover that the miners have found something of value\
                     and are willing to sell it to you.  Draw a World Card to\
                     see where the object is from, then draw an Artifact card\
                     from that world.  You may purchase the artifact for\
                     d6 x $50.",
                    ],
                    [
                     "High noon",
                     "Having a run in with one of the rougher looking locals,\
                     you find yourself challenged to a duel in the streets...\
                     at high noon!",
                     "One random hero must give up their day in town and\
                     immediately play the High Noon Duel (Solo) Mission.\n\n\
                     Alternatively, that hero may duck out the back door and\
                     run for it, ending their town stay and starting the next\
                     adventure with no grit.",
                    ],
                    [
                     "Traveling tonic wagon",
                     "Rolling into town, a traveling tonic salesman opens up\
                     the sides of his cart to show his wares!",
                     "Each hero may purchase up to 3 Tonic Tokens at a cost of\
                     $100 each.\n\nAfterward, roll a die for each Tonic Taken\
                     purchased.  On the roll of 1 or 2, that taken is little\
                     more than snake oil and is worthless (discard it).",
                    ],
                    [
                     "Wounded soldiers",
                     "The town is filled with wounded soldiers that marched\
                     in this morning from a nearby battle!  They are the last\
                     remnants of their division, overrun by horrors from\
                     beyond.",
                     "Each hero may give up their day in town to help the\
                     wounded.  Make a Lore 3+ test and gaing 10 XP for every\
                     3+ rolled.  If at least one 6 is rolled, you may also\
                     draw a Gear card, as a dying soldier passes something\
                     on to you.",
                    ],
                    [
                     "Heavy rain",
                     "A brutal rain hammers the town, flooding the streets\
                     with mud and soaking to the bone any who dare set foot\
                     outside.",
                     "All rolls on a Location Event Chart in town today are -1\
                     to the roll (minimum of 2).",
                    ],
                    [
                     "Just another day on the frontier.",
                     "It's just another day on the frontier of the wild west\
                     ... death and adventure around every corner!",
                     "No effect.",
                    ],
                    [
                     "Persecution",
                     "Filled with hate for the accursed Mutant, the Townsfolk\
                     form an angry mob and begin scouring the town to find and\
                     punish the unclean outsiders they have heard rumor of!",
                     "(This event is canceled if there is a Mutant Quarter\
                     in Town)\nEvery hero must roll a d6 for each mutation\
                     they currently have.  If any of these dice roll a 1, you\
                     have been discovered by the mob and must flee town to\
                     escape a lynching!  Your town stay is immediately over.",
                    ],
                    [
                     "Wide open skies",
                     "The big, blue sky has opened up and the sun is shining\
                     across the land.  This seems to be a respite from the\
                     Darkness... at least for the moment.",
                     "All rolls on a Location Event Chart in town today are\
                     +1 to the roll (max of 12).",
                    ],
                    [
                     "Market prices up",
                     "Supplies ar erunning short since the last demonic\
                     attack!  Everyone is a little spooked, trying to gear\
                     up before the next wave hits.",
                     "All prices in town today are +$10",
                    ],
                    [
                     "Just another day on the frontier.",
                     "It's just another day on the frontier of the wild\
                     west... death and adventure around every corner!",
                     "No effect.",
                    ],
                    [
                     "Just another day on the frontier.",
                     "It's just another day on the frontier of the wild\
                     west... death and adventure around every corner!",
                     "No effect.",
                    ],
                    [
                     "Mob riot",
                     "The townsfolk are fed up with the local authority and\
                     have begun to riot in the streets!",
                     "Each hero may attempt to help quell the riot by making\
                     a Strength 4+ test.  If failed, the hero is knocked over\
                     the head by the crowd, taking d6 wounds (ignoring\
                     defense) and may do nothing else during this day in\
                     town.  If passed, the hero gains 20 XP and may choose one\
                     building in town to protect.\n\nRoll a d6 for each\
                     building in town that was not protected.  On the roll of\
                     1 or 2, that building is destroyed in the riot.",
                    ],
                    [
                     "Market prices down",
                     "Time has passed since the last demonic attack and\
                     everyone is a little more at ease.",
                     "All prices in town today are -$10 (to a minimum of $10)",
                    ],
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
        print('*' * 80)
        if event_roll == 7 or event_roll == 8:
            event_roll = 6
        if event_roll == 11:
            event_roll = 10
        print(textwrap.dedent(event_table[event_roll]))
        print('*' * 80)
        input("Press enter when ready for the next day.")
    else:
        days_since_last_event += 1
    return days_since_last_event


def draw_daily_event(daily_event_deck):
    """Draw a daily event."""
    if len(daily_event_deck) == 0:
        daily_event_deck = initialize_daily_event_deck()
    event = random.sample(daily_event_deck, 1)
    return event, daily_event_deck


def day_in_town_start(daily_event_deck, town_type):
    """Draw Daily events."""
    print("Daily Event:")
    events = []
    new_event, daily_event_deck = draw_daily_event(daily_event_deck)
    events.append(new_event)
    if town_type == "Rail Town":
        new_event, daily_event_deck = draw_daily_event(daily_event_deck)
        events.append(new_event)
    return daily_event_deck, events


def end_of_day_prompt(days_since_last_event):
    """Prompt before rolling end of day event."""
    print("If a hero is Wanted or Most Wanted, be sure to roll as per the\
     card")
    print()
    quit = input("Press enter when the day is over.  Type quit to exit.")
    print()
    if quit == "quit":
        sys.exit
    days_since_last_event = day_in_town_end(game_data.town_event_table,
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
