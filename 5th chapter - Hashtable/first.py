

print()

# way 1 to dicliration HashTable
hashTable1 = {"Name": "Hazem", "Age": "21", "Address": "EGYPT"}


# way 2 dicliration HashTable
hashTable2 = dict(Name = "Hazem", Age = "21", Address = "EGYPT")



# way1 to update HsahTable
hashTable1.update(BirthDay = "5/5/2001")         # <HashTable name>.update(<new key> = <new value>)
# way2 to update HsahTable
hashTable2["College"] = "Mansoura University"    # <HashTable name>["<key>"] = "<value>"



# way 1 to print HashTable size
print(len(hashTable1))
# way 2 to print HashTable size
print(hashTable2.__len__())




# delete HashTable content only without delete HashTable itself
hashTable1.clear()


# delete intire hashTable
del hashTable2              #if we tried to print that HashTable, it will show error





# ways to print HashTable 
print()
print("HashTable 1 :" , hashTable1.items())
print("HashTable 1 : ", hashTable1)

print()
print("HashTable 2 : " , hashTable2.items())
print("HashTable 2 :" , hashTable2)