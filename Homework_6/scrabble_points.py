'''
    Alessia Pizzoccheri - CS 5001 02
'''

class Points:
    def __init__(self,word,points):
        self.points = points
        self.word = word.upper()
        self.total = []

    def check_word(self):

        for l in range(len(self.word)):
            if self.word[l] in self.points:
                # exception for invalid input
                try:
                    letter = self.word[l].upper()
                    # append each point to total list
                    self.total.append(self.points[letter])
                except KeyError:
                    return
        # sum all points together
        points_total = sum(self.total)

        return points_total

class Letters:
    def __init__(self,frequency):
        self.frequency = frequency

    def create_bag(self):
        bags_of_letters = []

        # iterate through the dictionary
        for item in self.frequency:
            # multiply each letter by its value
            repeat_letters = item * self.frequency[item]
    
            for item in repeat_letters:
                item.split()
                # create bag of letters
                bags_of_letters.append(item)
            
        return bags_of_letters

def bag_of_letters(letters):
    ''' Function: bag_of_letters
        Input: dict
        Returns: lst
    '''
    # instantiate Letters class
    abc = Letters(letters)
    bag_of_letters = abc.create_bag()

    return bag_of_letters

def get_word_value(word,points):
    ''' Function: bag_of_letters
        Input: str, dict
        Returns: int
    '''

    # instantiate POints class
    word = Points(word,points)
    total = word.check_word()

    return total