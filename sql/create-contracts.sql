
CREATE TABLE IF NOT EXISTS contracts (
    id SERIAL PRIMARY KEY,
    employee_id INT REFERENCES employees(id),
    start_date DATE,
    end_date DATE,
    contract_type VARCHAR(50),
    compensation_amount FLOAT
);