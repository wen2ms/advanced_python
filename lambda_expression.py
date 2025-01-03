compute_number_words = lambda str: len(str.split())

print(compute_number_words('This is a sentence'))

str_list = ['This is', 'Not', 'A pencil', 'Beautiful']
str_list.sort(key=lambda str: len(str.split()), reverse=True)

print(str_list)