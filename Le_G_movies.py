"""
------------------------------------------
CSC 110 Final Programming Project
File: MovieData.py
Author: Gabe Le
Due:  11 December 2017
Note: This program will read a data file containing movies that were released between
    2000 - 2009 and display information that the user requests.
    The file has: Title, Genre, Run Time, Rating, Studio, and Year

IMPORTANT: Please resize your idle window accordingly (most likely bigger)
since I spaced out the outputs to look nicer and neater.
------------------------------------------
"""
#------------------------------------------
# used to find most common occurrence as in lab 5
from collections import Counter


# Checks if the input is a valid file located in the same directory as
#  this file and throws an exception if it does not exist
def checkFile():
    while (True):
        try:
            prompt = input("Enter the name of the data file: ")
            myFile = open(prompt, 'r')
            break
        except IOError:
            print("Invalid file name, please try again ... ")
    return myFile


# checks if the choice is valid and prompts the user to
# enter it again if it is not
def checkChoice():
    while (True):
        try:
            choice = int(input('Choice >>> '))
            if 1 <= choice <= 8:
                return choice
            else:
                print("Please enter a valid number...")
        except ValueError:
            print('Please enter a valid number...')


# Checks if the input is a valid genre, rating, or studio &
#  continues doing this until a correct input is given
def checkInput(aString, aList):
    while(True):
        pick = input("Enter the " + aString + ": ")
        if(pick in aList):
            return pick
        else:
            print("Invalid " + aString + " please try again")


# Checks if the year is valid (between 2000 & 2009) & if the first year is
#  smaller than the second year. Do not exit until the years are correct
def checkYear():
    print("Enter your range to search (oldest year first) 2000 -> 2009")
    keepGoing = True
    while (keepGoing):
        while (True):
            try:
                year1 = int(input("Year 1: "))
                year2 = int(input("Year 2: "))
                if ((2000 <= year1 <= 2009) and (2000 <= year2 <= 2009)):
                    break
                else:
                    print("Please enter a valid year")
            except ValueError:
                print("Invalid year! Please try again")
        # year2 should be a year larger than the first
        if (year2 < year1):
            print("Second year should be after first year -- Please try again")
        else:
            keepGoing = False
    return year1, year2
#------------------------------------------


# Searches a sorted list by discarding half of the list that
#  it knows does not contain the value until the value is found
def binarySearch(myList, aString):
    front = 0
    back = len(myList)-1
    while True:
        # this will be the pivot of the list
        middle = (back+front)//2
        if myList[middle] == aString:
            return middle
        # bounds have intercepted & nothing is found
        if front == back:
            print("not found")
            return -1
        if aString < myList[middle]:
            # only use the lower half
            back = middle - 1
        else:
            # only use the upper half
            front = middle + 1


# Searching algorithm which returns two sorted lists by
#  finding the minimum element and swapping it with the first index.
# This is repeated until the whole list is sorted. Front index is incremented
#  after minimum is found
def selectionSort(runtimeList):
    # keep track of where the min indexes are
    indexList = list(range(0, len(runtimeList)))
    tempList = runtimeList.copy()
    for i in range(1, len(tempList)):
        min = i
        for j in range(i + 1, len(tempList)):
            # comparison
            if int(tempList[j]) < int(tempList[min]):
                min = j
        # swap & add to indexList
        indexList[i], indexList[min] = indexList[min], indexList[i]
        tempList[i], tempList[min] = tempList[min], tempList[i]
    return indexList


# Takes the data line by line from a text file and inserts it into
#  6 respective lists & return the lists
def getData():
    # change the headings to look cleaner
    titleList, genreList, runtimeList, \
    ratingList, studioList, yearList = ["TITLE"], ["GENRE"], ["RUNTIME"], \
                                        ["RATING"], ["STUDIO"], ["YEAR"]
    # check if the file is valid
    infile = checkFile()
    # skip the first line because we already "changed" it
    line = infile.readline()
    line = infile.readline()
    line = line.strip()
    while (line != ""):
        title, genre, runtime, rating, studio, year = line.split(",")
        titleList.append(title)
        genreList.append(genre)
        runtimeList.append(runtime)
        ratingList.append(rating)
        studioList.append(studio)
        yearList.append((year))
        line = infile.readline()
        line = line.strip()
    infile.close()
    return titleList, genreList, runtimeList, ratingList, studioList, yearList
#------------------------------------------


# Start of the functions to get data when a choice is picked

# Searches the genre List for all films with that specific genre and prints all the
#  information for movie genre
def getGenre(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    # check that the genre actually exists in the list
    genre = checkInput("Genre", genreList)
    print("\nThe films that meet your criteria are: \n")
    # format the output correctly to look clean
    print("%-45s" "%10s" "%15s" "%15s" "%30s" "%10s" % (titleList[0], genreList[0],
            runtimeList[0], ratingList[0], studioList[0], yearList[0]))
    for i in range(0, len(titleList)):
        if(genre == genreList[i]):
            print("%-45s" "%10s" "%15s" "%15s" "%30s" "%10s" % (titleList[i], genreList[i],
                    runtimeList[i], ratingList[i], studioList[i], yearList[i]))


# Searches the rating List for all films with that specific rating and prints all the
#  information for movie rating
def getRating(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    # checks if the rating is a valid input
    rating = checkInput("Rating", ratingList)
    print("\nThe films that meet your criteria are: \n")
    print("%-45s" "%15s" "%15s" "%15s" "%30s" "%10s" % (titleList[0], genreList[0],
            runtimeList[0], ratingList[0], studioList[0], yearList[0]))
    for i in range(0, len(titleList)):
        if(rating == ratingList[i]):
            print("%-45s" "%15s" "%15s" "%15s" "%30s" "%10s" % (titleList[i], genreList[i],
                    runtimeList[i], ratingList[i], studioList[i], yearList[i]))


# Find the film with the longest runtime by keeping track of the maximum
#  value while traversing the list
def getLongest(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    # checks if the studio actually exists in the list
    studio = checkInput("Studio", studioList)
    max = 0
    for i in range(1, len(runtimeList)):
        time = int(runtimeList[i])
        if(time > max and studioList[i] == studio):
            # override max once a new higher number is found
            max = int(runtimeList[i])
            # keep track of the index where max is
            index = i
    print("\nThe films that match your criteria are: \n")
    print("%-45s" "%15s" "%15s" "%15s" "%30s" "%10s" % (titleList[0], genreList[0],
            runtimeList[0], ratingList[0], studioList[0], yearList[0]))
    print("%-45s" "%15s" "%15s" "%15s" "%30s" "%10s" % (titleList[index], genreList[index],
            runtimeList[index], ratingList[index], studioList[index], yearList[index]))


# Searches the title list with Binary Search and print out its information
def getTitle(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    title = checkInput("Title", titleList)
    # call binary search to return the index where the title lies
    index = binarySearch(titleList, title)
    print("\nThe films that match your criteria are: \n") 
    print("%-45s" "%15s" "%15s" 
          "%15s" "%30s" "%10s" % (titleList[0], genreList[0],
                                runtimeList[0], ratingList[0], studioList[0], yearList[0]))
    print("%-45s" "%15s" "%15s" 
          "%15s" "%30s" "%10s" % (titleList[index], genreList[index],
                                runtimeList[index], ratingList[index], studioList[index],
                                yearList[index]))


# Accumulates the runtime of all films between two years then divides it by
#  the number of films to get the average runtime
def averageRuntime(runtimeList, yearList):
    count = 0
    # check if the years are valid
    year1, year2 = checkYear()
    total = 0
    for i in range(1, len(runtimeList)):
        if(year1 <= int(yearList[i]) <= year2):
            # count is needed to get the average since it is a counter
            count += 1
            # accumulate the runtimes
            total += int(runtimeList[i])
    print("The average runtime for films between " + str(year1) + " and "
          + str(year2) + " is " + str(total/count))


# Sorts all the lists according to the runtime and writes all the data to a new text file
#  in the same format as the original
def writeTo(titleList, genreList, runtimeList, ratingList, studioList, yearList):
    # sort only the runtime list
    indexList = selectionSort(runtimeList)
    # get rid of the headers to allow indexes to be correct (we don't need it)
    fname = input("\nEnter name of output file: ")
    outFile = open(fname, 'w')
    for i in indexList:
        # write data in the same format as the original
        outFile.write(titleList[i] + "," + genreList[i] + "," +
                      runtimeList[i] + "," + studioList[i] + "," + yearList[i] +"\n")
    outFile.close()
    print("Finished writing to file")
#------------------------------------------


# Finds the string that occurs the most in the studioList
#  using the module Counter from collections
def mostFilms(studioList):
    count = Counter(studioList)
    winnerName, numFilms = count.most_common()[0]
    print(winnerName + " has the most movies at " + str(numFilms) + " films")

#------------------------------------------


def getChoices():
    keepGoing = True
    titleList, genreList, runtimeList, ratingList, studioList, yearList = getData()
    while(keepGoing):
        print("\nPlease choose one of the following options:")
        print("1 -- Find all films of a certain genre")
        print("2 -- Find all films with a certain rating")
        print("3 -- Find the longest film made by a specific studio")
        print("4 -- Search for a film by title")
        print("5 -- Find the average runtime of films made in a given year range")
        print("6 -- Sort all lists by runtime & write the results to a new file")
        print("7 -- Quit")
        print("8 -- *Bonus* See which studio produced the most films!")
        choice = checkChoice()
        # runs the function that corresponds with the choice
        if(choice == 1):
            getGenre(titleList, genreList, runtimeList, ratingList, studioList, yearList)
        elif (choice == 2):
            getRating(titleList, genreList, runtimeList, ratingList, studioList, yearList)
        elif(choice == 3):
            getLongest(titleList, genreList, runtimeList, ratingList, studioList, yearList)
        elif(choice == 4):
            getTitle(titleList, genreList, runtimeList, ratingList, studioList, yearList)
        elif(choice == 5):
            averageRuntime(runtimeList, yearList)
        elif(choice == 6):
            writeTo(titleList, genreList, runtimeList, ratingList, studioList, yearList)
        elif(choice == 7):
            print("Goodbye")
            keepGoing = False
        else:
            mostFilms(studioList)

# Presents the User with a list of options to pick what they want to see
def main():
    getChoices()
#------------------------------------------
# end of Le_G_movies.py

main()