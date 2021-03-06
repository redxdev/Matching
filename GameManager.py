from WordList import WordList, WordCard
import pygame


class GameManager:
    def __init__(self):
        self.wordList = WordList()
        self.cards = []
        self.badCards = (None, None)
        self.goodCards = (None, None)
        self.timer = 0

    def startGame(self, pairCount):
        self.cards = self.wordList.getRandomCards(4)

    def generateCardPosition(self, screenSize, i):
        cardW, cardH = screenSize
        cardW /= 9
        cardH /= 5
        return ((i % 4) * (cardW * 2) + cardW, int(i / 4) * (cardH * 2) + cardH, cardW, cardH)

    def draw(self, screen):
        if self.timer <= 0:
            bad1, bad2 = self.badCards
            if bad1 is not None and bad2 is not None:
                bad1.selected = False
                bad2.selected = False
                self.badCards = (None, None)

            good1, good2 = self.goodCards
            if good1 is not None and good2 is not None:
                good1.selected = False
                good2.selected = False
                good1.active = False
                good2.active = False
                self.goodCards = (None, None)
                self.checkForGameEnd()


        if self.timer > 0:
            self.timer -= 0.08

        for i in range(0, len(self.cards)):
            card = self.cards[i]
            if card.active:
                screenW, screenH = screen.get_size()
                x, y, cardW, cardH = self.generateCardPosition((screenW, screenH), i)
                card.draw(screen, (x, y), (cardW, cardH), screenW / 64)

    def onClick(self, screen, x, y):
        bad1, bad2 = self.badCards
        if bad1 is not None and bad2 is not None:
            return

        good1, good2 = self.goodCards
        if good1 is not None and good2 is not None:
            return

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
            card.selected = True
            self.goodCards = (card, other)
            self.timer = 3.0
        else:
            card.selected = True
            self.badCards = (card, other)
            self.timer = 3.0

    def checkForGameEnd(self):
        for c in self.cards:
            if c.active:
                return

        self.startGame(4)