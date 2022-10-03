class Student:
    ...

def main():
    student = get_student()
    print(f'{student.name} from {student.house}')

def get_student():
    # calling Student class
    student = Student()

    # giving Student name--> attribute (storing values inside Student class)
    student.name = input('Name: ')
    student.house = input('House: ')

if __name__ == '__main__':
    main()
