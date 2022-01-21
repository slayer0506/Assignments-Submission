#FUNCTION 1:
def function_1(Name,Age,Programs_Learnt,Marks_scored,highest_marks,Salary,is_passed):
    print(f"My name is :{Name} aged {Age} i learnt {Programs_Learnt} programs marks of the subject: {Marks_scored} and highest marks scored in {highest_marks} earns {float(Salary)} passed status: {is_passed} .")

function_1('Pratham',19,['C','java','python'],(98,65,76.54),{'C': 98},87250,True)


#FUNCTION 2: 
def function_2(a):
    for key,values in a.items():
        print(f"key is: {key} and its value is: {values}")
dict = {
    'Name':'Pratham Goverkar',
    'Age':19,
    'Marks':89.98,
    'Place':'Navi Mumbai',
    'subject':'MP,OSTL,Maths',
    'salary': 29000.00
}  
function_2(dict)

#FUNCTION 3:
def function_3():
    Name = "Pratham Goverkar"
    Age = 19   
    return [Name, Age];  
    
list = function_3() 
print(list)
    