# Importing required modules
from bill import Bill  # Assuming 'Bill' class is defined in a file named 'bill.py'
from datetime import date

# Customer Class for managing hotel customer information and bookings
class Customer:
    def __init__(self, cust_name, cust_phone, cust_address, num_occupants):
        # Initialize customer attributes
        self.cust_name = cust_name
        self.cust_phone = cust_phone
        self.cust_address = cust_address
        self.num_occupants = int(num_occupants)
        self.cust_id = self.cust_name[0:2]  + str(self.cust_phone)[-4:]
        
        self.checked_in_date = None
        self.checked_out_date = None
        self.is_checked = False
        self.total_amount = 0
        self.num_days = 0
        self.assigned_room = []
        self.cust_bill = Bill()
    
    def return_is_checked(self):
        # return whether customer checked in or not
        return self.is_checked
    
    def set_is_checked(self,is_checked):
        #set customer is checked in
        self.is_checked = True
        
    def set_booking_dates(self, checked_in_date, checked_out_date):
        # Set customer's booking dates and calculate the number of days
        self.checked_in_date = date(checked_in_date[0], checked_in_date[1], checked_in_date[2])
        self.checked_out_date = date(checked_out_date[0], checked_out_date[1], checked_out_date[2])
        self.num_days = (self.checked_out_date - self.checked_in_date).days
        if self.num_days <= 0:
            print('The check-in date must be prior to the check-out date!')
    
    def set_customer_room(self, room_no):
       # Assign a room to the customer
        self.assigned_room.append(str(room_no))
        
    def reset_customer_data(self):
        # Reset customer data after check-out
        self.assigned_room = []
        self.checked_in_date = None
        self.checked_out_date = None
        self.cust_id = None
    
    def charge_customer(self, amount):
        # Charge the customer for room services
        self.total_amount+=amount
    
    def refund_customer(self, amount):
        # Refund a specific amount to the customer
        self.total_amount -= amount
        if self.total_amount <= 0:
            self.total_amount = 0
            print('Amount fully refunded: $', amount)

    def return_customer_details(self):
        # Return basic customer details
        return self.cust_name, self.cust_phone, self.cust_address, self.num_occupants

    def return_assigned_room(self):
        # Return the assigned room(s)
        return self.assigned_room
    
    def return_total_amount(self):
        # Return the total amount to be paid by the customer
        return self.total_amount
    
    def return_cust_id(self):
        # Return the customer ID
        return self.cust_id
    
    def return_dates(self):
        # Return the check-in and check-out dates
        return self.checked_in_date, self.checked_out_date
    
    def return_num_days(self):
        # Return the number of days of the booking
        return self.num_days
    
    def __str__(self):
        # Return a string representation of the customer
        return f"{self.cust_id}\t{self.cust_name}\t{self.cust_phone}\t{self.cust_address}\t{self.num_occupants}\t{self.assigned_room[0]}\t{self.checked_in_date}\t{self.checked_out_date}\t{self.total_amount}"