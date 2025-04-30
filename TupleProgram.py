Tuple 
# Tuple--> it is similar to list except its immutable 
student=(102,2,30.5,"ram") 
print(student) 
Output: 

student1=tuple("sanika") 
print(student1) 
Output: 
for i in student: 
 print(i) 
Output: 

stud=list(student) 
print(stud) 
Output: 

stud[1]=80 
print(stud) 
Output: 

student=tuple(stud) 
print(student) 
Output:

student2=(1,2,3) 
l=student+student2 
print(l) 
Output: 

tuple1=(1,"ram",100.40,[1,2,3]) 
tuple1[3][2]=100 
print(tuple1) 
Output: 

1. Tuple Basics 
Write a Python program to create a tuple with some numbers (e.g., 10, 20,  30, 40, 50) and print its elements one by one. 
number=(10,20,30,40,50) 
for i in number: 
 print(i) 
output: 

2. Tuple Indexing 
Create a tuple with the names of five countries. Write a program to: - Print the first element. 
- Print the last element using negative indexing. 
- Print the third elemen''' 
name=("sanika","shweta","pari","payal","surekha") 
stud=list(name)
print("print the first element:",stud[1]) 
print("print the last element using negative indexing:",stud[-1]) 
print("print the third element:",stud[3]) 
output: 

3.Tuple Slicing 
Create a tuple with the numbers from 1 to 10. Write a program to: - Slice and print the first three elements. 
- Slice and print the last three elements.''' 
name=("sanika vitthal waghamare") 
print("Slice and print the first three elements:",name[:1]) 
print("Slice and print the last three elements:",name[21:24]) 
output: 

4. Tuple Concatenation 
Write a Python program to: 
- Create two tuples: one with even numbers and one with odd numbers. - Concatenate them into a single tuple and print the result.''' list1=(2,4,6,8,10,12) 
list2=(1,3,5,7,9,11) 
new_list=list1+list2 
print("Create two tuples: one with even numbers and one with odd  numbers:",list1+list2) 
print("Concatenate them into a single tuple and print the result:",new_list) output: 

5. Tuple Repetition 
Write a program to create a tuple with a single element (e.g., "Python") and repeat it  five times using the multiplication operator''' 
name=("sanika") 
new_name= (name,) 
print("five times using element the multiplication operator:",new_name*5)
output: 

6. Check Element Existence 
Create a tuple with five random numbers. Write a program to: - Check if a specific number (e.g., 5) exists in the tuple. - Print an appropriate message based on the result.''' 
num=(22,34,54,65,77) 
i=22 
if i in num: 
 print("true") 
else: 
 print("false") 
output: 

num=(22,34,54,65,77) 
print(77 in num) 
print(66 in num) 
output: 

7. Unpacking a Tuple 
Create a tuple with three elements (e.g., name, age, and city). 
Write a program to unpack these values into separate variables and print them. 
''' 
tuple1=("sanika",21,"Dombivali") 
(name,age,city)=tuple1 
print(name,age,city) 
output: 

8. Count Occurrences in a Tuple 
Write a Python program to: 
- Create a tuple with duplicate elements (e.g., (1, 2, 2, 3, 3, 3, 4)). - Count and print the number of times each unique element appears in  the tuple.'''
number=(1,2,2,3,3,3,3,3,3,3,4) 
new_number=number 
print(new_number.count(3)) 
print(number.count(2)) 
#print(number.count(3)) 
Output: 

9. Tuple Length 
Write a program to create a tuple with at least five elements and find its length using  the len() function.''' 
name=("sanika",23,"pooja",88,"arti") 
print("Tuple length:",len(name)) 
output: 

10. Convert List to Tuple 
Write a program to: 
- Create a list of five fruits (e.g., ["apple", "banana", "cherry", "date", "elderberry"]). - Convert this list into a tuple and print the result.''' 
fruits=["apple", "banana", "cherry", "date", "elderberry"] 
fruits_name=tuple(fruits) 
print("convert list to tuple :",fruits_name) 
output:

