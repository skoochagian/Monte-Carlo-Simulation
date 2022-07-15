import numpy as np
import pandas as pd
import random

#Die Class
class Die():
    '''
    Purpose: the purpose of this class is to create a dice by defining face values and their respective weights.
    '''
    def __init__(self,face_list):
        """ 
        Purpose: The initializing of default parameters and inputs for the class.
        
        Input
        --------
        face_list: A list of the dice faces for creating the dice. The values in the list can be strings or integers.
    
        Default parameters
        ----------------------
        Weight: A default list of weights where the weight is 1.0 for all values in face_list.
        df: A private dataframe that will hold all the faces and weights of the dice.

        """
        self.face = face_list
        weight = [1.0 for x in range(0,len(face_list))]
        self._df = pd.DataFrame(
            {'Weight': weight}, index = self.face)
        self._df.index.name = 'Face'

    def change_weights(self,face_value,weight_value):
        """
        Purpose: To change the weight of a particular face in the face_list

        Input
        --------
        face_value: the face value that will have a new weight assigned in weight
        weight_value: the new weight of the face. This value must be a numerical value, either float or integer
        
        Output
        ---------
        There is no output.
        """
        if face_value not in self.face:
            print('Face not on dice, try again.')
        elif type(weight_value) == str:
            print('Weight needs to be a numerical value') 
        elif type(weight_value)== int:
            float(weight_value)
        self._df.loc[face_value] = weight_value
        
    def dice_roll(self,rolls):
        """
        Purpose: This function rolls the dice and produces the results by adding them to a list
        
        Input
        --------
        rolls: the number of times the dice will be rolled
        
        Output
        --------- 
        result: A list of the results that were rolled
        """
        self.result = random.choices(self._df.index, weights = self._df['Weight'], k = rolls)
        return self.result

    def show_dice(self):
        """
        Purpose: This function shows the dataframe of the faces and the weights

        Input
        -------
        None
        
        Output 
        --------
        df: The dataframe with the face values as the index and the weights as the column
        """
        return self._df

#Game Class
class Game():
    '''
    Purpose: The purpose of this class is to produce a game of rolling one or more dice.
    '''
    def __init__(self, die_list):
        """
        Purpose: Initializes the list of dice.

        Input
        -------
        die_list: A list of die,where the values are using the Die class. There must be a minimum of one die in the list in order to be used.

        Output
        --------
        There is no output.
        """
        self.die_list = die_list
        return None
    
    def play_game(self,rolls):
        """
        Purpose: This function plays a game where a dice is rolled. Each dice that is in the list is rolled a certain number of times. 
        The results are put into a private dataframe.

        Input
        -------
        rolls: The number of time each dice will be rolled. The value must be an integer, and at least one.
        
        Output 
        ---------
        _gamedf: A private dataframe. The roll numbers are the index of the dataframe and the dice numbers are the columns. 
        The columns have the resulting face values from the game as the elements in the columns.
        
        """
        self.rolls = rolls
        self._gamedf = pd.DataFrame() #will make this private later 'self._df
        for i in range(len(self.die_list)):
            x = pd.DataFrame({str(i+1) :self.die_list[i].dice_roll(rolls)}, index = range(1,rolls+1)) #Dice roll should be a number not a list
            x.index.name = 'Roll'
            self._gamedf = pd.concat([self._gamedf, x],axis = 1) #this is being problematic, need to get this into the dataframe
        return self._gamedf
    
    def show_results(self, type = 'Wide'):
        """
        Purpose: This function provides an option to style the previous dataframe in a certain style. 

        Input
        -------
        type: A string of how the dataframe will be formatted. The two options are 'Wide' or 'Narrow'. 
            - The wide format is the default format that the dataframe is normally formatted in.
            - The narrow format will format the dataframe with the roll number and dice number as the two indicies, with the one 
              column being the faces.
        
        Output 
        -------
        _gamedf: The result is the dataframe in the format that was put into the function.
        """
        self.rolls = self.rolls
        if type == 'Wide': 
            return self._gamedf
        elif type == 'Narrow':
            self._gamedf = pd.DataFrame(self._gamedf.stack())
            self._gamedf.columns = {'Face'}
            return self._gamedf
        else:
            print('Incorrect format type.')
#Analyzer class
class Analyzer():
    """
    Purpose: Analyzing the results of the Game class.
    """
    def __init__(self,game):
      """
      Purpose: Initializing the input of the class function.

      Input
      -------
      game: A game that is 
      """
      self.game = game
     
    def jackpot(self):
      """ 
      Purpose: This function shows how many times the dice produced the same face on the same roll 
      
      Input 
      --------
      There is no input

      Output
      ---------
      total: The number of times the dice produce the same face on the same roll.

      """
      self.rolls = self.game.rolls
      self.game._gamedf = self.game._gamedf
      self.total = 0
      x = pd.DataFrame({'Jackpot':self.game._gamedf.nunique(axis = 1)}, index = range(1,self.game.rolls))
      x.index.name = 'Roll'
      for i in x['Jackpot']:
        if i == 1:
          self.total += 1
      return self.total

    def combo(self):
        """
        Purpose: Calculates the number of times a combination of results appears through the game.

        Input 
        --------
        There is no input.

        Output 
        ---------
        combodf: A series with the rows as dice result combinations, and the column as the number of times that combination was rolled.
        
        """
        self.result = self.game.show_results()
        self.combodf = self.result.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('n')

    def show_face_count(self):
        """
        Purpose: Stores the count of face combinations rolled into a dataframe.

        Input 
        --------
        There is no input.

        Output
        --------
        There is no output.
        """
        self.result = self.game.show_results('Wide')
        self.facecountdf = self.result.apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)