def custom_key(string):
    return [strength.index(char) for char in string]

def ranking(values):
    final_rankings = []
    for i in range(1, 8):
        if i not in values:
            continue
        elif len(values[i]) == 1:
            final_rankings.append(values[i][0])
        else:
            strings_to_compare = values[i]
            sorted_strings = sorted(strings_to_compare, key=lambda x: (custom_key(x), -input_nicer[x]))
            for j in sorted_strings:
                final_rankings.append(j)
    return final_rankings

with open('input.txt') as f:
    strength = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    input_lines = f.read().strip().split("\n")
    input_nicer = {}
    hands = {}
    for round in input_lines:
        print("round ", round)
        joker = 0
        hand, bid = round.split(" ")
        input_nicer[hand] = int(bid)
        hand_cards = {}
        hand_type = 0
        for card in hand:
            if card == "J":
                joker += 1
            else:
                if card in hand_cards:
                    hand_cards[card] += 1
                else:
                    hand_cards[card] = 1
        if joker == 5:
            hands[1] = [hand]
        else:
            max_key = max(hand_cards, key=lambda k: hand_cards[k])
            hand_cards[max_key] += joker
            if len(hand_cards) == 1:
                hand_type = 1  # five of a kind
            if len(hand_cards) == 2:
                for key in hand_cards:
                    if hand_cards[key] == 4:
                        hand_type = 2  # four of a kind
                        break
                    hand_type = 3  # full house
            if len(hand_cards) == 3:
                for key in hand_cards:
                    if hand_cards[key] == 3:
                        hand_type = 4  # three of a kind
                        break
                    hand_type = 5  # two pair
            if len(hand_cards) == 4:
                hand_type = 6  # one pair
            if len(hand_cards) == 5:
                hand_type = 7  # high card
            if hand_type in hands:
                hands[hand_type].append(hand)
            else:
                hands[hand_type] = [hand]

    final_rank = ranking(hands)
    final_result = 0
    ranks = len(final_rank)
    for rank in final_rank:
        final_result += (ranks * input_nicer[rank])
        ranks -= 1
    print(final_result)
    print(250057090)
