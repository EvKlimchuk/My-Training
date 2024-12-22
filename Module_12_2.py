import unittest

# Code for testing

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
            """
            Original code
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        
            """
            for participant in sorted(self.participants, key = lambda x: x.speed, reverse=True):
                participant.run()
            for participant in list(self.participants): #Ensure removal doesn't interfere with iteration
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)
        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_usain = Runner("Usain", speed=10)
        self.runner_andrey = Runner("Andrey", speed=9)
        self.runner_nick = Runner("Nick", speed=3)

    @classmethod
    def tearDownClass(cls):
        print("\nAll Results:")
        for key, value in cls.all_results.items():
            readable_results = {k: v.name for k, v in value.items()}
            print(f"{key}: {readable_results}")

    def test_usain_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Nick"] = results
        self.assertTrue(results[max(results)].name == "Nick")

    def test_andrey_nick(self):
        tournament = Tournament(90, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Andrey vs Nick"] = results
        self.assertTrue(results[max(results)].name == "Nick")

    def test_usain_andrey_nick(self):
        tournament = Tournament(90, self.runner_usain, self.runner_andrey, self.runner_nick)
        results = tournament.start()
        TournamentTest.all_results["Usain vs Andrey vs Nick"] = results
        self.assertTrue(results[max(results)].name == "Nick")

    def test_no_progress_participant(self): # Дополнительный тест на проверку самого медленного бегуна
        slow_runner = Runner("Slow", speed=1)
        tournament = Tournament(20, self.runner_usain, slow_runner)
        results = tournament.start()
        TournamentTest.all_results['Usain vs Slow'] = results
        self.assertTrue(results[max(results)].name == "Slow")

if __name__ == "__main__":
    unittest.main()

