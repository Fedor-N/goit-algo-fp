import random


def roll_dice():
    return random.randint(1, 6)


def monte_carlo_simulation(num_trials):
    outcomes = [0] * 13  # Індекси від 2 до 12
    for _ in range(num_trials):
        roll1 = roll_dice()
        roll2 = roll_dice()
        total = roll1 + roll2
        outcomes[total] += 1

    probabilities = [outcome / num_trials * 100 for outcome in outcomes]
    return probabilities


def print_probabilities(probabilities):
    print("Сума\tІмовірність")
    for i, prob in enumerate(probabilities[2:], start=2):
        print(f"{i}\t{prob:.2f}% ({prob/100:.2f})")


def main():
    num_trials = 1000000
    probabilities = monte_carlo_simulation(num_trials)
    print_probabilities(probabilities)


if __name__ == "__main__":
    main()
