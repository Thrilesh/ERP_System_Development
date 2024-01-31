ERP System
This is a simplified ERP (Enterprise Resource Planning) system developed using Django. The system includes modules for Purchase Management and Inventory Management.

Project Structure
The project is organized as follows:

ERP_System: Main project directory.
purchase_management: Django app for Purchase Management.
inventory_management: Django app for Inventory Management.
static: Directory to store static files like CSS.
templates: Directory to store HTML templates.

Setup Instructions
1. Clone the Repository
git clone https://github.com/your-username/your-repository.git
cd ERP_System

2. Set Up Virtual Environment
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py makemigrations
python manage.py migrate

5. Create Superuser (Optional)
python manage.py createsuperuser

6. Run the Development Server
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser.

Modules
Purchase Management
Supplier Management: Create, update, and delete supplier information.
Purchase Order Management: Create, update, and delete purchase orders.
Inventory Management
Product Management: Create, update, and delete product information.
Stock Movement Management: Track stock movements for inventory adjustments.

Notes
The project uses Django for the backend.
Styling is applied using CSS (located in the static directory).
Ensure you have a compatible database configured in your settings.py.
Customize the project as needed for your specific requirements.
