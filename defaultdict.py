import collections


dict_list = collections.defaultdict(list)
dict_list["a"].append(1)
dict_list["a"].append(2)
dict_list["b"].append(3)
print(dict_list)
print(dict_list.keys())
print(dict_list.values())

dict_set = collections.defaultdict(set)
dict_set["a"].add(1)
dict_set["a"].add(2)
dict_set["b"].add(3)

dict_set["b"].add(3)
print(dict_set)

pairs = [("animal", "cat"), ("animal", "dog"), ("plant", "lily"), ("plant", "rose"), ("plant", "lily")]
dict_list = collections.defaultdict(list)
for key, value in pairs:
    dict_list[key].append(value)
print(dict_list)

dict_set = collections.defaultdict(set)
for key, value in pairs:
    dict_set[key].add(value)
print(dict_set)
