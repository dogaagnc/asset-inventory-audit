# Asset Inventory Audit

A Python-based IT asset inventory auditing tool developed to identify data quality issues within organizational device records.

The application validates asset information, detects missing or invalid fields, identifies duplicate inventory numbers, and generates a detailed audit report.

## Features

- Validates required asset fields
- Detects missing inventory information
- Checks device types against predefined valid values
- Validates asset status information
- Detects duplicate inventory numbers
- Separates valid and problematic asset records
- Generates detailed audit results for each device
- Produces an overall inventory audit summary

## Technologies

- Python 3
- Python dictionaries and lists
- Data validation
- Automated inventory auditing

## Project File

- `asset_audit.py` — Main Python application responsible for validating and auditing IT asset records

## Validation Checks

The application checks asset records for:

- Missing required fields
- Invalid device types
- Invalid asset statuses
- Duplicate inventory numbers

## Example Output

The generated audit report includes:

- Total number of assets
- Number of valid assets
- Number of problematic assets
- Individual audit results for each device
- Detailed descriptions of detected problems

Example detected issues may include:

- `Duplicate inventory number`
- `Missing fields`
- `Invalid device type`
- `Invalid status`

## Purpose

This project was developed as part of practical studies in Information Systems and Technologies to demonstrate IT asset management, data validation, and automated inventory auditing using Python.
