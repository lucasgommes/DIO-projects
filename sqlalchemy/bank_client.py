from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import (Column, Integer,
                        String, ForeignKey)


Base = declarative_base()


class Client(Base):
    __tablename__ = "client"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)

    account = relationship("Account",
                     back_populates = "client",
                     cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, full_name={self.full_name})"


class Account(Base):
    __tablename__ = "account"

    id = Column(Integer, primary_key = True)
    type = Column(String)
    agency = Column(String)
    num_account = Column(Integer)
    id_client = Column(Integer, ForeignKey("client.id"), nullable = True)

    client = relationship("Client",
                          back_populates = "account")
    

# Making connection with database
engine = create_engine("sqlite://example.db")

# Creating classes like a tables
Base.metadata.create_all(engine)


# Persisting some data in database with help of Sessions
with Session(engine) as session:
    lukas = Client(
        name = "Lukas",
        full_name = "Lukas Gomes",
        account = [Account(
            type = "Poupança",
            agency = "8933",
            num_account = 98321
        )])
    
    ana = Client(
        name = "Ana",
        full_name = "Ana Gabriele",
        account = [Account(
            type = "Corrente",
            agency = "7445",
            num_account = 64352
        )])
    
    # Sending data for database
    session.add_all([lukas, ana])
    session.commit()
    