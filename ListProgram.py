List programs
#1Create and Print a List: Write a program to create a list of 5 integers and print 

list1=[1,2,3,4,5]
for i in list1
print(i)

#1.Create and Print a List: Write a program to create a list of 5 integers and print each element using a loop.

list1=[1,2,3,4,5]
for i in list1:
    print(i)


#2. Sum of Elements: Write a function that takes a list as input and returns the sum of its elements
number=[2,4,5,6,7,]
total=sum(number)
print(total)

output:

#3. Find Maximum and Minimum: Write a program to find the maximum and minimum values in a list.
list1=[2,3,4,5,6,7]
print("maximum number:",max(list1))
print("miniimum number:",min(list1))

#4. Append an Element: Add an element to a list and display the updated list.
list=["sanika","sakshi","kiran","shweta"]
list.append("pooja")
print(list)
Output:


#5. Remove an Element: Remove a specific element from a list using remove() and display the updated list.

student=["sanika","sakshi","kiran","shweta"]
student.remove("sakshi")
print(student)

Output:


#7. Index of an Element: Find the index of a specific element in a list.

name=["sanika","sakshi","nandini","samir","samir"]
print("index of sakshi:",name.index("sakshi"))
Output:


name=["sanika","sakshi","nandini","samir","swara","samir","payal"]
print("index of sakshi:",name.index("sakshi"))
print("index of samir:",name.index ("samir",3,6))

Output:


#8. Reverse a List: Reverse a list using slicing and display the reversed list.
name=["swara",222,"maira",[2,3,4]]
name.reverse()
print(name)
Output:


name=["swara",222,"maira",[2,3,4]]
name.reverse()
print(name[-1:-3])

Output:


#9. Count Element Occurrences: Write a program to count how many times a specific element occurs in a list.

number=[23,45,32,56,78,90]
print("count of 56:",number.count(56) )

Output:


#10. Merge Two Lists: Merge two lists into a single list and display the result.
name=["swara",222,"maira",[2,3,4]]
number=[23,45,32,56,78,90]
name.extend(number)
print(name)'''
Output:


name=["swara",222,"maira",[2,3,4]]
number=[23,45,32,56,78,90]
new_list=name+number
print(new_list)
output:

















