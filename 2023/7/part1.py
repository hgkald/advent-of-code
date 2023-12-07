from sys import stdin 

class CardType:
    #Part 1 
    #types = [ 'A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    #Part 2
    types = [ 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
    
    size = len(types)
    rank = dict(zip(types, list(range(size))))

class HandType: 
    types = { "Five of a kind": 0,
            "Four of a kind": 1,
            "Full house": 2,
            "Three of a kind": 3,
            "Two pair": 4,
            "One pair": 5,
            "High card": 6 }
    size = len(types)

    def __init__(self, handtype):
        self.str = handtype
        self.int = self.types[handtype]

    def __str__(self):
        return self.str 
    
class Hand: 
    size = 5
    def __init__(self, cards, bid, joker=False):
        self.hand = cards
        self.bid = bid
        self.type = None
        self._assign_type(joker)

    def _assign_type(self, joker=False):
        cards = {}
        for card in self.hand:
            if card not in cards:  
                cards[card] = 1
            else: 
                cards[card] += 1

        if len(cards)==1: 
            self.type = HandType("Five of a kind")
        elif 4 in cards.values():
            if joker and 'J' in cards:
                self.type = HandType("Five of a kind")
            else:
                self.type = HandType("Four of a kind")
        elif set(cards.values())=={3,2}:
            if joker and 'J' in cards:
                self.type = HandType("Five of a kind")
            else:
                self.type = HandType("Full house")
        elif set(cards.values())=={3,1}:
            if joker and 'J' in cards:
                self.type = HandType("Four of a kind")
            else:
                self.type = HandType("Three of a kind")
        elif list(cards.values()).count(2) == 2: 
            if joker and 'J' in cards:
                if cards['J']==1: 
                    self.type = HandType("Full house")
                else: 
                    self.type = HandType("Four of a kind")
            else:
                self.type = HandType("Two pair")
        elif 2 in cards.values() and list(cards.values()).count(1)==3:
            if joker and 'J' in cards:
                self.type = HandType("Three of a kind")
            else:
                self.type = HandType("One pair")
        elif len(cards)==5:
            if joker and 'J' in cards:
                self.type = HandType("One pair")
            else:
                self.type = HandType("High card")

    def __str__(self):
        return self.hand + " (" + self.type.str + ")"

    def __repr__(self):
        return f'Hand("{self.hand}",{self.bid},{self.type.str})'

def _bucket_sort(hands, k):
    type_buckets = [ [] for x in range(CardType.size)]
    for h in hands:
        bucket = CardType.rank[h.hand[k]]
        type_buckets[bucket].append(h)

    hands = []
    for b in type_buckets: 
        if b: hands += b

    return hands

def radix_sort(hands):
    for i in range(Hand.size-1,-1,-1):
        hands = _bucket_sort(hands, i)
    return hands
        
def main():
    type_buckets = [ [] for x in range(HandType.size) ]
    for line in stdin: 
        line = line.split()
        hand = Hand(line[0], int(line[1]), True)
        type_buckets[hand.type.int].append(hand)

    hands = [] 
    for b in type_buckets:
        if b:
            b = radix_sort(b)
            hands += b

    total_winnings = 0
    rank = len(hands)
    for h in hands:
        total_winnings += rank*h.bid
        rank -= 1

    print(total_winnings)

if __name__=='__main__':
    main()
