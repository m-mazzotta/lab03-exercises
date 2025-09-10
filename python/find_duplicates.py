def find_duplicates_nested_loop(l: list) -> list:

    duplicates = []
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] == l[j] and l[i] not in duplicates:
                duplicates.append(l[i])
    return duplicates


def find_duplicates_dict(l: list) -> list:
#using a dictionary (or hashmap) data structure instead of nested loops
    count = dict()
    duplicates = []
    for num in l:
        # count[num] += 1
        count[num] = count.get(num, 0) + 1
        if count[num] == 2: #if the count is two, appeared two times
            duplicates.append(num)
    return duplicates

# In Python, if __name__ == "__main__" is a conditional check that determines whether 
# a Python file is being run as the main program or imported as a module into another 
# script.
if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_nested_loop(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))

    print("Sample 1 with dict:", find_duplicates_dict(sample1))
