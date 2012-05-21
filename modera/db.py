import modera_config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine_table = {}
def get_db_engine(uri=None, *args, **kwargs):
    uri = modera_config.MODERA_CONFIG['DATABASE_URI'] if not uri else uri
    if uri not in engine_table:
        engine_table[uri] = create_engine(uri, *args, **kwargs)
    return engine_table[uri]
    
def create_tables_for_entities(entity, engine=None):
    engine = get_db_engine() if not engine else engine
    entity.metadata.create_all(engine)

session_maker_table = {}
def create_session(engine=None):
    engine = get_db_engine() if not engine else engine
    uri = str(engine.url)
    if uri not in session_maker_table:
        session_maker_table[uri] = sessionmaker()
        session_maker_table[uri].configure(bind=engine)
    return session_maker_table[uri]()


