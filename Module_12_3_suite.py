import unittest
import Module_12_1, Module_12_2

moduleST = unittest.TestSuite()
moduleST.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_1.RunnerTest))
moduleST.addTest(unittest.TestLoader().loadTestsFromTestCase(Module_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(moduleST)