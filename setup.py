from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.pool import NullPool

from credentials import DATABASE_CREDENTIALS

MEDIA_ROOT = "media/images"

user = DATABASE_CREDENTIALS['user']
host = DATABASE_CREDENTIALS['host']
password = DATABASE_CREDENTIALS['password']
port = DATABASE_CREDENTIALS['port']
database = DATABASE_CREDENTIALS['database']

db_uri = f"mysql+aiomysql://{user}:{password}@{host}:{port}/{database}"
engine = create_async_engine(db_uri, echo=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
