def unique_names(names1, names2):
    for val in names2:
        if not val in names1:
            names2.append(val)
    return names2

names1 = ["Ava", "Emma", "Olivia"]
names2 = ["Olivia", "Sophia", "Emma"]
print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia