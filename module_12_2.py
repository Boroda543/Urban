class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

class Tournament:
    def __init__(self, distance, participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participants in self.participants:
                participants.run()
                if participants.distance >= self.full_distance:
                    finishers[place] = participants
                    place += 1
                    self.participants.remove(participants)

        return finishers



import unittest

class Tournamentest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner(name="Усейн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_rase_usain_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner3])
        results = tournament.start
        self.all_results = [max(results())]
        self.assertTrue == "Ник"

    def test_rase_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner2, self.runner3])
        results = tournament.start
        self.all_results = [max(results())]
        self.assertTrue == "Ник"

    def test_rase_usain_andrey_nik(self):
        tournament = Tournament(distance=90, participants=[self.runner1, self.runner2, self.runner3])
        results = tournament.start
        self.all_results = [max(results())]
        self.assertTrue == "Ник"

if __name__ == '__main__':
    unittest.main()