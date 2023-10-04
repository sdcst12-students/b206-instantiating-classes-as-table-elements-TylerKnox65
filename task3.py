import random
'''
Rules:

each primary stat is generated as 3 random dice rolls (random 1-6) (strength, intelligance, piety, agility, stamina, charm)
distribution of level is 1: 40%, 2: 30%, 3: 20%, 4: 10%
each npc gets random 1-10 hp per level
each npc gets some random money
30% chance to have 0-6 gold
50% chance go have 3-12 silver
if they had no gold, they have a 75% chance to have 4-20 copper
each gold is worth 10 silver and each silver is worth 10 copper
Create 100 NPC's Generate a report that shows the distribution of NPC's by level 
Generatea a report that shows the mean and standard deviation for the following:

HP
Wealth (in copper. For example 2 gold, 3 silver and 4 copper has a wealth of 234)

'''
class NPC:
    stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        self.levelpick()
    def levelpick(self):
        levelchoice = ['1'] * 40 + ['2'] * 30 + ['3'] * 20 + ["4"] *10
        levelchoice = random.choice(levelchoice)
        self.level = int(levelchoice)
        return self.level
    def goldpick(self):
        selector = random.randint(1,10)
        if selector <= 3:
            goldchoice = random.randint(0,6)
        else:
            goldchoice = 0
        selector = random.randint(1,10)
        if selector > 5:
            silverchoice = random.randint(3,12)
        else:
            silverchoice = 0
        if goldchoice == 0:
            selector = random.randint(1,100)
            if selector < 75:
                copperchoice = random.randint(4,20)
            else:
                copperchoice = 0
        else:
            copperchoice = 0
        self.gold = goldchoice
        self.silver = silverchoice
        self.copper = copperchoice
        return ((goldchoice * 100) + (silverchoice * 10) + copperchoice)
    def HPpick(self):
        hpchoice = 0
        deviation = []
        for i in range(self.level):
            temp = random.randint(1,10)
            hpchoice += temp
            deviation.append(temp)
        self.deviation = deviation
        self.hp = hpchoice
        return self.hp
    def statspick(self):
        stat = ("strength", "intelligance", "piety", "agility", "stamina", "charm")
        statchoice = []
        for i in range(3):
            statchoice.append(random.choice(stat))
        return statchoice
    '''
    def calcMeanDeviation(self):
        #HP DEVIATION
        count = 0
        temp = 0
        for i in self.deviation:
            count += 1
            temp += i
        self.mean = temp/count
        deviationList = []
        temp = 0                        THIS IS SO SAD, BOOGOO :( :()
        
        for i in self.deviation:
            deviationList.append((i-self.mean)**2)
        for i in deviationList:
            temp += i
        self.deviationCalc = (temp / (len(deviationList))) ** (1/2)
        return round(self.mean,2) , round(self.deviationCalc,2)

    def calcMeanWealth(self):
        goldConv = self.gold*100
        silvConv = self.silver*10
        copper = self.copper
    '''




levelList = []
wealthList = []
totalLevel = 0
totalWealth = 0
for i in range(100):
    x = NPC()
    stats = x.statspick()
    x.HPpick()

    level = x.levelpick()
    totalLevel += level
    levelList.append(level)

    wealth = x.goldpick()
    totalWealth += wealth
    wealthList.append(wealth)

def meanCalc(listin, total):
    mean = total / len(listin) #9
    deviationList = []
    temp = 0                       
        
    for i in listin:
            deviationList.append((i-mean)**2)
    for i in deviationList:
            temp += i
    deviation = (temp / (len(deviationList))) ** (1/2)
    return round(mean,2), round(deviation,2)
print(f"Level mean and deviation is: {meanCalc(levelList, totalLevel)}. Wealth mean and deviation is: {meanCalc(wealthList, totalWealth)}")