from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

DATABASE_URL = "sqlite:///thrive.db"

DB_IMAGE_UPLOAD_PATH = "api/static/uploads"
engine = create_engine(DATABASE_URL, echo=False, future=True)

# 2️⃣ Session factory (for creating new sessions per request)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
