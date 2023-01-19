from enum import Flag

# type == color, maar kan ook andere dingen aanpassen ipv kleur
# value == waarde van de kaart, denk aan +1, skip, 0, 6, om te kijken of je de kaart kan spelen
card = {
    "type": 0,
    "value": "",
    "skip": 2,
    "grab": 4,
    "rotateHands": 1,


}

# dimensionswitch number get's randomized of the total dimensions -1 (the number rotates through the list)
class suspicion(Flag):
     wildCard = 1  #    000001
     playAnotherTurn = 2  #    000010
     dimensionSwitch = 4 #     000100
     reset = 8 #   001000
     reverse = 16 #  010000
     arigato = 32 # 100000


i = 19 # 010011


def flags_set(num):
    return [sus.name for sus in suspicion if num & sus.value]

print(flags_set(i))