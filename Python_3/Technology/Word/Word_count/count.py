# list value
Dataset = list()
store_array = list()

# Data
Dataset = "Hello my name is Gildong"

# count init
word_count = 0
position_count = 0

# finding
for data in Dataset:
    for index in range(len(data)):

        if data[index] == "o":
            store_array.append(position_count)
            position_count += 1
            word_count += 1

        position_count += 1

# print output
print(f"Character counter is {word_count}")
print(f"Character position is {store_array}")