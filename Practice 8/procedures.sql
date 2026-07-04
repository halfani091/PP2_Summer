
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE phone = p_phone) THEN
        UPDATE contacts
        SET first_name = p_first_name,
            last_name  = p_last_name
        WHERE phone = p_phone;
    ELSE
        INSERT INTO contacts(first_name, last_name, phone)
        VALUES (p_first_name, p_last_name, p_phone);
    END IF;
END;
$$;


CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_first_names VARCHAR[],
    p_last_names  VARCHAR[],
    p_phones      VARCHAR[]
)
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
    bad_rows TEXT := '';
BEGIN
    FOR i IN 1 .. array_length(p_first_names, 1) LOOP
        IF p_phones[i] ~ '^\+?[0-9]{7,15}$' THEN
            CALL upsert_contact(p_first_names[i], p_last_names[i], p_phones[i]);
        ELSE
            bad_rows := bad_rows || format('[%s %s -> %s] ', p_first_names[i], p_last_names[i], p_phones[i]);
        END IF;
    END LOOP;

    IF bad_rows <> '' THEN
        RAISE NOTICE 'Некорректные записи (не добавлены): %', bad_rows;
    ELSE
        RAISE NOTICE 'Все записи добавлены успешно.';
    END IF;
END;
$$;




CREATE OR REPLACE PROCEDURE delete_contact_by(p_identifier VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE first_name = p_identifier OR phone = p_identifier;

    IF NOT FOUND THEN
        RAISE NOTICE 'Контакт "%": ничего не удалено (не найден).', p_identifier;
    END IF;
END;
$$;