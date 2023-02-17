class Operation_calls:
    def __init__(self):
        self.function_call_count = 0
        self.addition_call_count = 0
        self.subtraction_call_count = 0
        self.multiplication_call_count = 0
        self.comparison_call_count = 0
    
    def Get_Function_Count(self):
        return self.function_call_count
    
    def Get_Addition_Count(self):
        return self.addition_call_count
        
    def Get_Subtracion_Count(self):
        return self.subtraction_call_count
        
    def Get_Multiplication_Count(self):
        return self.multiplication_call_count
        
    def Get_Comparison_Count(self):
        return self.comparison_call_count

    def Increment_Function_Call(self):
        self.function_call_count += 1
        
    def Increment_Addition_Call(self):
        self.addition_call_count += 1
    
    def Increment_Subtraction_Call(self):
        self.subtraction_call_count += 1
        
    def Increment_Multiplication_Call(self):
        self.multiplication_call_count += 1

    def Increment_Comparison_Call(self):
        self.comparison_call_count += 1

#if __name__==__main__:

def RecurrsiveFactorial(x, Operation_calls):
    Operation_calls.Increment_Function_Call()
    Operation_calls.Increment_Comparison_Call()
    if x == 1:
        return 1
    elif x != 1:
        Operation_calls.Increment_Multiplication_Call()
        Operation_calls.Increment_Subtraction_Call()
        return x * RecurrsiveFactorial(x-1, Operation_calls)
        
def IterativeFactorial(x, Operation_calls):
    factorial_total = 1
    Operation_calls.Increment_Function_Call()
    Operation_calls.Increment_Addition_Call()
    for x in range(1, x + 1):
        Operation_calls.Increment_Multiplication_Call()
        factorial_total = factorial_total * x
    return factorial_total


target = 10
Recurrsive_Counter = Operation_calls()
Iterative_Counter = Operation_calls()
RecurrsiveFactorial(target, Recurrsive_Counter)
IterativeFactorial(target, Iterative_Counter)

print("Recurrsive Calls:")
print(f"Number of Function calls: {Recurrsive_Counter.Get_Function_Count()}")
print(f"Number of Subtraction calls: {Recurrsive_Counter.Get_Subtracion_Count()}")
print(f"Number of Multiplication calls: {Recurrsive_Counter.Get_Multiplication_Count()}")
print(f"Number of Addtion calls: {Recurrsive_Counter.Get_Addition_Count()}")
print(f"Number of Comparison calls: {Recurrsive_Counter.Get_Comparison_Count()}")

print("\nItterative Calls:")
print(f"Number of Function calls: {Iterative_Counter.Get_Function_Count()}")
print(f"Number of Subtraction calls: {Iterative_Counter.Get_Subtracion_Count()}")
print(f"Number of Multiplication calls: {Iterative_Counter.Get_Multiplication_Count()}")
print(f"Number of Addition calls: {Iterative_Counter.Get_Addition_Count()}")
print(f"Number of Comparison calls: {Iterative_Counter.Get_Comparison_Count()}")
