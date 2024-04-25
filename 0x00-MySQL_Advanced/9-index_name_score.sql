-- Task 9: This creates an index called idx_name_first_score on
-- the table names and then the first letter of the  name and
-- also the score
CREATE INDEX idx_name_first_score ON names ( name(1), score );
