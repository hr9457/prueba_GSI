create table taks(
	id_task SERIAL primary key,
	name_task varchar(100) not null,
	description varchar(500) not null,
	asigned_to varchar(100) not null
);

create table stack(
	id_stack serial primary key,
	name_stack varchar(100) not null,
	id_task int not null,
	constraint fk_taks foreign key (id_task) references taks(id_task)
);


create table kanban(
	id_kanban serial primary key,
	name_kanban varchar(100) not null,
	id_stack int null,
	constraint fk_stack foreign key (id_stack) references stack(id_stack)
);
