from fastapi import FastAPI
from app.api.v1.user import router
import json
import os
app = FastAPI()


file_path = os.path.join(os.path.dirname(__file__), 'data', 'global_metrics.json')


def load_api_data():
    # Fonction charger les données à partir du fichier JSON
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
# Route pour récupérer les données de l'API


@app.get("/")
def read_root():
    api_data = load_api_data()
    return api_data


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


app.include_router(router)
