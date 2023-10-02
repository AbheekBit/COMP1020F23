class Enemy:
    def __init__(self,start_health,greeting):
        self.health=start_health
        self.greeting=greeting
    def speak(self):
        print(self.greeting)

    def take_damage(self,damage):
        self.health=self.health-damage

def main():
    orc=Enemy(100, "Blargh!")
    orc.speak()
    orc.take_damage(20)

    orc2=Enemy(10,"Help me!")
    orc2.speak()

if __name__=="__main__":
    main()