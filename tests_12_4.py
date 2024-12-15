import logging
import unittest

logging.basicConfig(
    level=logging.INFO,
    filename='runner_tests.log',
    filemode='w',
    encoding='utf-8',
    format='%(asctime)s: %(levelname)s: %(message)s'
)

class Runner:
    def __init__(self, name, speed=5):
        if not isinstance(name, str):
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        if speed > 0:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
        self.name = name
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

#first = Runner('Вося', 10)
#second = Runner('Илья', 5)
#third = Runner('Арсен', 10)

#t = Tournament(101, first, second)
#print(t.start())

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner(name="Илья", speed=-5)


            logging.info('"test_walk" выполнен успешно')
        except ValueError :
            logging.warning("Неверная скорость для Runner")

    def test_run(self):
        try:
            runner = Runner(name=123, speed=10)

            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")