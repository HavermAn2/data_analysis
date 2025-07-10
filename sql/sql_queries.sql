COPY gdp_data(
    country,
    gdp_2005, gdp_2006, gdp_2007, gdp_2008, gdp_2009,
    gdp_2010, gdp_2011, gdp_2012, gdp_2013, gdp_2014,
    gdp_2015, gdp_2016, gdp_2017, gdp_2018, gdp_2019,
    gdp_2020, gdp_2021, gdp_2022
)
FROM 'D:/Data_analyse/data_analysis/data/clean_gdp.csv'
DELIMITER ','
CSV HEADER;
