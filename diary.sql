--
-- PostgreSQL database dump
--

-- Dumped from database version 12.1
-- Dumped by pg_dump version 12.1

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: events; Type: TABLE; Schema: public; Owner: eder
--

CREATE TABLE public.events (
    id integer NOT NULL,
    titre character varying(50) NOT NULL,
    date date NOT NULL,
    heure time without time zone NOT NULL,
    description character varying(250)
);


ALTER TABLE public.events OWNER TO eder;

--
-- Name: events_id_seq; Type: SEQUENCE; Schema: public; Owner: eder
--

CREATE SEQUENCE public.events_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.events_id_seq OWNER TO eder;

--
-- Name: events_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: eder
--

ALTER SEQUENCE public.events_id_seq OWNED BY public.events.id;


--
-- Name: events id; Type: DEFAULT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.events ALTER COLUMN id SET DEFAULT nextval('public.events_id_seq'::regclass);


--
-- Data for Name: events; Type: TABLE DATA; Schema: public; Owner: eder
--

COPY public.events (id, titre, date, heure, description) FROM stdin;
5	Angine	2020-03-09	09:20:00	verifier gorge
6	prise de sang	2020-04-02	09:30:00	rendez vous pour prise de sang
8	prescription	2020-03-03	08:30:00	prescription medicaments
10	rdv 1	2020-03-01	08:00:00	rendez vous 1
12	rdv3	2020-03-01	09:00:00	rdv3
13	rdv4	2020-03-01	09:30:00	rdv4
14	rdv5	2020-03-01	10:30:00	rdv5
11	rdv7	2020-03-01	08:30:00	rdv2
15	rdv10	2020-03-02	10:20:00	description jour 
16	rdvvvv6	2020-03-01	14:04:00	rdv 56
17	erffdg	2020-04-01	12:30:00	gvjhj:l
\.


--
-- Name: events_id_seq; Type: SEQUENCE SET; Schema: public; Owner: eder
--

SELECT pg_catalog.setval('public.events_id_seq', 17, true);


--
-- Name: events events_pkey; Type: CONSTRAINT; Schema: public; Owner: eder
--

ALTER TABLE ONLY public.events
    ADD CONSTRAINT events_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

