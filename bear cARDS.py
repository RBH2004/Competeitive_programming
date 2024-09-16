# Step 1: Input
t1, t2, t3, t4, t5 = map(int, input().split(" "))

# Step 2: Sort the numbers
numbers = [t1, t2, t3, t4, t5]
numbers.sort()

# Step 3: Case 1 - Discard two cards with the same number
for i in range(4):
    if numbers[i] == numbers[i + 1]:
        min_sum = sum(numbers) - 2 * numbers[i]
        break
else:
    min_sum = sum(numbers)  # If no two cards are the same

# Step 4: Case 2 - Discard three cards with the same number
for i in range(3):
    if numbers[i] == numbers[i + 1] == numbers[i + 2]:
        min_sum = min(min_sum, sum(numbers) - 3 * numbers[i])

# Step 5: Output
print(min_sum)
