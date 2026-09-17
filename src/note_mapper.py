GESTURE_TO_NOTE = {
    "FIST": "C4",
    "THUMB": "D4",
    "INDEX": "E4",
    "TWO_FINGERS": "F4",
    "THREE_FINGERS": "G4",
    "FOUR_FINGERS": "A4",
    "OPEN_HAND": "B4",
}


def gesture_to_note(gesture):
    return GESTURE_TO_NOTE.get(gesture)
