
try:
    input_list = [int(x) for x in input("Enter a list of integers: ").split()]
except ValueError:
    print("Error: Please enter valid integers.")
    exit(0)

if len(input_list) % 10 != 0 or len(input_list) == 0:
    print("Error: The length of the list must be a multiple of 10.")
    exit(0)

result = [num for i, num in enumerate(input_list) if (i + 1) % 2 != 0 and (i + 1) % 3 != 0]

if result is not None:
    print("Processed List:", result)
