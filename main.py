import logging
from sqlalchemy.exc import SQLAlchemyError
from app.database import SessionLocal, engine
from app import models, crud

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
logger = logging.getLogger(__name__)

def main():
    # Create tables (if not already created)
    models.Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    try:
        # Create a user
        new_user = crud.create_user(db, name="Alice", email="alice@example.com", password_hash="hashed_pw")
        logger.info(f"Created user: {new_user}")

        # Get user by email
        fetched_user = crud.get_user_by_email(db, email="alice@example.com")
        logger.info(f"Fetched user: {fetched_user}")

        # Create a leadership assessment
        assessment = crud.create_leadership_assessment(db, user_id=new_user.id, skill_name="Communication", self_rating=8)
        logger.info(f"Created assessment: {assessment}")

        # Delete a user module progress by id (replace the ID)
        # deleted_progress = crud.delete_user_module_progress(db, progress_id="ADD_ID_HERE")
        # logger.info(f"Deleted progress: {deleted_progress}")

    except SQLAlchemyError as e:
        logger.error(f"Database error occurred: {e}", exc_info=True)
        db.rollback()
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
    finally:
        db.close()
        logger.info("Database session closed.")

if __name__ == "__main__":
    main()