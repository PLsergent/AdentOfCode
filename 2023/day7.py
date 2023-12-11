with open('./day7.txt') as f:
    content = f.readlines()

content = [x.strip() for x in content]

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

# Part 1

type_dict = {"five": [], "four": [], "fh": [], "three": [], "two_pairs": [], "one_pair": [], "hc": []}
hands = []
values = []
index = 0
for line in content:
    cards_occ = {"A": 0, "K": 0, "Q": 0, "J": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0}
    hand = line.split(" ")[0]
    hands.append(hand)
    value = line.split(" ")[1]
    values.append(value)

    for card in hand:
        cards_occ[card] += 1
    
    if 5 in cards_occ.values():
        type_dict["five"].append(index)
    elif 4 in cards_occ.values():
        type_dict["four"].append(index)
    elif 3 in cards_occ.values() and 2 in cards_occ.values():
        type_dict["fh"].append(index)
    elif 3 in cards_occ.values():
        type_dict["three"].append(index)
    elif list(cards_occ.values()).count(2) == 2:
        type_dict["two_pairs"].append(index)
    elif 2 in cards_occ.values():
        type_dict["one_pair"].append(index)
    else:
        type_dict["hc"].append(index)
    
    index += 1

def determine_best_hand(list_of_indexes, index_to_check = 0):
    max = (len(cards), []) # value, indexes
    for i in list_of_indexes:
        if max[1] == []:
            max = (cards.index(hands[i][index_to_check]), [i])
        elif cards.index(hands[i][index_to_check]) < max[0]:
            max = (cards.index(hands[i][index_to_check]), [i])
        elif cards.index(hands[i][index_to_check]) == max[0]:
            max[1].append(i)
    if len(max[1]) == 1:
        return max[1][0]
    else:
        index_to_check += 1
        return determine_best_hand(max[1], index_to_check)

values_ordered = []
for card, index_list in type_dict.items():
    if len(index_list) == 0:
        continue
    elif len(index_list) == 1:
        values_ordered.append(index_list[0])
    else:
        while len(index_list) > 0:
            jindex = determine_best_hand(index_list)
            values_ordered.append(index_list.pop(index_list.index(jindex)))

k = len(values_ordered)
total = 0
for val in values_ordered:
    mul = int(values[val]) * k
    total += mul
    k -= 1

print(total)

# Part 2

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

type_dict = {"five": [], "four": [], "fh": [], "three": [], "two_pairs": [], "one_pair": [], "hc": []}
hands = []
values = []
index = 0
for line in content:
    cards_occ = {"A": 0, "K": 0, "Q": 0, "T": 0, "9": 0, "8": 0, "7": 0, "6": 0, "5": 0, "4": 0, "3": 0, "2": 0, "J": 0}
    hand = line.split(" ")[0]
    hands.append(hand)
    value = line.split(" ")[1]
    values.append(value)

    for card in hand:
        cards_occ[card] += 1
    if cards_occ["J"] == 0:
        if 5 in cards_occ.values():
            type_dict["five"].append(index)
        elif 4 in cards_occ.values():
            type_dict["four"].append(index)
        elif 3 in cards_occ.values() and 2 in cards_occ.values():
            type_dict["fh"].append(index)
        elif 3 in cards_occ.values():
            type_dict["three"].append(index)
        elif list(cards_occ.values()).count(2) == 2:
            type_dict["two_pairs"].append(index)
        elif 2 in cards_occ.values():
            type_dict["one_pair"].append(index)
        else:
            type_dict["hc"].append(index)

    else:
        c = cards_occ["J"]
        del cards_occ["J"]
        print("J ##########", c)
        print(hand)
        if 5 - c in cards_occ.values():
            type_dict["five"].append(index)
            print("five")
        elif 4 - c in cards_occ.values():
            type_dict["four"].append(index)
            print("four")
        elif list(cards_occ.values()).count(2) == 2:
            print("fh")
            type_dict["fh"].append(index)
        elif 3 - c in cards_occ.values():
            type_dict["three"].append(index)
            print("three")
        elif 2 in cards_occ.values():
            type_dict["two_pairs"].append(index)
            print("two_pairs")
        elif 2 - c in cards_occ.values():
            type_dict["one_pair"].append(index)
            print("one_pair")
        else:
            type_dict["one_pair"].append(index)
            print("one_pair")
    index += 1

values_ordered = []
for card, index_list in type_dict.items():
    if len(index_list) == 0:
        continue
    elif len(index_list) == 1:
        values_ordered.append(index_list[0])
    else:
        while len(index_list) > 0:
            jindex = determine_best_hand(index_list)
            values_ordered.append(index_list.pop(index_list.index(jindex)))

k = len(values_ordered)
total = 0
for val in values_ordered:
    mul = int(values[val]) * k
    total += mul
    k -= 1

print(total)