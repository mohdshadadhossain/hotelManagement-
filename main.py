from roombooking import RoomBooking
from datetime import datetime
from operator import attrgetter
from dateutil.relativedelta import relativedelta

# Create an instance of the RoomBooking class with 10 standard, 10 deluxe, and 10 executive rooms, and a 45-day booking window
hotel_system = RoomBooking(10, 10, 10, 45)

# Main menu loop
while True:
    hotel_system.display_menu()
    choice = str(input("Enter your choice: "))

    if choice == '1':
        hotel_system.hotel.display_rooms('S')
        hotel_system.hotel.display_rooms('D')
        hotel_system.hotel.display_rooms('E')
    elif choice == '2':
        try:
        # Get customer details and booking information from user input
            cname = str(input("Enter Customer Name: ")).upper()
            cadd = str(input("Enter Customer Address: ")).upper()
            ccontact = str(input("Enter Customer Contact: "))
            cguests = int(input("Enter number of Guests: "))
            cust_id=hotel_system.add_customer(cname,ccontact, cadd,cguests)

            # Convert check-in date to datetime format
            check_in_date = str(input("Enter Check-In Date (YYYY-MM-DD): "))
            numstay=int(input("Enter number of days to stay :"))
            
            datein = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            date1 = attrgetter(*RoomBooking.attrs)(datein)
            # Calculate check-out date based on the number of stay days
            dateout = datein + relativedelta(days = numstay)
            date2 = attrgetter(*RoomBooking.attrs)(dateout) 
            # Book a room for the customer
            hotel_system.book_room(cust_id, date1, date2)
        except(NameError, ValueError):
            print('Invalid Input(s), try again')

    elif choice == '3':
        # Get customer ID and room number for check-in
        try:
            cid = str(input("Enter Customer Id: ")).upper()
            rno = str(input("Enter Room Number: ")).upper()
            hotel_system.check_in(cid,rno)
        except(NameError, ValueError):
            print('Invalid Input(s), try again')
        
    elif choice == '4':
        # Get customer ID for check-out
        try:
            cid = str(input("Enter Customer Id: ")).upper()
            hotel_system.check_out(cid)
        except(NameError, ValueError):
            print('Invalid Input(s), try again')
            
    elif choice == '5':
        try:
            cid = str(input("Enter Customer Id: ")).upper()
     
            check_in_date = str(input("Enter New Check-In Date (YYYY-MM-DD): "))
            numstay=int(input("Enter number of days to stay :"))
            
            datein = datetime.strptime(check_in_date, '%Y-%m-%d').date()
            date1 = attrgetter(*RoomBooking.attrs)(datein)
            dateout = datein + relativedelta(days = numstay)
            date2 = attrgetter(*RoomBooking.attrs)(dateout) 
            hotel_system.update_room_booking(cid, date1, date2)
            
        except(NameError, ValueError):
            print('Invalid Input(s), try again')
        
    elif choice == '6':
        try:
            # Get customer ID for canceling room booking
            cid = str(input("Enter Customer Id: ")).upper()
            hotel_system.cancel_room_booking(cid)
        except(NameError, ValueError):
            print('Invalid Input(s), try again')
    elif choice == '7':
        # Display details of all customers
        hotel_system.print_all_customers()
    elif choice == '8':
        # Exit the main menu loop
        break
    else:
        print("Invalid choice. Please enter a valid option.")