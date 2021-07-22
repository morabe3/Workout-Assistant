import math
from math import sqrt

import numpy as np
import csv
import os
import statistics
from docutils.utils.math.math2html import file
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
from scipy.spatial import distance
import websocket
try:
    import thread
except ImportError:
    import _thread as thread
import time
import json
import pandas as pd
import pymysql
import pymysql.cursors
from matplotlib import pyplot



connection = pymysql.connect(host='localhost',user='root',password='',db='workout',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)




workout_training1 =[]


result1 = ""

shortest_distance1 =""

workout_testing1 =[]

workoutlist1 = []
workoutlist2 = []

workoutlisttrain1 = []
workoutlisttrain2 = []


counteradat=0

counterFive = 0
counterTen = 0


filename = "TestingFile.csv"

rows = []

# convert csv to dataframe using pandas
dataDF = pd.read_csv(filename, header=1, index_col=0)

# apply rolling algorithm and get the mean of the result
rollingMean = dataDF.rolling(window=3).mean()

# dataDF.plot()
# rollingMean.plot(color='red')
# pyplot.show()
#
# dataDF.to_csv("file before rolling .csv")

# get the values after rolling to a numpy array
rows1 = rollingMean.values

pd.DataFrame(rows1).to_csv("file after rolling.csv")


flag=False
flagU=False
Range=0
counter=0
countertest=""
IsBadData = True
rows2 =[]

# print(type(rows1))
# print(len(rows1[5]))

for i in range (len(rows1)):
    if i > 1:
        if (float(rows1 [i][1])<0.01) and IsBadData ==True  :

            continue

        else:
            IsBadData = False

            rows2.append(rows1[i])










cut=0
Acounter=0
distancePlus=0
distanceMinus=0

right=0
wrong=0
array=[]
velocityArr = []

ten = 0
five = 0
distance2 = 0
min = 10000
minpath = ''
fivemin = 0
tenmin = 0
weightresult = ''
framesFive = []
framesTen = []



for row in rows2[0: rows2.__len__() - 1]:

    a = [float(rows2[0][1])]
    b = [float(rows2[counter + 1][1]) ]


    counter += 1

    if (not flag):
        distancePlus = a
        flag = True

    if (distancePlus < b):
        distancePlus=b
        if(not flagU):
            cut+=1
            flagU = True





        for col in row:
            workoutlist2.append(float(col))
            # print(workoutlist2)
        workout_testing1.append((workoutlist2))
        workoutlist2=[]

    elif(distancePlus>b):
        distancePlus=b
        if(flagU):
            cut+=1
            flagU=False


        for col in row:
            workoutlist2.append(float(col))
        workout_testing1.append((workoutlist2))
        workoutlist2 = []


    if (cut !=0 and cut %3 == 0 ):
        cut+=1
        flagU = False
        counteradat+=1
        workout_trainingNP1=[]


        listq2 = []

        for y in range(0, workout_testing1.__len__() - 1):

            # listq2.append(statistics.mean(workout_testing1[y]))


             listq2.append(workout_testing1[y])

        workout_testing1 = []

        result1= ""
        for i in range(188) :

            workout_training1 = []

            workoutlisttrain1 = []

            flag2=False
            flagU2=False
            flagD2=False
            Range2=0
            pathh = ""
            counter2=0

            rows = []
            if i < 92:
                if i < 45:
                    pathh = "Right/Right Five (" + str(i + 1) + ").csv"

                else:
                    pathh = "Right/Right Ten (" + str(i + 1) + ").csv"

            else:
                # pathh = "Wrong_movement/Wrong_range_put_your_shoulder_and_elbow_in_ninety_degree (" + str((i - 92) + 1) + ").csv"
                if i < 137:
                    pathh = "Wrong/Wrong Five (" + str((i - 92) + 1) + ").csv"

                else:
                    pathh = "Wrong/Wrong Ten (" + str((i - 92) + 1) + ").csv"

            TrainingDataDF = pd.read_csv(pathh, header=1, index_col=0)

            TrainingRollingMean = TrainingDataDF.rolling(window=3).mean()

            rows = TrainingRollingMean.values

            # with open(pathh, 'r') as csvfile:
            #
            #
            #     csvreader2 = csv.reader(csvfile)
            #
            #
            #     for row in csvreader2:
            #         rows.append(row)

            IsBadData2 = True
            rows3 = []
            for i in range(len(rows)):
                if i > 1:

                    if (float(rows[i][1]) < 0.01) and IsBadData2 == True :



                        continue

                    else:
                        IsBadData2 = False

                        rows3.append(rows[i])

            cut2=0

            for row in rows3[0:rows3.__len__()-1]: #-4

                a2 = float(rows3[0][1])

                b2 = float(rows3[counter2 + 1][1])

                counter2 += 1
                if (not flag2):
                    Range2 = a2
                    flag2 = True

                if (Range2 < b2):
                    Range2=b2
                    if(not flagU2):
                        cut2+=1
                    flagU2 = True


                    for col in row:
                        workoutlisttrain1.append(float((col)))
                    workout_training1.append(workoutlisttrain1)
                    workoutlisttrain1=[]


                elif(Range2>b2):
                    if (flagU2):
                        cut2 += 1
                        flagU2 = False
                    for col in row:
                        workoutlisttrain1.append(float((col)))
                    workout_training1.append(workoutlisttrain1)
                    workoutlisttrain1=[]

                if (cut2 !=0 and cut2%3==0 ):
                    cut2+=1

                    flagU2 = False

                    # q1 = int((workout_training1.__len__()/3))

                    listq1 =[]


                    for x in range(0,workout_training1.__len__()-1):
                        # listq1.append(statistics.mean(workout_training1[x]))
                         listq1.append(workout_training1[x])



                    workout_trainingNP1 = np.array(listq1)
                    workout_testingNP1 = np.array( listq2)

                    testingFrames = workout_testingNP1.__len__()
                    trainingFrames = workout_trainingNP1.__len__()

                    sum = 0

                    for x in range (testingFrames - 1):
                        y1 = workout_testingNP1[x][0]
                        y2 = workout_testingNP1[x+1][0]
                        dist = abs(y2 - y1)
                        velocity = dist / 0.033333
                        sum = sum + velocity

                    repVelocity = sum / testingFrames
                    repVelocity = round(repVelocity, 2)



                    distance1, path = fastdtw(workout_testingNP1, workout_trainingNP1, dist=euclidean)

                    distance2 = testingFrames - trainingFrames
                    distance3 = abs(distance2)

                    if (distance3 == 0):  # if there's a match
                        if (pathh.find('Five') != -1):
                            five = five + 1
                        elif (pathh.find('Ten') != -1):
                            ten = ten + 1

                    elif (distance3 > 0):
                        if (min > distance3):
                            min = distance3
                            if (pathh.find('Five') != -1):
                                minpath = '5 Kg'
                            elif (pathh.find('Ten') != -1):
                                minpath = '10 Kg'

                    if (five | ten > 0):
                        if (five > ten):
                            weightresult = '5 Kg'
                        elif (ten > five):
                            weightresult = '10 Kg'
                        elif (five == ten):
                            weightresult = minpath
                    elif (five & ten == 0):
                        weightresult = minpath




                    workout_training1 =[]
                    workoutlisttrain1 =[]



                    if (result1 == "" ):
                        result1 = distance1
                        shortest_distance1 = pathh
                    elif (result1 > distance1):
                        result1 = distance1
                        shortest_distance1 = pathh


        #print(workout_testingNP1)
        if counteradat > 6:
            break
        workoutlist2 = []
        workout_training1 = []
        adat ="\nThe " + str(counteradat) + " Movement is :"
        print(adat)
        print(shortest_distance1)
        print ("Velocity =  " + str(repVelocity) + " m/sec")
        print(weightresult)
        #print (five)
        #print (ten)
        if (weightresult.find('10') != -1):
            counterTen = counterTen + 1
        else:
            counterFive = counterFive + 1

        framesFive.append(five)
        framesTen.append(ten)
        five = 0
        ten = 0
        minpath = ''
        min = 10000

        #print(result1)

        if (shortest_distance1[0] == 'W'):
            wrong = wrong + 1
            array.append('Wrong')
        else:
            right = right + 1
            array.append('Right')


        velocityArr.append(repVelocity)


    strDB = ''
    velDB = ''

    strDB = ' '.join(map(str, array))
    velDB = ' '.join(map(str, velocityArr))

    #print(strDB)

    totalFrames5 = np.sum(framesFive)
    totalFrames10 = np.sum(framesTen)

sumVel = np.sum(velocityArr)
avgVel = float(sumVel) / float(velocityArr.__len__())
avgVel = round(avgVel, 2)
        # print(result1)

if(result1==""):
    print("please record again")



detectedWeight = 0

if (counterFive > counterTen):
    detectedWeight = 5
    print( "you are playing with 5 kilograms")
elif(counterFive < counterTen):
    detectedWeight = 10
    print ("you are playing with 10 kilograms")
else :
    if(totalFrames5 > totalFrames10):
        detectedWeight = 5
    elif(totalFrames10 > totalFrames5):
        detectedWeight = 10
    print("you are playing with " + str(detectedWeight) + " kilograms")


#os.remove("TestingFile.csv")
print(str(right)+" right Movements")
print(str(wrong)+" wrong Movements")

dev1=right+wrong

right1=right/dev1
wrong1=wrong/dev1


if (right>wrong):
    percentage=right1*100
    shortest_distance=1
else:
    percentage=wrong1*100
    shortest_distance=2



try:
    with connection.cursor() as cursor:
        # Create a new record

        movementID = "SELECT id FROM `usermovement` ORDER BY id DESC LIMIT 1 "
        cursor.execute(movementID)
        res = cursor.fetchone()
        print('ID:' + str(res)+str(percentage))

        sql = "INSERT INTO `movementresult` (`usermovementID`, `resultID`,`ResultPercentage`,`repInfo`,`repNo`,`rightNo`,`wrongNo`,`DumbbellWeight`,`velocityInfo`,`avgVelocity`) VALUES (%s,%s,%s,%s, %s, %s, %s, %s,%s,%s)"

        cursor.execute(sql, (res['id'], shortest_distance,percentage,strDB,dev1,right,wrong, detectedWeight, velDB, avgVel))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

finally:
    connection.close()








os.system('PAUSE')




















