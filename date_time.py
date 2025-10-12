import datetime

# Get the current date and time
now = datetime.datetime.now()
print("Current date and time:", now)

# Get only the current date
today = datetime.date.today()
print("Today's date:", today)

# Get individual components
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
print("Hour:", now.hour)
print("Minute:", now.minute)
print("Second:", now.second)

# Create a specific date
custom_date = datetime.date(2025, 10, 12)
print("Custom date:", custom_date)

# Calculate the difference between dates
future_date = datetime.date(2025, 12, 31)
difference = future_date - today
print("Days until New Year:", difference.days)

# Format date and time
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("Formatted datetime:", formatted)
