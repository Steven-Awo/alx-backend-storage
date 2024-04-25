-- Task 4: We create a trigger that helps decreases the quantity
-- of any of the item after just adding a new order
CREATE TRIGGER order_decrease BEFORE INSERT ON orders
FOR EACH ROW UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name;
