-- ============================================
-- MEDIA DELIVERY OPERATIONS DATABASE SCHEMA
-- ============================================

CREATE TABLE partners (
    partner_id INT PRIMARY KEY,
    partner_name VARCHAR(100),
    region VARCHAR(50)
);

CREATE TABLE project_media (
    content_id INT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(50),
    format VARCHAR(20)
);

CREATE TABLE artwork (
    asset_id INT PRIMARY KEY,
    content_id INT,
    format VARCHAR(20),
    created_date DATE,
    FOREIGN KEY (content_id) REFERENCES project_media(content_id)
);

CREATE TABLE delivery_logs (
    delivery_id INT PRIMARY KEY,
    partner_id INT,
    asset_id INT,
    delivery_date DATE,
    actual_hours FLOAT,
    sla_hours FLOAT,
    approved_flag BOOLEAN,
    status VARCHAR(30),

    FOREIGN KEY (partner_id) REFERENCES partners(partner_id),
    FOREIGN KEY (asset_id) REFERENCES artwork(asset_id)
);

CREATE TABLE error_logs (
    error_id INT PRIMARY KEY,
    delivery_id INT,
    error_type VARCHAR(50),
    severity VARCHAR(20),

    FOREIGN KEY (delivery_id) REFERENCES delivery_logs(delivery_id)
);
