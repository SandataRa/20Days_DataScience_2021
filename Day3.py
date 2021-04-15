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
