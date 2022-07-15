file1 = open('newfile.txt')

newlist = list()
words_to_find = list()
final_dict = dict()

for line in file1:
    newlist = line.split()
    words_to_find.append(newlist[2])


print(words_to_find)

for word in words_to_find:
    if word not in final_dict.keys():
        final_dict[word] = 1
    else:
        final_dict[word] = final_dict[word] + 1

print(final_dict)
