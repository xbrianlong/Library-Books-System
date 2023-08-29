CREATE TABLE Members(
	memberID VARCHAR(8) NOT NULL,
    name VARCHAR(20) NOT NULL,
    faculty VARCHAR(15) NOT NULL,
    phoneNo INT,
    email VARCHAR(25),
    PRIMARY KEY (memberID));
CREATE TABLE Books(
    accessionNo VARCHAR(5) NOT NULL,
    title VARCHAR(60) NOT NULL,
    authors VARCHAR(60) NOT NULL,
    isbn BIGINT NOT NULL,
    publisher VARCHAR(40),
    publishYear SMALLINT,
    memberID VARCHAR(8),
    borrowDate DATE,
    dueDate DATE,
    PRIMARY KEY (accessionNo),
    FOREIGN KEY (memberID)
        REFERENCES Members (memberID)
        ON DELETE SET NULL ON UPDATE CASCADE);
CREATE TABLE Fines(
	memberID VARCHAR(8) NOT NULL,
    payAmount SMALLINT,
    payDate DATE,
    FOREIGN KEY (memberID) REFERENCES Members (memberID));
CREATE TABLE Reserves(
	memberID VARCHAR(8) NOT NULL,
    accessionNo VARCHAR(5) NOT NULL,
    reserveDate DATE,
    PRIMARY KEY (memberID, accessionNo));
    

