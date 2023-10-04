#!python3

# class objects with multiple instances in a table

class powers:
    val = 0
    def square(self):
        try:
            answer = self.val**2
        except:
            answer = "non number"
        return answer   

    def __init__(self,v): 
        #Constructor         
        self.val = v               


# Create a dictionary that we can store instances in
numbers = {}

# Instantiate 10 instances
namedIndexes = ["tyler","anson",15,20]
for i in namedIndexes:
    numbers[i] = powers(i)

print(f"We now have {len(numbers)} instances stored in our dictionary.\n")

print("Instance Data:")
print("**************")
for i in numbers:
    print(f"instance with index:{i} > number:{numbers[i].val} and square:{numbers[i].square()}")
