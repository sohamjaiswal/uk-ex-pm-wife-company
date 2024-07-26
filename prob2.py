valLimit = int(input("Enter the maximum value: "))
reqLength = int(input("Enter the maximum length: "))
result = []

def helper(current_array):
    if len(current_array) == reqLength:
        result.append(current_array)
        return
    last_element = current_array[-1]
    for i in range(last_element, valLimit+1, last_element):
        helper(current_array + [i])

for i in range(1, valLimit+1):
    helper([i])

print(len(result) % 10000)