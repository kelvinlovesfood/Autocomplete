from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary
import time
import random

# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):
    def __init__(self):
        self.dictionary = []

    def build_dictionary(self, words_frequencies: [WordFrequency]):
    # def build_dictionary(self, words_frequencies: WordFrequency):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        # NORMAL INITIALISATION
        self.dictionary = words_frequencies

        # LISTADD.CSV
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         success = True
        #         for index in self.dictionary:
        #             if index.word == object.word:
        #                 success = False
        #         if success == True:
        #             self.dictionary.append(object)
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         self.dictionary.append(object)

        # LISTDELETE.CSV
        # self.dictionary = words_frequencies
        # print("size,nanoseconds")
        # for i in range(len(words_frequencies)-1, 0-1, -1):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         self.dictionary.pop(i)
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         self.dictionary.pop(i)

        # LISTSEARCH.CSV
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         self.dictionary.append(object)
        #         start = time.time_ns()
        #         frequency = 0
        #         for index in self.dictionary:
        #             if index.word == random.choice(self.dictionary).word:
        #                 frequency = index.frequency
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self.dictionary.append(object)

        # LISTAC.CSV
        # print("size,nanoseconds")
        # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         predictions = []
        #         for index in self.dictionary:
        #             if index.word.startswith(random.choice(alphabet)):
        #                 predictions.append(index)
        #         frequency = lambda index: index.frequency
        #         predictions.sort(reverse=True, key=frequency)
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self.dictionary.append(object)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        frequency = 0
        for index in self.dictionary:
            if index.word == word:
                frequency = index.frequency

        end = time.time_ns()
        print(f"S {word:<20} {(end - start):<20} ns \t list")

        return frequency

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        success = True
        for index in self.dictionary:
            if index.word == word_frequency.word:
                success = False
        if success == True:
            self.dictionary.append(word_frequency)

        end = time.time_ns()
        print(f"A {word_frequency.word:<20} {(end - start):<20} ns \t list")

        return success

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        success = False
        for i, index in enumerate(self.dictionary):
            if index.word == word:
                success = True
                self.dictionary.pop(i)
        
        end = time.time_ns()
        print(f"D {word:<20} {(end - start):<20} ns \t list")

        return success

    def autocomplete(self, prefix_word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        predictions = []
        for index in self.dictionary:
            if index.word.startswith(prefix_word):
                predictions.append(index)

        # temporary because key only takes function object
        frequency = lambda index: index.frequency
        predictions.sort(reverse=True, key=frequency)

        end = time.time_ns()
        print(f"AC {prefix_word:<19} {(end - start):<20} ns \t list")

        return predictions[:3]