import json

def write_to_file(random_nums, number_of_retries):
    random_nums.sort()
    random_nums.append(number_of_retries)

    with open("Computer Science 2\Chapter 11\List_Of_Unique_Nums.json", "w") as file:
        json.dump(random_nums, file)

if __name__ == "__main__":
    random_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number_of_retries = 0
    write_to_file(random_nums, number_of_retries)