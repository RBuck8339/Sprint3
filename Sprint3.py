"""This is my first python project, it is a text-based game in which a player fights bosses using four spells. It
uses many functions in order to create loops. """
__author__ = "Ronan Buck"
import random

# Ronan Buck
# This is a small text-based boss fight
print("Hello There!" * 6)
print("This is your fight against Boss")
print("You have 4 spells to use against Boss")
print("Your spells are: \n fireball \n thunder \n punch \n barrier")
print("Input your spell in order to attack or defend")
print("fireball, thunder, and punch attack Boss, and barrier will heal you")
print("You have 500 health and Boss has 1500 health, KILL IT!")

player_health = int(500)
boss_health = int(1500)
fireball = int(2 ** 5 + 50)  # equals 82
thunder = int(100000 // 1000 - 30)  # equals 70
punch = int(4*25*2/3)  # equals 66
barrier = int(9 % 2 * 50 + 10)  # equals 60


def new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier):  # end fight
    """
    This is the last fight of the game, making use of the imported random functions in order to have the fireball
    burn the target based on a random number generator.
    :param god_health:
    :param player_health:
    :param burn:
    :param fireball:
    :param thunder:
    :param punch:
    :param barrier:
    """
    if god_health > 0 and player_health > 0:
        while burn >= 75:
            print("God was hurt by burn")
            burn_decrease = random.randint(0, 7)
            god_health -= 30
            burn -= burn_decrease
            if burn < 75:
                print("God's health is now: ", god_health, sep="")
        attack = input("Please choose a spell: ")
        if attack == "fireball":
            print("God's health is: ", int(god_health - fireball), sep="")
            god_health -= fireball
            print("God attacks, you now have: ", player_health - 50, sep="")
            player_health -= 50
            burn = random.randint(0, 100)
            if burn >= 75:
                print("You have burned God")
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
        elif attack == "thunder":
            print("God's health is: ", int(god_health - thunder), sep="")
            god_health -= thunder
            print("God attacks you, you now have: ", player_health - 50, sep="")
            player_health -= 50
            attacks(player_health, god_health)
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
        elif attack == "punch":
            print("God's health is: ", int(god_health - punch), sep="")
            god_health -= punch
            print("God attacks you,", end="")
            print("you now have: ", player_health - 50, sep="")
            player_health -= 50
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
        elif attack == "barrier":
            player_health += barrier  # Heals Player
            print("You now have: ", int(player_health), "HP", sep="")
            print("God attacks, you now have: ", int(player_health - 50), sep="")
            player_health -= 50
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
        else:
            print("That was not a valid response, please check spelling or enter a valid input")
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
    elif god_health <= 0 < player_health:
        print("You have defeated God")
    elif (god_health > 0) and (player_health <= 0):
        print("You Lost...")


def ambush(player_health, fireball, barrier, thunder, punch):
    """
    This is the fight that occurs if the player decides to go home during the "proceed" function. A while loop is
    used to place the player on a time constraint.
    :param player_health:
    :param fireball:
    :param barrier:
    :param thunder:
    :param punch:
    """
    print("The Ambusher lunges at you and stabs you")
    print("You have only 15 turns to defeat the Ambusher ", end="")
    print("or else you will bleed out")
    player_health = player_health * 0 + 500
    ambusher_health = 750
    for x in range(15):
        if ambusher_health > 0 and player_health > 0:
            attack = input("Please choose a spell: ")
            if attack == "fireball":
                print("It's health is: ", int(ambusher_health - fireball), sep="")
                ambusher_health -= fireball
                print("Boss attacks, you now have: ", player_health - 50, sep="")
                player_health -= 50
            elif attack == "thunder":
                print("It's health is: ", int(ambusher_health - thunder), sep="")
                ambusher_health -= thunder
                print("It attacks you, you now have: ", player_health - 50, sep="")
                player_health -= 50
            elif attack == "punch":
                print("It's health is: ", int(ambusher_health - punch), sep="")
                ambusher_health -= punch
                print("Ambusher attacks you,", end="")
                print("you now have: ", player_health - 50, sep="")
                player_health -= 50
            elif attack == "barrier":
                player_health += barrier  # Heals Player
                print("You now have: ", int(player_health), "HP", sep="")
                print("It attacks, you now have: ", player_health - 50, sep="")  # see if way to fix characters
                player_health -= 50
            else:
                print("That was not a valid response, please check spelling or enter a valid input")
                ambush(player_health, fireball, barrier, thunder, punch)
        elif ambusher_health > 0 >= player_health:
            print("You lost")
        elif ambusher_health <= 0 < player_health:
            print("You have defeated the Ambusher")
            print("You treat your wounds and armed with a newfound ", end="")
            print("rage you continue on to fight God himself")
            print("As soon as you see the God of this world, you tremble")
            print("However, you feel your spells get stronger")
            print("Your Fireball now has a chance to burn the target")
            print("Your Thunder has a chance to stun the target momentarily")
            print("Your Punch hits harder")
            print("Your Barrier heals for more")
            fireball += 10  # equals 92
            thunder += 30  # equals 100
            punch += 9  # equals 75
            barrier += 30  # equals 90
            god_health = 5000
            player_health = 1500
            burn = 0
            new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
    print("You have succumbed to your stab wound")
    print("You have died")


def proceed(player_health):  # text
    """
    This is the text that appears asking the player to make a choice on if they move on in the game or go home. If
    they choose to go home they will be ambushed. List functions are used to check the answer from the player.
    param player_health:
    """
    print("After defeating the Boss, you are now able to go home and relax")
    print("You now have a big choice to make")
    print("Say yes to go home to your family, say no to continue fighting")
    answer = input("Would you like to go home or continue fighting?")
    answer = answer.upper()
    answer = list(answer)
    if answer[0] == "N":  # see "if y in(answer)"
        god_health = 5000
        player_health = 1500
        burn = 0
        new_fight(god_health, player_health, burn, fireball, thunder, punch, barrier)
    elif answer[0] == "Y":
        print("You come home to find your family murdered")
        print("You are attacked by a strong enemy")
        print("It appears mostly human, but its behavior is definitely not")
        ambush(player_health, fireball, barrier, thunder, punch)
    elif answer[0] != "Y" and answer[0] != "N":
        print('Please try again')
        proceed(player_health)


def attacks(player_health, boss_health):  # the combat system to be repeated
    """
    This is the first fight of the game, with nothing special occurring within it.
    :param player_health:
    :param boss_health:
    """
    boss_health += 0
    player_health += 0
    if boss_health > 0 and player_health > 0 or fireball < 0:  # or serves no purpose
        attack = input("Please choose a spell: ")
        if attack == "fireball" and not attack == "thunder":
            print("Boss's health is: ", int(boss_health - fireball), sep="")
            boss_health -= fireball
            print("Boss attacks, you now have: ", player_health - 50, sep="")
            player_health -= 50
            attacks(player_health, boss_health)
        elif attack == "thunder":
            print("Boss's health is: ", int(boss_health - thunder), sep="")
            boss_health -= thunder
            print("Boss attacks you, you now have: ", player_health - 50, sep="")
            player_health -= 50
            attacks(player_health, boss_health)
        elif attack == "punch":
            print("Boss's health is: ", int(boss_health - punch), sep="")
            boss_health -= punch
            print("Boss attacks you,", end="")
            print("you now have: ", player_health - 50, sep="")
            player_health -= 50
            attacks(player_health, boss_health)
        elif attack == "barrier":
            player_health += barrier  # Heals Player
            print("You now have: ", int(player_health), "HP", sep="")
            print("Boss attacks, you now have: ", int(player_health - 50), sep="")
            player_health -= 50
            attacks(player_health, boss_health)
        else:  # here to detect human error
            print("That was not a valid response, please check spelling or enter a valid input")
            attacks(player_health, boss_health)
    elif boss_health <= 0 < player_health:
        print("YOU WIN!" + "YOU WIN!" + "YOU WIN!" + "YOU WIN!")
        proceed(player_health)
    elif (boss_health > 0) and (player_health <= 0):
        print("You Lost...")


attacks(player_health, boss_health)
