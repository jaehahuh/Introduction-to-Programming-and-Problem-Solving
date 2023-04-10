import csv

data = []
def clean_data(complete_weather_filename, cleaned_weather_filename):
    old_file = open(complete_weather_filename,'r')
    new_file = open(cleaned_weather_filename,'w')

    reader = csv.DictReader(old_file)
    fieldnames = ['City', 'Date', 'Low', 'High', 'Precipitation']
    writer = csv.DictWriter(new_file, fieldnames = fieldnames)
    writer.writeheader()

    for row in reader:
        if row['Precipitation'] == "T":
            writer.writerow({'City': row['City'], 'Date': row['Date'], 'Low': row['Low'], 'High': row['High'],'Precipitation': 0})
        else:
            writer.writerow({'City': row['City'], 'Date': row['Date'], 'Low': row['Low'], 'High': row['High'],'Precipitation': row['Precipitation']})
    
    new_file.close()
    old_file.close()



def f_to_c(f_temperature):
    celsius = (float(f_temperature) - 32) * 5/9
    return celsius 

def in_to_cm(inches):
    cms = float(inches) * 2.54
    return cms 

def convert_data_to_metric(imperial_weather_filename, metric_weather_filename):

    clean_file = open(imperial_weather_filename,'r')
    metric_file = open(metric_weather_filename,'w')
    reader = csv.DictReader(clean_file)
    fieldnames = ['City', 'Date', 'Low', 'High', 'Precipitation']
    writer = csv.DictWriter(metric_file, fieldnames = fieldnames)
    writer.writeheader()
    
    for row in reader:
        celsius_low = f_to_c(row['Low'])
        celsius_high = f_to_c(row['High'])
        centimeters = in_to_cm(row['Precipitation'])

        writer.writerow({'City': row['City'], 'Date': row['Date'], 'Low': celsius_low, 'High': celsius_high,'Precipitation': centimeters})
        
    metric_file.close()
    clean_file.close()   
    
    

def print_averages_per_month(city, weather_filename, unit_type):
    
    month_temp = {}
    each_month = {}
    month_temp_h = {}
    each_month_h = {}
    avgfile = open(weather_filename,'r')
    reader = csv.DictReader(avgfile)
    for row in reader:
        if city == row['City']:
            month = row['Date'].split('/')
            if '-' in row['Date']:
                cornercase = month[0].split('-')
                if int (cornercase[0]) in month_temp:
                    val = month_temp [int(cornercase[0])]
                    updated_val = float(row['Low']) + float(val)
                    month_temp [int(cornercase[0])] = updated_val
                    count = each_month [int(cornercase[0])] + 1
                    each_month [int(cornercase[0])] = count
                else:
                    month_temp [int(cornercase[0])] = float(row['Low'])
                    each_month [int(cornercase[0])] = 1
                    
                    
            else:
                if int(month[0]) in month_temp:
                    val = month_temp [int(month[0])]
                    updated_val = float(row['Low']) + float(val)
                    month_temp [int(month[0])] = updated_val
                    count = each_month [int(month[0])] + 1
                    each_month [int(month[0])] = count
                else:
                    month_temp [int(month[0])] = float(row['Low'])
                    each_month [int(month[0])] = 1


    avgfile.close()
    avgfile = open(weather_filename,'r')
    reader = csv.DictReader(avgfile)
    for row in reader:
        if city == row['City']:
            month = row['Date'].split('/')
            if '-' in row['Date']:
                cornercase = month[0].split('-')
                if int(cornercase[0]) in month_temp_h:
                    val = month_temp_h [int(cornercase[0])]
                    updated_val = float(row['High']) + float(val)
                    month_temp_h [int(cornercase[0])] = updated_val
                    count = each_month_h [int(cornercase[0])] + 1
                    each_month_h [int(cornercase[0])] = count
                else:
                    month_temp_h [int(cornercase[0])] = float(row['High'])
                    each_month_h [int(cornercase[0])] = 1
            else:
                if int(month[0]) in month_temp_h:
                    val = month_temp_h [int(month[0])]
                    updated_val = float(row['High']) + float(val)
                    month_temp_h [int(month[0])] = updated_val
                    count = each_month_h [int(month[0])] + 1
                    each_month_h [int(month[0])] = count
                else:
                    month_temp_h [int(month[0])] = float(row['High'])
                    each_month_h [int(month[0])] = 1
                    

    
    print ("Average Temperatures for " + city)
   
    print ("January : " + str(int(month_temp_h[1]/each_month_h[1])) + " High , " + str(int(month_temp[1]/each_month[1])) + " Low")
    print ("February : " + str(int(month_temp_h[2]/each_month_h[2])) + " High , " + str(int(month_temp[2]/each_month[2])) + " Low")
    print ("March : " + str(int(month_temp_h[3]/each_month_h[3])) + " High , " + str(int(month_temp[3]/each_month[3])) + " Low")
    print ("April : " + str(int(month_temp_h[4]/each_month_h[4])) + " High , " + str(int(month_temp[4]/each_month[4])) + " Low")
    print ("May : " + str(int(month_temp_h[5]/each_month_h[5])) + " High , " + str(int(month_temp[5]/each_month[5])) + " Low")
    print ("June : " + str(int(month_temp_h[6]/each_month_h[6])) + " High , " + str(int(month_temp[6]/each_month[6])) + " Low")
    print ("July : " + str(int(month_temp_h[7]/each_month_h[7])) + " High , " + str(int(month_temp[7]/each_month[7])) + " Low")
    print ("August : " + str(int(month_temp_h[8]/each_month_h[8])) + " High , " + str(int(month_temp[8]/each_month[8])) + " Low")
    print ("September : " + str(int(month_temp_h[9]/each_month_h[9])) + " High , " + str(int(month_temp[9]/each_month[9])) + " Low")
    print ("October : " + str(int(month_temp_h[10]/each_month_h[10])) + " High , " + str(int(month_temp[10]/each_month[10])) + " Low")
    print ("November : " + str(int(month_temp_h[11]/each_month_h[11])) + " High , " + str(int(month_temp[11]/each_month[11])) + " Low")
    print ("December : " + str(int(month_temp_h[12]/each_month_h[12])) + " High , " + str(int(month_temp[12]/each_month[12])) + " Low")
        
    avgfile.close()
        
        


def higher_rainfall(city1, city2, weatherfilename):
    avg_rain_file = open(weatherfilename,'r')
    reader = csv.DictReader(avg_rain_file)
    prep_count_city1 = 0
    prep_count_city2 = 0
    prep_sum_city1 = 0
    prep_sum_city2 = 0
    for row in reader:
        if city1 == row['City']:
            prep_count_city1 = prep_count_city1 + 1
            prep_sum_city1 = prep_sum_city1 + float(row['Precipitation'])

        if city2 == row['City']:
            prep_count_city2 = prep_count_city2 + 1
            prep_sum_city2 = prep_sum_city2 + float(row['Precipitation'])


    prep_avg_city1 = prep_sum_city1/prep_count_city1
    prep_avg_city2 = prep_sum_city2/prep_count_city2
    
    if prep_avg_city1 > prep_avg_city2:
        print ("Average precipitation of " + city1 + " is greater")
    else:
        print ("Average precipitation of " + city2 + " is greater")
    
    



def main():
    print ("Running Part A")
    clean_data("hw7 - weather.csv", "weather in imperial.csv")
    
    print ("Running Part B")
    convert_data_to_metric("weather in imperial.csv", "weather in metric.csv")
    
    print ("Running Part C")
    print_averages_per_month("San Francisco", "weather in imperial.csv", "imperial")
    print_averages_per_month("New York", "weather in metric.csv", "metric")
    print_averages_per_month("San Jose", "weather in imperial.csv", "imperial")


    print ("Running Part D")
    print ("Which city has higher average rainfall?")
    higher_rainfall('New York', 'San Francisco', "weather in imperial.csv")
    

    
main()
