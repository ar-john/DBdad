alter table car
add column COMP_ID int;

alter table car
add constraint
foreign key (COMP_ID)
references compatible(comp_id);


