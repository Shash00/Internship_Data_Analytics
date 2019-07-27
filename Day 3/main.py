from car import Car
if __name__ == '__main__':
    bmw = Car('KA19MH1204', 5)
    audi = Car('KA19MH12456', 6)
    rolls = Car('KA19MH2455', 5)
    honda = Car('KA19MH1245', 5)
    toyo = Car('KA19MH1224', 5)
    bmw.start()
    audi.start()
    honda.start()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.change_gear()
    bmw.stop()

    lst = [bmw, audi, rolls, honda, toyo]

    c = len(list(filter(lambda x: x.is_started and x.c_gear == 0, lst)))
    print(c)


