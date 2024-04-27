CREATE OR REPLACE PROCEDURE insert_user(
    p_name VARCHAR(255),
    p_surname VARCHAR(255),
    p_phone VARCHAR(20)
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO phone_number (name, surname, number_value)
    VALUES (p_name, p_surname, p_phone);
END;
$$;
