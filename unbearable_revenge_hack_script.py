import time

class Player:
    def __init__(self):
        self.health = 100
        self.position = (0, 0)
        self.inventory = {'traps': 5, 'health_potions': 3}
        self.stealth_mode = False

    def move(self, direction):
        if self.stealth_mode:
            print("Moving stealthily to", direction)
        else:
            print("Moving to", direction)
        # Update position based on direction

    def place_trap(self):
        if self.inventory['traps'] > 0:
            print("Placing trap")
            self.inventory['traps'] -= 1
        else:
            print("No traps left")

    def use_health_potion(self):
        if self.inventory['health_potions'] > 0:
            print("Using health potion")
            self.health += 20
            self.inventory['health_potions'] -= 1
        else:
            print("No health potions left")

    def toggle_stealth_mode(self):
        self.stealth_mode = not self.stealth_mode
        print("Stealth mode:", self.stealth_mode)

def main():
    player = Player()
    player.toggle_stealth_mode()
    
    start_time = time.time()
    while time.time() - start_time < 300:
        # Simulate player movement and survival
        player.move("forward")
        if player.health < 50:
            player.use_health_potion()
        if time.time() - start_time % 60 == 0:  # Place a trap every minute
            player.place_trap()
        time.sleep(10)  # Simulate time delay for movements

    print("Survived 5 minutes. Retrieving the flag.")

if __name__ == "__main__":
    main()


