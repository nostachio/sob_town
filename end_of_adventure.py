"""End of Adventure.

Functions related to the end of the Adventure.
"""
import os


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


def end_of_adventure():
    """Print out all text for end of adventure."""
    darkstone_corruption()
    recovery()
    restore()
    status_removal()
    mission_pass_fail()
    return
