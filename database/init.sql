-- Behavioral Intelligence Platform - Database Initial Setup Script
CREATE DATABASE bip_db;
CREATE USER bip_admin WITH PASSWORD 'bip_password_secure';
GRANT ALL PRIVILEGES ON DATABASE bip_db TO bip_admin;
