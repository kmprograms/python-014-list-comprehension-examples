# --------------------------------------------------------------
# Przyklad 1
# --------------------------------------------------------------
letters = []
for c in 'kmprograms':
    letters.append(c)
print(letters)

# [expression for item in list]
letters2 = [letter for letter in 'kmprograms']
print(letters2)

# --------------------------------------------------------------
# Przyklad 2
# --------------------------------------------------------------
# 0 .. 9
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)
even_numbers2 = [x for x in range(10) if x % 2 == 0 if x > 5]
print(even_numbers2)

# --------------------------------------------------------------
# Przyklad 3
# --------------------------------------------------------------
modified_expression = [c.upper() if ord(c) % 2 == 0 else c.lower() for c in 'abba']
print(modified_expression)

# --------------------------------------------------------------
# Przyklad 4
# --------------------------------------------------------------
reversed_expressions = [expression[::-1] for expression in ['monday', 'tuesday', 'friday']]
print(reversed_expressions)

# --------------------------------------------------------------
# Przyklad 5
# --------------------------------------------------------------
unities = [1, 2, 3, 4]
tens = [10, 20, 30, 40]
pairs = []

for t in tens:
    for u in unities:
        pairs.append([u, t])
print(pairs)

pairs2 = [[u, t] for t in tens for u in unities]
print(pairs2)
