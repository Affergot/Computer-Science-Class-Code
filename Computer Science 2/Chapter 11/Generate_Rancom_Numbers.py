import random

def generate_random_numbers(max_nums, number_of_random_numbers):
    random_nums = []
    number_of_retries = 0
    while len(random_nums) < number_of_random_numbers:
        random_num = random.randint(1, max_nums)
        if random_num not in random_nums:
            random_nums.append(random_num)
        else:
            number_of_retries += 1
    random_nums.sort()
    return random_nums, number_of_retries


if __name__ == "__main__":

    max_nums = 15
    number_of_random_numbers = 10
    random_nums, number_of_retries = generate_random_numbers(max_nums, number_of_random_numbers)
    
    print(random_nums)
    print(number_of_retries)