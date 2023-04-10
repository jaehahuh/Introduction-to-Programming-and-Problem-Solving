import csv

def cvs_to_dictionary():
    d = {}
    d['stop_id'] = []
    d['stop_code'] = []
    d['stop_name'] = []
    d['stop_desc'] = []
    d['stop_lat'] = []    
    d['stop_lon'] = []
    d['zone_id'] = []
    d['stop_url'] = []
    d['location_type'] = []
    d['parent_station'] = []

    reader = csv.DictReader(open('hw8 - mta train stop data.csv', 'r'))
    fieldnames = ['stop_id', 'stop_code', 'stop_name','stop_desc','stop_lat','stop_lon','zone_id','stop_url','location_type','parent_station']
    Index = 0
    for row in reader:
        if(Index!=0):
            for key in row:
                d[key].append(row[key])
        Index = Index + 1

    return d



def dictionary_to_useful_dictionary(d):
    dictionary = {}
    lastStringAdded = ""
    num = len(d['stop_id'])
    train_num = d['stop_id']
    station = d['stop_name']

    for n in range(0,num):
        trainLine = train_num[n][0]
        if trainLine in dictionary:
            if(lastStringAdded != station[n]):
                dictionary[trainLine] = dictionary[trainLine] + ", " + station[n]
                lastStringAdded = station[n]
        else:
            dictionary[trainLine] = station[n]
            lastStringAdded = station[n]

    return dictionary


def main():
    d = cvs_to_dictionary()
    dictionary = dictionary_to_useful_dictionary(d)
    train_line = input("Please enter a train line, or 'done' to stop: ")
    while (train_line != 'done'):
        if train_line in dictionary:
            print(train_line ,"line: ", dictionary[train_line], '\n')
        else:
            print("This is not a valid train line \n")
        train_line = input("Please enter a train line, or 'done' to stop: ")



main()

