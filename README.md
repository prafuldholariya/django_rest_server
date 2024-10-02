## Step-by-Step Guide to Creating the Django REST Server

### **Prerequisites**
- **Python 3.8+** installed on your system.
- **pip** package manager.
- **Virtualenv** (optional but recommended).
- **Postman** or **curl** for testing APIs.

### **Set Up the Project Environment**

1. **Clone Project**
   ```bash
    git clone https://github.com/prafuldholariya/django_rest_server.git
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python3 -m venv _venv
   source _venv/bin/activate  # On Windows: _venv\Scripts\activate
   ```

3. **Install Required Packages**
   ```bash
   pip install django djangorestframework
   ```

4. **Apply Migrations**
   ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```