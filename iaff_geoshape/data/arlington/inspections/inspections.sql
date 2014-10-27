CREATE TABLE arlington_inspections
(
  id serial,
  inspection_type varchar(100),
  address varchar(255),
  subaddress varchar(100),
  zip integer,
  city varchar(25),
  inspection_date date,
  next_inspection_date date,
  inspection_cause varchar(75),
  activity_type varchar(25),
  region varchar(25),
  property_use varchar(50),
  occupancy varchar(50),
  geom geometry(Point,4326),
  error boolean
);
