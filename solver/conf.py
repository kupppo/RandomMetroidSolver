from utils.parameters import medium

class Conf:
    # keep getting majors of at most this difficulty before going for minors or changing area
    difficultyTarget = medium

    # display the generated path (spoilers!)
    displayGeneratedPath = False

    # choose how many items are required (possible value: all (100%)/any (any%)).
    # for rando solver only: all_strict to fail if 100% is not possible.
    itemsPickup = 'any'

    # the list of items to not pick up
    itemsForbidden = []
