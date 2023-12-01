# class for managing the Room of hotel
# Importing required modules
from roomcalendar import RoomCalendar
from room_status import room_status
from operator import attrgetter
from dateutil.relativedelta import relativedelta


class Room:
    # Class variable to track room reservation status
    reserve_status = {}
    reserve_status['1'] = room_status.AVAILABLE
    reserve_status['2'] = room_status.BOOKED
 
    def __init__(self, room_number, room_type, room_price, nd):
        # Initialize Room object with room details and calendar

        self.room_number = room_number
        self.room_type = room_type
        self.room_calendar = RoomCalendar(nd)
        self.room_status = Room.reserve_status['1']
        self.is_booked = False
        self.is_rflag = False
        self.check_start = None
        self.check_end = None
        # Set room price based on room type 'S' for standard , 'D' for deluxe and 'E' for executive
        
        if self.room_type == 'S':
            self.room_price = 150
        elif self.room_type == 'D':
            self.room_price = 250
        elif self.room_type == 'E':
            self.room_price = 350
            
    def return_room_calendar(self):
        # Return the complete room calendar
        return self.room_calendar.return_all_booking_dates()

    def return_room_calendar(self):
        # Return the complete room calendar
        return self.room_calendar.return_all_booking_dates()

    def return_room_calendar_dates(self):
        # Return the available dates in the room calendar
        return self.room_calendar.return_available_dates()

    def return_room_price(self):
        # Return the room price
        return self.room_price
   
    def book_customer(self, cust_id):
        # Book a customer for the specified reservation dates
        for i in range(self.check_start, self.check_end):
            self.room_calendar.return_all_booking_days()[i][1]=cust_id

    def check_reservation_dates(self, checked_in_date, checked_out_date):
       # Check if the room is available for the specified reservation dates
        self.is_rflag = False
        self.check_start = None
        self.check_end = None

        dates_only = [date[0] for date in self.room_calendar.return_all_booking_days()]
        # Find the indices for the check-in and check-out dates
        
        for i in range (len(dates_only)):
            if dates_only[i] == checked_in_date:
                self.check_start = i
            elif dates_only[i] == checked_out_date:
                self.check_end = i
        # Check if the room is available for the specified dates

        if (self.check_start and self.check_end)!=None:
            id_only = [days[1] for days in self.room_calendar.return_all_booking_days()[self.check_start:self.check_end]]
            result = all(elem == 'none' for elem in id_only)
            if result:
                self.room_status = Room.reserve_status['1'] 
                self.is_rflag = True
            else:
                self.room_status = Room.reserve_status['2']
                self.is_rflag = False
        else:
            print('Dates out of range or invalid values')
            self.is_rflag = False
        return self.is_rflag, self.room_status
    
    def cancel_booking_by_custid(self, cust_id):
        # Cancel a booking based on customer ID
        for i in range(0, len(self.room_calendar.return_all_booking_days())):
            if self.room_calendar.return_all_booking_days()[i][1] == cust_id:
                self.room_calendar.return_all_booking_days()[i][1] = 'none'
                
    def __str__(self):
        return f"{self.room_type}  ${self.room_price}"
