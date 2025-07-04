num = int(input("Enter the number: "))

temp = num

count = 0

# Count number of digits

while temp > 0:

count += 1

temp //= 10

if count >= 4:

mid1_pos = count // 2

mid2_pos = mid1_pos - 1

temp = num

position = 0

mid1 = mid2 = 0

while temp > 0:

digit = temp % 10

if position == mid1_pos:

mid1 = digit

if position == mid2_pos:

mid2 = digit

temp //= 10

position += 1

product = mid1 * mid2

print(f"\nProduct of middle digits ({mid1} * {mid2}) = {product}")

else:

print("\nIt's not a 4 or more digit number!")