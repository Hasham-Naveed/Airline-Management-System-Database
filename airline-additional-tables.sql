-- Assuming your database name is "airline"  other than change in below command
USE airline;
GO

-- History tables

-- Example for Reservation_History: 
CREATE TABLE Reservation_History (
    Reservation_no INT,
    P_id INT,
    S_id INT,
    Seat_no INT,
    Action VARCHAR(10),
    Timestamp DATETIME,
    [User] VARCHAR(30)  -- Use [User] instead of User since it's a reserved keyword
);
GO

-- Example for Person_History: 
CREATE TABLE Person_History (
    P_id INT,
    P_fname VARCHAR(60),
    P_lname VARCHAR(60),
    P_contact VARCHAR(30),
    P_age INT,
    P_gender VARCHAR(60),
    C_id INT,
    Action VARCHAR(10),
    Timestamp DATETIME,
    [User] VARCHAR(30)  -- Use [User] here too
);
GO

-- Example for Payment_History: 
CREATE TABLE Payment_History (
    Pay_id INT,
    Ticket_no INT,
	Amount int,
	Payment_date date,
	Action VARCHAR(10),
    Timestamp DATETIME,
    [User] VARCHAR(30)  -- Use [User] instead of User since it's a reserved keyword
);
GO

-- Triggers for Update and Delete:
-- Create triggers for Reservation update and delete 

-- Example Trigger for Reservation Delete: 
CREATE TRIGGER Reservation_Delete_Trigger
ON Reservation
AFTER DELETE
AS
BEGIN
    INSERT INTO Reservation_History (Reservation_no, P_id, S_id, Seat_no, Action, Timestamp, [User])
    SELECT Reservation_no, P_id, S_id, Seat_no, 'Delete', CURRENT_TIMESTAMP, SYSTEM_USER
    FROM DELETED;
END;
GO

-- Example Trigger for Payment Delete: 
CREATE TRIGGER Payment_Delete_Trigger
ON Payment
AFTER DELETE
AS
BEGIN
    INSERT INTO Payment_History (Pay_id, Ticket_no, Amount, Payment_date, Action, Timestamp, [User])
    SELECT Pay_id, Ticket_no, Amount, Payment_date, 'Delete', CURRENT_TIMESTAMP, SYSTEM_USER
    FROM DELETED;
END;
GO

-- Procedure for Insertion:

-- Create procedures for inserting records into the Reservation, Payment
CREATE PROCEDURE GeneratePaymentReport
AS
BEGIN
    -- Declare variables
    DECLARE @totalPayments INT;
    DECLARE @averagePayment DECIMAL(10, 2);

    -- Calculate total payments
    SELECT @totalPayments = SUM(Amount) FROM Payment;

    -- Calculate average payment
    SELECT @averagePayment = AVG(Amount) FROM Payment;

    -- Display the report
    SELECT 
        'Total Payments: ' AS Report, 
        @totalPayments AS TotalPayments, 
        'Average Payment: ' AS Report, 
        @averagePayment AS AveragePayment;
END;
GO
