#from cgi import test
from montecarlo import Die
from montecarlo import Game
from montecarlo import Analyzer
import unittest
import pandas as pd

class DieTestSuite(unittest.TestCase):
    
    def test_weight_change(self):
        dice = [1,2,3,4,5,6]
        dicetest = Die(dice)
        dicetest.change_weights(4,3.0)
        testValue = 3.0
        message = 'Weight was not changed'
        self.assertTrue(testValue,message)
    def test_dice_roll(self):
        dice = [1,2,3,4,5,6]
        dicetest = Die(dice)
        dicetest.dice_roll(5)
        testValue = len(dicetest.result)
        actual = 5
        self.assertEqual(testValue,actual)
    def test_show_dice(self):
        dice = [1,2,3,4,5,6]
        dicetest = Die(dice)
        dicetest.dice_roll(5)
        testValue = len(dicetest._df.columns)
        expected = 1
        self.assertEqual(testValue,expected)
class GameTestSuite(unittest.TestCase):
    def test_play_game(self):
        dice = Die([1,2,3,4,5,6])
        dice2 = Die([2,4,6,8,10])
        thelist = [dice, dice2]
        dicetest = Game(thelist)
        dicetest.play_game(5)
        testValue = len(dicetest._gamedf.index)
        expected = 5
        self.assertEqual(testValue,expected)
    def test_show(self):
        dice = Die([1,2,3,4,5,6])
        dice2 = Die([2,4,6,8,10,12])
        thelist = [dice, dice2]
        dicetest = Game(thelist)
        dicetest.play_game(5)
        dicetest.show_results('Narrow')
        testValue = len(dicetest._gamedf.columns)
        expected = 1
        self.assertEqual(testValue,expected)
class AnalyzerTestSuite(unittest.TestCase):
    def test_jackpot(self):
        dice = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        thelist = [dice, dice2]
        dicetest = Game(thelist)
        dicetest.play_game(300)
        analyze = Analyzer(dicetest)
        analyze.jackpot()
        testValue = analyze.total >= 1
        message = 'Try again'
        self.assertTrue(testValue,message)
    def test_combo(self):
        dice = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        thelist = [dice, dice2]
        dicetest = Game(thelist)
        dicetest.play_game(300)
        analyze = Analyzer(dicetest)
        analyze.combo()
        testValue = sum(analyze.combodf['n'])
        expected = 300
        self.assertEqual(testValue,expected)
    def test_show_face_count(self):
        dice = Die([1,2,3,4,5,6])
        dice2 = Die([1,2,3,4,5,6])
        thelist = [dice, dice2]
        dicetest = Game(thelist)
        dicetest.play_game(300)
        analyze = Analyzer(dicetest)
        analyze.show_face_count()
        testValue = len(analyze.facecountdf.index)
        expected = 300
        self.assertEqual(testValue,expected)

if __name__ == '__main__':
    unittest.main(verbosity=3)