import pyodbc
from faker import Faker
import random
import datetime
# Establish a connection to the SQL Server database
conn = pyodbc.connect(
 'Driver={SQL Server};'
 'Server=DESKTOP-EPPSLLR;'
 'Database=airline;'
 'Trusted_Connection=yes;'
)
# Create an instance of the Faker generator
fake = Faker()
# Create a cursor to execute SQL queries
cursor = conn.cursor()
# Generate and insert data into the Airport table
for i in range(1, 21): # Insert 20 records with airport codes from 101 to 120
 airport_code = i
 airport_name = fake.city() + ' Airport'
 airport_location = airport_name
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Airport (Airport_code, Airport_name, Airport_location) VALUES (?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, airport_code, airport_name, airport_location)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Airline table
for i in range(1,51): # Insert 50 records
 airline_code = i
 airline_name = fake.company() + ' Airline'
 airline_contact = fake.phone_number()
 airport_code = int(fake.random_int(1,20))
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Airline (Airline_code, Airline_name, Airline_contact, Airport_code) VALUES (?, ?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, airline_code, airline_name, airline_contact, airport_code)
# Commit the changes to the database 
conn.commit()
# Generate and insert data into the Flight table
for i in range(1,101): # Insert 100 records
 flight_no = i
 airline_code = fake.random_int(min=1, max=50)
 origin = fake.city()
 destination = fake.city()
 seat_capacity = fake.random_int(min=100, max=200)
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Flight (Flight_no, Airline_code, Origin, Destination, Seat_capacity) VALUES (?, ?, ?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, flight_no, airline_code, origin, destination, seat_capacity)
# Commit the changes to the database 
conn.commit()
# Generate and insert data into the Schedule table
for i in range(1, 201): # Insert 200 records
 s_id = i
 departure_date = fake.date()
 departure_time = fake.time_object()
 arrival_date = departure_date
 # Generate random number of hours to add
 hours_to_add = random.randint(3, 6)
 # Convert the Faker time to a datetime.datetime object
 datetime_obj = datetime.datetime.combine(datetime.datetime.now().date(), departure_time)
 # Add the random number of hours to the datetime object
 new_datetime_obj = datetime_obj + datetime.timedelta(hours=hours_to_add)
 # Extract the new time as a datetime.time object
 arrival_time = new_datetime_obj.time()
 flight_no = fake.random_int(min=1, max=100)
 # Prepare the SQL query with parameter values
 query = "INSERT INTO Schedule (S_id, Departure_date, Departure_time, Arrival_date, Arrival_time, Flight_no) VALUES ({}, '{}', '{}', '{}', '{}', {})".format(s_id, departure_date, departure_time, arrival_date, arrival_time, flight_no)
 # Execute the query
 cursor.execute(query)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Class table
for i in range(1,4): # Insert 3 records
 c_id = i
 c_name = 'Economy' if i == 3 else ('Business' if i == 2 else 'First Class')
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Class (C_id, C_name) VALUES (?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, c_id, c_name)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Person table
for i in range(1,1001): # Insert 1000 records
 random = fake.random_element(['F','M'])
 p_id = i
 p_fname = fake.first_name_female() if random == 'F' else fake.first_name_male()
 p_lname = fake.last_name()
 p_contact = fake.phone_number()
 p_age = fake.random_int(min=10, max=60)
 p_gender = 'Female' if random == 'F' else 'Male'
 c_id = fake.random_int(min=1, max=3)
 # Prepare the SQL query with parameter placeholders
 query = 'INSERT INTO Person (P_id, P_fname, P_lname, P_contact, P_age, P_gender, C_id) VALUES (?, ?, ?, ?, ?, ?, ?)'
 
 # Execute the query with the parameter values
 cursor.execute(query, p_id, p_fname, p_lname, p_contact, p_age, p_gender, c_id)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Reservation table
for i in range(1,1001): # Insert 1000 records
 reservation_no = i
 p_id = i
 s_id = fake.random_int(min=1, max=200)
 seat_no = fake.random_int(min=1, max=200)
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Reservation (Reservation_no, P_id, S_id, Seat_no) VALUES (?, ?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, reservation_no, p_id, s_id, seat_no)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Baggage table
for i in range(1,101): # Insert 100 records
 b_id = i
 p_id = i
 weight = fake.random_int(min=10, max=50)
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Baggage (B_id, P_id, Weight) VALUES (?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, b_id, p_id, weight)
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Ticket table
for i in range(1,1001): # Insert 1000 records
 ticket_no = i
 reservation_no = i
 fare = fake.random_int(min=100, max=500)
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Ticket (Ticket_no, Reservation_no, Fare) VALUES (?, ?, ?)"
 # Execute the query with the parameter values
 cursor.execute(query, ticket_no, reservation_no, fare)
 
# Commit the changes to the database
conn.commit()
# Generate and insert data into the Payment table
import random
population = list(range(1, 1001))
for i in range(1, 701): # Insert 700 records
 pay_id = i
 num = random.sample(population, 1)[0] # Randomly select one element from the population list
 ticket_no = num
 amount = fake.random_int(min=100, max=500) + 50
 payment_date = fake.date() #datetime.date.today() to use current system date
 # Prepare the SQL query with parameter placeholders
 query = "INSERT INTO Payment (Pay_id, Ticket_no, Amount, Payment_date) VALUES (?, ?, ?, ?)"
 
 # Execute the query with the parameter values
 cursor.execute(query, pay_id, ticket_no, amount, payment_date)
# Commit the changes to the database
conn.commit()
# Close the cursor and the database connection
cursor.close()
conn.close()