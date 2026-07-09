-- ============================================================
-- TSIS1: PhoneBook — Extended Contact Management
-- Schema extension on top of Practice 7/8 "contacts" table.
-- Safe to run multiple times (IF NOT EXISTS / ADD COLUMN IF NOT EXISTS).
-- ============================================================

-- Base table, kept for backward compatibility with Practice 7/8 logic.
CREATE TABLE IF NOT EXISTS contacts (
    id         SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50),
    phone      VARCHAR(20) NOT NULL UNIQUE
);

-- 3.1 Contact group / category
CREATE TABLE IF NOT EXISTS groups (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

INSERT INTO groups (name)
VALUES ('Family'), ('Work'), ('Friend'), ('Other')
ON CONFLICT (name) DO NOTHING;

-- 3.1 Extended contact fields: email, birthday, group, created_at (for sorting by "date added")
ALTER TABLE contacts ADD COLUMN IF NOT EXISTS email      VARCHAR(100);
ALTER TABLE contacts ADD COLUMN IF NOT EXISTS birthday   DATE;
ALTER TABLE contacts ADD COLUMN IF NOT EXISTS group_id   INTEGER REFERENCES groups(id);
ALTER TABLE contacts ADD COLUMN IF NOT EXISTS created_at TIMESTAMP NOT NULL DEFAULT now();

-- 3.1 Multiple phone numbers per contact (1-to-many)
CREATE TABLE IF NOT EXISTS phones (
    id         SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone      VARCHAR(20)  NOT NULL,
    type       VARCHAR(10)  CHECK (type IN ('home', 'work', 'mobile'))
);

CREATE INDEX IF NOT EXISTS idx_phones_contact_id ON phones(contact_id);
CREATE INDEX IF NOT EXISTS idx_contacts_email    ON contacts(email);
CREATE INDEX IF NOT EXISTS idx_contacts_group_id ON contacts(group_id);
