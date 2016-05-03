from WordList import WordList, WordCard
import pygame


class GameManager:
    def __init__(self):
        self.wordList = WordList()
        self.cards = []

    def startGame(self, pairCount):
        self.cards = self.wordList.getRandomCards(4)

    def generateCardPosition(self, screenSize, i):
        cardW, cardH = screenSize
        cardW /= 9
        cardH /= 5
        return ((i % 4) * (cardW * 2) + cardW, int(i / 4) * (cardH * 2) + cardH, cardW, cardH)

    def draw(self, screen):
        for i in range(0, len(self.cards)):
            card = self.cards[i]
            if card.active:
                x, y, cardW, cardH = self.generateCardPosition(screen.get_size(), i)
                card.draw(screen, (x, y), (cardW, cardH))

    def onClick(self, screen, x, y):
        found = None
        for i in range(0, len(self.cards)):
            card = self.cards[i]
            cx, cy, cw, ch = self.generateCardPosition(screen.get_size(), i)
            if x >= cx and x <= cx + cw and y >= cy and y <= cy + ch:
                found = card
                break

        if found is not None:
            self.select(found)

    def select(self, card):
        if card.selected:
            card.selected = False
            return

        other = None
        for c in self.cards:
            if c.selected:
                other = c
                break

        if other == None:
            card.selected = True
            return

        if other.matches(card):
            other.selected = False
            card.selected = False
            card.active = False
            other.active = False
        else:
            other.selected = False
            card.selected = False

        for c in self.cards:
            if c.active:
                return

        self.startGame(4)
