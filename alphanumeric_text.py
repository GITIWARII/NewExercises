sample_text = "Learning Journal 2020"
alpha_count = 0
numeric_count = 0
for i in sample_text:
    if i.isalpha():
        alpha_count += 1
    if i.isnumeric():
        numeric_count += 1
print("Number of Letters:",alpha_count)
print("Number of Digits:",numeric_count)


