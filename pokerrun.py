# textpoker.py
# run application modules

from pokerapp import Dice, PokerApp
from graphicspoker import GraphicsInterface

inter = GraphicsInterface()
app = PokerApp(inter)
app.run()

