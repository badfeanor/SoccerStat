--
-- PostgreSQL database dump
--

-- Dumped from database version 11.8
-- Dumped by pg_dump version 11.2

-- Started on 2020-08-30 22:20:17

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 8 (class 2615 OID 16456)
-- Name: england; Type: SCHEMA; Schema: -; Owner: soccer
--

CREATE SCHEMA england;


ALTER SCHEMA england OWNER TO soccer;

--
-- TOC entry 11 (class 2615 OID 16459)
-- Name: germany; Type: SCHEMA; Schema: -; Owner: soccer
--

CREATE SCHEMA germany;


ALTER SCHEMA germany OWNER TO soccer;

--
-- TOC entry 10 (class 2615 OID 16458)
-- Name: italy; Type: SCHEMA; Schema: -; Owner: soccer
--

CREATE SCHEMA italy;


ALTER SCHEMA italy OWNER TO soccer;

--
-- TOC entry 12 (class 2615 OID 16520)
-- Name: metadata; Type: SCHEMA; Schema: -; Owner: soccer
--

CREATE SCHEMA metadata;


ALTER SCHEMA metadata OWNER TO soccer;

--
-- TOC entry 9 (class 2615 OID 16457)
-- Name: spain; Type: SCHEMA; Schema: -; Owner: soccer
--

CREATE SCHEMA spain;


ALTER SCHEMA spain OWNER TO soccer;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 205 (class 1259 OID 16460)
-- Name: champ_stat; Type: TABLE; Schema: england; Owner: soccer
--

CREATE TABLE england.champ_stat (
    place smallint,
    team character varying(30),
    played smallint,
    win smallint,
    draw smallint,
    loss smallint,
    goals_for smallint,
    goals_against smallint,
    points smallint,
    team_id character varying(100)
);


ALTER TABLE england.champ_stat OWNER TO soccer;

--
-- TOC entry 210 (class 1259 OID 17067)
-- Name: players; Type: TABLE; Schema: england; Owner: soccer
--

CREATE TABLE england.players (
    number smallint,
    name character varying(30),
    team character varying(30),
    played smallint,
    min smallint,
    bz smallint,
    vnz smallint,
    goals smallint,
    pen smallint,
    p smallint,
    gp smallint,
    yc smallint,
    rc smallint
);


ALTER TABLE england.players OWNER TO soccer;

--
-- TOC entry 214 (class 1259 OID 24648)
-- Name: teams; Type: TABLE; Schema: england; Owner: soccer
--

CREATE TABLE england.teams (
    team_id character varying(30) NOT NULL,
    cyrillic_name character varying(200)
);


ALTER TABLE england.teams OWNER TO soccer;

--
-- TOC entry 207 (class 1259 OID 16466)
-- Name: champ_stat; Type: TABLE; Schema: germany; Owner: soccer
--

CREATE TABLE germany.champ_stat (
    place smallint,
    team character varying(30),
    played smallint,
    win smallint,
    draw smallint,
    loss smallint,
    goals_for smallint,
    goals_against smallint,
    points smallint,
    team_id character varying(100)
);


ALTER TABLE germany.champ_stat OWNER TO soccer;

--
-- TOC entry 212 (class 1259 OID 17111)
-- Name: players; Type: TABLE; Schema: germany; Owner: soccer
--

CREATE TABLE germany.players (
    number smallint,
    name character varying(30),
    team character varying(30),
    played smallint,
    min smallint,
    bz smallint,
    vnz smallint,
    goals smallint,
    pen smallint,
    p smallint,
    gp smallint,
    yc smallint,
    rc smallint
);


ALTER TABLE germany.players OWNER TO soccer;

--
-- TOC entry 216 (class 1259 OID 24672)
-- Name: teams; Type: TABLE; Schema: germany; Owner: soccer
--

CREATE TABLE germany.teams (
    team_id character varying(30) NOT NULL,
    cyrillic_name character varying(200)
);


ALTER TABLE germany.teams OWNER TO soccer;

--
-- TOC entry 208 (class 1259 OID 16469)
-- Name: champ_stat; Type: TABLE; Schema: italy; Owner: soccer
--

CREATE TABLE italy.champ_stat (
    place smallint,
    team character varying(30),
    played smallint,
    win smallint,
    draw smallint,
    loss smallint,
    goals_for smallint,
    goals_against smallint,
    points smallint,
    team_id character varying(100)
);


ALTER TABLE italy.champ_stat OWNER TO soccer;

--
-- TOC entry 211 (class 1259 OID 17089)
-- Name: players; Type: TABLE; Schema: italy; Owner: soccer
--

CREATE TABLE italy.players (
    number smallint,
    name character varying(30),
    team character varying(30),
    played smallint,
    min smallint,
    bz smallint,
    vnz smallint,
    goals smallint,
    pen smallint,
    p smallint,
    gp smallint,
    yc smallint,
    rc smallint
);


ALTER TABLE italy.players OWNER TO soccer;

--
-- TOC entry 217 (class 1259 OID 24677)
-- Name: teams; Type: TABLE; Schema: italy; Owner: soccer
--

CREATE TABLE italy.teams (
    team_id character varying(30) NOT NULL,
    cyrillic_name character varying(200)
);


ALTER TABLE italy.teams OWNER TO soccer;

--
-- TOC entry 209 (class 1259 OID 16521)
-- Name: parser_info; Type: TABLE; Schema: metadata; Owner: soccer
--

CREATE TABLE metadata.parser_info (
    champ character varying(30) NOT NULL,
    info json NOT NULL
);


ALTER TABLE metadata.parser_info OWNER TO soccer;

--
-- TOC entry 206 (class 1259 OID 16463)
-- Name: champ_stat; Type: TABLE; Schema: spain; Owner: soccer
--

CREATE TABLE spain.champ_stat (
    place smallint,
    team character varying(30),
    played smallint,
    win smallint,
    draw smallint,
    loss smallint,
    goals_for smallint,
    goals_against smallint,
    points smallint,
    team_id character varying(100)
);


ALTER TABLE spain.champ_stat OWNER TO soccer;

--
-- TOC entry 213 (class 1259 OID 17131)
-- Name: players; Type: TABLE; Schema: spain; Owner: soccer
--

CREATE TABLE spain.players (
    number smallint,
    name character varying(30),
    team character varying(30),
    played smallint,
    min smallint,
    bz smallint,
    vnz smallint,
    goals smallint,
    pen smallint,
    p smallint,
    gp smallint,
    yc smallint,
    rc smallint
);


ALTER TABLE spain.players OWNER TO soccer;

--
-- TOC entry 215 (class 1259 OID 24667)
-- Name: teams; Type: TABLE; Schema: spain; Owner: soccer
--

CREATE TABLE spain.teams (
    team_id character varying(30) NOT NULL,
    cyrillic_name character varying(200)
);


ALTER TABLE spain.teams OWNER TO soccer;


--
-- TOC entry 2907 (class 2606 OID 24707)
-- Name: teams team_pk; Type: CONSTRAINT; Schema: england; Owner: soccer
--

ALTER TABLE ONLY england.teams
    ADD CONSTRAINT team_pk PRIMARY KEY (team_id);


--
-- TOC entry 2911 (class 2606 OID 24719)
-- Name: teams team_pk; Type: CONSTRAINT; Schema: germany; Owner: soccer
--

ALTER TABLE ONLY germany.teams
    ADD CONSTRAINT team_pk PRIMARY KEY (team_id);


--
-- TOC entry 2913 (class 2606 OID 24725)
-- Name: teams team_pk; Type: CONSTRAINT; Schema: italy; Owner: soccer
--

ALTER TABLE ONLY italy.teams
    ADD CONSTRAINT team_pk PRIMARY KEY (team_id);


--
-- TOC entry 2909 (class 2606 OID 24713)
-- Name: teams team_pk; Type: CONSTRAINT; Schema: spain; Owner: soccer
--

ALTER TABLE ONLY spain.teams
    ADD CONSTRAINT team_pk PRIMARY KEY (team_id);


--
-- TOC entry 2914 (class 2606 OID 24769)
-- Name: champ_stat champ_stat_team_id_fkey; Type: FK CONSTRAINT; Schema: england; Owner: soccer
--

ALTER TABLE ONLY england.champ_stat
    ADD CONSTRAINT champ_stat_team_id_fkey FOREIGN KEY (team_id) REFERENCES england.teams(team_id);


--
-- TOC entry 2918 (class 2606 OID 24730)
-- Name: players players_team_fkey; Type: FK CONSTRAINT; Schema: england; Owner: soccer
--

ALTER TABLE ONLY england.players
    ADD CONSTRAINT players_team_fkey FOREIGN KEY (team) REFERENCES england.teams(team_id);


--
-- TOC entry 2916 (class 2606 OID 24784)
-- Name: champ_stat champ_stat_team_id_fkey; Type: FK CONSTRAINT; Schema: germany; Owner: soccer
--

ALTER TABLE ONLY germany.champ_stat
    ADD CONSTRAINT champ_stat_team_id_fkey FOREIGN KEY (team_id) REFERENCES germany.teams(team_id);


--
-- TOC entry 2920 (class 2606 OID 24745)
-- Name: players players_team_fkey; Type: FK CONSTRAINT; Schema: germany; Owner: soccer
--

ALTER TABLE ONLY germany.players
    ADD CONSTRAINT players_team_fkey FOREIGN KEY (team) REFERENCES germany.teams(team_id);


--
-- TOC entry 2917 (class 2606 OID 24779)
-- Name: champ_stat champ_stat_team_id_fkey; Type: FK CONSTRAINT; Schema: italy; Owner: soccer
--

ALTER TABLE ONLY italy.champ_stat
    ADD CONSTRAINT champ_stat_team_id_fkey FOREIGN KEY (team_id) REFERENCES italy.teams(team_id);


--
-- TOC entry 2919 (class 2606 OID 24740)
-- Name: players players_team_fkey; Type: FK CONSTRAINT; Schema: italy; Owner: soccer
--

ALTER TABLE ONLY italy.players
    ADD CONSTRAINT players_team_fkey FOREIGN KEY (team) REFERENCES italy.teams(team_id);


--
-- TOC entry 2915 (class 2606 OID 24774)
-- Name: champ_stat champ_stat_team_id_fkey; Type: FK CONSTRAINT; Schema: spain; Owner: soccer
--

ALTER TABLE ONLY spain.champ_stat
    ADD CONSTRAINT champ_stat_team_id_fkey FOREIGN KEY (team_id) REFERENCES spain.teams(team_id);


--
-- TOC entry 2921 (class 2606 OID 24735)
-- Name: players players_team_fkey; Type: FK CONSTRAINT; Schema: spain; Owner: soccer
--

ALTER TABLE ONLY spain.players
    ADD CONSTRAINT players_team_fkey FOREIGN KEY (team) REFERENCES spain.teams(team_id);


-- Completed on 2020-08-30 22:20:35

--
-- PostgreSQL database dump complete
--

