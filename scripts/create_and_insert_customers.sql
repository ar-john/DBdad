create table CUSTOMER (
	CUST_ID int primary key auto_increment,
    CAR_ID int,
    fName varchar(50),
    lname varchar(50),
    FOREIGN KEY (CAR_ID) REFERENCES CAR(CAR_ID)
);

insert into CUSTOMER (CAR_ID, fname, lname)values ( 256, 'Lance', 'Stroll');
insert into CUSTOMER (CAR_ID, fname, lname)values ( 884, 'Lewis', 'Hamilton');
insert into CUSTOMER (CAR_ID, fname, lname)values ( 643, 'Samuel','Picard');
insert into CUSTOMER (CAR_ID, fname, lname)values (752,'Yuki','Tsunoda');
insert into CUSTOMER (CAR_ID, fname, lname)values (736,'Valtteri','Bottas');
insert into CUSTOMER (CAR_ID, fname, lname)values (697,'Charles','Leclerc');
insert into CUSTOMER (CAR_ID, fname, lname)values (23,'George','Russel');
insert into CUSTOMER (CAR_ID, fname, lname)values (854,'Carlos','Sainz');
insert into CUSTOMER (CAR_ID, fname, lname)values (648,'Fernando','Alonso');
insert into CUSTOMER (CAR_ID, fname, lname)values (798,'Esteban','Ocon');
insert into CUSTOMER (CAR_ID, fname, lname)values (465,'Gregory','Gregoryson');
insert into CUSTOMER (CAR_ID, fname, lname)values (123,'Geoffrey','Van der Gring');
insert into CUSTOMER (CAR_ID, fname, lname)values (587,'Erik','Zomboniol');
insert into CUSTOMER (CAR_ID, fname, lname)values (864,'Reese','Alfredo');
insert into CUSTOMER (CAR_ID, fname, lname)values (237,'Carter','Scott');