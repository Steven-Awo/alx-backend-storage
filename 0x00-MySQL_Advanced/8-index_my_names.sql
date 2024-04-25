-- Task 8: This  creates an index to idx_name_first
-- on the table with names and also the first
-- letter of name
CREATE INDEX idx_name_first ON names ( name(1) );
