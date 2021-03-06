import random
import pygame

class WordList:
    def __init__(self):
        self.wordList = [
            ['Annual', 'Occurring once every year'],
            ['Apparent', 'Clearly visible or understood'],
            ['Assist', 'To help someone'],
            ['Attempt', 'To make an effort to complete a task'],
            ['Attractive', 'Pleasing or appealing to the senses'],
            ['Baggage', 'Personal belongings packed into suitcases for traveling'],
            ['Benefit', 'An advantage gained from something'],
            ["Ability", "the power or skill to do something"],
            ["Accurate", "exactly correct"],
            ["Address", "direct a question at someone"],
            ["Afford", "have the financial means to do something or buy something"],
            ["Alert", "an automatic signal (usually a sound) warning of danger"],
            ["Analyze", "To examine carefully; study closely"],
            ["Ancestor", "someone from whom you are descended (but usually more remote than a grandparent)"],
            ["Appropriate", "suitable for a particular person or place or condition"],
            ["Arena", "Type of performance space with audience surrounding all sides of the stage."],
            ["Arrest", "the act of apprehending (especially apprehending a criminal)"],
            ["Ascend", "To move upward"],
            ["Assist", "to aid; to help"],
            ["Attentive", "alert and watchful; considerate; thoughtful"],
            ["Awkward", "lacking grace or skill in manner or movement or performance"],
            ["Basic", "essential, fundamental"],
            ["Blend", "mix together different elements"],
            ["Blossom", "develop or come to a promising stage"],
            ["Burrow", "a hole in the ground made by an animal for shelter"],
            ["Calculate", "to work out by using arithmetic"],
            ["Capable", "have the skills and qualifications to do things well"],
            ["Captivity", "the state of being held against one's will; loss of freedom"],
            ["Carefree", "free from worries; having no problems"],
            ["Century", "100 years"],
            ["Chamber", "a natural or artificial enclosed space"],
            ["Circular", "having the shape of a circle"],
            ["Coax", "To persuade or urge in a gentle way"],
            ["Column", "an article giving opinions or perspectives, usually in a newspaper"],
            ["Communicate", "To make known; to give or exchange information"],
            ["Competition", "an occasion on which a winner is selected from among two or more contestants"],
            ["Complete", "to finish"],
            ["Concentrate", "To focus all one's thoughts or efforts on."],
            ["Concern", "a feeling of sympathy for someone or something"],
            ["Conclude", "decide by reasoning"],
            ["Confuse", "mistake one thing for another"],
            ["Congratulate", "to express pleasure over someone's success"],
            ["Considerable", "great in amount, size, importance"],
            ["Content", "satisfied"],
            ["Contribute", "to give, along with others who are giving"],
            ["Crafty", "skilled at tricking others"],
            ["Create", "bring into existence"],
            ["Demonstrate", "provide evidence for"],
            ["Descend", "to go down"],
            ["Desire", "expect and wish"],
            ["Destructive", "causing harm or damage"],
            ["Develop", "come into existence"],
            ["Disaster", "something that causes great damage or harm"],
            ["Disclose", "to make known"],
            ["Distract", "draw someone's attention away from something"],
            ["Distress", "To cause pain or sorrow; to trouble or worry."],
            ["Dusk", "the time of day immediately following sunset"],
            ["Eager", "full of energy and desire to do something"],
            ["Ease", "make easier"],
            ["Entertain", "to interest and amuse"],
            ["Entire", "Having nothing left out; whole; complete"],
            ["Entrance", "something that provides access; a way to get into something"],
            ["Envy", "jealousy"],
            ["Essential", "absolutely necessary"],
            ["Extraordinary", "beyond what is ordinary or usual"],
            ["Flexible", "bending and snapping back readily without breaking"],
            ["Focus", "direct one's attention on something"],
            ["Fragile", "easily broken or damaged or destroyed"],
            ["Frantic", "wildly excited"],
            ["Frequent", "happening often"],
            ["Frontier", "a wilderness at the edge of a settled area of a country"],
            ["Furious", "very angry"],
            ["Generosity", "act of giving to others, willingness to contribute"],
            ["Hail", "greet enthusiastically or joyfully"],
            ["Hardship", "something that is hard to bear; difficulty"],
            ["Heroic", "showing extreme courage"],
            ["Host", "a person who invites guests to a social event"],
            ["Humble", "not proud; modest"],
            ["Impact", "influencing strongly"],
            ["Increase", "make bigger or more"],
            ["Indicate", "to show"],
            ["Inspire", "to motivate, guide, or influence; to give hope and courage."],
            ["Instant", "without delay; happening at once"],
            ["Invisible", "impossible or nearly impossible to see"],
            ["Jagged", "having a sharp, pointed edge or outline"],
            ["Lack", "to be without"],
            ["Limb", "an arm, leg, or wing"],
            ["Limp", "not having strength, or walking unevenly"],
            ["Manufacture", "the act of making something (a product) from raw materials"],
            ["Master", "be or become completely proficient or skilled in"],
            ["Mature", "characteristic of maturity, characteristic of maturity"],
            ["Meadow", "A field of grass or wildflowers."],
            ["Mistrust", "doubt about someone's honesty"],
            ["Mock", "to make fun of"],
            ["Modest", "Simple; not fancy or extreme"],
            ["Noble", "showing greatness of character by unselfish behavior"],
            ["Orchard", "a place where fruit trees grow"],
            ["Outstanding", "distinguished from others in excellence"],
            ["Peculiar", "unusual, strange"],
            ["Peer", "an equal in age or position"],
            ["Permit", "a legal document giving official permission to do something"],
            ["Plead", "to beg"],
            ["Plentiful", "in great supply, easily available; more than enough"],
            ["Pointless", "serving no useful purpose"],
            ["Portion", "a part or share of the whole"],
            ["Practice", "learn by repetition"],
            ["Precious", "very valuable"],
            ["Prefer", "like better"],
            ["Prepare", "to make or get ready"],
            ["Proceed", "continue with one's activities"],
            ["Queasy", "sick to one's stomach; nauseated"],
            ["Recent", "of a time just before the present"],
            ["Recognize", "to identify someone or something seen before"],
            ["Reduce", "make smaller"],
            ["Release", "to let go"],
            ["Represent", "to stand for or in place of"],
            ["Request", "to ask for"],
            ["Resist", "to work or fight against"],
            ["Response", "a statement that is made in reply to a question, request, criticism, or accusation"],
            ["Reveal", "make visible"],
            ["Routine", "regular way of doing something"],
            ["Severe", "very bad or serious"],
            ["Shabby", "showing signs of wear and tear"],
            ["Shallow", "not deep"],
            ["Sole", "the underside of the foot"],
            ["Source", "the place where something begins, where it springs into being"],
            ["Sturdy", "Strongly built"],
            ["Surface", "the outside layer; the top"],
            ["Survive", "continue to live"],
            ["VTerror", "an overwhelming feeling of fear and anxiety"],
            ["Threat", "something that is a source of danger"],
            ["Tidy", "neat and in good order"],
            ["Tour", "A trip or journey in which one usually returns to the starting point."],
            ["Tradition", "values and beliefs passed from generation to generation"],
            ["Tragic", "causing great sadness; terrible or dreadful"],
            ["Typical", "regular; normal; usual"],
            ["Vacant", "Empty; unoccupied"],
            ["Valiant", "brave, courageous"],
            ["Variety", "A number of different kinds; assortment"],
            ["Vast", "very great or very large"],
            ["Venture", "to go somewhere despite the risk of possible dangers"],
            ["Weary", "very tired"]
        ]
        self.pictureList = [
            ["Acute", "images/Acute.png"],
            ["Line", "images/Line.png"],
            ["Obtuse", "images/Obtuse.png"],
            ["Parallel", "images/Parallel.png"],
            ["Perpendicular", "images/Perpendicular.png"],
            ["Point", "images/Point.png"],
            ["Ray", "images/Ray.png"],
            ["Right", "images/Right.png"],
            ["Segment", "images/Segment.png"],
            ["Acute Triangle", "images/TriangleAcute.png"],
            ["Obtuse Triangle", "images/TriangleObtuse.png"],
            ["Right Triangle", "images/TriangleRight.png"],
        ]
        self.mathList = [
            ["Perimeter", "The distance around a figure."],
            ["Circumference", "The distance around a circle."],
            ["Acute angle", "An angle that measures less than 90 degrees."],
            ["Angle", "A figure formed by 2 rays that have the same endpoint."],
            ["Capacity", "A measure of how much liquid a container can hold."],
            ["Array", "An arrangement of objects or pictures in equal columns and rows."],
            ["Concentric circles", "Circles that have the same center but different diameters."],
            ["Congruent", "Same size, same shape."],
            ["Consecutive", "Following in order without interruption."],
            ["Denominator", "The number below the bar in a fraction, which names the total number of equal parts."],
            ["Diameter", "The distance across the circle going through the middle."],
            ["Difference", "Answer to a subtraction problem."], ["Dividend", "The number being divided in division."],
            ["Divisor", "The number that divides the dividend in division."],
            ["Equivalent fractions", "Different fractions that name the same number."],
            ["Expanded form", "A number written to show the value of each digit."],
            ["Factor", "A number times another number."],
            ["Fraction", "A number that names a part of a whole, a part of a collection, or a part of a region."],
            ["Hexagon", "A six sided figure."], ["Horizontal", "Side to side."],
            ["Hundredth", "On of the 100 equal parts of a whole."],
            ["Intersecting lines", "Lines that meet or cross at a common point."],
            ["Interval", "The space or distance between two points on a scale or number line."],
            ["Line", "A straight path that extends infinitely in opposite directions."],
            ["Line of symmetry", "A line that divides a shape into two equal parts that match when folded on the line."],
            ["Line segment", "Part of a line defined by two endpoints along the line."],
            ["Mass", "The amount of matter in an object."],
            ["Mixed number", "A number containing a whole number part and a fraction part."],
            ["Numerator", "The top number of the fraction. The numerator names the number of equal parts."],
            ["Obtuse angle", "An angle that measures more than 90 degrees and less that 180 degrees."],
            ["Octagon", "An eight sided figure."],
            ["Parallel", "Lines that stay the same distance apart and never meet."],
            ["Parallelogram", "A quadrilateral that has two pairs of parallel lines."],
            ["Pentagon", "A five sided figure."],
            ["Period", "Each group of three digits in a number separated by a comma."],
            ["Perpendicular", "Lines that intersect at 90 degrees."],
            ["Polygon", "A simple closed two-dimensional figure made up of three or more line segments."],
            ["Product", "Answer to a multiplication problem."],
            ["Proper fraction", "A fraction where the numerator is less than the denominator."],
            ["Quadrilateral", "A polygon with four sides and four vertices."],
            ["Quotient", "Answer to a division problem."],
            ["Radius", "The distance from the center to the edge of a circle."],
            ["Ray", "Are parts of a line that extend in one direction from one endpoint to infinity."],
            ["Reflection", "'Flipping' a figure"],
            ["Rhombus", "A parallelogram with all four sides the same length."],
            ["Right angle", "An angle that measures 90 degrees."], ["Rotation", "'Spinning' a figure."],
            ["Standard form", "The simplest way to show a number using digits."],
            ["Sum", "Answer to an additional problem."],
            ["Tenth", "One of the 10 equal parts of a whole or collection."],
            ["Transformation", "Changing the position of a figure by rotating, reflecting or translating."],
            ["Translation", "'Sliding' a figure"],
            ["Trapezoid", "A quadrillateral with exactly on pair of parallel sides."],
            ["Vertex", "The corner of an angle."], ["Vertices", "More than one vertex."], ["Vertical", "Up and down."],
            ["Volume", "The number of cubic units that fit inside a three-dimensional figure."],
            ["Weight", "A measure of how much gravity pulls on an object."],
            ["Area", "The number of squares to cover the surfact of a figure."], ["Equivalent", "Equal."]
        ]

    def getRandomCards(self, pairCount):
        if pairCount > len(self.wordList) + len(self.pictureList) + len(self.mathList):
            raise IndexError("count is > the number of words/pictures defined in WordList")

        cards = []
        availableWords = [list(self.wordList), list(self.mathList),list(self.pictureList)]

        for i in range(0, pairCount):
            listIdx = random.randrange(0, len(availableWords))
            wlist = availableWords[listIdx]
            index = random.randrange(0, len(wlist))
            wordPair = wlist[index]
            del wlist[index]
            if len(wlist) == 0:
                del availableWords[listIdx]
            if listIdx <= 1:
                wordPair = [wordPair[0], ("text", wordPair[1])]
            else:
                wordPair = [wordPair[0], ("image", pygame.image.load(wordPair[1]))]
            cards.append(WordCard(wordPair[0], ("text", wordPair[0])))
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

    def draw(self, screen, position, size, fontSize=30):
        x, y = position
        width, height = size
        pygame.draw.rect(screen, (180, 180, 180), (x, y, width, height), 0)

        myfont = pygame.font.SysFont("monospace", fontSize)

        if self.selected:
            pygame.draw.rect(screen, (255, 255, 0), (x - 5, y - 5, width + 8, height + 8), 8)
            type, display = self.display
            if type == "text":
                drawText(screen, display, (0, 0, 0), (x + 5, y + 5, width - 10, height - 10), myfont, True)
            elif type == "image":
                display = pygame.transform.scale(display, (width, width))
                screen.blit(display, (x, y + ((height/2) - (width/2)), width, width))


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
