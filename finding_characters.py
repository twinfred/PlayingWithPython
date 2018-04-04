def finding_characters(word_list, char):
    new_list = []
    for i in range(0, len(word_list)):
        if word_list[i].count(char) > 0:
            new_list.append(word_list[i])
    print new_list

finding_characters(['magic', 'tim', 'apple'], "i")