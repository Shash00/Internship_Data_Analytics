class Car:

    def __init__(self, regno, no_gear):
        self.regno = regno
        self.no_gear = no_gear
        self.is_started = False
        self.c_gear = 0

    def start(self):
        if self.is_started:
            print('Car is already started')
        else:
            print(f"Car {self.regno} has started")
            self.is_started = True

    def stop(self):
        if self.is_started:
            print(f"Car {self.regno} has stopped")
            self.is_started = False
        else:
            print('Car is already stopped')

    def change_gear(self):
        if self.is_started:
            if self.c_gear <= self.no_gear:
                print(f"Car {self.regno} has changed gear to {self.c_gear}")
                self.c_gear += 1
            else:
                print('Car already in top gear')
        else:
            print('Car is stopped, cannot change gears')
