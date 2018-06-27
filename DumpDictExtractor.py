import pickle
from random import randint

result_dict = pickle.load(open("result_dict_saved.p", "rb"))

counter = 0
while counter < 4:
    rand_index = str(randint(0, 140000))
    if rand_index in result_dict:
        entry = result_dict[rand_index]
        print('Q: ' + entry[0])
        print('T:' + str(entry[2]))
        for answer in entry[1]:
            print('A: ' + answer)

        counter += 1
