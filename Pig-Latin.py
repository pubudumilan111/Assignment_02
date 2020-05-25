word_list = ["pen", "I", "don't", "understand", "Please", "speak", "more", "slowly", "Please", "say", "that", "again", "Do", "you", "speak", "English"]
print(word_list)
new_list = []
for word in word_list:
    li = []
    if word[0].lower() in ('a', 'e', 'i', 'o', 'u'):
        new_list.append(word+'way')
    else:
        li = list(word)
        p = str(li.pop(0)).lower()
        new_list.append("".join(li)+p+'ay')

print(new_list)
