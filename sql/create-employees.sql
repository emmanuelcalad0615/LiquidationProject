CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    document BIGINT UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    department VARCHAR(50),
    hire_date DATE,
    contract_type VARCHAR(50),
    salary FLOAT,
    status VARCHAR(20) DEFAULT 'activo'
);


