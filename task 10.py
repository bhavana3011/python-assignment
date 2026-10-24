
# Smart Parking Fee Management

from datetime import datetime
import math

# Vehicle parking rates per hour
rates = {
    "car": 30,
    "bike": 10,
    "bus": 50
}

daily_limit = 300
penalty = 100

# Get vehicle details
vehicle = input("Enter vehicle type (car/bike/bus): ").lower()
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

# Validate vehicle type
if vehicle not in rates:
    print("Invalid vehicle type!")

else:
    try:
        entry_time = datetime.strptime(entry, "%H:%M")
        exit_time = datetime.strptime(exit_time, "%H:%M")

        # Calculate parking duration
        duration = (exit_time - entry_time).total_seconds() / 3600

        # Handle overnight parking
        if duration < 0:
            duration += 24

        if duration == 0:
            print("Invalid parking duration!")

        else:
            hours = math.ceil(duration)

            # Calculate fee with daily limit
            fee = min(hours * rates[vehicle], daily_limit)

            # Apply penalty for parking over 12 hours
            if duration > 12:
                fee += penalty
                print("Overnight/long-stay penalty: Rs.", penalty)

            print("\n--- Parking Bill ---")
            print("Vehicle Type:", vehicle.title())
            print("Parking Duration:", round(duration, 2), "hours")
            print("Chargeable Hours:", hours)
            print("Parking Fee: Rs.", fee)

    except ValueError:
        print("Invalid time! Please enter time in HH:MM format.")
