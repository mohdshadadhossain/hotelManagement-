#required imports
from hotel import Hotel
from customer import Customer
from operator import attrgetter

#this class is used to perform all the required task for hotem management
class RoomBooking:
    attrs = ('year', 'month', 'day')
    
    def __init__(self, n_std_rooms, n_dlx_rooms, n_exe_rooms, nd):
        # Initialize RoomBooking with a Hotel instance
        self.hotel = Hotel(n_std_rooms, n_dlx_rooms, n_exe_rooms, nd)
        
        # Initialize customer details storage
        self.customer_details = {}
        self.customer_details['cust_id'] = []
        self.customer_details['Customers'] = []
        
        # Initialize current customer and flags
        self.current_customer = None
        self.current_flag = False
        
        # Flags for booking and current active room
        self.booked_flag = False
        self.current_active_room = None
        self.current_index = 0
    
    def dates_available_list(self):
        # Display available dates for booking
        check_room = self.hotel.return_rooms_data()['Room'][0]
        print('Your check in and check out dates must be within:')
        print(check_room.print_room_calendar_days())
    
    def add_customer(self, cust_name, cust_phone, cust_address, num_occupants):
        # Add a new customer to the system
        customer = Customer(cust_name, cust_phone, cust_address, num_occupants)
        cust_id = customer.return_cust_id()
        if cust_id not in self.customer_details['cust_id']:
            self.customer_details['Customers'].append(customer)
            self.customer_details['cust_id'].append(cust_id)
        else:
            print('Customer already exists!')
        return cust_id

    def book_room(self, cust_id,  checked_in_date, checked_out_date):
        # Book a room for a customer
        # check dates are available or not and room is available or not
        self.booked_flag = False
        if self.get_current_customer(cust_id):
            self.current_customer.set_booking_dates(checked_in_date, checked_out_date)
            date_in, date_out = self.current_customer.return_dates()
            if self.hotel.check_hotel_booked(date_in, date_out) == 0:
                
                if self.current_customer.return_assigned_room() == []:
                    try:
                        print('\nBooking for Customer id', cust_id)
                        room_id = input('Choose a room from the available list: ').upper()
                        self.current_active_room = self.hotel.search_room(room_id)
                        flag = self.current_active_room.check_reservation_dates(date_in, date_out)[0]

                        if flag == True:
                            self.current_active_room.book_customer(cust_id)
                            self.current_customer.set_customer_room(room_id)
                            amount = self.current_customer.return_num_days()*self.current_active_room.return_room_price()
                            self.current_customer.charge_customer(amount)
                            self.return_booking_details(cust_id)
                            self.booked_flag = True
                        else:
                            print('Booking unsuccessful for customer id:',cust_id)
                            print('Failed to assign customer booking dates')
                    except (ValueError, AttributeError):
                        print('Incorrect Room Choice')
                else:
                    print('\n')
                    print(cust_id, 'is already booked Room:', self.current_customer.return_assigned_room())
                    print('\n')
            else:
                print(cust_id, ' Hotel is sold out for the selected dates!')
        else:
            print('Invalid customer id')
        return self.booked_flag
    
    def check_in(self,cust_id, room_number):
        # Perform check-in for a customer
        if self.get_current_customer(cust_id):
            print(self.current_customer.return_assigned_room()[0])
            if self.current_customer.return_assigned_room()[0]==room_number:
                self.current_customer.set_is_checked(True)
                print(cust_id ,"checked in successfully in room ",room_number)
                print("Welcome to Hotel Comfort\n")
            else:
                print(room_number," does not exist!!")
        else:
            print(cust_id, " does not exist!!")
        
    def check_out(self,cust_id):
        # Perform check-out for a customer
        if self.get_current_customer(cust_id):
            if self.current_customer.return_is_checked():
                try:
                    booked_rooms = self.current_customer.return_assigned_room()[0]
                except IndexError:
                    booked_rooms = []
                    print('Either the index is out of range or there is no room booking!')
                if booked_rooms != []:
                    self.return_booking_details(cust_id)
                    print("Many thanks to you for your visit.... ")
                    room = self.hotel.search_room(booked_rooms)
                    room.cancel_booking_by_custid(cust_id)            
                    del self.customer_details['cust_id'][self.current_index]
                    del self.customer_details['Customers'][self.current_index]
        
    def cancel_room_booking(self,cust_id):
        # Cancel room booking for a customer
        if self.get_current_customer(cust_id):
            try:
                booked_rooms = self.current_customer.return_assigned_room()[0]
            except IndexError:
                booked_rooms = []
                print('Either the index is out of range or there is no room booking!')
            if booked_rooms != []:
                    room = self.hotel.search_room(booked_rooms)

                    room.cancel_booking_by_custid(cust_id)
                    amount = self.current_customer.return_total_amount()
                    self.current_customer.refund_customer(amount)
                    self.current_customer.reset_customer_data()
                    print('Booking for', cust_id, 'Cancelled')

                    del self.customer_details['cust_id'][self.current_index]
                    del self.customer_details['Customers'][self.current_index]
            else:
                print('No rooms assigned for customer', cust_id)
        else:
            print('Invalid customer id')
        
    def return_booking_details(self, cust_id):
        # Return booking details for a customer
        if self.get_current_customer(cust_id):
            (cust_name, cust_phone, cust_address, num_occupants) = self.current_customer.return_customer_details()
            total_amount = self.current_customer.return_total_amount()
            booked_rooms = self.current_customer.return_assigned_room()
            booked_dates = self.current_customer.return_dates()
            if len(booked_rooms) != 0:
                room_id = booked_rooms[0]
            else:
                room_id = booked_rooms
            self.current_customer.cust_bill.print_bill(cust_name, cust_phone, cust_address, num_occupants,\
                                                    room_id, total_amount, booked_dates[0], booked_dates[1], cust_id)
        else:
            print('Invalid customer id')
    
    def update_room_booking(self, cust_id, new_in_date, new_out_date):
        # Update room booking for a customer
        #find customer by ID index, go to that customer
        if self.get_current_customer(cust_id):
            rooms = self.current_customer.return_assigned_room()
            if rooms:
                (cust_name, cust_phone, cust_address, num_occupants) = self.current_customer.return_customer_details()
                old_book_dates = self.current_customer.return_dates()
                print(cust_id, 'has booked room', rooms, 'between', old_book_dates[0], 'and', old_book_dates[1])

                self.cancel_room_booking(cust_id)
                self.add_customer(cust_name, cust_phone, cust_address, num_occupants)

                book_flag = self.book_room(cust_id, new_in_date, new_out_date)
                if not book_flag:
                    print('Because another customer is already booked, the modification was unsuccessful, and the dates were reset....\n')
                    old_cust_in_date = attrgetter(*RoomBooking.attrs)(old_book_dates[0])
                    old_cust_out_date = attrgetter(*RoomBooking.attrs)(old_book_dates[1])
                    self.book_room(cust_id, old_cust_in_date, old_cust_out_date)
            else:
                print('No rooms booked!!')
        else:
            print('Invalid Customer id!!')
        
    def get_current_customer(self, cust_id):
        # Get the current customer based on customer id
        try:
            self.current_index = self.customer_details['cust_id'].index(cust_id)
            self.current_customer = self.customer_details['Customers'][self.current_index]
            self.current_flag = True
        except ValueError:
            print('The selected customer does not exist in the database')
            self.current_flag = False
        return self.current_flag

    def print_all_customers(self):
        # print the details of all customers
        cust_list = self.customer_details.get('Customers')

        if cust_list is not None:
            print("CustomerId  CustomerName  ContactNumber  Address   NoOfPersons   RoomNo  CheckedIn   CheckedOut  Amount")
            print('-'*100)
            for element in cust_list:
                print(f"{element}")
            print('-'*100)
        else:
            print(f"Customers not found.")

    def display_menu(self):
        # Display the main menu options
        print("Hotel Comfort")
        print("-"*20)
        print("1. Room Display")
        print("2. Room Booking")
        print("3. Check In")
        print("4. Check Out")
        print("5. Modify Room Booking")
        print("6. Cancel Room Booking")
        print("7. Display Customer List")
        print("8. Exit")
