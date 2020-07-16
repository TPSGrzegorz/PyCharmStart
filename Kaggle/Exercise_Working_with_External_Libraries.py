def blackjack_hand_greater_than(hand_1: list, hand_2: list):
    """
    Return True if hand_1 beats hand_2, and False otherwise.

    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21

    Hands are represented as a list of cards. Each card is represented by a string.

    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.

    When determining a hand's total, you should try to count aces in the way that
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.

    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    values = {
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
    }
    ases_1 = hand_1.count('A')

    temp_hand = [values.get(x) for x in hand_1]
    sum_1 = sum(temp_hand)
    for i in range(ases_1):
        if sum_1 > 21 and 'A' in hand_1:
            sum_1 -= 10
        else:
            break


    temp_hand = [values.get(x) for x in hand_2]
    sum_2 = sum(temp_hand)
    ases_2 = hand_2.count('A')
    for i in range(ases_2):
        if sum_2 > 21 and 'A' in hand_2:
            sum_2 -= 10
        else:
            break
    # sum_1 = sum(int(x) if x.isdecimal() else x for x in hand_1)
    return (sum_1 > sum_2) and (sum_1 <= 21) or (sum_2 > 21 and sum_1 <= 21)


result = blackjack_hand_greater_than(['A', 'A', '9', '3'], ['3'])
print(result)
