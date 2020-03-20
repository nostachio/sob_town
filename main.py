"""Town Generator.

Generates a town for Shadows of Brimstone using the rules found in the
Frontier Town Adventure Book.
"""
import os
import end_of_adventure
import town_generation
import town_days
import travel
import display


def main():
    """Run it all."""
    os.system('clear')
    end_of_adventure.end_of_adventure()
    size = travel.travel_to_town()
    type = town_generation.town_type()
    locations = town_generation.generate_town(size, type)
    text = town_generation.town_special_effects(type)
    daily_event_deck = town_days.initialize_daily_event_deck()
    days_since_last_event = 0
    while True:
        daily_event_deck, events =\
         town_days.day_in_town_start(daily_event_deck, type)
        display.display_town(locations, text, type, events)
        days_since_last_event = \
            town_days.end_of_day_prompt(days_since_last_event)
    return


main()
