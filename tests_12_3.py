import unittest

def skip_if_frozen(test_func):
    def wrapper(self, *args, **kwargs):
        if getattr(self, 'is_frozen', False):
            self.skipTest('Тесты в этом кейсе заморожены')
        return test_func(self, *args, **kwargs)
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_challenge(self):
        self.assertEqual(1 + 1, 2)

    @skip_if_frozen
    def test_run(self):
        self.assertTrue(True)

    @skip_if_frozen
    def test_walk(self):
        self.assertFalse(False)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @skip_if_frozen
    def test_first_tournament(self):
        self.assertEqual(1, 1)

    @skip_if_frozen
    def test_second_tournament(self):
        self.assertEqual(2, 2)

    @skip_if_frozen
    def test_third_tournament(self):
        self.assertEqual(3,3)