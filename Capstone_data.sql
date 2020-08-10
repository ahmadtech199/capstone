--
-- PostgreSQL database dump
--

-- Dumped from database version 12.2
-- Dumped by pg_dump version 12.2

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

SET default_with_oids = false;

--
-- Name: actor; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.actor (
    id integer NOT NULL,
    name character varying(20) NOT NULL,
    age integer NOT NULL,
    gender character varying(10) NOT NULL
);


ALTER TABLE public.actor OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.actor_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.actor_id_seq OWNER TO postgres;

--
-- Name: actor_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.actor_id_seq OWNED BY public.actor.id;


--
-- Name: movie; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.movie (
    id integer NOT NULL,
    title character varying(20) NOT NULL,
    "releaseDate" timestamp without time zone NOT NULL,
    actor_id integer
);


ALTER TABLE public.movie OWNER TO postgres;

--
-- Name: movie_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.movie_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.movie_id_seq OWNER TO postgres;

--
-- Name: movie_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.movie_id_seq OWNED BY public.movie.id;


--
-- Name: actor id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor ALTER COLUMN id SET DEFAULT nextval('public.actor_id_seq'::regclass);


--
-- Name: movie id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie ALTER COLUMN id SET DEFAULT nextval('public.movie_id_seq'::regclass);


--
-- Data for Name: actor; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.actor (id, name, age, gender) FROM stdin;
1	jordi	40	male
2	Yidah	39	female
5	pepe Gotera	45	male
8	pepe Gotera	45	male
7	Otilio	54	male
9	pepe Gotera	45	male
4	Otilio	54	male
10	pepe Gotera	45	male
11	pepe Gotera	45	male
\.


--
-- Data for Name: movie; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.movie (id, title, "releaseDate", actor_id) FROM stdin;
1	Por amor	2020-03-25 11:55:11.271041	2
2	Por amor	2020-03-25 11:55:11.271041	1
4	Lucha	2020-03-25 11:55:11.271041	1
6	random title	2020-05-17 00:00:00	1
5	avengers vs godzilla	2021-03-25 11:55:11.271041	1
9	random title	2020-05-17 00:00:00	4
10	random title	2020-05-17 00:00:00	4
11	random title	2020-05-17 00:00:00	1
12	random title	2020-05-17 00:00:00	2
13	random title	2020-05-17 00:00:00	4
8	avengers vs godzilla	2021-03-25 11:55:11.271041	4
14	random title	2020-05-17 00:00:00	1
15	random title	2020-05-17 00:00:00	2
16	random title	2020-05-17 00:00:00	4
\.


--
-- Name: actor_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.actor_id_seq', 11, true);


--
-- Name: movie_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.movie_id_seq', 16, true);


--
-- Name: actor actor_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.actor
    ADD CONSTRAINT actor_pkey PRIMARY KEY (id);


--
-- Name: movie movie_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);


--
-- Name: movie movie_actor_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_actor_id_fkey FOREIGN KEY (actor_id) REFERENCES public.actor(id);


--
-- PostgreSQL database dump complete
--
