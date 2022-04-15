create database if not exists DadsParts;
use DadsParts;

-- creating the CAR table
create table CAR (
	CAR_ID char(5) primary key,
    CAR_YEAR int not null,
    MAKE varchar(100) not null,
    MODEL varchar(100) not null,
    SUBMODEL varchar(15),
    ENG_SIZE decimal(10,1)
);
    
 -- table PART has PartNum  
 create table PART (
	PART_NUM char(5) primary key,
    CATEGORY varchar(100) not null,
    PART_DESC varchar(255),
    PRICE float not null,
    STOCK_QTY int(5) not null,
    DATE_AVAIL date
);

-- compatible table
create table COMPATIBLE (
	COMP_ID char(5) primary key,
    PART_NUM char(5),
    CAR_ID char(5),
    FOREIGN KEY (PART_NUM) REFERENCES PART(PART_NUM),
    FOREIGN KEY (CAR_ID) REFERENCES CAR(CAR_ID)
);

-- customer table
create table CUSTOMER (
	CUST_ID char(5) primary key,
    CAR_ID char(5),
    fName varchar(50),
    lname varchar(50),
    FOREIGN KEY (CAR_ID) REFERENCES CAR(CAR_ID)
);



-- Employee table
create table EMPLOYEE (
	EMP_ID char(5) primary key,
    firstname varchar(100),
    lastname varchar(100),
    admin bool,
    passwd varchar(64)
);

-- invoice table

create table INVOICE (
	INV_NUM char(5) primary key,
    CUST_ID char(5),
    EMP_ID char(5),
    PART_NUM char(5),
    PARTQTY int(5),
    FOREIGN KEY (PART_NUM) REFERENCES PART(PART_NUM),
    FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER(CUST_ID),
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
);

-- inserting into Car and Part
insert into CAR values('00001', 1999, 'Ford', 'Explorer', 'XLT', 5.1);
insert into CAR values('00002', 2005, 'Ford', 'Mustang', '', 7.2);
insert into CAR values('00003', 2014, 'BMW', 'i8', '', 6.3);
insert into CAR values('00004', 2017, 'Chevrolet', 'Cruze', '', 5.1);
insert into CAR values('00005', 2021, 'GMC', 'Sierra', '1500 Limited', 3.0);
insert into CAR values('00006', 2010, 'Ferrari', '458 Italia', '', 6.5);
insert into CAR values('00007', 2011, 'Volkswagen', 'GTI', '', 2.2);
insert into CAR values('00008', 2022, 'Tesla', 'Model Y', '', null);
insert into CAR values('00009', 2012, 'KIA', 'Forte', 'Koup', 3.1);
insert into CAR values('00010', 2021, 'McLaren', 'Artura', '', 3.0);
insert into PART values('00001', 'Windshield Wiper', 'Great Values 22 Inch Windshield Wiper; budget option', '19.99', '13', '2022-02-12');
insert into PART values('00002', 'Headlight', 'Great Values Headlight; budget option, works with most models', '9.99', '27', '2022-01-12');
insert into PART values('00003', 'Battery', 'Super Start Platinum Battery Group Size 48 H6', '59.99', '5', '2022-03-15');
insert into PART values('00004', 'Motor Oil', 'Great Values Motor Oil; budget option', '9.99', '0', '2022-04-12');
insert into PART values('00005', 'Motor Oil', 'PowerSports Motor Oil', '19.99', '51', '2021-12-22');
insert into PART values('00006', 'Windshield Wiper', 'Bosch Focus 22 Inch Wiper Blade', '27.99', '18', '2022-02-02');
insert into PART values('00007', 'Accessories', 'Motorola Bluetooth Radio', '199.99', '2', '2022-3-12');
insert into PART values('00008', 'Brakes', 'BrakeBeast 11.6 Inch Brake Shoe', '59.99', '9', '2022-3-12');
insert into PART values('00009', 'Alternator', 'Ultima Selevt 75 Amp Alternator', '74.99', '0', '2022-5-01');
insert into PART values('00010', 'Tools', 'Husky 3-ton Floor Garage Jack', '139.99', '4', '2022-3-12');

-- inserting into customer table
insert into CUSTOMER values ('00001', '00001', 'Lance', 'Stroll');
insert into CUSTOMER values ('00002', '00002', 'Lewis', 'Hamilton');
insert into CUSTOMER values ('00003', '00003', 'Samuel','Picard');
insert into CUSTOMER values ('00004','00004','Yuki','Tsunoda');
insert into CUSTOMER values ('00005','00005','Valtteri','Bottas');
insert into CUSTOMER values ('00006','00006','Charles','Leclerc');
insert into CUSTOMER values ('00007','00007','George','Russel');
insert into CUSTOMER values ('00008','00008','Carlos','Sainz');
insert into CUSTOMER values ('00009','00009','Fernando','Alonso');
insert into CUSTOMER values ('00010','00010','Esteban','Ocon');

-- inserting into employee and compatibility

INSERT INTO EMPLOYEE VALUES('00001', 'OLIVER', 'ROSS', TRUE, 'JWYvaXnV');
INSERT INTO EMPLOYEE VALUES('00002', 'ALAN', 'FISHER', TRUE, 'qAc35GEG');
INSERT INTO EMPLOYEE VALUES('00003', 'ANDREA', 'ANDERSON', TRUE, 'yDxS7gL7');
INSERT INTO EMPLOYEE VALUES('00004', 'LEAH', 'ELLISON', FALSE, 'nuZn2kRW');
INSERT INTO EMPLOYEE VALUES('00005', 'JUSTIN', 'KNOX', FALSE, 'TKC9dNbk');
INSERT INTO EMPLOYEE VALUES('00006', 'ZOE', 'PARR', FALSE, 'p68RZWRR');
INSERT INTO EMPLOYEE VALUES('00007', 'TIM', 'HARDACRE', FALSE, 'vzn7f4wj');
INSERT INTO EMPLOYEE VALUES('00008', 'FAITH', 'CAMPBELL', FALSE, 'eXrVpAmG');
INSERT INTO EMPLOYEE VALUES('00009', 'VICTOR', 'OGDEN', FALSE, 'TeFLmpcG');
INSERT INTO EMPLOYEE VALUES('00010', 'MATT', 'ALLAN', FALSE, '5uncF9Yd');

-- inserting into invoice table
insert into INVOICE values ('00001','00001','00001','00001', 5);
insert into INVOICE values ('00002','00002','00002','00002', 3);
insert into INVOICE values ('00003','00003','00003','00003', 16);
insert into INVOICE values ('00004','00004','00004','00004', 4);
insert into INVOICE values ('00005','00005','00005','00005', 1);
insert into INVOICE values ('00006','00006','00006','00006', 7);
insert into INVOICE values ('00007','00007','00007','00007', 2);
insert into INVOICE values ('00008','00008','00008','00008', 4);
insert into INVOICE values ('00009','00009','00009','00009', 2);
insert into INVOICE values ('00010','00010','00010','00010', 3);



INSERT INTO COMPATIBLE VALUES('00001', '00001', '00009');
INSERT INTO COMPATIBLE  VALUES('00002', '00001', '00004');
INSERT INTO COMPATIBLE VALUES('00003', '00001', '00007');
INSERT INTO COMPATIBLE VALUES('00004', '00002', '00008');
INSERT INTO COMPATIBLE VALUES('00005', '00002', '00003');
INSERT INTO COMPATIBLE VALUES('00006', '00004', '00001');
INSERT INTO COMPATIBLE VALUES('00007', '00004', '00002');
INSERT INTO COMPATIBLE VALUES('00008', '00004', '00005');
INSERT INTO COMPATIBLE VALUES('00009', '00005', '00003');
INSERT INTO COMPATIBLE VALUES('00010', '00005', '00006');

