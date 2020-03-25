class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police


    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f' Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

        def show_speed(self):
            print(f'Current speed of work car {self.name} is {self.speed}')

            if self.speed > 60:
                return f'Speed of {self.name} is higher than allow for work car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'

audi = SportCar(100, 'Black', 'Audi', False)
jeep = TownCar(30, 'Silver', 'Jeep', False)
skoda = WorkCar(70, 'White', 'Skoda', True)
ford = PoliceCar(110, 'Blue',  'Ford', True)
print(skoda.turn_left())
print(f'When {jeep.turn_right()}, then {audi.stop()}')
print(f'{skoda.go()} with speed exactly {skoda.show_speed()}')
print(f'{skoda.name} is {skoda.color}')
print(f'Is {audi.name} a police car?? {audi.is_police}')
print(f'Is {skoda.name} a police car? {skoda.is_police}')
print(audi.show_speed())
print(jeep.show_speed())
print(ford.police())
print(ford.show_speed())