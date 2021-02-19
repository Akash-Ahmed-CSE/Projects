
CREATE TABLE Country
(
 CtID INT NOT NULL ,
CountryName varchar(25) NOT NULL,
 PRIMARY KEY (CtID) 
);
insert into Country values(101,'Bangladesh');
	insert into Country values(102,'India');
	insert into Country values(103,'Thailand');
	insert into Country values(104,'Nepal');
	insert into Country values(105,'Bhutan');


CREATE TABLE State
(
StID INT NOT NULL  ,
StateName varchar(25) NOT NULL,
Country INT NOT NULL,
 PRIMARY KEY (StID),
 FOREIGN KEY (Country) REFERENCES Country(CtID) on delete cascade  
);
	insert into State values(111,'Dhaka',101);
    insert into State values(112,'Dille',102);
	insert into State values(113,'Bangkok',103);
	insert into State values(114,'Kathmandu',104);
	insert into State values(115,'Thimphu',105);

CREATE TABLE Contact_Details
(
CnID INT NOT NULL ,
Email varchar(25) NOT NULL,
Mobile varchar(16) NOT NULL,
State INT NOT NULL,
 PRIMARY KEY (CnID),
 FOREIGN KEY (State) REFERENCES State(StID) on delete cascade 
 );
insert into Contact_Details values(151,'abc@gmail.com','01712345678',111);
insert into Contact_Details values(161,'def@gmail.com','01612345678',112);
insert into Contact_Details values(171,'ghi@gmail.com','01812345678',113);
insert into Contact_Details values(181,'jkl@gmail.com','01912345678',114);
insert into Contact_Details values(191,'mno@gmail.com','01512345678',115);




CREATE TABLE Passenger
(
PsID INT NOT NULL ,
Name varchar(25) NOT NULL,
Address varchar(25) NOT NULL,
Age INT NOT NULL,
Nationality varchar(16) NOT NULL,
Contacts INT NOT NULL,
 PRIMARY KEY (PsID),
 FOREIGN KEY (Contacts) REFERENCES Contact_Details(CnID) on delete cascade 
);
insert into Passenger values(171,'Akash Ahmed','savar',22,'Bnagladeshi',151);
insert into Passenger values(172,'Zaman Chowdury','shemultoly',23,'Indian',161);
insert into Passenger values(173,'Md. Hasan Imam','Thana Stand',24,'Thai',161);
insert into Passenger values(174,'Md. Mirajul Islam','Kashimpur',25,'Nepali',161);
insert into Passenger values(175,'Aktaruzzaman Joti','Anarkoli',26,'Bhutanese',161);



CREATE TABLE Route  
(
RtID INT NOT NULL ,
Airport varchar(25) NOT NULL,
Destination varchar(25) NOT NULL,
RouteCode varchar(16) NOT NULL ,
 PRIMARY KEY (RtID)
);


insert into Route values(555,'Shahajalal','India','zzzz');
insert into Route values(444,'indianAir','Bangladesh','pppp');
insert into Route values(333,'Suvarnabhumi','Thailand','mmmm');
insert into Route values(222,'Tribhuvan','Nepal','tttt');
insert into Route values(111,'Paro','Bhutan','hhhh');  


CREATE TABLE AirFare
(
AfID INT NOT NULL ,
Route INT NOT NULL,
Fare INT NOT NULL,
 PRIMARY KEY (AfID),
 FOREIGN KEY (Route) REFERENCES Route(RtID) on delete cascade 
);
insert into AirFare values(201,555,1000);
insert into AirFare values(202,444,1500);
insert into AirFare values(203,333,2000);
insert into AirFare values(204,222,2500);
insert into AirFare values(205,111,3000); 



CREATE TABLE AirCraft_Type      
(
ActID INT NOT NULL ,
Type varchar(25) NOT NULL,
Capacity INT NOT NULL,
 PRIMARY KEY (ActID)
);

insert into AirCraft_Type values(111,'First Class',80);
insert into AirCraft_Type values(211,'Business Class',90);
insert into AirCraft_Type values(311,'Premium Economy',100);
insert into AirCraft_Type values(411,'Economy',110);
insert into AirCraft_Type values(511,'Normal',120);


CREATE TABLE AirCraft      
(
AcID INT NOT NULL ,
Ac_Type INT NOT NULL,
Mfg_Date DATE NOT NULL,
 PRIMARY KEY (AcID),
 FOREIGN KEY (Ac_Type) REFERENCES AirCraft_Type(ActID) on delete cascade 
);

insert into AirCraft values(111,111,'20-NOV-19');
insert into AirCraft values(211,211,'20-DEC-19');
insert into AirCraft values(311,311,'20-JAN-20');
insert into AirCraft values(411,411,'20-FEB-20');
insert into AirCraft values(511,511,'20-MAR-20');


CREATE TABLE Flight_Schedule
(
FlID INT NOT NULL ,
FlightDate DATE NOT NULL,
Departure DATE NOT NULL,
Arrival DATE NOT NULL,
AirCraft INT NOT NULL,
NetFare INT NOT NULL,
 PRIMARY KEY (FlID),
 FOREIGN KEY (AirCraft) REFERENCES AirCraft(AcID) on delete cascade ,
 FOREIGN KEY (NetFare) REFERENCES AirFare(AfID) on delete cascade 
);
insert into Flight_Schedule values(111,'25-NOV-19','30-NOV-19','20-APR-20',111,201);
insert into Flight_Schedule values(122,'25-DEC-19','30-DEC-19','20-MAY-20',211,202);
insert into Flight_Schedule values(133,'25-JAN-20','30-JUN-20','20-JUN-20',311,203);
insert into Flight_Schedule values(144,'25-FEB-20','29-FEB-20','20-JUL-20',411,204);
insert into Flight_Schedule values(155,'25-MAR-20','30-MAR-20','20-AUG-20',511,205);




CREATE TABLE Transaction
(
TsID INT NOT NULL ,
BookingDate DATE NOT NULL,
Passenger INT NOT NULL,
Flight INT NOT NULL,
 PRIMARY KEY (TsID),
 FOREIGN KEY (Passenger) REFERENCES Passenger(PsID) on delete cascade ,
 FOREIGN KEY (Flight) REFERENCES Flight_Schedule(FlID) on delete cascade 
);
insert into Transaction values(511,'20-NOV-19',171,111);
insert into Transaction values(522,'20-DEC-19',172,122);
insert into Transaction values(533,'20-JAN-20',173,133);
insert into Transaction values(544,'20-FEB-20',174,144);
insert into Transaction values(555,'20-MAR-20',175,155); 
