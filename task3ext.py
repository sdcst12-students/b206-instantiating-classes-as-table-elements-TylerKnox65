import random
import names 
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
    equipment = {"Headwear": {"Iron cap":2, "Leather cap":1, "Helmet":3}, "Armor": {"Studded Leather":9, "Chainmail":21, "Scalemail":15, "Platemail":29}, "Shield": {"Buckler":1, "Embossed Leather":2, "Kite":4}}
    #headwear: iron cap (2), leather cap (1), helmet (3) armor: studded leather(9), chainmail(21), scalemail(15), platemail(29) shield: buckler(1), embossed leather shield(2), kite shield(4)
    level = 0
    hp = 0
    gold = 0
    silver = 0
    copper = 0

    def __init__(self):
        self.levelpick()
        self.stats = { 'str' : 0, 'int' : 0, 'pie' : 0, 'agi' : 0, 'stm' : 0, 'cha' : 0 }
        self.name = names.get_full_name()
        self.HPpick()
        self.statspick()
        self.getequip()
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
        for i in self.stats:
            for o in range(3):
                self.stats[i] += random.randint(1,6)
        return self.stats
    def getequip(self):
        self.headwear = random.choice(list(self.equipment["Headwear"]))
        self.armor = random.choice(list(self.equipment["Armor"]))
        self.shield = random.choice(list(self.equipment["Shield"]))
        self.armorRating = self.equipment["Headwear"][self.headwear] + self.equipment["Armor"][self.armor] + self.equipment["Shield"][self.shield]
        return self.armorRating, self.headwear, self.armor, self.shield
    def display(self):
        print(f"\033[38;2;255;255;255;48m--------------------------------------------------------------------------------------------------------------\n\n\033[3;30;48m Name: {self.name}\n\n\033[1;31;48m HP: {self.hp} \n\n\033[38;2;128;0;128;48mTotal wealth: \033[1;33;48m{self.gold} Gold, \033[1;30;48m{self.silver} Silver, \033[38;2;184;115;51;48m{self.copper} Copper \n\n\033[38;2;255;0;0;48mStats: Strength:{self.stats['str']}, \033[38;2;68;154;249;48mIntelligence:{self.stats['int']}, \033[38;2;255;255;255;48mPiety:{self.stats['pie']}, \033[38;2;0;100;0;48mAgility:{self.stats['agi']}, \033[38;2;144;238;144;48mStamina:{self.stats['stm']}, \033[38;2;255;192;203;48mCharisma:{self.stats['cha']}\n\n\033[38;2;0;0;0;48mEquipment: \033[38;2;200;200;200;48mHelm: {self.headwear}, Armor: {self.armor}, Shield: {self.shield}\n\n\033[38;2;255;192;203;48mLevel: {self.level}\n")
        
        #184, 115, 51

levelList = []
wealthList = []
totalLevel = 0
totalWealth = 0
for i in range(100):
    
    x = NPC()
    

    level = x.levelpick()
    totalLevel += level
    levelList.append(level)

    wealth = x.goldpick()
    totalWealth += wealth
    wealthList.append(wealth)
    x.display()
    x = None
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

