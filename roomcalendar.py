#class for setting the room calendar for specific number of days
from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import timedelta

class RoomCalendar:
    def __init__(self, nd):
        # Initialize the RoomCalendar object with a specified number of days
        if nd > 0:
            self.num_days = int(nd)
        else:
            print('The calendar needs to be more than just one day ahead of schedule! Default is one day')
            self.num_days = 1
            
        # Initialize the booking_days list with date and 'none' status
        self.booking_days = []
        # Get today's date (string)
        start_date = date.today()
        self.booking_date = start_date.strftime('%Y-%m-%d')

        # Calculate the final date based on the specified number of days
        end_date = start_date + relativedelta(days=self.num_days)
        self.final_date = end_date.strftime('%Y-%m-%d')
        
        # Populate booking_days with date and 'none' status for each day in the range
        delta = end_date - start_date
        for i in range(delta.days + 1):
            day = start_date + timedelta(days=i)
            x = list((day, 'none'))
            self.booking_days.append(x)

    def return_all_booking_days(self):
        # Return the list of all booking days
        return self.booking_days 
    
    def return_available_dates(self):
        # Return the booking start date and final date
        return self.booking_date, self.final_date
