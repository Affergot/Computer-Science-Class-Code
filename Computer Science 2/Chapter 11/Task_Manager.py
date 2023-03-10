from Generate_Rancom_Numbers import generate_random_numbers
from Write_To_Json import write_to_file
from Get_User_Range import get_range
from Get_User_Numbers import get_number_of_random_numbers
from Print_Unique_List import print_results
from Ask_Yes_Or_No import ask_for_seed


ask_for_seed()
max_nums = get_range()
number_of_random_numbers = get_number_of_random_numbers()
random_nums, number_of_retries = generate_random_numbers(max_nums, number_of_random_numbers)
write_to_file(random_nums, number_of_retries)
print_results()