import json
from xor import xor
import collections

def load_comb():
    global cardTest
    with open('combination_test.json', 'r') as f:
        cardTest = json.load(f)

load_comb()
KEY = 'data'
main_arr_test = []
for i in cardTest[KEY]:
    # print(i)
    for j in i:
        # print(j)
        main_arr_test.append(j)



EXAMPLE_TABLE = main_arr_test[3] #[['pika', 'J'], ['cherv', '3'], ['cherv', '5'], ['pika', '7'], ['pika', 'T'], ['krest', '7'], ['buba', '6']]
# EXAMPLE_TABLE[2][1] = 'J'
EXAMPLE_TABLE_2 = [['pika', '3'], ['cherv', '3'], ['cherv', '2'], ['pika', '3'], ['pika', '5'], ['krest', '7'], ['buba', '6']]


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


def cards_set(hand_and_table):
    cards_count = 0
    arr = []
    for s in hand_and_table:
        arr.append(s[1]) #добавление в массив значений
    ss = 0
    finded_para = 0
    count_elem = collections.Counter(arr)
    # print(count_elem)
    for i in count_elem:
        if count_elem[str(i)] == 3:
            return True


for tbl in main_arr_test: # прогоняем тесты
    if cards_set(tbl):
        print(tbl)
        print(True)



# print (EXAMPLE_TABLE_2)
# print(cards_set(EXAMPLE_TABLE_2))


