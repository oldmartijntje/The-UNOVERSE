class timelineObject:
    def __init__(self, grabPileList, discardPileList, players, turn = 0):
        self.players = players
        self.grabPileList = grabPileList
        self.discardPileList = discardPileList
        self.turn = turn
        self.historyPerPlayer = {}

    