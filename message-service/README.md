## Message Service

### Overview
The `message-service` folder contains the codebase for the message service application, which is built using Python and Flask. This service provides functionalities for creating, retrieving, and searching messages. The codebase is organized into the `app` directory for the main application logic and the `tests` directory for unit tests.

### Folder Structure

#### app/
```
app/
├── __init__.py    # Application factory and initialization code
├── config.py      # Configuration settings for different environments
├── models.py      # Database models and schema definitions
├── utils.py       # Utility functions and helper methods
└── views.py       # API endpoints and view logic
```

#### tests/
```
tests/
└── test_views.py  # Unit tests for the API endpoints in views.py
```

### Files Explanation

#### app/ Directory

1. **`__init__.py`**
   - This file contains the application factory function `create_app()`, which initializes the Flask app, configures it, and registers the blueprints for different components of the service.

2. **config.py**
   - Defines configuration settings for different environments (e.g., development, testing, production). It includes database URIs, debug flags, and other application-specific settings.

3. **models.py**
   - Contains the SQLAlchemy models representing the data structures for the service, such as the `Message` model, which stores message details like `account_id`, `message_id`, `sender_number`, and `receiver_number`.

4. **utils.py**
   - Includes utility functions that support various aspects of the application, such as data validation, UUID generation, and other helper methods.

5. **views.py**
   - Defines the API endpoints for the message service. It includes routes for:
     - **GET /get/messages/<account_id>**: Retrieves all messages for a specific account.
     - **POST /create**: Creates a new message record.
     - **GET /search**: Searches for messages based on `message_id`, `sender_number`, or `receiver_number`.

#### tests/ Directory

1. **test_views.py**
   - Contains unit tests for the API endpoints defined in `views.py`. These tests ensure that the endpoints work as expected, validating the responses and the correct functioning of the service.

### Running the Application

To run the message service locally:

1. **Install Dependencies**:
   - Navigate to the `message-service` directory and install the necessary Python dependencies using pip:
     ```
     pip install -r requirements.txt
     ```

2. **Start MySql DB**:
   - Run below command to bring MySql DB.
     ```
     docker run --name mysql -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=messages -e MYSQL_USER=user -e MYSQL_PASSWORD=password -p 3306:3306 -d mysql:5.7
     ```
3. **Validation and Testing**:
    - Run below commands for creating and searching messages
     ```
     curl -X POST http://127.0.0.1:5000/create -H "Content-Type: application/json" -d '{"account_id": "1234", "sender_number": "123456789564550", "receiver_number": "1234567890"}'

     curl "http://127.0.0.1:5000/search?sender_number=123456789564550"
     
     ```
    - Make sure `curl` is installed in your sysytem.

3. **Run the Application**:
   - Start the Flask development server:
     ``` FLASK_APP=app flask run
     ```

### Testing the Application

To run the unit tests:

1. **Navigate to the `message-service` directory**.

2. **Run the tests using pytest**:
   ```
   pytest
   ```

