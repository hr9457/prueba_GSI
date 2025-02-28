


create table if not exists kanban(
	id_kanban serial primary key,
	name_kanban varchar(100) not null
);


create table if not exists stack(
	id_stack serial primary key,
	name_stack varchar(100) not null,
	id_kanban int not null,
	constraint fk_kanban foreign key (id_kanban) references kanban(id_kanban)
);

create table if not exists taks(
	id_task SERIAL primary key,
	name_task varchar(100) not null,
	description varchar(500) not null,
	asigned_to varchar(100) not null,
	id_stack int not null,
	constraint fk_stack foreign key (id_stack) references stack(id_stack)
);



