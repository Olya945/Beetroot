class Person:
    def __init__(self, name):
        self.name = name
        self.status = 'active'

    def info(self):
        raise NotImplementedError
    
    def change_status(self, new_status):
        self.status = new_status
        return self.status
    
class Teacher(Person):

    def __init__(self, name, salary, subject, group):
        super().__init__(name)
        self.salary = salary
        self.subjects = []
        self.groups = []
        self.assign_subject(subject)
        self.assign_group(group)
    
    def info(self):
        return f'<Teacher: {self.name}, status: {self.status}, groups: {len(self.groups)}, subjects: {len(self.subjects)}>'

    def assign_subject(self, subject_name):
        if subject_name not in self.subjects:
            self.subjects.append(subject_name)
    
    def remove_subject(self, subject_name):
        if subject_name in self.subjects:
            self.subjects.remove(subject_name)
    
    def assign_group(self, group_name):
        if group_name not in self.groups:
            self.groups.append(group_name)
    
    def remove_group(self, group_name):
        if group_name in self.groups:
            self.groups.remove(group_name)

    def get_all_subjects(self):
        return self.subjects.copy()
    
    def detailed_info(self):
        return (f'Teacher: {self.name}\n'
                f'Status: {self.status}\n'
                f'Salary: {self.salary}\n'
                f'Subjects: {', '.join(self.subjects)}\n'
                f'Groups: {', '.join(self.groups)}'
                )

class Student(Person):

    def __init__(self, name, age, group, year, status = 'active'):
        super().__init__(name)
        self.age = age
        self.group = group
        self.year = year
        self.status = status
        self.grades = []
        self.avg_grade = 0.0
    
    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
            self.calculate_avg_grade()
        else:
            print(f'Error: grade must be from 1 to 12')

    def calculate_avg_grade(self):
        if self.grades:
            self.avg_grade = sum(self.grades) / len(self.grades)
        else:
            self.avg_grade = 0.0
        return round(self.avg_grade, 2)
    
    def get_all_grades(self):
        return self.grades.copy()

    def info(self):
        return f'<Student: {self.name}, {self.group}, {self.avg_grade}>'
    
    def promote_to_next_year(self):
        self.year += 1
        return self.year
    
    def detailed_info(self):
        return (f'Student: {self.name}\n'
                f'Age: {self.age}\n'
                f'Group: {self.group}\n'
                f'Course: {self.year}\n'
                f'Status: {self.status}\n'
                f'Average score: {round(self.avg_grade, 2)}\n'
                )



s1 = Student('Ivan', 20, 'a1', 5)
s2 = Student('Olena', 19, 'a2', 5)

s1.add_grade(12)
s1.add_grade(11)
s1.add_grade(0)

s2.add_grade(8)
s2.add_grade(9)
s2.add_grade(7)

print(s1.name)
print(s2.name)
print(s1.info())
print(s2.info())
print(s1.detailed_info())
print(s2.detailed_info())

teacher = Teacher('Ivanova', 40000, 'math', 'a1')
teacher.assign_subject('biology')
print(teacher.info())
print(teacher.name)
print(teacher.get_all_subjects())