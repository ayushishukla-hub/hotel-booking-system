#Initial data structures using lists, tuples and dictionaries

#Room types and their fixed  attributes (Tuple: Room Type Name , Base Price)
ROOM_TYPES={"1:" ("Regular",1500),
            "2:" ("Deluxe", 3500),
            "3:" ("Suite", 6500)}

#Master dictionary of all rooms in the hotel
#Format: {"room_no":[Room type, Status]} where status is "Vacant" or "Booked"

ROOMS_DATABASE={"101":["Regular","Vacant"]
                "102":["Regular","Vacant"]
                "201":["Deluxe","Vacant"]
                "202":["Deluxe","Vacant"]
                "301":["Suite","Vacant"]}
    
#Bookings dictionary to track active reservations
#Format: {"booking_id":{"room_no":str,"guest_name":str,"days":int}}
BOOKINGS_DATABASE={}    