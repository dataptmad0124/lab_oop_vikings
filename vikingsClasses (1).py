import random

# Soldier

class Soldier:

        def __init__(self, 
                     health, 
                     strength):
        
            '''
            La clase soldado tiene dos atributos propios, salud y daño.
            '''

            # atributos del objeto
            self.health = health
            self.strength = strength

        def attack(self): 
            
            '''
            La funcion ataque no recibe argumentos y devuelve
            la fortaleza del soldado.
            '''
            return self.strength
        
        def receiveDamage(self, damage):
            
            '''
            Esta función recibe el argumento de damage que influye en healt,
            y a la vez tiene que modificar healt.
            No regresa nada.
            '''
        
            self.health = self.health - damage
                 
        
# Viking

class Viking(Soldier):
    
    def __init__(self,
                 name,
                 health, 
                 strength):
        '''
        La clase vikingo tienen tres atributos, dos propios de la clase
        soldado y uno propio, name.
        '''
       
        #Metodo constructor de soldado. Herencia.
        super().__init__(health, strength)
        
        self.name = name
       
    
    def receiveDamage(self, damage):
        
        '''
        La funcion recibir daño del vikingo sera un poco diferente a esta misma función
        en la clase soldado. Daño se restará a salud.
        Si el vikingo esta vivo, devuelve nombre y los puntos de daño.
        Si el vikingo esta muerto devuelve nombre y muerto en acto de combate.
        '''
            
        self.health = self.health - damage
        
        if self.health > 0:
            
            return f'{self.name} has received {damage} points of damage'
        
        else:
            
            return f'{self.name} has died in act of combat'
        

    def battleCry(self):
        
        '''
        No recibe argumentos y devuelve una frase.
        '''
        
        return 'Odin Owns You All!'

    
# Saxon

class Saxon(Soldier):
    
    def __init__(self,
                 health, 
                 strength):
        
        # Metodo constructor de soldado. Herencia
        super().__init__(health, strength)
        
        
    
    def receiveDamage(self, damage):
        
            
        self.health = self.health - damage
        
        if self.health > 0:
            
            return f'A Saxon has received {damage} points of damage'
        
        else:
            
            return f'A Saxon has died in combat'
        


# War

class War:
    
    def __init__(self):
        
        self.vikingArmy = []
        self.saxonArmy = []
    
    
    def addViking(self, viking):
        
        '''
        A esta función se le añade un objeto vikingo. Esta función 
        añade un vikingo al ejercito vikingo.
        No devuelve nada.
        '''
        
        self.vikingArmy.append(viking)
        
    
    def addSaxon(self, saxon):
        
        '''
        A esta función se le añade un objeto Saxon. Esta función 
        añade un Saxon al ejercito Saxon.
        No devuelve nada.
        '''
        
        self.saxonArmy.append(saxon)
        


    def vikingAttack(self):
        
        '''
        En este método tenemos que elegir un vikingo al azar y atacar a otro sajon al azar.
        Entonces si el sajon se queda sin salud, entonces lo borramos de la lista de los sajones.
        '''
            
        s = random.choice(self.saxonArmy)
        
        v = random.choice(self.vikingArmy)
        
        attack_v = s.receiveDamage(v.attack())
        
        if s.health <= 0:
            
            self.saxonArmy.remove(s)
        
        return attack_v
        
        
    def saxonAttack(self):
        
        '''
        En este método tenemos que elegir un sajon al azar y atacar a otro vikingo al azar.
        Entonces si el vikingo se queda sin salud, entonces lo borramos de la lista de los sajones.
        '''
        
        v = random.choice(self.vikingArmy)
        
        s = random.choice(self.saxonArmy)
        
        
        attack_s = v.receiveDamage(s.attack())
        
        
        if v.health <= 0:
            
            self.vikingArmy.remove(v)
        
        return attack_s
        
        
    def showStatus(self):
        
        '''
        Este metodo hace una comparación entre los dos ejercitos en tamaño.
        En cuanto un ejercito llegue a 0, el otro es el ganador.
        '''
        
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            
            return 'Vikings have won the war of the century!'
    
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            
            return 'Saxons have fought for their lives and survive another day...'
        
        else:
            
            return 'Vikings and Saxons are still in the thick of battle.'
    
    
    
    
    
