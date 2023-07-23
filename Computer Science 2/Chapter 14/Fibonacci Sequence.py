'''
The Fibonacci sequence begins with 0 and then 1 follows.
All subsequent values are the sum of the previous two,
for example: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci()
function, which takes in an index, n, and returns the nth value in the sequence.
Any negative index values should return -1.
'''

def fibonacci_sequence(index):
    if index < 0:
        return -1
    elif index == 0:
        return 0
    elif index == 1 or index == 2:
        return 1
    else:
        return fibonacci_sequence(index-1) + fibonacci_sequence(index-2)

if __name__ == "__main__":
    user_desired_index = int(input("Enter the index number of the fibonacci sequence to have it returned\n:"))
    print(fibonacci_sequence(user_desired_index))