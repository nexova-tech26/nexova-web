from sqlmodel import SQLModel, create_engine

# Definimos el nombre del archivo de la base de datos local
sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

# check_same_thread=False es necesario solo para SQLite en FastAPI
connect_args = {"check_same_thread": False}

# El engine es el conector principal. echo=True hará que veamos en la terminal
# todo el código SQL que se genera por debajo (ideal para depurar)
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)

# Esta función la llamaremos al iniciar el servidor para crear las tablas
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)