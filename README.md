https://aymandev.pythonanywhere.com/api/docs/

# Little Lemon - Restaurant API 🍋

This is a comprehensive RESTful API built with **Django REST Framework (DRF)** for the **Meta Back-End Developer Professional Certificate** Capstone Project. 

The API serves as the backend for the "Little Lemon" restaurant, managing menu items, user roles, cart items, and order processing.

## 🚀 Features

* **User Authentication:** Token-based authentication using Djoser/DRF tokens.
* **Role-Based Access Control (RBAC):**
  * **Manager:** Full access to manage menu items, assign delivery crews, and update order statuses.
  * **Delivery Crew:** Can view assigned orders and update their delivery status.
  * **Customer:** Can browse the menu, add items to the cart, and place orders.
* **Cart Management:** Endpoints to add, view, and clear the shopping cart.
* **Order Processing:** Seamlessly convert cart items into an official order.
* **Advanced Querying:** Supports Pagination, Searching (by title), Filtering (by category & featured), and Ordering (by price).

## 🛠️ Tech Stack

* **Backend:** Python 3.14, Django 5.1
* **API Framework:** Django REST Framework (DRF)
* **Database:** MySQL 8.0
* **Other Tools:** django-filter, djoser

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Ayman-lemo/LittleLemon.git](https://github.com/Ayman-lemo/LittleLemon.git)
   cd LittleLemon 


Create and activate a virtual environment:

python -m venv env
# On Windows:
.\env\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up environment variables:
Create a .env file in the project root and add your database credentials:

DB_PASSWORD=your_mysql_password

Run Database Migrations:

python manage.py migrate

Create a Superuser & Run the Server:

python manage.py createsuperuser
python manage.py runserver

📡 Key API Endpoints
Menu Items
GET /restaurant/menu-items/ - List all menu items (Supports search, order, and filter)

POST /restaurant/menu-items/ - Create a new menu item (Managers only)

GET, PUT, PATCH, DELETE /restaurant/menu-items/{id}/ - Manage single item (Managers only)

User Group Management
GET, POST, DELETE /restaurant/groups/manager/users/ - Manage managers

GET, POST, DELETE /restaurant/groups/delivery-crew/users/ - Manage delivery crew

Cart Management
GET /restaurant/cart/menu-items/ - View current user's cart

POST /restaurant/cart/menu-items/ - Add item to cart

DELETE /restaurant/cart/menu-items/ - Clear cart

Order Management
GET /restaurant/orders/ - List orders (Logic varies by user role)

POST /restaurant/orders/ - Checkout and place an order

GET, PUT, PATCH, DELETE /restaurant/orders/{id}/ - Manage single order (Role-based access)

Developed by Ayman Ahmed
