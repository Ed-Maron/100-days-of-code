#2
def best_items(racers):
    """Given a list of racer dictionaries, return a dictionary mapping items to the number
    of times those items were picked up by racers who finished in first place.
    """
    winner_item_counts = {}
    for i in range(len(racers)):
        # The i'th racer dictionary
        racer = racers[i]
        # We're only interested in racers who finished in first
        if racer['finish'] == 1:
            for item in racer['items']:
                # Add one to the count for this item (adding it to the dict if necessary)
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1

        # Data quality issues :/ Print a warning about racers with no name set. We'll take care of it later.
        if racer['name'] is None:
            print("WARNING: Encountered racer with unknown name on iteration {}/{} (racer = {})".format(
                i+1, len(racers), racer['name'])
                 )
    return winner_item_counts

sample = [
    {'name': None,'items': ['mushroom'],'finish':1}
]
#best_items(sample)


#3

def blackjack_hand_greater_than(hand_1, hand_2):
    result_hand_1 = calculate_hand(hand_1)
    result_hand_2 = calculate_hand(hand_2)
    return (result_hand_1 > result_hand_2 and result_hand_1 <= 21) or (result_hand_2 > 21 and result_hand_1 <= 21)


def calculate_hand(hand):
    count_of_A = 0
    result = 0
    for el in hand:
        if el in ['J','Q','K']:
            result +=10
        elif el == 'A':
            count_of_A +=1
        else:
            result += int(el)
   
    if count_of_A > 0:
        result += count_of_A

    if count_of_A > 0 and result<= 12:
        result += 9
    return result

blackjack_hand_greater_than(['9'], ['9', 'Q', '8', 'A'])
 #False
blackjack_hand_greater_than(['A', '10','2'], ['10'])
#    False
blackjack_hand_greater_than(['A', 'A', 'A'], ['3'])
#    False