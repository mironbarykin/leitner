# Leitner System
[leitner system](https://en.wikipedia.org/wiki/Leitner_system) is a method of efficient learning using flashcards and an implementation of spaced repetition, where card are reviewed with an increasing interval.

This script is in-console implementation of Leiter System.

**Usage: python leitner.py `source` `destination`**

where `source`, is a path to the .csv file with the cards in format `content`, `solution`, `pile` and 
optional `destination`, is a path to the .csv file where the result of the programm will be written in `content`, `solution`, `pile` format.
if `destination` is not provided, the result of the programm will be written in source file in the same format.

# Piles

Pile 0 - is a pile in which cards that have been never reviewed are stored.
Pile 1 - is a pile in which cards that have been reviewed once or answered wrong are stored.
Pile $n > 1$ - is a pile in which reviewed card are stored. The smaller $n$ is, the card should be reviewed more often.

# Algorithm

When the user is represented with the card in pile 0, this card should be assigned to pile 1.

When user have answered the card wrong, this card should be assigned to pile 1.
When user have answered the card right, this card shoule be assigned to pile $n + 1$.

When there are no cards in pile $n$, the user should be represented with the cards in pile $n + 1$.


