compute_number_words = lambda word: len(word.split())

print(compute_number_words("This is a sentence"))

str_list = ["This is", "Not", "A pencil", "Beautiful"]
str_list.sort(key=lambda word: len(word.split()), reverse=True)

print(str_list)
