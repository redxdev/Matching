from WordList import WordList, WordCard
import pygame

class GameManager:
    def __init__(self):
        self.wordList = WordList()
        self.cards = []

    def startGame(self, pairCount):
        self.cards = self.wordList.getRandomCards(4)

    def draw(self, screen):
        cardW, cardH = screen.get_size()
        cardW /= 9
        cardH /= 5
        for i in range(0, len(self.cards)):
            card = self.cards[i]
            if card.active:
                x = (i % 4) * (cardW * 2) + cardW
                y = int(i / 4) * (cardH * 2) + cardH
                card.draw(screen, (x, y), (cardW, cardH))
