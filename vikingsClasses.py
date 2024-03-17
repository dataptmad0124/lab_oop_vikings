import random
# Soldier


class Soldier:
    def __innit__(self,health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        
        return self.strength
    
    def receiveDamage(self, damage):
        self.health = self.health - damage
        

# Viking


class Viking(Soldier):
    def __innit__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
        
    
    def receiveDamage(self, damage):
        
        self.health = self.health - damage
        
        if self.health > 0:
            print(f"{self.name}has received {damage} points of damage)
        
        else:
            print(f"{self.name} has died in act of combat")
    
    def battleCry(self):
                  return "Odin Owns You All!
    
    
    

# Saxon


class Saxon(Soldier):
    def __innit__(self, health, strength):
        super().__innit__(health, strength)
                  
    def receiveDamage(self, damage):
        self.health = self.health - damage
                  if self.health > 0:
                  print(f"A Saxon has received {damage} points of damage")
                  
                  else:
                  print(f"A Saxon has died in combat")
                  
    

# War


class War:
    def __innit__(self):
        self.vikingArmy = []
        self.saxonArmy = []
                  
    def addViking(self, viking):
        self.vikingArmy.append(viking)
                  
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
                  
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        attack_viking = saxon.receiveDamage(viking.attack())
                  
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
                  
        return attack_viking
                  
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        attack_saxon = viking.receiveDamage(saxon.attack())
          
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
                  
         return attack_saxon
                  
    def showStatus(self):
        if len(saxonArmy) == 0 and len(vikingArmy) > 0:
            return "Vikings have won the war of the century!"
                  
        elif len(vikingArmy) == 0 and len(saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
                  
        else:
            return "Vikings and Saxons are still in the thick of battle."