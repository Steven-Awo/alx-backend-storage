-- a SQL script that hels the lists of all bands with Glam rock
-- as their main style thats ranked by their own longevity
SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET("Glam rock", style)
ORDER BY lifespan DESC;
