# app/main.py
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.api.v1.user import router
import os
import json
from app.controllers.function_graph import load_json_data, create_graphs_from_json
import logging

app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Chemin vers le fichier JSON contenant les données
file_path = os.path.join(os.path.dirname(__file__), 'data', 'global_metrics.json')


def load_api_data():
    try:
        # Charger les données à partir du fichier JSON
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        raise HTTPException(status_code=404, detail="File not found")
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from file: {file_path}")
        raise HTTPException(status_code=400, detail="Invalid JSON format")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.get("/")
def read_root():
    api_data = load_api_data()
    return api_data


@app.get("/create-graphs")
def create_graphs():
    try:
        data = load_json_data(file_path)
        images = create_graphs_from_json(data)
        return JSONResponse(content=images)
    except HTTPException as e:
        logger.error(f"HTTPException: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Error creating graphs: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

app.include_router(router)
