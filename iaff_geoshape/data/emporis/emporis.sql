CREATE TABLE IF NOT EXISTS emporis_buildings2
(building_number_ebn char(255), building_number_bin char(255), official_name char(255), alternative_name char(255), construction_type char(255),
current_status char(255), architectural_style char(255), main_usages char(255), side_usages char(255), facade_system char(255),
facade_material char(255), facade_color char(255), structural_system char(255), structural_material char(255), foundation_system char(255),
features_and_amenities text, official_website char(1000), facts text, address_as_text text, address_main char(255), side_address char(255),
address_virtual char(255), postcode char(255), latitude char(255), longitude char(255), complex_name char(255), complex_type char(255),
lot_number char(255), block_number char(255), zone_name char(255), district_1st_level char(255), district_2nd_level char(255), city_name char(255),
metro_area_name char(255), state_name char(255), state_code char(255), country_name char(255), continent_name char(255), height_tip_ft char(255),
height_architectural_ft char(255), height_estimated_ft char(255), height_roof_ft char(255), height_main_roof_ft char(255),
height_top_floor_ft char(255), height_obs__deck_ft char(255), height_floor_floor_ft char(255), height_floor_ceiling_ft char(255),
length_ft char(255), width_ft char(255), floors_overground char(255), floors_underground char(255), year_construction_start char(255),
year_construction_end char(255), year_last_reconstruction char(255), year_destruction char(255), gross_floor_area_gfa_ft2 char(255),
usable_floor_area_ufa_ft2 char(255), volume_ft3 char(255), elevators char(255), escalators char(255), workplaces char(255),
parking_places char(255), units char(255), construction_costs char(255)
);

COPY emporis_buildings (building_number_ebn, building_number_bin, official_name, alternative_name, construction_type, current_status,
architectural_style, main_usages, side_usages, facade_system, facade_material, facade_color, structural_system, structural_material,
foundation_system, features_and_amenities, official_website, facts, address_as_text, address_main, side_address, address_virtual,
postcode, latitude, longitude, complex_name, complex_type, lot_number, block_number, zone_name, district_1st_level, district_2nd_level,
city_name, metro_area_name, state_name, state_code, country_name, continent_name, height_tip_ft, height_architectural_ft, height_estimated_ft,
height_roof_ft, height_main_roof_ft, height_top_floor_ft, height_obs__deck_ft, height_floor_floor_ft, height_floor_ceiling_ft, length_ft,
width_ft, floors_overground, floors_underground, year_construction_start, year_construction_end, year_last_reconstruction, year_destruction,
gross_floor_area_gfa_ft2, usable_floor_area_ufa_ft2, volume_ft3, elevators, escalators, workplaces, parking_places, units, construction_costs)
from 'All_Buildings_Jan_4_2015.csv' DELIMITER ','
NULL AS ''
CSV HEADER;

alter table emporis_buildings ADD COLUMN geom geometry(Point, 4326);

update emporis_buildings set geom = st_setsrid(st_makepoint(longitude::double precision, latitude::double precision), 4326)
where latitude != '';

update emporis_buildings set building_number_ebn=null where building_number_ebn='';
update emporis_buildings set building_number_bin=null where building_number_bin='';
update emporis_buildings set official_name=null where official_name='';
update emporis_buildings set alternative_name=null where alternative_name='';
update emporis_buildings set construction_type=null where construction_type='';
update emporis_buildings set current_status=null where current_status='';
update emporis_buildings set architectural_style=null where architectural_style='';
update emporis_buildings set main_usages=null where main_usages='';
update emporis_buildings set side_usages=null where side_usages='';
update emporis_buildings set facade_system=null where facade_system='';
update emporis_buildings set facade_material=null where facade_material='';
update emporis_buildings set facade_color=null where facade_color='';
update emporis_buildings set structural_system=null where structural_system='';
update emporis_buildings set structural_material=null where structural_material='';
update emporis_buildings set foundation_system=null where foundation_system='';
update emporis_buildings set features_and_amenities=null where features_and_amenities='';
update emporis_buildings set official_website=null where official_website='';
update emporis_buildings set facts=null where facts='';
update emporis_buildings set address_as_text=null where address_as_text='';
update emporis_buildings set address_main=null where address_main='';
update emporis_buildings set side_address=null where side_address='';
update emporis_buildings set address_virtual=null where address_virtual='';
update emporis_buildings set postcode=null where postcode='';
update emporis_buildings set latitude=null where latitude='';
update emporis_buildings set longitude=null where longitude='';
update emporis_buildings set complex_name=null where complex_name='';
update emporis_buildings set complex_type=null where complex_type='';
update emporis_buildings set lot_number=null where lot_number='';
update emporis_buildings set block_number=null where block_number='';
update emporis_buildings set zone_name=null where zone_name='';
update emporis_buildings set district_1st_level=null where district_1st_level='';
update emporis_buildings set district_2nd_level=null where district_2nd_level='';
update emporis_buildings set city_name=null where city_name='';
update emporis_buildings set metro_area_name=null where metro_area_name='';
update emporis_buildings set state_name=null where state_name='';
update emporis_buildings set state_code=null where state_code='';
update emporis_buildings set country_name=null where country_name='';
update emporis_buildings set continent_name=null where continent_name='';
update emporis_buildings set height_tip_ft=null where height_tip_ft='';
update emporis_buildings set height_architectural_ft=null where height_architectural_ft='';
update emporis_buildings set height_estimated_ft=null where height_estimated_ft='';
update emporis_buildings set height_roof_ft=null where height_roof_ft='';
update emporis_buildings set height_main_roof_ft=null where height_main_roof_ft='';
update emporis_buildings set height_top_floor_ft=null where height_top_floor_ft='';
update emporis_buildings set height_obs__deck_ft=null where height_obs__deck_ft='';
update emporis_buildings set height_floor_floor_ft=null where height_floor_floor_ft='';
update emporis_buildings set height_floor_ceiling_ft=null where height_floor_ceiling_ft='';
update emporis_buildings set length_ft=null where length_ft='';
update emporis_buildings set width_ft=null where width_ft='';
update emporis_buildings set floors_overground=null where floors_overground='';
update emporis_buildings set floors_underground=null where floors_underground='';
update emporis_buildings set year_construction_start=null where year_construction_start='';
update emporis_buildings set year_construction_end=null where year_construction_end='';
update emporis_buildings set year_last_reconstruction=null where year_last_reconstruction='';
update emporis_buildings set year_destruction=null where year_destruction='';
update emporis_buildings set gross_floor_area_gfa_ft2=null where gross_floor_area_gfa_ft2='';
update emporis_buildings set usable_floor_area_ufa_ft2=null where usable_floor_area_ufa_ft2='';
update emporis_buildings set volume_ft3=null where volume_ft3='';
update emporis_buildings set elevators=null where elevators='';
update emporis_buildings set escalators=null where escalators='';
update emporis_buildings set workplaces=null where workplaces='';
update emporis_buildings set parking_places=null where parking_places='';
update emporis_buildings set units=null where units='';
update emporis_buildings set construction_costs=null where construction_costs='';


alter table emporis_buildings alter column building_number_ebn type integer using (building_number_ebn::integer);
alter table emporis_buildings alter column longitude type double precision using (longitude::double precision);
alter table emporis_buildings alter column latitude type double precision using (latitude::double precision);
alter table emporis_buildings alter column floors_underground type double precision using (floors_underground::double precision);
alter table emporis_buildings alter column usable_floor_area_ufa_ft2 type integer using (usable_floor_area_ufa_ft2::integer);
alter table emporis_buildings alter column block_number type integer using (block_number::integer);
alter table emporis_buildings alter column year_last_reconstruction type integer using (year_last_reconstruction::integer);
alter table emporis_buildings alter column building_number_bin type integer using (building_number_bin::integer);
alter table emporis_buildings alter column volume_ft3 type integer using (volume_ft3::integer);
alter table emporis_buildings alter column year_destruction type integer using (year_destruction::integer);
alter table emporis_buildings alter column workplaces type integer using (workplaces::integer);
alter table emporis_buildings alter column elevators type integer using (elevators::integer);
alter table emporis_buildings alter column lot_number type integer using (lot_number::integer);
alter table emporis_buildings alter column year_construction_start type integer using (year_construction_start::integer);
alter table emporis_buildings alter column units type integer using (units::integer);
alter table emporis_buildings alter column year_construction_end type integer using (year_construction_end::integer);
alter table emporis_buildings alter column escalators type integer using (escalators::integer);
alter table emporis_buildings alter column parking_places type integer using (parking_places::integer);
alter table emporis_buildings alter column construction_costs type bigint using (construction_costs::bigint);
alter table emporis_buildings alter column floors_overground type double precision using (floors_overground::double precision);
alter table emporis_buildings alter column height_obs__deck_ft type double precision using (height_obs__deck_ft::double precision);
alter table emporis_buildings alter column height_main_roof_ft type double precision using (height_main_roof_ft::double precision);
alter table emporis_buildings alter column height_estimated_ft type double precision using (height_estimated_ft::double precision);
alter table emporis_buildings alter column height_floor_floor_ft type double precision using (height_floor_floor_ft::double precision);
alter table emporis_buildings alter column height_tip_ft type double precision using (height_tip_ft::double precision);
alter table emporis_buildings alter column height_architectural_ft type double precision using (height_architectural_ft::double precision);
alter table emporis_buildings alter column gross_floor_area_gfa_ft2 type double precision using (gross_floor_area_gfa_ft2::double precision);
alter table emporis_buildings alter column width_ft type double precision using (width_ft::double precision);
alter table emporis_buildings alter column official_name type char(100);
alter table emporis_buildings alter column alternative_name type char(200);
alter table emporis_buildings alter column construction_type type char(50);
alter table emporis_buildings alter column current_status type char(50);
alter table emporis_buildings alter column architectural_style type char(50);
alter table emporis_buildings alter column main_usages type char(200);
alter table emporis_buildings alter column height_roof_ft type double precision using (height_roof_ft::double precision);
alter table emporis_buildings alter column length_ft type double precision using (length_ft::double precision);
alter table emporis_buildings alter column height_top_floor_ft type double precision using (height_top_floor_ft::double precision);
alter table emporis_buildings alter column height_floor_ceiling_ft type double precision using (height_floor_ceiling_ft::double precision);
alter table emporis_buildings alter column facade_system type char(75);
alter table emporis_buildings alter column official_website type char(200);
alter table emporis_buildings alter column facade_color type char(150);
alter table emporis_buildings alter column address_as_text type char(150);
alter table emporis_buildings alter column postcode type char(50);
alter table emporis_buildings alter column complex_type type char(50);
alter table emporis_buildings alter column continent_name type char(25);
alter table emporis_buildings alter column country_name type char(25);
alter table emporis_buildings alter column structural_system type char(50);
alter table emporis_buildings alter column address_main type char(200);
alter table emporis_buildings alter column zone_name type char(75);
alter table emporis_buildings alter column architectural_style type char(50);
alter table emporis_buildings alter column foundation_system type char(50);
alter table emporis_buildings alter column side_usages type char(175);
alter table emporis_buildings alter column complex_name type char(100);
alter table emporis_buildings alter column side_address type char(200);
alter table emporis_buildings alter column metro_area_name type char(75);
alter table emporis_buildings alter column city_name type char(50);
alter table emporis_buildings alter column current_status type char(50);
alter table emporis_buildings alter column district_1st_level type char(75);
alter table emporis_buildings alter column state_name type char(50);
alter table emporis_buildings alter column address_virtual type char(255);
alter table emporis_buildings alter column district_2nd_level type char(50);
alter table emporis_buildings alter column main_usages type char(200);
alter table emporis_buildings alter column structural_material type char(50);
alter table emporis_buildings alter column construction_type type char(50);
alter table emporis_buildings alter column alternative_name type char(200);
alter table emporis_buildings alter column state_code type char(10);
