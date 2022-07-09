from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
import time
import random


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):
    def __init__(self):
        self.dictionary = {}

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        # NORMAL INITIALISATION
        for index in words_frequencies:
            self.dictionary.update({index.word: index.frequency})

        # HASHADD.CSV
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         self.dictionary.update({object.word: object.frequency})
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         self.dictionary.update({object.word: object.frequency})
        
        # HASHDELETE.CSV
        # for index in words_frequencies:
        #     self.dictionary.update({index.word: index.frequency})
        # print("size,nanoseconds")
        # for i, object in reversed(list(enumerate(self.dictionary.keys()))):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         self.dictionary.pop(object)
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         self.dictionary.pop(object)

        # HASHSEARCH.CSV
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         self.dictionary.update({object.word: object.frequency})
        #         param = random.choice(list(self.dictionary.keys()))
        #         start = time.time_ns()
        #         frequency = 0
        #         for index in self.dictionary:
        #             if index == param:
        #                 frequency = self.dictionary.get(index)
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self.dictionary.update({object.word: object.frequency})

        # HASHAC.CSV
        # print("size,nanoseconds")
        # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         self.dictionary.update({object.word: object.frequency})
        #         start = time.time_ns()
        #         predictions = []
        #         for index in self.dictionary.items():
        #             if index[0].startswith(random.choice(alphabet)):
        #                 predictions.append(index)
        #         for j, pred in enumerate(predictions):
        #             predictions[j] = WordFrequency(pred[0], pred[1])
        #         frequency = lambda index: index.frequency
        #         predictions.sort(reverse=True, key=frequency)
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self.dictionary.update({object.word: object.frequency})

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
            if index == word:
                frequency = self.dictionary.get(index)

        end = time.time_ns()
        print(f"S {word:<20} {(end - start):<20} ns \t hashtable")

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
            if index == word_frequency.word:
                success = False
        if success == True:
            self.dictionary.update({word_frequency.word: word_frequency.frequency})

        end = time.time_ns()
        print(f"A {word_frequency.word:<20} {(end - start):<20} ns \t hashtable")

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

        # cast list() to prevent resizing dictionary during iteration
        for index in list(self.dictionary.keys()):
            if index == word:
                success = True
                self.dictionary.pop(index)
        
        end = time.time_ns()
        print(f"D {word:<20} {(end - start):<20} ns \t hashtable")

        return success

    def autocomplete(self, word: str) -> [WordFrequency]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        predictions = []

        # extract and iterate through list of tuple pairs
        for index in self.dictionary.items():
            if index[0].startswith(word):
                predictions.append(index)

        for i, pred in enumerate(predictions):
            predictions[i] = WordFrequency(pred[0], pred[1])
        
        frequency = lambda index: index.frequency
        predictions.sort(reverse=True, key=frequency)
        
        end = time.time_ns()
        print(f"AC {word:<19} {(end - start):<20} ns \t hashtable")

        return predictions[:3]
