# input data
string_data = "ACGT"

# list
store_data = list()
revers_data = list()

# list store
for raw_data in string_data:
    store_data.append(raw_data)

revers_data = store_data[::-1]

print(revers_data)





