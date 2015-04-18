# file which will start the game
from weapon_class import Weapon
from spell_class import Spell
from hero_class import Hero
# from enemy_class import Enemy
from dungeon_class import Dungeon
# from fight_class import Fight
import sys


def create_hero():
    hero_name = input("Type your hero name: ")
    hero_title = input("Type your hero title: ")

    hero = Hero(hero_name, hero_title)
    return hero


def chooce_weapon():
    weapon0 = Weapon(name="The Axe of Destiny", damage=20)
    weapon1 = Weapon(name="Hammer of Kharas", damage=15)
    weapon2 = Weapon(name="Sword of Kas", damage=21)

    weapons = [weapon0, weapon1, weapon2]
    print (weapons)

    choice = input("Enter the number of weapon you want to equip your hero: ")
    return weapons[int(choice)]


def chooce_spell():
    spell0 = Spell(name="Fireball", damage=30, mana_cost=50, cast_range=2)
    spell1 = Spell(name="Wind Wall", damage=20, mana_cost=50, cast_range=1)

    spells = [spell0, spell1]
    print (spells)

    choice = input("Enter the number of spell you want to equip your hero: ")
    return spells[int(choice)]


def main():
    print ("Welcome to my game called Dungeons and Pythons!")
    print (20 * '*')
    print ("First, you'll create your hero:")
    my_hero = create_hero()
    print (20 * '~')
    print ("Good job. Now, chooce one weapon from the list:")
    my_weapon = chooce_weapon()
    print (20 * '~')
    print ("If you wish, You can learn one of the spells below")
    my_spell = chooce_spell()
    print (20 * '~')

    level = input("Yeah, It's the final step bro. Enter the level you want to play: ")
    print ("Enjoy the game :)")

    my_hero.equip(my_weapon)
    my_hero.learn(my_spell)

    current_map = Dungeon(level)
    current_map.spawn(my_hero)

    print (20 * '<>')

    print ("The game is started. Menu of options: ")
    print ("1. Print the current map")
    print ("2. Move UP")
    print ("3. Move DOWN")
    print ("4. Move RIGHT")
    print ("5. Move LEFT")
    print ("0. Exit the game")

    while True:
        choice = input("Enter your choice: ")

        if choice is '1':
            current_map.print_map()
            print (20 * '-')
        elif choice is '2':
            current_map.move_hero("up")
        elif choice is '3':
            current_map.move_hero("down")
        elif choice is '4':
            current_map.move_hero("right")
        elif choice is '5':
            current_map.move_hero("left")
        else:
            sys.exit()

if __name__ == '__main__':
    main()
