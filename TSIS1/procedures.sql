-- ============================================================
-- TSIS1: new stored procedures / functions (3.4)
-- Does NOT duplicate upsert_contact / insert_many_contacts / delete_contact_by
-- or get_contacts_by_pattern / get_contacts_paginated from Practice 8.
-- ============================================================

-- Helper is inlined in each routine: resolve a contact by "first_name"
-- or "first_name last_name" (both are accepted as p_contact_name).

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
       OR (first_name || ' ' || COALESCE(last_name, '')) = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Контакт "%" не найден.', p_contact_name;
        RETURN;
    END IF;

    IF p_type NOT IN ('home', 'work', 'mobile') THEN
        RAISE NOTICE 'Некорректный тип телефона: "%". Допустимо: home / work / mobile.', p_type;
        RETURN;
    END IF;

    INSERT INTO phones (contact_id, phone, type)
    VALUES (v_contact_id, p_phone, p_type);

    RAISE NOTICE 'Телефон % (%) добавлен контакту "%".', p_phone, p_type, p_contact_name;
END;
$$;


CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
    v_group_id   INT;
BEGIN
    SELECT id INTO v_contact_id
    FROM contacts
    WHERE first_name = p_contact_name
       OR (first_name || ' ' || COALESCE(last_name, '')) = p_contact_name
    LIMIT 1;

    IF v_contact_id IS NULL THEN
        RAISE NOTICE 'Контакт "%" не найден.', p_contact_name;
        RETURN;
    END IF;

    SELECT id INTO v_group_id FROM groups WHERE name = p_group_name;

    IF v_group_id IS NULL THEN
        INSERT INTO groups (name) VALUES (p_group_name)
        RETURNING id INTO v_group_id;
        RAISE NOTICE 'Группа "%" не существовала — создана.', p_group_name;
    END IF;

    UPDATE contacts SET group_id = v_group_id WHERE id = v_contact_id;

    RAISE NOTICE 'Контакт "%" перемещён в группу "%".', p_contact_name, p_group_name;
END;
$$;


-- Extends Practice 8's get_contacts_by_pattern: also matches email and
-- ALL phones of a contact from the new phones table (1-to-many).
CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE (
    id         INT,
    first_name VARCHAR,
    last_name  VARCHAR,
    email      VARCHAR,
    group_name VARCHAR,
    phone      VARCHAR,
    phone_type VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT
        c.id, c.first_name, c.last_name, c.email, g.name AS group_name,
        p.phone, p.type
    FROM contacts c
    LEFT JOIN groups g ON g.id = c.group_id
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.first_name ILIKE '%' || p_query || '%'
       OR c.last_name  ILIKE '%' || p_query || '%'
       OR c.email      ILIKE '%' || p_query || '%'
       OR c.phone      ILIKE '%' || p_query || '%'
       OR EXISTS (
            SELECT 1 FROM phones p2
            WHERE p2.contact_id = c.id AND p2.phone ILIKE '%' || p_query || '%'
       )
    ORDER BY c.id;
END;
$$ LANGUAGE plpgsql;
