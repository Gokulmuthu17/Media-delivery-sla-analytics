-- ==============================
-- KPI METRICS
-- ==============================

-- Total Deliveries
SELECT COUNT(*) AS total_deliveries
FROM delivery_logs;

-- SLA Breach %
SELECT 
ROUND(
    100.0 * SUM(CASE WHEN actual_hours > sla_hours THEN 1 ELSE 0 END) 
    / COUNT(*),2
) AS sla_breach_rate
FROM delivery_logs;

-- Success Rate %
SELECT 
ROUND(
    100.0 * SUM(CASE WHEN status = 'SUCCESS' THEN 1 ELSE 0 END) 
    / COUNT(*),2
) AS success_rate
FROM delivery_logs;

-- Avg Delivery Hours
SELECT ROUND(AVG(actual_hours),2) AS avg_delivery_hours
FROM delivery_logs;
