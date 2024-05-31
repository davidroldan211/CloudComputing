from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models, schemas

# Crear todas las tablas si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/set_params", response_model=schemas.MLModel)
def create_ml_model(ml_model: schemas.MLModelCreate, db: Session = Depends(get_db)):
    db_model = models.MLModel(**ml_model.dict())
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
    return db_model

@app.get("/get_params/{model_id}", response_model=schemas.MLModel)
def read_ml_model(model_id: str, db: Session = Depends(get_db)):
    db_model = db.query(models.MLModel).filter(models.MLModel.id == model_id).first()
    if db_model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return db_model


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
