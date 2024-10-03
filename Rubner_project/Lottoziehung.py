import random

pulled_numbers_statistic = {i: 0 for i in range(1, 46)}


def statistics(selected_numbers):
    for i in selected_numbers:
        pulled_numbers_statistic[i] += 1


def pull_number():
    for _ in range(1000):
        numbers = [i for i in range(1, 46)]
        top_border = 44
        selected_numbers = []

        for _ in range(5):
            random_number = random.randint(0, top_border)
            selected_number = numbers[random_number]

            numbers[random_number], numbers[top_border] = numbers[top_border], numbers[random_number]

            top_border -= 1

            selected_numbers.append(selected_number)

        statistics(selected_numbers)


if __name__ == "__main__":
    pull_number()
    for key, value in pulled_numbers_statistic.items():
        print(f"{key} : {value}")