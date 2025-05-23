# HumanChain AI Safety Incident Log API

This is a RESTful API built with Python and Flask to log and manage AI safety incidents. The API allows for the creation, retrieval, and deletion of incidents related to AI systems.

## Features

- **GET /incidents**: List all AI safety incidents.
- **POST /incidents**: Create a new AI safety incident.
- **GET /incidents/{id}**: Retrieve details of a specific AI safety incident.
- **DELETE /incidents/{id}**: Delete an AI safety incident.

## Tech Stack

- **Python** (Version 3.x)
- **Flask**: Web framework
- **SQLite**: Lightweight database for storing incident records
- **SQLAlchemy**: ORM for interacting with the SQLite database

## Requirements

- Python 3.x
- Flask
- Flask-SQLAlchemy

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/incident-log-api.git
   cd incident-log-api
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Mac/Linux
   venv\Scripts\activate     # For Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database and add sample incidents:
   ```bash
   python db_init.py
   ```

## Usage

1. Start the Flask development server:
   ```bash
   python app.py
   ```
   The API will be available at `http://localhost:5000`.

2. Use the following endpoints:

   ### List all incidents:
   - **Method**: `GET`
   - **URL**: `/incidents`
   - **Response**: A list of all incidents in JSON format.

   ### Create a new incident:
   - **Method**: `POST`
   - **URL**: `/incidents`
   - **Request Body**:
     ```json
     {
       "title": "AI malfunction",
       "description": "Generated incorrect output",
       "severity": "Medium"
     }
     ```
   - **Response**: Details of the created incident, including `id`, `title`, `description`, `severity`, and `reported_at`.

   ### Get an incident by ID:
   - **Method**: `GET`
   - **URL**: `/incidents/{id}`
   - **Response**: Details of the specified incident.

   ### Delete an incident by ID:
   - **Method**: `DELETE`
   - **URL**: `/incidents/{id}`
   - **Response**: A confirmation message that the incident was deleted successfully.

## Example API Calls

### 1. Get all incidents:
```bash
curl http://localhost:5000/incidents
```

### 2. Create a new incident:
```bash
curl -X POST http://localhost:5000/incidents -H "Content-Type: application/json" -d '{"title": "AI malfunction", "description": "Generated incorrect output", "severity": "Medium"}'
```

### 3. Get an incident by ID:
```bash
curl http://localhost:5000/incidents/1
```

### 4. Delete an incident by ID:
```bash
curl -X DELETE http://localhost:5000/incidents/1
```

## Error Handling

- **Missing Required Fields in POST**: If the required fields `title`, `description`, and `severity` are missing in the POST request, you will receive an error message:
  ```json
  {
    "error": "Missing required fields (title, description, severity)"
  }
  ```

- **Invalid Severity in POST**: If the `severity` field has a value other than `Low`, `Medium`, or `High`, you will receive an error message:
  ```json
  {
    "error": "Invalid severity level. Must be one of: Low, Medium, High"
  }
  ```

- **Incident Not Found**: If the `GET` or `DELETE` request is made with an invalid ID (non-existent incident), you will receive an error message:
  ```json
  {
    "error": "Incident not found"
  }
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Sections:
- **Tech Stack**: Lists the technologies used.
- **Installation**: Instructions to set up the project locally.
- **Usage**: Details how to run the API and make requests using `curl`.
- **Error Handling**: Describes potential error messages and causes.
- **Example API Calls**: Shows examples of how to interact with the API.

You can save this file as `README.md` in your project directory.

Let me know if you need any more changes or additions to this!
