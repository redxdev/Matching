import random
import pygame

class WordList:
    def __init__(self):
        self.list = [
            ['Accurate', 'Capable or successful in reaching a target'],
            ['Afford', 'To have enough money to pay for'],
            ['Alert', 'To warn (someone) of a danger, threat, or problem'],
            ['Analyze', 'To examine in detail'],
            ['Annual', 'Occurring once every year'],
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

        random.shuffle(cards)

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
        pygame.draw.rect(screen, (180, 180, 180), (x, y, width, height), 0)

        if self.selected:
            pygame.draw.rect(screen, (255, 255, 0), (x, y, width, height), 4)

        myfont = pygame.font.SysFont("monospace", 30)

        drawText(screen, self.display, (0,0,0), (x, y, width, height), myfont, True)


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
