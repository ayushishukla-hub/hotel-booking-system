import random
from data import ROOM_TYPES, ROOMS_DATABASE, BOOKINGS_DATABASE

class BookingManager:
    @staticmethod
    def book_room():
        print("\n---ROOM BOOKING---")
        print("Select Room Type:")
        for key, value in ROOM_TYPES.items():
            print(f"{key} {value[0]}  (Rs. {value[1]} per night)")

        choice=input("Enter your choice (1-3): ").strip()
        if choice not in ROOM_TYPES:
            print("Invalid room type choice.")
            return
        
        selected_type = ROOM_TYPES[choice][0]
        
        target_room=None
        for r_no, details in ROOMS_DATABASE.items():
            if details[0]==selected_type and details[1]=="Vacant":
                target_room=r_no
                break

        if not target_room:
            print(f"Sorry, no vacant rooms available for type: {selected_type}")
            return

        guest_name=input("Enter guest name:").strip()
        try:
            days=int(input("Enter number of days for booking:"))
        except ValueError:
            print("Invalid input for number of days. Booking failed.")
            return

        booking_id=str(random.randint(1000,9999))

        #Update database list status to "Booked"
        ROOMS_DATABASE[target_room][1]="Booked"
        BOOKINGS_DATABASE[booking_id]={"room_no":target_room,"guest_name":guest_name,
                                       "days":days,"type":selected_type}
        print(f"Booking successful! Booking ID: {booking_id}, Room No: {target_room}, 
              Guest: {guest_name}, Days: {days}")

    @staticmethod
    def update_booking():
        print("\n---UPDATE BOOKING---")
        booking_id=input("Enter Booking ID to update:").strip()
        if booking_id not in BOOKINGS_DATABASE:
            print("Booking ID not found.")
            return

        booking=BOOKINGS_DATABASE[booking_id]
        print(f"Current Booking Details: Room No: {booking['room_no']}, 
              Guest: {booking['guest_name']}, Days: {booking['days']}")
              
        new_name=input("Enter new guest name (leave blank to keep current):").strip()
        new_days=input("Enter new number of days (leave blank to keep current):").strip()
        if new_name:
            booking['guest_name']=new_name
        if new_days:
            try:
                booking["days"]=int(new_days)
            except ValueError:
                print("Invalid input for number. Days not updated")
            
        print("Booking updated successfully!")

    @staticmethod
    def cancel_booking():
        print("\n---CANCEL BOOKING---")
        booking_id=input("Enter booking ID to cancel.").strip()
        if booking_id not in BOOKINGS_DATABASE:
            print("Booking ID not found")
            return
        
        booking=BBOKING_DATABASE.pop(booking_id)
        room_no=booking["room_no"]

        if room_no in ROOMS_DATABASE:
            ROOMS_DATABASE[room_no][1]="Vacant"
        
        print(f"Booking {booking_id} cancelled successfully. Room {room_no} is now vacant.")