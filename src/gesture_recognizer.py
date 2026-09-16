def is_index_up(hand):
    return hand[8].y < hand[6].y


def is_middle_up(hand):
    return hand[12].y < hand[10].y


def is_ring_up(hand):
    return hand[16].y < hand[14].y


def is_pinky_up(hand):
    return hand[20].y < hand[18].y


def recognize_gesture(hand):
    """
    Recognize a hand gesture based on finger states.
    """
    index = is_index_up(hand)
    middle = is_middle_up(hand)
    ring = is_ring_up(hand)
    pinky = is_pinky_up(hand)

    if index and not middle and not ring and not pinky:
        return "ONE_FINGER"

    if index and middle and not ring and not pinky:
        return "TWO_FINGERS"
    if index and middle and ring and not pinky:
        return "THREE_FINGERS"

    if index and middle and ring and pinky:
        return "FOUR_FINGERS"
    if not index and not middle and not ring and not pinky:
        return "FIST"
    return "UNKNOWN"
