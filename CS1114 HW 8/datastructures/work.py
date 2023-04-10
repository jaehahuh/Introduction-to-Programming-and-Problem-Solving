import os
import csv





def CSVToDictionary():
    # decalre an empty dictionary
    d = {}
    # The first column has key (or attribute or column name) = 'stop_id'
    d['stop_id'] = []
    # The second column has key (or attribute or column name) = 'stop_code'
    d['stop_code'] = []
    # The third column has key (or attribute or column name) = 'stop_name'
    d['stop_name'] = []
    # The fourth column has key (or attribute or column name) = 'stop_desc'
    d['stop_desc'] = []
    # The fifth column has key (or attribute or column name) = 'stop_lat'
    d['stop_lat'] = []
    # The sixth column has key (or attribute or column name) = 'stop_lon'
    d['stop_lon'] = []
    # The seventh column has key (or attribute or column name) = 'zone_id'
    d['zone_id'] = []
    # The eighth column has key (or attribute or column name) = 'stop_url'
    d['stop_url'] = []
    # The ninth column has key (or attribute or column name) = 'location_type'
    d['location_type'] = []
    # The tenth column has key (or attribute or column name) = 'parent_station'
    d['parent_station'] = []


    # now open the data.csv file taking into account all column names and that each column is seperated by a comma
    # because this is how CSV files are structured, each column is seperated by a comma
    dictReader = csv.DictReader(open('data.csv'), fieldnames = ['stop_id', 'stop_code', 'stop_name','stop_desc','stop_lat','stop_lon','zone_id','stop_url','location_type','parent_station'], delimiter = ',', quotechar = '"')
    # initialise rowIndex to 0. This variable will keep track of the row index
    rowIndex = 0
    # loop into each row in the csv file
    for row in dictReader:
        # we do not want the first row because it contains the key names, which we do not care about and do not carry any
        # information
        if(rowIndex!=0):
            # append each entry to its corresponding key
            for key in row:
                 d[key].append(row[key])
        # increment the rowIndex because we are about to go to another row
        rowIndex = rowIndex + 1
    # output the computed dictionary
    return d
def DictionaryToUsefulDictionary(d):
    # decalre an empty dictionary
    dictionary = {}
    # declare an empty string
    lastStringAdded = ''
    # compute the number of rows in the csv file
    N = len(d['stop_id'])
    # we care above the first column in the csv file which is saved in the list col1
    col1 = d['stop_id']
    # we care above the third column in the csv file which is saved in the list col3
    col3 = d['stop_name']
    # loop over all rows in the csv file
    for n in range(0,N):
        # extract the trainLine which is the first character in the first entry of each row, i.e. the first character of
        # each entry in col1
        trainLine = col1[n][0]
        # if trainLine is already found in the dictionary
        if trainLine in dictionary:
            # if the lastStringAdded is equal to the current col3 value, then we do not add it because we do not need
            # to duplicate our data structure
            if(lastStringAdded != col3[n]):
                dictionary[trainLine] = dictionary[trainLine] + ", " + col3[n]
                lastStringAdded = col3[n]
        # if trainLine is not found in the dictionary
        else:
            # we create a ney trainLine key and insert the stop_name in col3 as a value to this key
            dictionary[trainLine] = col3[n]
            # insert the value of col3[n] as the lastStringAdded
            lastStringAdded = col3[n]

    # output the computed dictionary
    return dictionary
def main():
    # run the CSVtoDictionary() function we wrote above to extract all the CSV file as a dictionary
    d = CSVToDictionary()
    # now we run the DictionaryToUsefulDictionary(d) function above that converts the dictionary
    # extracted from CSVtoDictionary() function to a useful dictionary that we entry as key the train_line
    # and returns the stop in the format we want
    dictionary = DictionaryToUsefulDictionary(d)
    # prompt the user with the message "Please enter a train line, or 'done' to stop: " and read from user train_line
    train_line = input("Please enter a train line, or 'done' to stop: ")
    # only stop when train_line is equal to "done"
    while (train_line != 'done'):
        # if the train_line that is inputed by the user is found in one of the keys in the dictionary,
        # then we print the dictionary stop_name, else we print the message "This is not a valid train line"
        if train_line in dictionary:
            print(train_line,"line: ", dictionary[train_line])
        else:
            print("This is not a valid train line")
        # prompt the user with the message "Please enter a train line, or 'done' to stop: " and read from user train_line
        train_line = input("Please enter a train line, or 'done' to stop: ")










# run the main() function
main()
