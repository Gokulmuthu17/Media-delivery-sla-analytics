-- =============================================
-- DELIVERY MASTER ANALYTICS VIEW
-- Combines deliveries, partners, content,
-- artwork metadata and KPI flags
-- =============================================

USE media_delivery_dw;

CREATE OR REPLACE VIEW delivery_master_view AS

SELECT
    -- ----------------------------
    -- Delivery Identifiers
    -- ----------------------------
    d.delivery_id,
    d.delivery_date,

    -- ----------------------------
    -- Partner Information
    -- ----------------------------
    d.partner_id,
    p.partner_name,
    p.region,

    -- ----------------------------
    -- Content Metadata
    -- ----------------------------
    d.content_id,
    c.title,
    c.genre,
    c.release_date,

    -- ----------------------------
    -- Artwork Metadata
    -- ----------------------------
    d.asset_id,
    a.format,
    a.resolution,
    a.approved_flag,

    -- ----------------------------
    -- SLA & Timing
    -- ----------------------------
    d.sla_hours,
    d.actual_hours,

    -- ----------------------------
    -- Delivery Status
    -- ----------------------------
    d.status,

    -- ----------------------------
    -- KPI FLAGS
    -- ----------------------------

    -- SLA breach indicator
    CASE
        WHEN d.actual_hours > d.sla_hours THEN 1
        ELSE 0
    END AS sla_breach_flag,

    -- Success indicator
    CASE
        WHEN UPPER(d.status) = 'SUCCESS' THEN 1
        ELSE 0
    END AS success_flag,

    -- Failure indicator
    CASE
        WHEN UPPER(d.status) = 'FAILED' THEN 1
        ELSE 0
    END AS failure_flag,

    -- Delivery delay amount
    (d.actual_hours - d.sla_hours) AS delay_hours

FROM project_media d

JOIN partners p
    ON d.partner_id = p.partner_id

JOIN content_master c
    ON d.content_id = c.content_id

JOIN artwork a
    ON d.asset_id = a.asset_id;
