class Time:
    def __init__(self, hours: int, minutes: int):
        if 0 <= hours < 24 and 0 <= minutes < 60:
            self.hours = hours
            self.minutes = minutes
        else:
            print ("invalid time value")

    def show(self):
        if self.minutes < 10:
            return f'{self.hours}:0{self.minutes}'
        else:
            return f'{self.hours}:{self.minutes}'

    def isDay(self):
        if 12 <= self.hours < 18:
            self.hello = "Добрый день"
            return True

    def isMorning(self):
        if 6 <= self.hours < 12:
            self.hello = "Доброе утро"
            return True

    def isEvening(self):
        if 18 <= self.hours <= 23:
            self.hello = "Добрый вечер"
            return True

    def isNight(self):
        if 0 <= self.hours < 6:
            self.hello = "Доброй ночи"
            return True

    def sayHello(self):
        self.hello = ""
        Time.isDay(self)
        Time.isMorning(self)
        Time.isEvening(self)
        Time.isNight(self)
        return self.hello

    def add(self, new_min: int):
        self.minutes += new_min
        if self.minutes >= 60:
            self.hours += int(self.minutes / 60)
            self.minutes = self.minutes % 60
        if self.hours >= 24:
            self.hours = self.hours % 24

time_example1 = Time(25, 40)
time_example2 = Time(25.5, 40)

time_example3 = Time(15, 40)
print(time_example3.show())
print(time_example3.sayHello())
time_example3.add(600)
print(time_example3.show())
print(time_example3.sayHello())
