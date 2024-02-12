import art
import game_data
import random

print(art.logo)

score = 0
game = True

while game:
    rand_num_a = random.randint(0, len(game_data.data) - 1)
    filtered_game_data = [item for item in game_data.data if item != game_data.data[rand_num_a]]
    rand_num_b = random.randint(0, len(filtered_game_data) - 1)

    compare_a = game_data.data[rand_num_a]
    compare_b = filtered_game_data[rand_num_b]

    print(f"Compare A: {compare_a['name']}, {compare_a['description']}, from {compare_a['country']}")
    print(art.vs)
    print("Compare B: {}, {}, from {}".format(compare_b['name'], compare_b['description'], compare_b['country']))
    choise = input("Who has more followers? Type 'A' or 'B': ").lower()

    folowers_a = compare_a['follower_count']
    folowers_b = compare_b['follower_count']

    if (choise == 'a' and folowers_a > folowers_b) or (choise == 'b' and folowers_a < folowers_b):
        score+=1
        print(f"\nYou are right! Current score = {score}")
    elif folowers_a == folowers_b:
        print(f"\nFollowers of Compare A and Compare B are equal. Current score: {score}")
    else:
        print(f"\nYou are loose. Current score is: {score}")
        game=False




