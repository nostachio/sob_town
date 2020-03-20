"""Data.

Contains all the data for decks and charts.
"""


town_event_table = \
    {
     2:
     """\
     VOID TWISTER
     
     A Void Twister sweeps through the town, annihilating it in a flash!
     Livestock, buildings, and people are swept away right before your
     eyes and it's coming toward you!
     
     Every hero must make an Agility 5+ or Strength 5+ to avoid or resist
     the powerful pull of the twister!  If failed, the Hero is swept away,
     broken and battered - they are killed.  The town is destroyed and the
     town stay is over.""",
     3:
     """\
     TOWN OVERRUN
     
     The town is overrun with monsters, slaughtering people
     and razing buildings.  It's time to get out while you can!
     
     Each hero in town must roll a number of dice equal to the number of
     Dark Stone they currently carry.  For every roll of 1, that hero takes
     d6 wounds, ignoring Defense, as they are assaulted by monsters.
     Any hero KO'd by this is killed in the firey ruins of the town.
     The town is destroyed and the town stay is over.""",
     4:
     """\
     FIRE
     
     A fire has broken out, setting the town ablaze.
     
     d3 random town locations burn to the ground in the fire and are
     destroyed.""",
     5:
     """\
     THE FEVER
     
     A terrible sickness spreads through town, causing Void
     Boils and death.
     
     Each hero must make a Spirit 6+ test to avaid the
     plague.  If successful, gain 10XP.  If failed, take d6+3 Wounds,
     ignoring Defense.""",
     6:
     """\
     SPREADING FEAR
     
     Fear Spreads through the town as the days grow dark
     and the demonic attacks more frequent.
     
     One Random Town Location
     closes up shop and may not be visited for the rest of this town stay.
     The Camp Site dissipates (may no longer be used or visited) and the
     Hotel doubles their current rate.""",
     9:
     """\
     INTENSE DREAD
     
     A dark cloud on the horizon makes your soul sink as
     you see a Void Twister in the distance wipe through a neighboring town!
     
     Each hero must make a Cunning 6+ test.  If successful, gain 10XP.
     If failed, take d6+3 Sanity Damage, ignoring Willpower.  If no hero
     passes this test, also add a Growing Dread card to the stack at the
     start of the next adventure.""",
     10:
     """\
     THE END IS NIGH
     
     The people are stocking up on supplies and
     weapons, feeling like the next big attack could come at any time!
     
     All prices in town are +$50 due to the increasing demand.""",
     12:
     """\
     ROTTEN FROM WITHIN
     
     It has become clear that the officials running
     this town are twisted and tainted by their greed, and the very Dark
     Stone they have been hearding!  When they see something they want, they
     take it!
     
     Randomly choose a hero to be singled out by the corrupt
     sheriff.  That hero must either hand over P Dark Stone or one item with
     a Dark Stone icon to pay off the 'Law Man' and his mutated gang of
     thugs.  If the hero has neither, the gang opens fire on them and they
     must escape town.  They take 2d6 Wounds, ignoring Defense, and the town
     stay is over.""",
    }

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
