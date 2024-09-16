s=input()
new_string=""
t1,t2,t3,t4,t5=0,0,0,0,0
numbers=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        new_string+=s[i]
    elif s[i]==" ":
        numbers.append(int(new_string))
        new_string=""
numbers.append(int(new_string))
t1,t2,t3,t4,t5=numbers[0],numbers[1],numbers[2],numbers[3],numbers[4]
for i in range(4):
    if numbers[i] == numbers[i + 1]:
        min_sum = sum(numbers) - 2 * numbers[i]
        break
else:
    min_sum = sum(numbers)


for i in range(3):
    if numbers[i] == numbers[i + 1] == numbers[i + 2]:
        min_sum = min(min_sum, sum(numbers) - 3 * numbers[i])


print(min_sum)
