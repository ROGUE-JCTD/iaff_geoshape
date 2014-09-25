--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: firestations; Type: TABLE; Schema: public; Owner: geonode; Tablespace: 
--

CREATE TABLE firestations (
    ogc_fid integer NOT NULL,
    wkb_geometry geometry(Point,4326),
    objectid integer,
    code integer,
    name character varying,
    symbol character varying,
    seniorcenter integer,
    address character varying
);


ALTER TABLE public.firestations OWNER TO geonode;

--
-- Name: firestations_ogc_fid_seq; Type: SEQUENCE; Schema: public; Owner: geonode
--

CREATE SEQUENCE firestations_ogc_fid_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.firestations_ogc_fid_seq OWNER TO geonode;

--
-- Name: firestations_ogc_fid_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: geonode
--

ALTER SEQUENCE firestations_ogc_fid_seq OWNED BY firestations.ogc_fid;


--
-- Name: ogc_fid; Type: DEFAULT; Schema: public; Owner: geonode
--

ALTER TABLE ONLY firestations ALTER COLUMN ogc_fid SET DEFAULT nextval('firestations_ogc_fid_seq'::regclass);


--
-- Data for Name: firestations; Type: TABLE DATA; Schema: public; Owner: geonode
--

COPY firestations (ogc_fid, wkb_geometry, objectid, code, name, symbol, seniorcenter, address) FROM stdin;
1	0101000020E61000007B5EA6EB864A53C08EF3D75995714340	79	1	Fire Station 6	FS	0	6950 LITTLE FALLS RD
2	0101000020E6100000D36D6C99224853C0F27A68FBC5724340	80	1	Fire Station 8	FS	0	4845 LEE HWY
3	0101000020E61000006025A813E74453C0D1A9C58784724340	81	1	Fire Station 10	FS	0	1599 WILSON BLVD
4	0101000020E6100000C50C5962AD4753C0DC207B1E78704340	82	1	Fire Station 2	FS	0	4805 WILSON BLVD
5	0101000020E610000010801C3B284653C0CC049D253C714340	83	1	Fire Station 4 & HDQTRS	FS	0	3121 N 10TH ST
6	0101000020E61000005F22DA58224653C0712F6343F46E4340	84	1	Fire Station 1	FS	0	500 S GLEBE RD
7	0101000020E61000000918E1E1DF4553C082DD8A82026D4340	85	1	Fire Station 9	FS	0	1900 S WALTER REED DR
8	0101000020E6100000A4D242F9B84353C02AC89474C16D4340	86	1	Fire Station 5	FS	0	1750 S HAYES ST
9	0101000020E61000001023D3FE1E4653C0D914D32E186B4340	87	1	Fire Station #7	FS	0	3116 S ABINGDON ST
10	0101000020E61000008F799EBE0B4753C0C1BA6766E5724340	112	1	Fire Station 3	FS	0	4100 OLD DOMINION DR
\.


--
-- Name: firestations_ogc_fid_seq; Type: SEQUENCE SET; Schema: public; Owner: geonode
--

SELECT pg_catalog.setval('firestations_ogc_fid_seq', 10, true);


--
-- Name: firestations_pk; Type: CONSTRAINT; Schema: public; Owner: geonode; Tablespace: 
--

ALTER TABLE ONLY firestations
    ADD CONSTRAINT firestations_pk PRIMARY KEY (ogc_fid);


--
-- Name: firestations_geom_idx; Type: INDEX; Schema: public; Owner: geonode; Tablespace: 
--

CREATE INDEX firestations_geom_idx ON firestations USING gist (wkb_geometry);


--
-- PostgreSQL database dump complete
--

