
# def Sentence(target):
#     for word in target.split():
#         yield word
#
# #
# my_sentence = Sentence('this is a test')
#
# for word in my_sentence:
#     print(word)

# print(next(my_sentence))


class Sentence():
    def __init__(self,sentence):
        self.sentence = sentence
        self.index = 0
        self.words = sentence.split()     ###split on space by default


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        self.index += 1
        return word


my_sentence = Sentence('this is a test')

for word in my_sentence:
    print(word)

# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))
# print(next(my_sentence))



