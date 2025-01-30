--Choose database name of your choice and write below command below database name is "airline"
CREATE DATABASE airline;
GO

use airline;
GO
create table Airport(
Airport_code int primary key,
Airport_name varchar(60),
Airport_location varchar(60),
)

create table Airline(
Airline_code int not null,
Airline_name varchar(60),
Airline_contact varchar(30),
primary key(Airline_code),
Airport_code int foreign key references Airport(Airport_code)
)

create table Flight(
Flight_no int not null primary key,
Airline_code int foreign key references Airline(Airline_code),
Origin varchar(60),
Destination varchar(60),
Seat_capacity int,
)

create table Schedule(
S_id int primary key,
Departure_date date,
Departure_time time,
Arrival_date date,
Arrival_time time,
Flight_no int foreign key references Flight(Flight_no),
)

create table Class(
C_id int primary key,
C_name varchar(60),
)

create table Person(
P_id int primary key,
P_fname varchar(60),
p_lname varchar(60),
P_contact varchar(30),
P_age int,
P_gender varchar(60),
C_id int foreign key references Class(C_id)
)

create table Reservation(
Reservation_no int primary key,
P_id int foreign key references Person(P_id),
S_id int foreign key references Schedule(S_id),
Seat_no int,
)

create table Baggage(
B_id int primary key,
P_id int foreign key references Person(P_id),
Weight int ,
)

create table Ticket(
Ticket_no int primary key,
Reservation_no int foreign key references Reservation(Reservation_no),
Fare int,
)

create table Payment(
Pay_id int primary key,
Ticket_no int foreign key references Ticket(Ticket_no),
Amount int,
Payment_date date
)
