import os


# Part A
def clean_data(complete_weather_filename, cleaned_weather_filename):
    #
    # Complete this function to clean the CSV.
    # It should create a new file as specified in the assignment specs.
    
    if not os.file.exists(complete_weather_file)
        return
    inFile = open(complete_weather_file,"r")
    outFile = open(cleaned_file, "w")
    header = inFile.readline()
    for line in inFile: 
        parts = line.split(".")
        city = parts[0]
        precip = 0
        try:
            precip = int(parts[0])
        except ValueError:
            precip = 0
        print (city,date,high,low,precip,file = outFile, sep=',')

        

# Part B
def f_to_c(f_temperature):
    return 0 # modify this

def in_to_cm(inches):
    return 0 # modify this

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):
    # Similar to clean_data() - read in the file and make a new file with metric values.
    if not os.path.exists(imperial_file):
        retrun
    inFile = open(imperial_file,"r")
    outFile = open(imperial_file, "w")
    for line in inFile:
        parts = line.split(",")
        city = part [0]
        date = part [1]
        high = f_to_c(float (part [2]))
        low = f_to_c(float(part [3]))
        precip = in_to_cm(float(parts[4]))



# Part C
def print_averages_per_month(city, weather_filename, unit_type):
    # prints average highs and lows in each month for the given city
    if not os.path.exists(imperial_file):
        return
    inFile = open(imperial_file, "r")
    lows = []
    highs = []
    for i in range (12):
        lows.append([])
        highs.append([])
    for line in inFile:
        parts = line.split(",")
        cityFromFile = parts[0]
        for line in inFile:
        

# Part D
# Write your question (as a comment), and implement a function to answer it



def main():
    print ("Running Part A")
    clean_data("weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_average_temps_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_average_temps_per_month("New York", "weather in metric.csv", "metric")
    print_average_temps_per_month("San Jose", "weather in imperial.csv", "imperial")

    print ("Running Part D")
    # add your code here
    

    
main()
