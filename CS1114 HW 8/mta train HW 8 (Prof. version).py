import os

def printStations (stations, line):
    print (line, "line" , end = ' ')
    for station in stations[line]:
        print (station + ", " ,end = '')
    print()



def main():
    stations = { }
    inFile = open ("hw8 - mta train stop data.csv" , "r")
    for fileLine in inFile:
        parts = fileLine.split(",")
        stopid = parts[0]
        line = stopid[0]
        station = parts[2]
        if line not in station:
            station[line] = []
        if not station in station[line]:
            station[line].append(station)

    train_line = input("Please enter a train line, or 'done' to stop: ")
    
    


main()
