phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook['Jake']=938273443
phonebook.pop("Jill")

# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
    print(phonebook['Jake'])
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")