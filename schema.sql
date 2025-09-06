DROP TABLE IF EXISTS user;

CREATE TABLE settelments (
    LocNameHeb TEXT NOT NULL UNIQUE,
    pop_approx INT NOT NULL,
    ReligionHeb TEXT NOT NULL,
    hh_MidatDatiyut TEXT NOT NULL
);
