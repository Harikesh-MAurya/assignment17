# 1. Write a python program to store all the programming languages known to you using
# Set.
# 2. Write a python program to store your own information {name, age, gender, so on..}
# 3. Write a python script to get the data type of a Set.
# 4. Write a Python script to find if “Python” is present in the set thisset = {"Java",
# "Python", "Django"}
# 5. Write a python program to add items from another set to the current set. thisset =
# {"Java", "Python", "SQL"}
# secondset= {"C", "Cpp", "NoSQL"}
# 6. Write a python program to add elements of list to a set
# thisset = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]
# 7. Write a python program to remove last item of the given set
# thisset = {"Python", "Django", "JavaScript", “SQL”}
# 8. Write a python program to delete the set completely.
# 9. Write a python program to loop through the set and print values
# thisset = {"Python", "Django", "JavaScript", “SQL”}
# 10. Write a python program to find the maximum and minimum value in a set.

# 1) ....................................
# s={'C','C++','Java','Python','HTML','Css','js'}
# print(s)


# 2) ..................................
# from http.client import _DataType


# name=input("Enter name : ")
# age=int(input("ENter age : "))
# gender=input('Enter gender : ')
# a={name,age,gender}
# print((a))


# 3) ...........................
# a={1,2}
# print(type(a))

# 4) ...........................
# thisset = {"Java","Python", "Django"}
# if 'Python' in thisset:
#     print("Find")
# else:
#     print("not find")

# 5) ..........................
# thisset1 = {"Java", "Python", "SQL"}
# thisset2={'C','C++','HTML','Css','js'}
# thisset1=thisset1.union(thisset2)
# print(thisset1)


# 6) ................................
# thisset3 = {"Python", "Django", "JavaScript"}
# mylist = ["Java", "C"]
# for e in mylist:
#     thisset3.add(e)
# print(thisset3)

# 7) ...................................
# thisset5 = {"Python", "Django", "JavaScript", 'SQL'}
# thisset5.remove("SQL")
# print(thisset5)


# 8) ...........................
# thisset6 = {"Python", "Django", "JavaScript", 'SQL'}
# del thisset6
# print(thisset6)

# 9) ....................................
# thisset7 = {"Python", "Django", "JavaScript"}
# for i in thisset7:
#     print(i,end=' ')

# 10) .................................
min_max={1,2,3,4,22,66,11,77,99,45,23,12}
print(max(min_max))
print(min(min_max))