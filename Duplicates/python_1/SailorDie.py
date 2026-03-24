import random

def roll_dice(num_dice):
    return [random.randint(1, 6) for _ in range(num_dice)]

def play_round():
    dice = roll_dice(5)
    ship = captain = crew = False

    print("Initial roll:", dice)

    # Try up to 3 rolls
    for roll_num in range(3):
        if 6 in dice and not ship:
            dice.remove(6)
            ship = True
            print("Got the ship (6)")
        
        if ship and 5 in dice and not captain:
            dice.remove(5)
            captain = True
            print("Got the captain (5)")
        
        if captain and 4 in dice and not crew:
            dice.remove(4)
            crew = True
            print("Got the crew (4)")

        if ship and captain and crew:
            cargo = sum(dice)
            print("Cargo dice:", dice)
            return cargo

        # reroll remaining dice
        dice = roll_dice(len(dice))
        print(f"Roll {roll_num + 2}:", dice)

    return 0

def main():
    score = play_round()
    print("Final cargo score:", score)

if __name__ == "__main__":
    main()