import random
def devCredits():
    print('Coded by Ethan Barnes\nstarted July 22nd\nended August 2nd')

def mainMenu():
    match input("Enter Start or Credits:"):
        case 'credits':
            devCredits()
            mainMenu()
        case 'start':
            print('Enjoy the game!')
mainMenu()





def roundTeammate(monsters):
    teammate = []

    print(f"{name}, here\'s a list of usable monsters:")
    for index, monster in enumerate(monsters):
        print(f"{index + 1}. {monster}")

    while True:
        choice = input("Enter Monster #: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(monsters):
            teammate.append(monsters[int(choice) - 1])
            break
        else:
            print("Invalid choice. Please enter a valid number from the list.")

    return teammate

def battle(playerMon, enemyMon, money, enemyName):
    player_monster_health = 200
    enemy_monster_health = 300
    player_heal_count = 0
    enemy_heal_count = 0
    max_heals = 3

    while player_monster_health > 0 and enemy_monster_health > 0:
        move = input('What would you like to do? ("fight" or "heal"): ').strip().lower()
        
        if move == 'fight':
            damage = random.randint(1, 150)
            enemy_monster_health -= damage
            print(f'{name} attacked {enemyName}\'s {enemyMon[0]} for {damage} damage! {enemyMon[0]} is now at {enemy_monster_health}.')
            
        elif move == 'heal':
            if player_heal_count < max_heals:
                replenish = random.randint(1, 100)
                player_monster_health += replenish
                player_heal_count += 1
                print(f'{playerMon} replenished {replenish} HP! Health is now at {player_monster_health}. You have {max_heals - player_heal_count} heals left.')
            else:
                print("You have used all your heals!")
                continue
            
        else:
            print("Move is invalid! (enter 'fight' or 'heal')")
            continue
        
        if enemy_monster_health <= 0:
            print(f"You defeated {enemyName}!")
            print(f"You won {money} from your bet!")
            return 'win'
        
        # Computer's move
        enemy_move = random.choice(['fight', 'heal'])
        
        if enemy_move == 'fight':
            damage = random.randint(1, 150)
            player_monster_health -= damage
            print(f'{enemyName} attacked you for {damage} damage! Your health is now {player_monster_health}.')
            
        elif enemy_move == 'heal':
            if enemy_heal_count < max_heals:
                replenish = random.randint(1, 100)
                enemy_monster_health += replenish
                enemy_heal_count += 1
                print(f'{enemyName} has replenished {replenish} HP! {enemyMon[0]}\'s health is now {enemy_monster_health}. {enemyName} has {max_heals - enemy_heal_count} heals left.')
            else:
                print(f"{enemyName} tried to heal but has no heals left!")
        
        if player_monster_health <= 0:
            print(f"{enemyName}'s {enemyMon} defeated you!")
            print(f"You have lost {money} from your bet!")
            return 'loss'

# Main game loop
def main():
    print('Welcome to the arena! Prepare to duel!')
print("RULES: 1. Place a bet!\n       2. Battle!\n       3. One play per turn!\n       4. Winner takes all!")
name = input("What is your name?")

mellowMons = ['Battery', 'Gooda', 'VV', 'Schpoon', 'Fentineel', 'Bosco', 'Doughnut', 'Mousse', 'Hweed', 'kameleon']
computer_names = ['Brodie', 'Gavin', 'Madi', 'Ethan', 'Becca', 'Johnny', 'Riley', 'Donny', 'Natalie', 'Xavier', 'Leila', 'Barney', 'Joshua', 'Tanner', 'Annie', 'Tony', 'Barkley', 'Keegan','J','Yugi','Denise','Dave','Phil','Frank']
wins = 0
losses = 0
balance = 500

while True:
    money = int(input(f"Your balance is ${balance}, how much would you like to bet on this round {name}? "))
    
    # Player chooses their monster
    playersMon= roundTeammate(mellowMons)
    print(f"{name}, you have chosen: {playersMon}")
    
    # Computer randomly chooses its monster
    enemyMon = random.sample(mellowMons, 1)
    enemyName = random.choice(computer_names)
    print(f"Your opponent this round is {enemyName}! It appears {enemyName} has chosen {enemyMon}!")
    print("The battle has begun!\n")

    # Start the battle
    result = battle(playersMon, enemyMon, money, enemyName)
    if result == 'win':
        wins += 1
        balance += money
    elif result == 'loss':
        losses += 1
        balance -= money

    print(f"Total Wins: {wins}")
    print(f"Total Losses: {losses}")

    # Ask if the player wants to battle again
    play_again = input("Would you like to battle again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print(f"Thank you for playing! You walked away with {money} dollars!")
        break
