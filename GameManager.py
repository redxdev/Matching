from WordList import WordList, WordCard


class GameManager:
    def __init__(self):
        self.wordList = WordList()
        self.cards = []

    def startGame(self, pairCount):
        self.cards = self.wordList.getRandomCards(4)

    def draw(self, screen):
        for card in self.cards:
            if card.active:
                card.draw(screen, (50, 50))
