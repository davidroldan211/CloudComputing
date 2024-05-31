from sqlalchemy import Column, String, Float, Integer, JSON
from database import Base

class MLModel(Base):
    __tablename__ = "ml_models"

    id = Column(String(50), primary_key=True, index=True)  # Especifica la longitud del String
    learning_rate = Column(Float)
    epochs = Column(Integer)
    batch_size = Column(Integer)
    neurons = Column(JSON)
    weights = Column(JSON)
    biases = Column(JSON)

