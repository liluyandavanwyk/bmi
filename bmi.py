name = "Luyanda Isaac Van Wyk"
age = int(input("Enter your age: "))
height_meter = 2.0
weight_kilograms = 76


bmi = weight_kilograms / (height_meter ** 2)
print ("bmi: ")
print (bmi)


if bmi < 25:
    print ("age: ")
    print (age)
    print (name)
    print ("is not overweight")
           
else:
    print ("age: ")
    print (age)
    print (name)
    print ("is overweight")
               
