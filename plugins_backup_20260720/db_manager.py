"""
Database Manager Central — PostgreSQL + SQLite fallback
Usado por todos os plugins
"""
import os
import logging
from datetime import datetime
from typing import Optional, List, Dict, Any
import uuid

logger = logging.getLogger(__name__)

# Tentar PostgreSQL, fallback para SQLite
DATABASE_URL = os.getenv("DATABASE_URL", "")

_engine = None
_SessionLocal = None
_use_postgres = False

def init_db():
    global _engine, _SessionLocal, _use_postgres
    try:
        if DATABASE_URL and "postgres" in DATABASE_URL:
            from sqlalchemy import create_engine
            from sqlalchemy.orm import sessionmaker
            url = DATABASE_URL.replace("postgres://", "postgresql://")
            _engine = create_engine(url, pool_pre_ping=True, pool_size=5, max_overflow=10)
            _SessionLocal = sessionmaker(bind=_engine)
            _use_postgres = True
            logger.info("✅ PostgreSQL conectado")
        else:
            raise Exception("Sem PostgreSQL, usando SQLite")
    except Exception as e:
        logger.info(f"Usando SQLite: {e}")
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        _engine = create_engine("sqlite:///./emotion_platform.db", connect_args={"check_same_thread": False})
        _SessionLocal = sessionmaker(bind=_engine)
        _use_postgres = False

def get_db():
    if _SessionLocal is None:
        init_db()
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_engine():
    if _engine is None:
        init_db()
    return _engine

class SimpleDB:
    """
    Banco simples baseado em SQLite/PostgreSQL
    Cada plugin usa uma tabela própria
    """
    def __init__(self, table_name: str):
        self.table = table_name
        self._mem: Dict[str, Any] = {}  # fallback memória
        self._ready = False
        self._init_table()

    def _init_table(self):
        try:
            engine = get_engine()
            from sqlalchemy import text
            with engine.connect() as conn:
                conn.execute(text(f"""
                    CREATE TABLE IF NOT EXISTS {self.table} (
                        id VARCHAR(8) PRIMARY KEY,
                        user_id VARCHAR(100),
                        nome VARCHAR(500),
                        valor TEXT,
                        dados TEXT,
                        categoria VARCHAR(100),
                        criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        atualizado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """))
                conn.commit()
            self._ready = True
            logger.debug(f"Tabela {self.table} pronta")
        except Exception as e:
            logger.warning(f"DB {self.table} usando memória: {e}")
            self._ready = False

    def create(self, nome: str, valor: str = "", user_id: str = "",
               dados: str = "", categoria: str = "") -> Dict:
        item_id = str(uuid.uuid4())[:8]
        now = datetime.utcnow().isoformat()
        item = {
            "id": item_id, "nome": nome, "valor": valor,
            "user_id": user_id, "dados": dados,
            "categoria": categoria, "criado_em": now
        }
        if self._ready:
            try:
                engine = get_engine()
                from sqlalchemy import text
                with engine.connect() as conn:
                    conn.execute(text(f"""
                        INSERT INTO {self.table} (id, nome, valor, user_id, dados, categoria)
                        VALUES (:id, :nome, :valor, :user_id, :dados, :categoria)
                    """), item)
                    conn.commit()
                return item
            except Exception as e:
                logger.warning(f"DB create error: {e}")
        self._mem[item_id] = item
        return item

    def get(self, item_id: str) -> Optional[Dict]:
        if self._ready:
            try:
                engine = get_engine()
                from sqlalchemy import text
                with engine.connect() as conn:
                    r = conn.execute(text(
                        f"SELECT * FROM {self.table} WHERE id = :id"
                    ), {"id": item_id}).fetchone()
                    if r:
                        return dict(r._mapping)
            except Exception as e:
                logger.warning(f"DB get error: {e}")
        return self._mem.get(item_id)

    def list(self, user_id: str = None, limite: int = 50) -> List[Dict]:
        if self._ready:
            try:
                engine = get_engine()
                from sqlalchemy import text
                with engine.connect() as conn:
                    if user_id:
                        rows = conn.execute(text(
                            f"SELECT * FROM {self.table} WHERE user_id = :uid ORDER BY criado_em DESC LIMIT :lim"
                        ), {"uid": user_id, "lim": limite}).fetchall()
                    else:
                        rows = conn.execute(text(
                            f"SELECT * FROM {self.table} ORDER BY criado_em DESC LIMIT :lim"
                        ), {"lim": limite}).fetchall()
                    return [dict(r._mapping) for r in rows]
            except Exception as e:
                logger.warning(f"DB list error: {e}")
        items = list(self._mem.values())
        if user_id:
            items = [i for i in items if i.get("user_id") == user_id]
        return items[-limite:]

    def delete(self, item_id: str) -> bool:
        if self._ready:
            try:
                engine = get_engine()
                from sqlalchemy import text
                with engine.connect() as conn:
                    conn.execute(text(
                        f"DELETE FROM {self.table} WHERE id = :id"
                    ), {"id": item_id})
                    conn.commit()
                return True
            except Exception as e:
                logger.warning(f"DB delete error: {e}")
        if item_id in self._mem:
            del self._mem[item_id]
            return True
        return False

    def count(self, user_id: str = None) -> int:
        if self._ready:
            try:
                engine = get_engine()
                from sqlalchemy import text
                with engine.connect() as conn:
                    if user_id:
                        r = conn.execute(text(
                            f"SELECT COUNT(*) FROM {self.table} WHERE user_id = :uid"
                        ), {"uid": user_id}).scalar()
                    else:
                        r = conn.execute(text(
                            f"SELECT COUNT(*) FROM {self.table}"
                        )).scalar()
                    return r or 0
            except Exception:
                pass
        return len(self._mem)

# Inicializar na importação
try:
    init_db()
except Exception:
    pass
