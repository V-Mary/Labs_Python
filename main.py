class Lift:
    shop = "World of lifts"

    @staticmethod
    def greeting():
       return Lift.shop

    def __init__(self, name, load_capacity, power_consumption):
        self.name = name
        self.load_capacity = load_capacity
        self.power_consumption = power_consumption

    def __str__(self):
        return f"Lift- {self.name},load capacity- {self.load_capacity} kg,engine consumption- {self.power_consumption}W"

    def __del__(self):
        pass


def main():
    Apple = Lift("SUPER", 3000, 640)
    Nokia = Lift("MINI", 3500, 250)
    Acer = Lift("HUGE", 4000, 800)

    print(Apple, "\n", Nokia, "\n", Acer)

    Lift.greeting()

if __name__ == '__main__':
    main()
