-- Task 2: ranking the country's origins of bands,
-- in ordered by its number of its (non-unique) fans
SELECT DISTINCT `origin`, SUM(`fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
