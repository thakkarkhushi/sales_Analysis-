name_list = []
names = input("Enter a list of first names (separated by spaces): ")
names = names.split()
name_list.extend(names)
count_a = 0
for name in name_list:
    count_a += name.lower().count('a')
print(f"The letter 'a' appears {count_a} time(s) in the list.")