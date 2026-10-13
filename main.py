from room_manager import RoomManager
from booking import BookingManager

def main():
    while True:
        print("\n===========================================")
        print("    HOTEL ROOM BOOKING MANAGEMENT SYSTEM     ")
        print("=============================================")
        print("1. View Vacant Rooms")
        print("2. View Booked Rooms")
        print("3. Book a Room")
        print("4. Update Room Booking")
        print("5. Cancel Booking")
        print("6. Exit")

        choice=input("Enter your choice (1-6)").strip()

        if choice==1:
            RoomManager.display_vacant_rooms()
        elif choice==2:
            RoomManager.display_booked_rooms()
        elif choice==3:
            BookingManager.book_room()
        elif choice==4:
            BookingManager.update_booking()
        elif choice==5:
            BookingManager.cancel_booking()
        elif choice==6:
            print("Thank You for using the Hotel Room Booking Management System")
            break
        else:
            print("Invalid Choice. Please select between 1-6")
        
if __name__=="__main__":
    main()