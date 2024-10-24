CREATE TABLE IF NOT EXISTS liquidations (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    severance_pay FLOAT,
    severance_pay_interest FLOAT,
    service_bonus FLOAT,
    vacation FLOAT,
    total_liquidation FLOAT,
    liquidation_date DATE DEFAULT CURRENT_DATE
);