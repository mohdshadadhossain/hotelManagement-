# class for printing the bill
from datetime import date

class Bill:
    def __init__(self):
        # Initialize the Bill object with the current date
        self.create_time = date.today()

    def print_bill(self, cust_name, cust_phone, cust_address, num_occupants, assigned_room, total_amount, checked_in_date, checked_out_date, cust_id):
        # Print a formatted bill for a hotel stay

        # Header
        print('---------------------------------------------')
        print('\t\t\tComfort Hotel')
        print('---------------------------------------------')

        # Display creation date of the bill
        print('Created on       :', self.create_time)

        # Customer information
        print('Name             :', cust_name)
        print('Address          :', cust_address)
        print('Number of Guests :', num_occupants)
        print('Contact Number   :', cust_phone)

        # Booking details
        print('Room Booked      :', assigned_room)
        print('Check In Date    :', checked_in_date)
        print('Check Out Date   :', checked_out_date)
        print('\n')

        # Customer ID and Total Amount
        print('Your ID          :', cust_id)
        print('Total Amount     :', total_amount)

        # Footer
        print('---------------------------------------------')
        print('\n')
