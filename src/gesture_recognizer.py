def is_index_up(hand):
    return hand[8].y < hand[6].y


def is_middle_up(hand):
    return hand[12].y < hand[10].y


def is_ring_up(hand):
    return hand[16].y < hand[14].y


def is_pinky_up(hand):
    return hand[20].y < hand[18].y
