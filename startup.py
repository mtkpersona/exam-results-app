import os
import logging
from app import app, db
from flask_migrate import upgrade


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_database():
    try:
        if not os.path.exists('instance/exam_results.db'):
            logger.info("Creating database...")
            with app.app_context():
                db.create_all()
                logger.info("Database created.")

        logger.info("Applying database migrations...")
        with app.app_context():
            upgrade()
            logger.info("Migrations applied.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    initialize_database()