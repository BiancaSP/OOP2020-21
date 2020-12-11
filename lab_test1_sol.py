# solution to lab test 1
# OOP Python
# 2020-21

import collections

class FindUncommonWord:
    def __init__(self, s1, s2):
        self.find_un_common(s1, s2)


    def find_un_common(self, sen1, sen2):
        a_split = sen1.lower().split()
        b_split = sen2.lower().split()

        uncommon_words = set(a_split).symmetric_difference(set(b_split))
        print(uncommon_words)
        # a_counter = collections.Counter(a_split)
        # b_counter = collections.Counter(b_split)
        my_counter = collections.Counter(a_split+b_split)

        # solution = []
        # for word in uncommon_words:
        #     if a_counter[word]==1 or b_counter[word]==1:
        #         solution.append(word)

        solution = [word for word in uncommon_words if my_counter[word] == 1]
        print(solution)


sentence1 = "You used to love cake but now you don't."
sentence2 = "We used to enjoy cake but now we don't."
f = FindUncommonWord(sentence1, sentence2)

