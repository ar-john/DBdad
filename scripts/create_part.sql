CREATE TABLE PART (
PART_NUM int primary key auto_increment,
CATEGORY varchar(100) not null,
PART_DESC varchar(255),
PRICE float not null,
STOCK_QTY int(5) not null,
COMP_ID int,
FOREIGN KEY (COMP_ID) REFERENCES compatible(COMP_ID))