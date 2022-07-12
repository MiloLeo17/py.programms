class car:
    def __init__(self, num):
        self.num = num
        self.list_status = ['Стоит', 'Едет']
        self.status = self.list_status[0]

    def stop(self):  # Машина стоит
        self.status = self.list_status[0]
        return self.status

    def drive(self):  # Машина едет
        self.status = self.list_status[1]
        return self.status


class car_stream:
    def __init__(self, video):
        self.stream = [car(index) for index in range(1, video.calc_cars() + 1)]

    def stream_wait(self):  # Поток машин ждет
        return all([car.stop() for car in self.stream])

    def stream_drive(self):  # Поток машин едет
        return all([car.drive() for car in self.stream])

    def stream_clean(self):  # Очистить очередь(машины проехали)
        return self.stream.clear()


class traffic_light:
    def __init__(self, auto_stream, switch_time=30):
        self.list_colors = ['Красный', 'Зелёный']
        self.color = self.list_colors[0]
        self.switch_time = switch_time
        self.auto_stream = auto_stream

    def change_color(self):  # меняет цвет сигналa светофора
        if self.color == self.list_colors[0]:
            self.color = self.list_colors[1]
        else:
            self.color = self.list_colors[0]
        return self.color

    def calculate_time(self):  # считает время, необходимое для преодоления перекрестка машинами
        time = 0
        for i in self.auto_stream.stream:
            if time == 0:
                time += 7
            else:
                time += 4
        average_time = time / self.switch_time
        if average_time < 0.8:
            while average_time < 0.8:
                time += 1
                average_time = time / self.switch_time
            return time
        elif average_time > 1.2:
            while average_time > 1.2:
                time -= 1
                average_time = time / self.switch_time
            return time
        else:
            return time


class camera:
    def __init__(self, enum):
        self.enum = enum

    def calc_cars(self):  # считает количество машин
        num_cars = int(input('Обнаруено машин: '))
        return num_cars


cam = camera(1)
cars = car_stream(cam)
traf = traffic_light(cars)
print(traf.color)
if traf.color == 'Красный':
    cars.stream_wait()
else:
    cars.stream_drive()
for car in cars.stream:
    print(f'Машина №{car.num} {car.status}')
print(f'Зелёный будет гореть {traf.calculate_time()} секунд')
print(f'Загорелся {traf.change_color()}')
cars.stream_drive()
for car in cars.stream:
    print(f'Машина №{car.num} {car.status}')
cars.stream_clean()
print(f'Машин осталось{cars.stream}')
