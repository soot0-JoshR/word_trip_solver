######################################################
###                    pyscrabble                  ###
###          Programmed by Michael Warmbier        ###
### https://github.com/MichaelWarmbier/PyScrabbler ###
######################################################

### Libraries ###

import re 
import sys
import os
import random

##### Data Storage #####

# __file__ = '"C:\Users\r1tt3\Sikuli\word_trip.sikuli\word_trip.py"'

with open("C:\\Users\\r1tt3\\Sikuli\\word_trip.sikuli\\Dictionary.txt", 'r') as file:#  os.path.join(os.path.dirname(__file__), 'Dictionary.txt'), 'r') as file:
    wordList = file.read().splitlines()

## Constant letter point values
class letterValue:
  values = [[' '], 
            ['A','E','I','L','N','O','R','S','T','U'],
            ['D','G'],
            ['B','C','M','P'],
            ['F','H','V','W','Y'],
            ['K'],
            [],
            [],
            ['J','X'],
            [],
            ['Q','Z']];

class tempMemory:
  def __init__(self):
    self.storedLetters = []
    self.scannedLetters = []

##### Methods #####

## Returns point value of a specific letter
def getLetterValue(letter):
  for value in letterValue.values:
    if letter.upper() in letterValue.values[letterValue.values.index(value)]:
      return letterValue.values.index(value);
  raise Exception('Argument is NOT a valid Scrabble letter.');

def getWordValue(word):
  finalValue = 0;
  for char in word:
    finalValue += getLetterValue(char);
  return finalValue;

## Create table of letters and appearances
def createLetterTable(string):
  letterTable = [];
  index = 0;
  for letter in string: 
    letterTable.append([])
    letterTable[index].append(letter);
    letterTable[index].append(1)
    for entry in letterTable:
      if letterTable[index][0] == entry[0] and index != letterTable.index(entry):
        letterTable.remove(letterTable[index]);
        letterTable[letterTable.index(entry)][1] += 1;
        index -= 1;
    index += 1;
  return letterTable;

## Filters letters based on total
def filterRepeats(wordList, letters):
    filteredList = []
    for word in wordList:
        valid_word = True
        if word not in filteredList:
            for char in word:
                if word.count(char) > letters.count(char):
                    valid_word = False
            if valid_word:
                filteredList.append(word)
    return filteredList

## Gets all possible words given provided letters
def getScrabbleWords(letters):
  # if (len(letters) < 7 or len(letters) > 15):
  #  raise Exception ('Error: Letter count must be between seven and fifteen.');
    
  regex = re.compile('^([' + letters.upper() + '])*$');
  validWords = [];
  for word in wordList:
    if regex.match(word):
      validWords.append(word);
  validWords = filterRepeats(validWords, letters);
  # for word in validWords[:]:
  #  validWords[validWords.index(word)] = [word, getWordValue(word)];
  return validWords;

# If run from the console, print results based off arguments
"""
try:
  if (sys.argv == None or sys.argv[1] == None):
    raise IndexError;
  else:
    results = getScrabbleWords(sys.argv[1]);
    for index in results:
      print ('[' + index[0] + ']: ' + str(index[1]) + 'pts');
except IndexError:
  print('Error: No argument provided');
"""

def countAll(rege, image):
    count = 0
    for i in findAll(image):
        count += 1
    return count

holdup_region = Region(665,39,551,941)
x_region = Region(1157,152,37,34)
center = Region(922,729,38,31)

while True:
   
#    elif holdup_region.exists("1676886376718.png"):
#        click(holdup_region.find("1676886376718.png"))
    
    if x_region.exists("1677908043798.png"): 
        click("1677908043798.png")
        wait(1)
        
    elif holdup_region.exists("1676863951877.png"):
        click(holdup_region.find("1676863951877.png"))
        wait(1)
    
    elif holdup_region.exists("1676852909712.png"):
        click(holdup_region.find("1676852909712.png"))
        wait(1)
        
    elif holdup_region.exists("1676853252065.png"):
        click(holdup_region.find("1676853252065.png"))
        wait(1)
    
    elif holdup_region.exists("1676853434915.png"):
        click(holdup_region.find("1676853434915.png"))
        wait(1)
        
#    elif holdup_region.exists("1676959588008.png"):
#        click(holdup_region.find("1676959588008.png"))
#        wait(1)

    if holdup_region.exists("1676883823682.png"):
        click(holdup_region.find("1676883823682.png"))

    if holdup_region.exists("1676970154359.png"):
        click(holdup_region.find("1676970154359.png"))

    if holdup_region.exists("1676970612110.png"):
        click(holdup_region.find("1676970612110.png"))
        wait(1)

        if holdup_region.exists("1676970756092.png"):
            click(holdup_region.find("1676970756092.png"))
            wait(1)

        if holdup_region.exists("1677181853627.png"):
            click(holdup_region.find("1677181853627.png"))
            wait(1)

#    if holdup_region.exists("1676970154359.png"):
#        click(holdup_region.find("1676970154359.png"))
#        wait(2)
#        click(holdup_region.find("1676885153232.png"))

    swipe_circle = Region(765,574,352,352)
    #current_letters = swipe_circle.findText('S')
    
    letter_images = {'A': [Pattern("1676858539242.png").similar(0.87), Pattern("1677700006131.png").similar(0.86)], 'B': [Pattern("1676868122381.png").similar(0.85), Pattern("1677701679090.png").similar(0.90)], 'C': [Pattern("1676969154828.png").similar(0.93), Pattern("1677699929121.png").similar(0.92)], 'D': [Pattern("1676874980366.png").similar(0.91), Pattern("1677895830859.png").similar(0.90)], 'E': [Pattern("1676868240429.png").similar(0.88), Pattern("1677895165509.png").similar(0.89)], 
                        'F': [Pattern("1676882938766.png").similar(0.91), Pattern("1677893863948.png").similar(0.90)], 'G': [Pattern("1676874935172.png").similar(0.91), Pattern("1677660007863.png").similar(0.85)], 'H': [Pattern("1676853536051.png").similar(0.73), Pattern("1677917126824.png").similar(0.87)], 'I': [Pattern("1676868259952.png").similar(0.91), Pattern("1677659819492.png").similar(0.87)], 'J': [Pattern("1677408444157.png").similar(0.85)], 'K': [Pattern("1677181564533.png").similar(0.86)], 
                        'L': [Pattern("1676870167962.png").similar(0.84), Pattern("1677895877922.png").similar(0.88)], 'M': ["1676878614165.png", Pattern("1677701726099.png").similar(0.87)], 'N': [Pattern("1676873122716.png").similar(0.81), Pattern("1677700138266.png").similar(0.86)], 'O': [Pattern("1676853546164.png").similar(0.91), Pattern("1677699873734.png").similar(0.91)], 'P': [Pattern("1676858439980.png").similar(0.86), Pattern("1677700057501.png").similar(0.88)], 
                        'Q': '', 'R': [Pattern("1676858495828.png").similar(0.86), Pattern("1677659862076.png").similar(0.86)], 'S': [Pattern("1676853504751.png").similar(0.82), Pattern("1677908123476.png").similar(0.89)], 'T': [Pattern("1676868324615.png").similar(0.83), Pattern("1677659937217.png").similar(0.89)], 'U': [Pattern("1676968374769.png").similar(0.86), Pattern("1677659895142.png").similar(0.86)], 'V': [Pattern("1676970239118.png").similar(0.85), Pattern("1677775975048.png").similar(0.91)], 
                        'W': ["1676853554935.png", Pattern("1677916680352.png").similar(0.87)], 'X': ['', Pattern("1677895125541.png").similar(0.87)], 'Y': [Pattern("1676858518677.png").similar(0.85), Pattern("1677699162283.png").similar(0.85)], 'Z': ''}
    current_letters = ""
    image_locations = []
    for i in range(65, 91):
        if letter_images[chr(i)] != '':
            for image in letter_images[chr(i)]:
                if swipe_circle.exists(image):
                    all_current_letter = swipe_circle.findAll(image)
                    for current_letter_image in all_current_letter:
                        current_letters += chr(i)
                        image_locations.append(current_letter_image)
                    if len(current_letters) == 6:
                        break
            if len(current_letters) == 6:
                break
    
    print(current_letters)
    words = ""
    
    largest = len(current_letters)
    
    if current_letters != "":
        words = getScrabbleWords(current_letters)
    
    print(words)

    word_lengths =[] 
    
    for i in range(3, largest + 1):
        word_lengths.append(i)

    print(word_lengths)
    
    words = [word for word in words if len(word) in word_lengths]

    words = sorted(words, key=len, reverse=True)
    print(words)

    
    end_o_largest = 0
    for word in words:
        if len(word) < largest:
            break
        end_o_largest += 1

    n_lettered = words[:end_o_largest]
    smaller_words = words[end_o_largest:]
    
    random.shuffle(n_lettered)
    random.shuffle(smaller_words)

    words = n_lettered + smaller_words

    print(words)

    def mapToLocations(word):
        indices = []
        index = 0
        for letter in word:
            if word[:index+1].count(letter)> 1:
                indices.append(current_letters.find(letter, current_letters.find(letter) + word[:index].count(letter)))
            else:
                indices.append(current_letters.find(letter))
            index += 1
        return indices
    
    try:
        size_index = largest - 5
        for word in words:
            if not holdup_region.exists("1677701604850.png"):
                break
            
            print(word)
            locales = mapToLocations(word)
            i = 0
            for i in range(0, len(word)-2):
                #drag(swipe_circle.find(letter_images[word[i]][size_index]))
                drag(image_locations[locales[i]])
                drag(center)
           
            # dragDrop(swipe_circle.find(letter_images[word[0][i+1]]), swipe_circle.find(letter_images[word[0][i+2]]).offset(0,0))
            #drag(swipe_circle.find(letter_images[word[i+1]][size_index]))
            #dropAt(swipe_circle.find(letter_images[word[i+2]][size_index]))
            drag(image_locations[locales[i+1]])
            drag(center)
            dropAt(image_locations[locales[i+2]])

            if swipe_circle.exists("1677181853627.png"):
                click(swipe_circle.find("1677181853627.png"))

            if holdup_region.exists("1676970612110.png"):
                click(holdup_region.find("1676970612110.png"))
                wait(1)
        
                if holdup_region.exists("1676970756092.png"):
                    click(holdup_region.find("1676970756092.png"))
                    wait(1)
            
    except:
        print("Not sure what happened")
    
    wait(8)
    
    sys_region = Region(1868,938,48,95)
    click(sys_region.find("1676880803811.png"))
    wait(1)
    word_trip = Region(712,923,455,96)
    if word_trip.exists("1676880907507.png"): 
        click(word_trip.find("1676880907507.png"))
    elif word_trip.exists("1676881870412.png"):
        click(word_trip.find("1676881870412.png"))
    wait(1)
    click(sys_region.find("1676881009867.png"))
    word_trip_icon = Region(1008,509,136,147)
    wait(3)
    click(word_trip_icon.find("1676881103980.png"))
    wait(10)




