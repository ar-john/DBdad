create database if not exists DadsParts1;
use DadsParts1;

create table car (
	CAR_ID int primary key auto_increment,
    CAR_YEAR int not null,
    MAKE varchar(100) not null,
    MODEL varchar(100) not null);

create table COMPATIBLE (
COMP_ID int primary key auto_increment,
COMP_TYPE char(8)
);

alter table car
add column COMP_ID int;

alter table car
add constraint
foreign key (COMP_ID)
references compatible(comp_id);

CREATE TABLE PART (
	PART_NUM int primary key auto_increment,
	CATEGORY varchar(100) not null,
	PART_DESC varchar(255),
	PRICE float not null,
	STOCK_QTY int(5) not null,
	COMP_ID int,
	FOREIGN KEY (COMP_ID) REFERENCES compatible(COMP_ID));

create table CUSTOMER (
	CUST_ID int primary key auto_increment,
    CAR_ID int,
    fName varchar(50),
    lname varchar(50),
    FOREIGN KEY (CAR_ID) REFERENCES CAR(CAR_ID)
);

create table EMPLOYEE (
	EMP_ID char(5) primary key,
    firstname varchar(100),
    lastname varchar(100),
    admin bool,
    passwd varchar(64)
);

create table INVOICE (
	INV_NUM char(5) primary key,
    CUST_ID int,
    EMP_ID char(5),
    PART_NUM int,
    PARTQTY int,
    FOREIGN KEY (PART_NUM) REFERENCES PART(PART_NUM),
    FOREIGN KEY (CUST_ID) REFERENCES CUSTOMER(CUST_ID),
    FOREIGN KEY (EMP_ID) REFERENCES EMPLOYEE(EMP_ID)
);
