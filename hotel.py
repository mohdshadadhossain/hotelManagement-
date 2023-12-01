# class for managing the Hotel and creating rooms of different types and setting room calendar
#import required module
from room import Room

class Hotel:
    def __init__(self, n_std_rooms, n_dlx_rooms, n_exe_rooms ,nd):
        # Initialize Hotel object with specified number of rooms
        try:
            self.rooms_detail = {}
            self.rooms_detail['room_number'] = []
            self.rooms_detail['Room'] = []
            self.fully_booked = 0
            
            # Ensure the total number of rooms is greater than 0
            if int(n_std_rooms + n_dlx_rooms + n_exe_rooms) > 0:
                self.n_std_rooms = int(n_std_rooms)
                self.n_dlx_rooms = int(n_dlx_rooms)
                self.n_exe_rooms = int(n_exe_rooms)
            else:
                print('Hotel must have more than 1 room!, 1 standard room by default..')
                self.n_std_rooms = 1
                self.n_dlx_rooms = 0
                self.n_exe_rooms = 0
        except ValueError:
            print('Invalid Data Type, One standard room by default')
            self.n_std_rooms = 1
            self.n_dlx_rooms = 0
            self.n_exe_rooms = 0    
            
        # Calculate total number of rooms
        self.total_rooms = self.n_std_rooms + self.n_dlx_rooms + self.n_exe_rooms
        # Create Room objects and populate rooms_detail
        for i in range(self.n_std_rooms):
            r_no = str(i+1)+'S'
            rm = Room(r_no,'S', i,nd)
            self.rooms_detail['room_number'].append(r_no)
            self.rooms_detail['Room'].append(rm)
            
        for i in range(self.n_dlx_rooms):
            r_no = str(i+1) +'D' 
            rm = Room(r_no,'D', i, nd)
            self.rooms_detail['room_number'].append(r_no)
            self.rooms_detail['Room'].append(rm)
        
        for i in range(self.n_exe_rooms):
            r_no= str(i+1)+'E' 
            rm = Room(r_no,'E', i, nd)
            self.rooms_detail['room_number'].append(r_no)
            self.rooms_detail['Room'].append(rm)
            
    def display_rooms(self, rm_type):
        # Display available rooms of the specified type
        rm_type = str(rm_type)
        if rm_type == 'S':
            room_available = self.rooms_detail['room_number'][0:self.n_std_rooms]
            print('Standard Rooms:')
            print(room_available)
        elif rm_type == 'D':
            room_available = self.rooms_detail['room_number'][self.n_std_rooms:self.n_std_rooms+self.n_dlx_rooms]
            print('Deluxe Rooms')
            print(room_available)
        elif rm_type == 'E':
            room_available = self.rooms_detail['room_number'][self.n_std_rooms+self.n_dlx_rooms:self.n_std_rooms+self.n_dlx_rooms+self.n_exe_rooms]
            print('Executive Rooms')
            print(room_available)
        else:
            print('Room type does not exist!')
            
    def check_hotel_booked(self, checked_in_date, checked_out_date):
        # Check if the hotel is fully booked for the specified dates
        num_booking = 0
        print("Available Rooms")
        print("---------------")
        for i in range(len(self.rooms_detail['Room'])):
            (a, b) = self.rooms_detail['Room'][i].check_reservation_dates(checked_in_date, checked_out_date)
            if b == Room.reserve_status['2'] :
                num_booking += 1
            else:
                print('Room #:', self.rooms_detail['room_number'][i],self.rooms_detail['Room'][i])
        if num_booking == self.total_rooms:
            self.fully_booked = 1
        else:
            self.fully_booked = 0
        return self.fully_booked
            
    def search_room(self, room_id):
        # Search for and return the Room object based on room number
        self.room_index = self.rooms_detail['room_number'].index(room_id)
        self.room = self.rooms_detail['Room'][self.room_index]
        return self.room
    
    def return_rooms_data(self):
        # Return details of all rooms in the hotel
        return self.rooms_detail