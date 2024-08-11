import random
import json
from combinations import unpack_json, cards_set,flush_royal
'combination_test.json'
# cards = {}
masts = ["krest", "cherv", "buba", "pika"]
chisla = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "T"]
# for _mast in range(4):
#     cards[masts[_mast]] = chisla


class Player:
    def __init__(self):
        player_bank = 10
        hand = [[],[]]


class Table:
    def __init__(self, cards):
        self.table_cards = pick_cards(cards,2)

    def add_card(self, cards):
        self.table_cards.append(pick_cards(cards,1)[0])

class Game:
    def __init__(self, player_count):
        bank = 0
        players = []
        for i in range(player_count):
            players.append(Player())


def enter():
    global cards
    with open('cards.json', 'r') as f:
        cards = json.load(f)

def pick_cards(cards, count):
    final_hand = []
    for i in range(count):
        mast_index = random.randrange(0,4)
        mast_list = cards[masts[mast_index]]
        chislo_index = random.randrange(0,len(mast_list))    #вторая i четвертой итерации j пропадает массив mast_list
        # mast_list = ['Q', 'K', 'T']

        final_hand.append([masts[mast_index], mast_list[chislo_index]])
        mast_list.pop(chislo_index)

    return final_hand

# for i in range(100000):
#     enter()
#     P1.hand = pick_cards(cards)
#     P2.hand = pick_cards(cards)

#     if P1.hand != P2.hand:
#         print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", i)
#     else:
#         break

# //
enter() #переменную cards необходимо обязательно передавать в функцию иначе не работает

# // надо

def set_json_comb_test (rng,wrt = False):
    if wrt:
        with open('combination_test.json','w') as file:
            set_json_comb_test(rng)
    test = {"data":0}
    fin_arr = []
    for j in range(rng):
        enter()
        arr = []
        data = pick_cards(cards,7)
        # print('a')
        arr.append(data)
        fin_arr.append(arr)
        arr = []
        test["data"] = fin_arr
        # json.dump(test,file)
        # return(unpack_json('not js',test))
    return test

zxc = 0
# print(unpack_json('not js',set_json_comb_test(rng=1000)))
for z in unpack_json('not js',set_json_comb_test(rng=10000000)):
    zxc += 1
    if flush_royal(z):
        print(z)
        print(zxc)
        break
# P1 = Player()
# P2 = Player()
# P1.hand = pick_cards(cards, 2)
# P2.hand = pick_cards(cards, 2)


# table = Table(cards)
# table.add_card(cards) 

# print(pick_cards(cards,7))

# print(table.table_cards)
#гоу в лигу