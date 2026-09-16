def is_index_up(hand):
    """
    Check whether the index finger is extended.

    MediaPipe landmark IDs:
    6  = index PIP joint
    8  = index fingertip
    """
    index_pip = hand[6]
    index_tip = hand[8]

    return index_tip.y < index_pip.y
