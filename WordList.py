import random
import pygame


class WordList:
    def __init__(self):
        self.list = [
            ['Accurate', 'Capable or successful in reaching a target'],
            ['Afford', 'To have enough money to pay for'],
            ['Alert', 'To warn (someone) of a danger, threat, or problem'],
            ['Analyze', 'To examine in detail'],
            ['Annual', 'Occuring once every year'],
            ['Apparent', 'Clearly visible or understood'],
            ['Assist', 'To help someone'],
            ['Attempt', 'To make an effort to complete a task'],
            ['Attractive', 'Pleasing or appealing to the senses'],
            ['Awkward', 'Hard to do or deal with'],
            ['Baggage', 'Personal belongings packed into suitcases for traveling'],
            ['Benefit', 'An advantage gained from something']
        ]

    def getList(self):
        return self.list

    def getRandomCards(self, pairCount):
        if pairCount > len(self.list):
            raise IndexError("count is > the number of words defined in WordList")

        cards = []
        availableWords = list(self.list)

        for i in range(0, pairCount):
            index = random.randrange(0, len(availableWords))
            wordPair = availableWords[index]
            del availableWords[index]
            cards.append(WordCard(wordPair[0], wordPair[0]))
            cards.append(WordCard(wordPair[0], wordPair[1]))

        return cards


class WordCard:
    def __init__(self, word, display):
        self.word = word
        self.display = display
        self.selected = False
        self.active = True

    def matches(self, other):
        return self.word == other.word

    def draw(self, screen, position, size):
        x, y = position
        width, height = size
        pygame.draw.rect(screen, (128, 128, 128), (x, y, width, height), 0)

        myfont = pygame.font.SysFont("monospace", 30)

        # render text
        label = myfont.render(self.display, 1, (0, 0, 0))
        screen.blit(label, (x, y))
