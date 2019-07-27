class Employee:
    def __init__(self, emp_no, name, qual, sal, dept_name):
        self.emp_no = emp_no
        self.name = name
        self.qual = qual
        self.sal = sal
        self.dept_name = dept_name

    def show_info(self):
        print(f"{self.emp_no}:{self.name}:{self.qual}:{self.sal}:{self.dept_name}")

    def increment_sal(self, inc_amount):
        self.sal += inc_amount
        print(f"{self.name} salary after increment {self.sal}")

