# Food Inventory Management System

A Python-based application that combines a Flask RESTful API backend with an interactive Command-Line Interface (CLI) frontend. The system manages a local food product inventory and integrates with the external **OpenFoodFacts API** to retrieve live nutritional and product information.

---

## Features

* **Flask REST API**: Full CRUD endpoints (`GET`, `POST`, `PATCH`, `DELETE`) operating on an in-memory inventory array.
* **CLI Frontend**: Interactive terminal interface to view, add, update, and remove inventory items.
* **OpenFoodFacts API Integration**: Queries external product details (brand, ingredients, product name) using barcodes or product names.
* **Unit Testing**: Automated tests built with `pytest` and `unittest.mock` to validate endpoints and API logic.

---

## Project Structure

```text
food-inventory-app/
├── app.py          # Flask REST API server and OpenFoodFacts helper function
├── cli.py          # Interactive Command-Line Interface
├── test_app.py     # Unit tests for API endpoints and logic
├── requirements.txt # Project dependencies
└── README.md       # Project documentation