import random

# constant values

'''
dummy CAN FRAME SPECIFICATION
2 bits - MODULE
3 bits - Function
6 bits - value 

|----|-------|-------------|
|2   | 3     | 6           |
|1 1 | 1 1 1 | 1 1 1 1 1 1 |
|Mod | Funct.| Value       |
|----|-------|-------------|
'''
'''
01 ENGINE
*Functionality:
010 - speed
020 - gear indicator
*Value 
according to selected functionality

46 COMFORT
010 - Windows
100 - Mirrors

03 ABS (module)
001 ABS
010 ESP
100 TC

08 HVAC
001 - Temp
010 - Fan speed
100 - Zone

16 STEERING
001 - Rotation (degree)
010 - Mode (Race, Comfort, Auto)

37 NAVIGATION
001 - Height above see level
010 - Latitude
020 - Longitude
100 - number of satelites

56 RADIO
010 - Band (AM/FM)
050 - Current Frequency
100 - RDS

35 CENTRAL LOCK
001 - door lock status
'''

# Module listing with IDs
modulesList = {
    'ENGINE': '01',
    'COMFORT': '46',
    'ABS': '03',
    'HVAC': '08',
    'STEERING_WHEEL': '16',
    'NAVIGATION': '37',
    'RADIO': '56',
    'CENTRAL_LOCK': '35'
}

SPEED = 50
LONGITUDE = 14.552
LATITUDE = 53.428
HEIGHT = 25
ITER = 0


def engine():
    global SPEED

    st = "01"
    listOfFunctions = ['010']

    functionChoise = random.choice(listOfFunctions)
    st += functionChoise

    SPEED += random.randint(-4, 10)

    st += '0000' + str(SPEED)
    return st


def comfort():
    st = "46"

    st += '010'
    st += '000001'

    return st


def abs():
    st = "03"
    st += "001"
    st += "000000"

    return st


def hvac():
    st = "08"
    st += "001"
    st += '000017'

    return st


def steeringWheel():
    st = "16"
    st += '010'
    st += '000002'

    return st


def navi():
    global HEIGHT
    st = "37"
    st += "001"
    st += '0000' + str(HEIGHT)

    return st


def radio():
    st = "56"
    st += "010"
    st += "000001"

    return st


def centralLock():
    st = "35"
    st += '001'
    st += '000001'

    return st


functionList = [engine, comfort, abs, hvac, steeringWheel, navi, radio, centralLock]


def readCANNetwork():
    global ITER
    res = functionList[ITER]()

    if ITER < len(functionList) - 1:
        ITER += 1
    else:
        ITER = 0

    return res
