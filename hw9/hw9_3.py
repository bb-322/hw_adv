import unittest

class Student():
    def __init__(self, name:str, surname:str, avg_grade:int | float):
        
        if not isinstance(name, str):
            raise TypeError('invalid name: expected str')
        if not isinstance(surname, str):
            raise TypeError('invalid surname: expected str')
        if not isinstance(avg_grade, (int,float)):
            raise TypeError('invalid avg_grade: expected int or float') 
        if not avg_grade > 0:
            raise ValueError('invalid avg_grade: expected more than 0')
        
        self._name = name
        self._surname = surname
        self._avg_grade = avg_grade

class TestStudent(unittest.TestCase):
    def test_students(self):
        st_list = [
            ('Alice', 'Smith', 88.5, None),
            ('Bob', 'Johnson', 75, None),
            ('Charlie', 'Brown', 92, None),
            
            (123, 'Williams', 80, TypeError),           # err: name not str
            ('David', 456, 85, TypeError),              # err: surname not str
            ('Eve', 'Davis', '90', TypeError),          # err: avg_grade not int or float
            ('Frank', 'Miller', -10, ValueError),        # err: avg_grade < 0
            ('Grace', 'Wilson', 0, ValueError),          # err: avg_grade = 0
            ('Heidi', 'Moore', None, TypeError),        # err: avg_grade None
            ('Ivan', 'Taylor', [100], TypeError),       # err: avg_grade - list
        ]
        for name, surname, avg_grade, expected_err in st_list:
            with self.subTest(name=name, surname=surname, avg_grade=avg_grade):
                if expected_err is None:
                    student = Student(name, surname, avg_grade)
                    self.assertIsInstance(student._name, str)
                    self.assertIsInstance(student._surname, str)
                    self.assertIsInstance(student._avg_grade, (int, float))
                else:
                    with self.assertRaises(expected_err):
                        Student(name, surname, avg_grade)