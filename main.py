import random

# Constants
NUM_SIMULATIONS = 1_000_000


def simulate_no_switch():
    wins = 0
    for _ in range(NUM_SIMULATIONS):
        winning_door = random.randint(1, 3)
        chosen_door = random.randint(1, 3)
        if chosen_door == winning_door:
            wins += 1
    return wins


def simulate_switch():
    wins = 0
    for _ in range(NUM_SIMULATIONS):
        winning_door = random.randint(1, 3)
        chosen_door = random.randint(1, 3)
        # Host reveals a door that is not the winning door and not the chosen door
        remaining_doors = [
            door for door in [1, 2, 3] if door != chosen_door and door != winning_door
        ]
        revealed_door = random.choice(remaining_doors)
        # Contestant switches to the remaining door
        switch_door = [
            door for door in [1, 2, 3] if door != chosen_door and door != revealed_door
        ][0]
        if switch_door == winning_door:
            wins += 1
    return wins


def main():
    no_switch_wins = simulate_no_switch()
    switch_wins = simulate_switch()

    print(
        f"Winning percentage without switching: {no_switch_wins / NUM_SIMULATIONS * 100:.2f}%"
    )
    print(
        f"Winning percentage with switching: {switch_wins / NUM_SIMULATIONS * 100:.2f}%"
    )


if __name__ == "__main__":
    main()
