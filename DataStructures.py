#Data structures are containers to hold multiple values.

#list - Ordered, Mutable collection
fruits = ['apple', 'banana', 'grapes','orange','Mango'];
print("1", fruits[2]);
print("2", fruits.append('Mango'));
print("3", fruits.count('Mango'));
fruits.reverse()
print("4", fruits);
fruits.remove('orange')
print("5", fruits);
print("6", fruits.pop(-1));
print("7", fruits);


#tuple - Ordered, immutable collection
marks = (85, 95, 70, 65, 80, 100, 44);
#marks[0] = 100; #Error as it is immutable;
print(marks);
print(len(marks));

#Set - Unordered collection of unique items
cars =  {"Hyundai", "Maruti", "Skoda", "Suzuki", "Ford"};
cars.add("Volkswagen");
print(cars);
print(cars.pop());
carsCopy = cars.copy();
cars.add('Jaguar');
print(carsCopy);
carsDiff = cars.difference(carsCopy);
print(carsDiff);
cars.remove('Skoda')
print(cars);
print(carsCopy);
carsCopy.remove('Hyundai')
print('------')
print(cars);
print(carsCopy);

#dict - Key Value Pairs. Python 3.7 (officially), dictionaries preserve insertion order.  (Ordered &  Mutable collection)
students = {"name":"alice", "age":20, "city":"ohio", "pincode":606010, "result":"PASS"};
print(students["name"]);
students["grade"] = "A";
students["isActive"] = True;
print(students);
students["age"] = 30;
print(students);
print(students.keys());
