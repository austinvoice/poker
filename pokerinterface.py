
class PokerInterface:

	def choose(self, choices):
		buttons = self.buttons

		# activate choice buttons, deactivate others
		for b in buttons:
			if b.getLabel() in choices:
				b.activate()
			else:
				b.deactivate()

		# get mouse clicks until an active button is clicked
		while True:
			p = self.win.getMouse()
			for b in buttons:
				if b.clicked(p):
					return b.getLabel() # function exit here