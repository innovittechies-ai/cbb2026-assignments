# The Midnight Ticket Scam

n = int(input("Enter number of ticket bookings: "))

bookings = {}
violations = set()   # use set to avoid duplicates

for i in range(n):
    user_id, booking_hour = input(
        "Enter user_id and booking_hour: "
    ).split()

    booking_hour = int(booking_hour)  # valid, even if not used

    bookings[user_id] = bookings.get(user_id, 0) + 1 #count the number of booking for each user_id

    if bookings[user_id] > 5:
        violations.add(user_id)

if violations:
    print("Violating user IDs:", list(violations))
else:
    print("No violations")


