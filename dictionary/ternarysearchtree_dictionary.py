from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node
import time
import random


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'Son Hoang Dau'
# __copyright__ = 'Copyright 2022, RMIT University'
# ------------------------------------------------------------------------


class TernarySearchTreeDictionary(BaseDictionary):
    def __init__(self):
        self.root = Node()
        self.pointer = None

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        # TO BE IMPLEMENTED

        # NORMAL INITIALISATION
        for word in words_frequencies:
            self._add(word.word, word.frequency, self.root)
        
        # TSTADD.CSV
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         self._add(object.word, object.frequency, self.root)
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         self._add(object.word, object.frequency, self.root)

        # TSTDELETE.CSV
        # for word in words_frequencies:
        #     self._add(word.word, word.frequency, self.root)
        # print("size,nanoseconds")
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         start = time.time_ns()
        #         randomint = self._search(object.word, self.root)
        #         self.pointer.end_word = False
        #         end = time.time_ns()
        #         print(f"{i},{(end - start)}")
        #     else:
        #         randomint = self._search(object.word, self.root)
        #         self.pointer.end_word = False

        # TSTSEARCH.CSV
        # print("size,nanoseconds")
        # wordsPresent = []
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         self._add(object.word, object.frequency, self.root)
        #         self._traversal("", self.root, wordsPresent)
        #         param = random.choice(wordsPresent)
        #         start = time.time_ns()
        #         frequency = self._search(param, self.root)
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self._add(object.word, object.frequency, self.root)

        # TSTAC.CSV
        # print("size,nanoseconds")
        # alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        # for i, object in enumerate(words_frequencies):
        #     if i % (len(words_frequencies) / 20) == 0:
        #         self._add(object.word, object.frequency, self.root)
        #         param = random.choice(alphabet)
        #         start = time.time_ns()
        #         predictions = []
        #         randomint = self._search(param, self.root)
        #         self._autocomplete("", self.pointer, param, predictions)
        #         frequency = lambda index: index.frequency
        #         predictions.sort(reverse=True, key=frequency)
        #         end = time.time_ns()
        #         print(f"{i},{(end-start)}")
        #     else:
        #         self._add(object.word, object.frequency, self.root)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        # separated out because other methods are dependent on _search
        # this is to avoid extra prints
        freq = self._search(word, self.root)
        
        end = time.time_ns()
        print(f"S {word:<20} {(end - start):<20} ns \t tst")

        return freq
    
    def _search(self, word, node):
        for i, letter in enumerate(word):
            found = False
            lastLetter = (i == len(word)-1)

            while found is False:
                if node is None:
                    return 0
                elif node.letter == letter:
                    if node.end_word is True and lastLetter is True:
                        self.pointer = node
                        return node.frequency
                    elif lastLetter is True and node.end_word is False:
                        if node is not None:
                            self.pointer = node
                        return 0
                    node = node.middle
                    found = True
                elif letter < node.letter:
                    node = node.left
                elif letter > node.letter:
                    node = node.right
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        # TO BE IMPLEMENTED
        # place holder for return
        start = time.time_ns()

        success = False
        if self._search(word_frequency.word, self.root) == 0:
            self._add(word_frequency.word, word_frequency.frequency, self.root)
            success = True
        
        end = time.time_ns()
        print(f"A {word_frequency.word:<20} {(end - start):<20} ns \t tst")

        return success
    
    def _add(self, word, freq, node):
        head = word[0]
        if node.letter is None:
            node.letter = head

        if head < node.letter:
            if node.left is None:
                node.left = Node()
            self._add(word, freq, node.left)
        elif head > node.letter:
            if node.right is None:
                node.right = Node()
            self._add(word, freq, node.right)
        else:
            if len(word) == 1:
                node.end_word = True
                node.frequency = freq
                return
            if node.middle is None:
                node.middle = Node()
            self._add(word[1:], freq, node.middle)

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
        if self._search(word, self.root) != 0:
            self.pointer.end_word = False
            success = True
        
        end = time.time_ns()
        print(f"D {word:<20} {(end - start):<20} ns \t tst")

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
        randomint = self._search(word, self.root)
        self._autocomplete("", self.pointer, word, predictions)

        frequency = lambda index: index.frequency
        predictions.sort(reverse=True, key=frequency)

        end = time.time_ns()
        print(f"AC {word:<19} {(end - start):<20} ns \t tst")

        return predictions[:3]
    
    def _autocomplete(self, word, node, prefix, collect):
        if node is None:
            return
        
        self._autocomplete(word, node.left, prefix, collect)

        if (node.end_word is True) and ((prefix[:-1] + (word + node.letter)).startswith(prefix) is True):
            add = WordFrequency(prefix[:-1] + word + node.letter, node.frequency)
            collect.append(add)
        
        self._autocomplete(word + node.letter, node.middle, prefix, collect)
        self._autocomplete(word, node.right, prefix, collect)
    
    def _traversal(self, word, node, collect):
        if node is None:
            return
        
        self._traversal(word, node.left, collect)
        if node.end_word is True:
            collect.append(word + node.letter)
        self._traversal(word + node.letter, node.middle, collect)
        self._traversal(word, node.right, collect)