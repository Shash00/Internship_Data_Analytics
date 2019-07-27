from emp import Employee

if __name__ == '__main__':

    emp1 = Employee(1, 'Shash', 'BE', 30000, 'IS')
    emp2 = Employee(2, 'abcd', 'MTech', 50000, 'CS')
    emp1.show_info()
    emp2.increment_sal(2000)
    emp2.show_info()
