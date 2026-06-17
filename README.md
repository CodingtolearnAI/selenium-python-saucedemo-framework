# Selenium Python Automation Framework

## Overview

This project is a UI Test Automation Framework developed using Selenium WebDriver, Python, and Pytest following the Page Object Model (POM) design pattern.

The framework automates end-to-end user workflows on the SauceDemo application, including login, product selection, cart management, checkout, and logout functionalities.

---

## Features

* Page Object Model (POM) Architecture
* Reusable Base Page Implementation
* Explicit Wait Handling
* Logging using Python Logging Module
* Screenshot Capture on Test Failure
* HTML Test Reporting
* End-to-End Purchase Workflow Automation
* GitHub Version Control
* Pytest Framework Integration

---

## Tech Stack

| Tool               | Purpose                  |
| ------------------ | ------------------------ |
| Python             | Programming Language     |
| Selenium WebDriver | Browser Automation       |
| Pytest             | Test Execution Framework |
| WebDriver Manager  | Driver Management        |
| Pytest HTML        | HTML Report Generation   |
| Logging            | Execution Tracking       |
| Git & GitHub       | Version Control          |

---

## Framework Architecture

```text
SELENIUM-QA-PROJECT
│
├── pages
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── tests
│   ├── test_login.py
│   ├── test_logout.py
│   ├── test_cart.py
│   ├── test_checkout.py
│   └── test_endtoend.py
│
├── utils
│   ├── logger.py
│   ├── screenshots.py
│   └── driver_setup.py
│
├── logs
│   └── automation.log
│
├── screenshots
│
├── reports
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---
## Project Structure
<img width="484" height="895" alt="project-structure" src="https://github.com/user-attachments/assets/22be0b2a-acad-4486-ada0-df78350cc9f2" />


## Test Scenarios Covered

### Login Module

* Valid Login
* Locked User Validation
* Multiple User Login Validation

### Inventory Module

* Product Visibility Validation
* Add Product To Cart

### Cart Module

* Verify Added Product
* Open Cart

### Checkout Module

* Complete Purchase Flow
* Order Completion Validation

### Logout Module

* Successful Logout

### End-To-End Module

* Login
* Add Product
* Checkout
* Complete Order

---
## Logging

<img width="1615" height="989" alt="logs" src="https://github.com/user-attachments/assets/42ac5371-a7c0-4b32-85fd-c05fabbc85ac" />

## HTML Report

<img width="1919" height="671" alt="html-report" src="https://github.com/user-attachments/assets/7ddd2fb5-fbe1-4071-b518-cd05f0a28ed4" />


## How To Run The Project

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Execute All Tests

```bash
pytest -v
```

### Execute Specific Test

```bash
pytest tests/test_login.py -v
```

### Generate HTML Report

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## Logging

Execution logs are automatically generated under:

```text
logs/automation.log
```

Sample Log Output:

```text
INFO - Login Successful
INFO - Product Added To Cart
INFO - Checkout Started
INFO - Order Completed Successfully
```

---

## Screenshots On Failure

Whenever a test fails, a screenshot is automatically captured and stored under:

```text
screenshots/
```

This helps with debugging and failure analysis.

---

## HTML Reports

After execution, a detailed HTML report is generated:

```text
reports/report.html
```

The report includes:

* Test Status
* Pass/Fail Summary
* Execution Duration
* Failure Details

---

## Future Enhancements

* Cross Browser Execution
* Parallel Test Execution
* Allure Reporting
* Jenkins CI/CD Integration
* Dockerized Test Execution
* API Automation Integration

---

## Author

Mrigaya Saini

QA Engineer | Selenium | Python | Pytest | Automation Testing
