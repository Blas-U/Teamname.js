class Building:
    def __init__(self):
        self.level = 1
        self.untilNextLevel = 10

    def upgradeBuilding(self, gold):
        if gold < self.untilNextLevel:
            print("not enough to upgrade")
        else:
            gold -= self.untilNextLevel
            self.level += 1
            self.untilNextLevel *= 2
            print("building upgraded!")
        return gold
    
    