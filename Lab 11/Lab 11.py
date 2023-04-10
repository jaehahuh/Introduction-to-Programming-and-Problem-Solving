class Calender:
    def __init__(self):
        today_date = input("Please enter tdoay's date (mm/dd/yy): ")

        self.day = int(today_date[3:5])
        self.day = int(today_date[:2])
        self.year = int(today_date[6: ])

        self.day_of_week = int(input("Please enter the day of the week today (1 for Monday and 7 for Sunday): "))

        self.to_do_list = ToDoList():

    def set_next_day_of_week(self):
        self.day_of_week = (self.day_of
        
        
    def convert_int_to_day_of_week(self):
        if self.day_of_week == 1:
            return "Monday"
        elif self.day_off_week == 2:
            return "Tuesday"
        elif self.day_off_week == 3:
            return "Wednesday"
        elif self.day_off_week == 4:
            return "Thursday"
        elif self.day_off_week == 5:
            return "Friday"
        elif self.day_off_week == 6:
            return "Saturday"
        else:
            return "Sunday"




        
class ToDoList:
    def __init__(self):
