-- TABLE 1: Хувийн мэдээлэл
CREATE TABLE IF NOT EXISTS huviin_medeelel (
    employee_id      SERIAL PRIMARY KEY,
    ner              VARCHAR(100),
    ovog             VARCHAR(100),
    nas              INTEGER,
    huis             VARCHAR(20),
    utas             VARCHAR(50),
    email            VARCHAR(150),
    haig             VARCHAR(200),
    bolovsrol        VARCHAR(50),
    alban_tushaal    VARCHAR(100),
    heltes           VARCHAR(100),
    elessen_ognoo    DATE,
    ajliin_jil       INTEGER,
    tuluv            VARCHAR(50)
);

-- TABLE 2: Ажлын мэдээлэл
CREATE TABLE IF NOT EXISTS ajliin_medeelel (
    id                      SERIAL PRIMARY KEY,
    employee_id             INTEGER REFERENCES huviin_medeelel(employee_id),
    undsen_tsalin           NUMERIC,
    ajillah_ystoi_tsag      INTEGER,
    ajilsan_tsag            INTEGER,
    iluu_tsag               INTEGER,
    dutuu_tsag              INTEGER,
    tsagiin_unelgee         NUMERIC,
    iluu_tsagiin_tuluv      NUMERIC,
    guitsetgeliiin_unelgee  VARCHAR(5),
    bonus                   NUMERIC,
    niit_tsalin             NUMERIC,
    tatvar                  NUMERIC,
    ndsh                    NUMERIC,
    gart_avah_tsalin        NUMERIC,
    tsalin_ognoo            DATE,
    tuluv                   VARCHAR(50)
);