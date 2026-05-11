DROP TABLE IF EXISTS water_country;
CREATE TABLE water_country (
    country TEXT,
    year SMALLINT,
    population_thousands INTEGER,
    rural_available REAL,
    rural_contam_free REAL,
    urban_available REAL,
    urban_contam_free REAL,
    total_available REAL,
    total_contam_free REAL
);

DROP TABLE IF EXISTS water_region;
CREATE TABLE water_region (
    country TEXT,
    year SMALLINT,
    population_thousands INTEGER,
    rural_available REAL,
    rural_contam_free REAL,
    urban_available REAL,
    urban_contam_free REAL,
    total_available REAL,
    total_contam_free REAL
);