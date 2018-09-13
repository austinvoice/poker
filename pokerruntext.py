# textpoker.py
# run application modules

from pokerapp import PokerApp, Dice
from textpoker import TextInterface

inter = TextInterface()
app = PokerApp(inter)
app.run()

