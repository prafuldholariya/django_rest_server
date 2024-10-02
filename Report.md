## Report

### **Introduction**
This report outlines the design decisions made in developing a Django REST server featuring three primary APIs: Login, Create Account, and Store User Data. The implementation leverages Django REST Framework (DRF) for robust API development, ensuring security, scalability, and ease of maintenance.

### **Framework and Tools Selection**
- **Django and Django REST Framework (DRF):** Chosen for their comprehensive features, scalability, and strong community support. DRF simplifies the creation of RESTful APIs with built-in serialization, authentication, and view handling.
- **SQLite Database:** Selected for simplicity and ease of setup during development. For production, a more robust database like PostgreSQL is recommended.
- **Postman and curl:** Utilized for testing APIs due to their widespread use and reliability in sending HTTP requests.

### **API Design and Functionality**
1. **Create Account API:**
   - **Endpoint:** `/api/register/`
   - **Method:** POST
   - **Functionality:** Allows new users to register by providing necessary credentials. Utilizes Django’s built-in `User` model to handle user data and password hashing automatically.
   - **Security:** Passwords are hashed using Django’s default password hasher before storage, ensuring user credentials are securely managed.

2. **Login API:**
   - **Endpoint:** `/api/login/`
   - **Method:** POST
   - **Functionality:** Authenticates users by verifying their credentials. Upon successful authentication, a unique token is generated (or retrieved if existing) and returned to the user for subsequent authenticated requests.

3. **Store User Data API:**
   - **Endpoint:** `/api/users/`
   - **Methods:** GET, PUT
   - **Functionality:** Enables users to retrieve their personal information, including name, phone number, and address.

### **Serialization and Data Handling**
- **Serializers:** Utilized DRF serializers to convert complex data types (like Django models) into native Python data types suitable for JSON rendering. Custom serializers (`UserSerializer` and `UserDataSerializer`) manage input validation and control the data exposed via the APIs.
- **Data Validation:** Implemented through serializer fields, ensuring that incoming data adheres to required formats and constraints before processing.

### **Security**
- **Password Hashing:** Leveraged Django’s built-in password hashing mechanisms to store user passwords securely. This abstracts the complexity of hashing algorithms and ensures adherence to best security practices.
- **Permissions:** Configured API permissions to restrict access appropriately. The `Create Account` and `Login` APIs are publicly accessible, while the `Store User Data` API requires authentication, preventing unauthorized data access.
