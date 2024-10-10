#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.

    :param boxes: List of lists, where each sublist contains keys to other boxes.
    :return: True if all boxes can be unlocked, False otherwise.
    """
    unlocked = set([0])  # Box 0 is unlocked initially
    keys = list(boxes[0])  # Start with the keys from box 0

    # While there are still keys to check
    while keys:
        key = keys.pop()

        # Ensure the key is valid and the corresponding box isn't already unlocked
        if isinstance(key, int) and key < len(boxes) and key not in unlocked:
            unlocked.add(key)  # Unlock the box
            keys.extend(boxes[key])  # Add keys from the newly unlocked box

    # Check if the number of unlocked boxes equals the total number of boxes
    return len(unlocked) == len(boxes)
