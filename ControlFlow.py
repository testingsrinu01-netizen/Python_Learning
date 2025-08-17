#For Loop
for i in range(6):
 print(i)

fruits = ["Apple","Banana","Grapes"];
for fruit in fruits:
 print(fruit);

husband = ["Bob", "John", "Steve"]
wife = ["Alice", "Mary", "Jessica"]
counter=0;
for h in husband:
 for w in wife:
  print(h,w)
  wife.remove(w);
  break;


#While
i=0
while i<6:
 print(i)
 i=i+1

#if-Else
age = 18;
if age>=18:
 print("Adult")
else:
 print("child")