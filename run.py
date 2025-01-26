from app import app
from startup import initialize_database

if __name__ == "__main__":
    # Initialize and migrate the database
    initialize_database()

    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)