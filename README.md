
# Puddle

Puddle is a Django-based marketplace project that allows users to buy and sell goods. This repository contains the source code for the Puddle application.

## Features

- User authentication and authorization
- Product listings with images
- Search and filter functionality
- User profiles and dashboard
- Order management
- Reviews and ratings
- Messaging between users

## Technologies

- Python
- Django
- HTML
- CSS
- JavaScript
- SQLite (default) or any other Django-supported database

## Project Structure

- `core/`: Contains the core functionality of the marketplace.
- `item/`: Manages the product listings.
- `dashboard/`: User profile and dashboard management.
- `conversation/`: Handles messaging between users.
- `media/`: Stores user-uploaded media files.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/puddle.git
   cd puddle
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```sh
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000`.

## Usage

- Navigate to the homepage to view product listings.
- Sign up or log in to access user-specific features like adding products, managing your profile, and messaging other users.
- Admin functionalities are accessible at `http://127.0.0.1:8000/admin`.

## URL Configuration

The `urls.py` file in the root directory includes the following URL patterns:

- `path('', include('core.urls'))`: Core functionalities.
- `path('items/', include('item.urls'))`: Product listings.
- `path('dashboard/', include('dashboard.urls'))`: User dashboard.
- `path('inbox/', include('conversation.urls'))`: Messaging.
- `path('admin/', admin.site.urls)`: Admin site.

