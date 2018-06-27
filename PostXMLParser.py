import pickle

import xmltodict

POST_TYPE_ID = '@PostTypeId'
BODY = '@Body'
PARENT_ID = '@ParentId'
ID = '@Id'
TAGS = '@Tags'

result_dict = {}
with open('data/PostsSmall.xml') as fd:
    doc = xmltodict.parse(fd.read())
    print(len(doc['posts']['row']))

    counter = 0
    for post in doc['posts']['row']:
        type_id = post[POST_TYPE_ID]
        if type_id == '1':
            post_tags = post[TAGS].split(',')
            result_dict[post[ID]] = (post[BODY], list(), post_tags)
        counter += 1
        if counter % 5000 == 0:
            print("1 iteraton: " + str(counter))

    counter = 0
    for post in doc['posts']['row']:
        type_id = post[POST_TYPE_ID]
        if type_id == '2' or type_id == '3':
            question = result_dict[post[PARENT_ID]][0]
            answer_list = result_dict[post[PARENT_ID]][1]
            post_tags = result_dict[post[PARENT_ID]][2]
            new_answer = post[BODY]
            answer_list.append(new_answer)
            result_dict[post[PARENT_ID]] = (question, answer_list, post_tags)
        counter += 1
        if counter % 5000 == 0:
            print("2 iteraton: " + str(counter))
print(len(result_dict))
pickle.dump(result_dict, open("result_dict_saved.p", "wb"))
