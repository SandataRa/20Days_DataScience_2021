#Task N°1
import csv, json, sys

input_file = './CSV File/iris.csv'
output_file = './iris.json'
data = {}
species = set()

try:
    with open(input_file) as fileC:
        reader = csv.DictReader(fileC) 
        for row in reader:
            if row['species'] not in species:
                species.add(row['species'])
                data[row['species']] = { 'count': 0,
                                        'flowers': []
                                        }
            iris = {}
            for e in row:
                if e != 'species':
                    iris[e] = row[e]
            data[row['species']]['count'] +=  1 
            data[row['species']]['flowers'].append(iris)

except IOError:
    print('Failed to read file.')

if not data:
    raise ValueError('No data found.')           

try:
    with open(output_file,'w') as fileJ:
        json.dump(data, fileJ, indent = 2)
except IOError:
    print('Failed to write JSON file.')
except:
    print(sys.exc_info())    
finally:
    print("END of the program")

#Exercice N°1

class Student:

    def __init__(self, name, gpa):
        self.__name = name
        self.__gpa = gpa
        self.__clubs = set() # contains unique elements 
        self.__active = True

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name 

    def get_gpa(self):
        return self.__gpa
    
    def set_gpa(self, gpa):
        self.__gpa = gpa

    def add_club(self, clubname):
        self.__clubs.add(clubname)

    def remove_club(self, clubname):
        self.__clubs.remove(clubname)

    def list_clubs(self):
        return self.__clubs
    
    def get_active(self):
        return self.__active

    def set_active(self, status):
        self.__active = status

    def student_details(self):
        print("STUDENT IDENTITY " + self.__name)
        print("_ GPA  :" + str(self.__gpa) )
        print("_ Clubs:")
        print(self.__clubs)

# s1 = Student('Mark',4.2)
# s1.add_club('Theatre')
# s1.add_club('Dance')
# print(s1.get_name())
# s1.student_details()

students = [
    {'name': 'Nina', 'gpa': 3.6, 'clubs': ['tennis','chess']},
    {'name': 'Emily', 'gpa': 3.9, 'clubs': ['tennis'], 'active': False},
    {'name': 'Michael', 'gpa': 3.2, 'clubs': ['football','chess']},
    {'name': 'Joe', 'gpa': 3.3, 'is_honors_student': True}
]


def init_classroom(students):
    classroom = []
    for std in students:
        s = Student(std['name'], std['gpa'])
        # print(std)
        try:
            if 'active' in std.keys() :
                s.set_active(std['active'])

            if 'clubs' in std.keys():
                for c in std['clubs']:
                    s.add_club(c)
        except KeyError:
            print('The student does not have this attribute')
            continue
        finally:
            s.student_details()
            classroom.append(s)

    return classroom

res = init_classroom(students)
print(res)

#Exercice N°2
import math as m

class Circle:
    pi = m.pi

    def __init__(self,radius):
        self.__radius = radius

    def set_radius(self, rad):
        self.__radius = rad

    def get_perimeter(self):
        print(2 * Circle.pi * self.__radius)

    def get_area(self):
        print(Circle.pi * self.__radius**2)

c1 = Circle(12)
c1.get_perimeter()
c1.get_area()

# Task N°2
class Employee():

    def __init__(self ,employeeID ,salary):
        self.__employeeID = employeeID
        self.__salary = salary
    
    def show_employee_card(self):
        print("Employe ID : " + self.__employeeID)

    def get_total_pay(self):
        print("I earn:", self.__salary,"$ per month")

    def get_employee_id(self):
        return self.__employeeID

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary 

class FulltimeEmployee(Employee):

    def __init__(self ,employeeID ,salary ,stockoption):
        fulltimeID = 'FT_' + employeeID
        super().__init__(fulltimeID, salary)
        self.__stockoption = stockoption #percentage 

    def get_total_pay(self):
        s = self.get_salary() + int(self.get_salary() * self.__stockoption) 
        print("I earn:", s,"$ per month")

class ContractEmployee(Employee):
    
    def __init__(self, employeeID, salary, commissionFee):
        contractID = 'CT_' + employeeID
        super().__init__(contractID, salary) 
        self.__commissionFee = commissionFee

    def get_total_pay(self):
        s = self.get_salary() + self.__commissionFee
        print("I earn:", s,"$ per day")

# INSTANCIATION
e1 = Employee('001',1000)
f2 = FulltimeEmployee('002',1500, 0.2)
c3 = ContractEmployee('003',550, 120)

e1.show_employee_card()
f2.show_employee_card()
c3.show_employee_card()
        
e1.get_total_pay()
f2.get_total_pay()
c3.get_total_pay()
    
#Task N°3
class Competition:

    def __init__(self, name, prize):
        self.__name = name
        self.__prize = prize

    def __repr__(self):
        return "('{}' - {})".format(self.__name, self.__prize)

    def __str__(self):
        return "NAME: {} | PRIZE: {}".format(self.__name, self.__prize)

archery = Competition('Archery', 2000)
print(archery)
print(repr(archery))

#Exercice N°3
class Employee:

    __companyName = 'TRA Corp'

    def __init__(self, employeeID):
        self.__employeeID = employeeID

    @property
    def employeeID(self):
        return self.__employeeID

    @employeeID.setter 
    def employeeID(self, id):
        self.__employeeID = id

    @classmethod
    def workplace(cls):
        print("I work at ", cls.__companyName)

    @classmethod
    def renameCompany(cls, company):
        cls.__companyName = company

    @staticmethod
    def companyInformation():
        print("Founded in 2020 by Sandratra")

# INSTANCIATION
e1 = Employee('Laura Jones')
print(e1.employeeID)
e1.workplace()
e1.renameCompany('SR Company')
e1.workplace()
Employee.companyInformation()

    
#Task N°4
from abc import ABC, abstractmethod
class Hominidae(ABC):

    @abstractmethod
    def diet(self):
        pass

    abstractmethod
    def walk(self):
        pass

    def behavior(self):
        print("I'm a complex living being.")

class Human(Hominidae):

    def diet(self):
        print("I am Omnivorious")

    def walk(diet):
        print("I am biped")

h1 = Human()
h1.diet()
h1.walk()
h1.behavior()