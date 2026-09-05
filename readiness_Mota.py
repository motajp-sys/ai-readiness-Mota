import statistics

# Global Variables

number_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
my_name = "Juan Pablo Mota"
student_id = "R02424260"
hellow = "Hello, I am " + my_name + ", and my student ID is " + student_id + "."

# Function Definitions

def myfunc(num_list):
    print("Max:  " + str(max(num_list)))
    print("Mean: " + str(statistics.mean(num_list)))

# Execution

# print("Hello, I am Juan Pablo Mota, and my student ID is R02424260.")
print(hellow)
myfunc(number_list)
