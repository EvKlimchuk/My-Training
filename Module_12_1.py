import unittest
from Unit_test import Runner


"""class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name
"""

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        # Тестирование метода walk
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50, "After walking 10 times, distance should be 50")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        # Тестирование метода run
        runner = Runner("TestRunner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100, "After running 10 times, distance should be 100")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        # Тестирование вызова run и walk для двух объектов
        runner1 = Runner("Runner1")
        runner2 = Runner("Runner2")
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance, "Runner distances should not be equal")
        self.assertEqual(runner1.distance, 100, "Runner1 should have a distance of 100")
        self.assertEqual(runner2.distance, 50, "Runner2 should have a distance of 50")


if __name__ == "__main__":
    unittest.main()
