Smart Inventory Management System

A modern Inventory Management System developed using **Django**, **Django REST Framework**, and **ShaktiDB**. The system helps businesses manage products, suppliers, purchases, sales, and inventory efficiently through a user-friendly dashboard.

Features
Product Management

* Add, view, update, and delete products
* Manage stock quantities
* Track selling price and cost price
* Low stock threshold monitoring
* Product categorization

Supplier Management

* Store supplier details
* Manage supplier information
* Link suppliers to products and purchases

Purchase Management

* Record product purchases
* Automatically update inventory stock
* Maintain purchase history

Sales Management

* Record product sales
* Automatically reduce stock levels
* Maintain sales history

Dashboard & Reports

* Inventory overview dashboard
* Product stock monitoring
* Sales and purchase tracking
* Low stock alerts

Technology Stack

Backend

* Python
* Django
* Django REST Framework

 Database

* ShaktiDB

Frontend

* HTML
* CSS
* JavaScript
* React (CDN-based components)

Version Control

* Git
* GitHub

Project Structure

inventory_project/
├── inventory/
├── inventory_project/
├── templates/
├── manage.py
└── requirements.txt

Installation

1. Clone the repository
2. Install Python dependencies
3. Configure ShaktiDB
4. Run migrations
5. Start the Django development server

```bash
python manage.py migrate
python manage.py runserver
```

Current Status

* Django Backend Setup ✅
* ShaktiDB Integration ✅
* REST API Development ✅
* Product Module ✅
* Supplier Module 🚧
* Purchase Module 🚧
* Sales Module 🚧
* Reports Module 🚧
* Authentication 🚧

Future Enhancements

* User Authentication and Authorization
* Advanced Reports and Analytics
* Export Reports to PDF/Excel
* Email Notifications for Low Stock
* Role-Based Access Control

Authors

Abdul Haseeb

License

This project is developed for educational and learning purposes.
