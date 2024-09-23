import json
from xor import xor
import collections

def load_comb(name):
    global cardTest
    with open(name, 'r') as f:
        cardTest = json.load(f)

load_comb('combination_test.json')

def unpack_json(js,test):
    # if js != "not js":
        #  load_comb('combination_test.json')
    KEY = 'data'
    """костыль. можешь глянуть в json combinations_test, я вроде просто
    не смог сохранить словарь без ключа"""
    main_arr_test = [] #массив в который будут помещаться массивы в уже распакованном виде
    
    for i in test[KEY]:
        # print(i)
        for j in i:
            # print(j)
            main_arr_test.append(j) 
    return main_arr_test
"""крч это просто функция для распаковки, можно особо не вдаваться в ее работу
правда если измениться вид json придется менять и функцию"""

main_arr_test = unpack_json('not js', cardTest)


EXAMPLE_TABLE = main_arr_test[3] #[['pika', 'J'], ['cherv', '3'], ['cherv', '5'], ['pika', '7'], ['pika', 'T'], ['krest', '7'], ['buba', '6']]
# EXAMPLE_TABLE[2][1] = 'J'
"""выбор массива из 7 карт/ стол + рука"""
EXAMPLE_TABLE_2 = [['krest', '10'], ['pika', 'T'], ['cherv', 'K'], ['krest', '6'], ['buba', '8'], ['krest', 'Q'], ['pika', 'J']]


# вернет true если в массиве есть одинаковые значения
def para(hand_and_table): # передаем массив из руки и стола
    arr = []
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    for ss in range(0,len(arr)): 
        find_val = arr.pop(ss-ss) #т.к из массива удаляеться значение отнимаем кол во итераций
        if find_val in arr:
            return True
    return False


def two_pars (hand_and_table):
    pars_count = 0
    arr = []
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    ss = 0
    while ss < len(arr):
        # arr_len = ss-ss
        find_val = arr.pop(ss-ss) #т.к из массива удаляеться значение отнимаем кол во итераций
        if find_val in arr: 
            arr.pop(arr.index(find_val))
            pars_count+=1
            ss+=1
    # for ss in range(0,len(arr)): 
    #     arr_len = ss-ss-pars_count
    #     find_val = arr.pop(arr_len) #т.к из массива удаляеться значение отнимаем кол во итераций
    #     if find_val in arr: 
    #         arr.pop(arr.index(find_val))
    #         pars_count+=1
    if pars_count > 1:
        return True
    return False 


def cards_set(hand_and_table, kareOrSet='set'): #эта функция используеться также для нахождения каре при передачи вторым параметром строки каре
    cards_count = 0
    arr = []
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    ss = 0
    finded_para = 0
    count_elem = collections.Counter(arr)
    # print(count_elem)
    kareOrSet = 4 if kareOrSet == 'kare' else 3
    for i in count_elem:
        if count_elem[str(i)] == kareOrSet:
            return True

    return False


def straight(hand_and_table, sf='straight'):
    # pass
    cards_count = 0
    arr = []

    def find_joker(card):
        if card == 'J':
            return '11'
        elif card == 'Q':
            return '12'
        elif card == 'K':
            return '13'
        elif card == 'T':
            return '14'
        else:
            return False

    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    for i in range(len(arr)):
        # print(arr[i])
        if find_joker(arr[i]):
            arr[i] = find_joker(arr[i])
    for j in range(0,len(arr)):
        arr[j] = int(arr[j])
    sort_arr = sorted(arr)
    for k in range(len(sort_arr)):
        if k == len(arr)-1:
            cards_count +=1
            break
        if (sort_arr[k]) == (sort_arr[k+1]-1):
            cards_count +=1
        else:
            cards_count = 0
    # print(sort_arr)
    # print(f'card_count: {cards_count}')
    if sf != "straight":
        return sort_arr
    if cards_count > 4:
        # print(sort_arr)
        # print(f'card_count: {cards_count}')
        return True
    return False
    # return sort_arr


def flush(hand_and_table, sf='flush'):
    cards_count = 0
    arr = []
    for s in hand_and_table:
        arr.append(s[0]) #добавление в массив мастей
    count_elem = collections.Counter(arr)

    for m, v in count_elem.items():
        # print (v)
        if count_elem[m] > 4:
            if sf != flush:
                arr.append(m)
                return arr
            # print (count_elem)
            return True
    return False


def full_haus(hand_and_table):
    cards_count = 0
    arr = []
    arr 
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    count_elem = collections.Counter(arr)
    # print(count_elem)
    # print(count_elem)
    for i in count_elem:
        # print(i)
        if count_elem[str(i)] == 3 or (cards_count > 0 and count_elem[str(i)] > 2):
            cards_count +=1
            # print(count_elem)
        if cards_count > 1:
            return True
    return False


def straight_flush(hand_and_table):
    if flush(hand_and_table):
        mast_arr = flush(hand_and_table,'zxc')
        main_mast = mast_arr[-1]
        mast_arr.pop(-1)
        i = 0
        while i < len(hand_and_table):
            if hand_and_table[i][0] != main_mast:
                hand_and_table.pop(i)
                i -= 1
            i+=1
        if straight(hand_and_table):
            return True
    return False
# удаляет другие масти (надо пофиксить)

def flush_royal(hand_and_table):
    if straight_flush(hand_and_table) and straight(hand_and_table, 'zxc')[0] == 10:
        return True
    return False


# for tbl in main_arr_test: # прогоняем тесты
#     print(tbl)
#     print(f'para: {para(tbl)}\n two_pars: {two_pars(tbl)}\n set: {cards_set(tbl)}\n straight: {straight(tbl)}\n flush: {flush(tbl)}\n full_haus: {full_haus(tbl)}\n kare: {cards_set(tbl, 'kare')}\n straight_flush: {straight_flush(tbl)}\n flush_royal: {flush_royal(tbl)}')




# print (EXAMPLE_TABLE_2)
# print(straight(EXAMPLE_TABLE_2))


