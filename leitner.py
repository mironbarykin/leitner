import csv
import sys
import os

import copy
import time

def main():
    
    # Verify the proper usage
    if len(sys.argv) == 2:
        # Assigns the provided path as both source and destination
        source, destination = sys.argv[1], sys.argv[1]
    elif len(sys.argv) == 3:
        # Assigns the provided paths separated as source and destination
        source, destination = sys.argv[1], sys.argv[2]
    else:
        # Provides to user a proper usage
        sys.exit('Usage: python leitner.py source destination')
    
    # Parses entries from the source
    entries = parse(source)
    repetition = 0
    
    qflag = False

    while not qflag:
        
        # Display information about the exit and answers for the user
        print('To exit with saving enter "-q".')
        print('To show the answer press "ENTER"')

        # Iterates through the distribution of entries
        for pile, cards in distribute(entries).items():
            
            print(f'Starting with the pile {pile}...')
            # Checks if current repetition implies current pile's revision
            if repetition <= pile:
                for card in cards:
                    # Represents the user with card's content
                    print(f'Question: {card.content}')
                    # Asks the user to react on the question
                    toggle = input()
                    # Checks if user wants to quite
                    if toggle == '-q':
                        qflag = True
                        print('Closing the application.')
                        break
                    else:
                        # Represents the user with the solution
                        print(f'Answer: {card.solution}')
                        # Waiting for the user's decision
                        while True:
                            # Represents the user with decision input
                            decision = input(f'R/W').lower()
                            # Checks whether the decision is 'r' for right or 'w' for wrong
                            if decision == 'r':
                                card.success()
                                break
                            if decision == 'w':
                                card.fail()
                                break
                            else:
                                print('Please enter your decision, `r` for right or `w` for wrong.')

            # Checks if user quite
            if qflag:
                break
            else:
                print('Ending the repetition...')
                repetition += 1
                break
        
        if qflag:
            break


    # Saves all changes in entries to the provided destination
    compose(destination, entries)


def parse(source):
    """Parses the .csv file provided as a source.

        Parameters:
            source (str): the path to the source file

        Returns:
            entries (list): list of cards in the source
    """
    # Reading the file
    with open(source, 'r') as file:
        # Initializing CSV Reader
        reader = csv.reader(file)
        # Skiping header
        next(reader)
        # Reading entries with 3rd row as integer
        entries = [Card(i[0], i[1], int(i[2])) for i in reader]

    return entries

def compose(destination, entries: list):
    """Composes entries to the .csv file provided as a destination.
        
        Parameters:
            destination (str): the path to the composing file
            entries (list): list of cards

        Returns:
            None
    """
    # Writing the file
    with open(destination, 'w') as file:
        # Initializing CSV Reader
        writer = csv.writer(file)
        # Writing header
        writer.writerow(['content','solution','pile'])
        # Writing entries
        writer.writerows([entry.list() for entry in entries])

def distribute(entries: list):
    """Distributes entries by the piles in a dictionary.

        Parameters:
            entries (list): list of cards
        Returns:
            distribution (dict): dictionary of cards by pile
    """
    distribution = dict()

    # Loops through the cards
    for entry in sorted(entries, key=lambda x: x.pile):
        # Checks whether the card's pile already was discovered
        if entry.pile not in list(distribution.keys()):
            # Assigns an empty list to the card's pile key in dictionary
            distribution[entry.pile] = list()
        # Adds the card into the dictionary in specific key
        distribution[entry.pile].append(entry)

    return distribution


class Card:
    """A class to represent an entry as a card.

        Attributes:
            content (str): content of the card
            solution (str): solution for the card
            pile (int): the pile in which the card is
        
        Methods:
            list : returns the card as a list
            fail : drops the card to initial pile
            success : promotes the card to the upper pile
    """
    def __init__(self, content: str, solution: str, pile: int):
        self.content = content
        self.solution = solution
        self.pile = pile

    def __str__(self):
        return f'[{self.pile}] {self.content} - {self.solution}'
    
    def list(self):
        """Generates a list from the card.
            
            Returns:
                [content, solution, pile] (list): card's representing list
        """
        return [self.content, self.solution, self.pile]

    def fail(self):
        """Fails the card. Dropping card to pile 1.
        """
        self.pile = 1
    
    def success(self):
        """Rise the card to the upper pile.
        """
        self.pile += 1


if __name__ == '__main__':
    main()

