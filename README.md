# Grocery Store Web Application

## Overview

Welcome to our Grocery Store Web Application! This application allows users to explore a variety of products, add them to their cart, and make online purchases. It provides a seamless shopping experience for customers looking to buy groceries online.

## Features

- **Product Catalog:** Browse through a diverse range of grocery products conveniently categorized for easy navigation.
- **User-Friendly Interface:** Enjoy a user-friendly and intuitive interface designed for a smooth shopping experience.
- **Shopping Cart:** Add products to your cart, review your selections, and proceed to checkout.
- **Checkout Process:** A secure checkout process ensures the safety of your personal and payment information.

## Getting Started

### Prerequisites

1. **Install MySQL Workbench:** Follow the [MySQL Workbench Installation Guide](https://dev.mysql.com/doc/workbench/en/wb-installing.html) to install MySQL Workbench on your machine.

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/grocery-store-web-app.git
   cd grocery-store-web-app
   ```

2. **Set Up the Database:**
   - Open MySQL Workbench and connect to your local MySQL server.
   - Create a new schema (database) for your grocery store web application.

     ```sql
     CREATE SCHEMA `grocery_store_db`;
     ```

   - Use the created schema:

     ```sql
     USE `grocery_store_db`;
     ```

   - Open the `db.txt` file included in the project and execute the commands in MySQL Workbench to create tables and populate the database.

3. **Configure Database Connection:**
   - Open the `server.py` file in a text editor.
   - Locate the database connection configuration section:

     ```python
     # Database Configuration
     db_host = "localhost"
     db_user = "root"
     db_password = "your_password"
     db_name = "grocery_store_db"
     ```

   - Replace `"your_password"` with your MySQL root password.

4. **Run the Application:**
   - Install the required Python packages:

     ```bash
     pip install Flask Flask-MySQLdb
     ```

   - Run the Flask application:

     ```bash
     python server.py
     ```

   - Open your web browser and go to `http://localhost:5000` to access the Grocery Store Web Application.

## Explore and Enjoy

Now you have successfully set up the Grocery Store Web Application on your local machine! Explore the product catalog, add items to your cart, and experience the convenience of online grocery shopping.
