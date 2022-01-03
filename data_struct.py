#Task 1
#write a Python program which accepts the radius of a circle from the user and computes area.
radius=float(input("Enter radius of circle: "))
pi=22/7
print(pi*radius**2)

#Task 2
#write a Python program to accept a filename from the user and print the extension of that.
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + (f_extns[-1]))
