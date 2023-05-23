
# for rolls for d20
import random

# similar to character sheet, but simple
class Atributes:
    def __init__(self, HP, AC, STR, DEX, ATK):
        self.HP = HP
        self.AC = AC
        self.STR = STR
        self.DEX = DEX
        self.ATK = ATK
# dice can be a shortcut roll for weapon      
def DMG_roll(dice):
         DMG = random.randint(1, dice)
         return DMG
     
        
     
# example of ppl in battle        
player = Atributes(10,14,12,11,4)

enemy = Atributes(10, 10, 8, 6, 3)

while player.HP >0 and enemy.HP > 0:
    player_ATK_roll = random.randint(1,20) + player.ATK
    print(f'Your attack roll was {player_ATK_roll}')
    if player_ATK_roll > enemy.AC:
        player_dmg = DMG_roll(5)
        enemy.HP = enemy.HP - player_dmg
        print(f'You hit! You deal {player_dmg} DMG to enemy! Enemy has\n'
              f'{enemy.HP} HP left!')
    else:
        print('You missed!')
    print('-'*20)
    
    if enemy.HP <=0:
        continue
        
    print( 'Now it\'s the enemy turn')
    
    enemy_ATK_roll = random.randint(1,20) + enemy.ATK
    print(f'Enemy attack roll was {enemy_ATK_roll}')
    if enemy_ATK_roll > player.AC:
        enemy_dmg = DMG_roll(5)
        player.HP = player.HP - enemy_dmg
        print(f'You have been hit! Enemy dealt {enemy_dmg} to you! Now you have\n'
              f'{player.HP} HP left!')
    else:
        print('Enemy missed!')
        
    print('-'*20)
    if player.HP <= 0:
        continue
if player.HP <= 0:
    print('You lost! Better luck next time.')
elif enemy.HP <= 0:
    print('You win!')














