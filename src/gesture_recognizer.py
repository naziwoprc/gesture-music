import math


def distance(point1, point2):
    return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)


def is_index_up(hand):
    return hand[8].y < hand[6].y


def is_middle_up(hand):
    return hand[12].y < hand[10].y


def is_ring_up(hand):
    return hand[16].y < hand[14].y


def is_pinky_up(hand):
    return hand[20].y < hand[18].y


def is_thumb_up(hand, handedness):
    thumb_tip = hand[4]
    thumb_mcp = hand[2]
    index_mcp = hand[5]

    thumb_length = distance(thumb_tip, thumb_mcp)
    palm_distance = distance(thumb_mcp, index_mcp)

    return thumb_length > palm_distance * 1.2


def recognize_gesture(hand, handedness):

    thumb = is_thumb_up(hand, handedness)
    index = is_index_up(hand)
    middle = is_middle_up(hand)
    ring = is_ring_up(hand)
    pinky = is_pinky_up(hand)

    # Thumb
    if thumb and not index and not middle and not ring and not pinky:
        return "THUMB"

    # Index only
    if index and not middle and not ring and not pinky:
        return "INDEX"

    # Index + middle
    if index and middle and not ring and not pinky:
        return "TWO_FINGERS"

    # Index + middle + ring
    if index and middle and ring and not pinky:
        return "THREE_FINGERS"

    # Open hand
    if thumb and index and middle and ring and pinky:
        return "OPEN_HAND"

    # Four fingers (thumb folded)
    if not thumb and index and middle and ring and pinky:
        return "FOUR_FINGERS"

    # Fist
    if not thumb and not index and not middle and not ring and not pinky:
        return "FIST"

    return "UNKNOWN"
