from random import randint

POSSIBLE_DICE = ('D3', 'D4', 'D6', 'D8', 'D10', 'D12', 'D20', 'D100')


def roll_the_dice():
    user_inp = input('Enter the combination:\n').upper()
    for dice in POSSIBLE_DICE:
        if dice in user_inp:
            try:
                multiply, modifier = user_inp.split(dice)
            except ValueError:
                return 'Wrong input'
            dice_value = dice[1:]
            break
    else:
        return 'Wrong value'

    if multiply:
        try:
            multiply = int(multiply)
        except ValueError:
            return 'Wrong input'
    else:
        multiply = 1

    # --------------------------------------------------
    # try:
    #     multiply = int(multiply) if multiply else 1
    # except ValueError:
    #     return 'Wrong input'
    # --------------------------------------------------

    if modifier:
        try:
            modifier = int(modifier)
        except ValueError:
            return 'Wrong input'
    else:
        modifier = 0

    prod_ = sum([randint(1, int(dice_value)) for _ in range(multiply)]) + modifier
    return f'Your result of a roll: {user_inp} equals -> {prod_}'


print(roll_the_dice())
