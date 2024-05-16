# app/controllers/function_graph.py
import json
import matplotlib.pyplot as plt
import io
import base64
import logging

logger = logging.getLogger(__name__)


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def create_graphs_from_json(data):
    images = {}
    for graph_name, graph_data in data.items():
        try:
            logger.info(f"Creating graph for {graph_name}")
            plt.figure()
            plt.plot(graph_data['x'], graph_data['y'])
            plt.title(graph_name)
            plt.xlabel('X-axis label')
            plt.ylabel('Y-axis label')
            
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            plt.close()
            
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            images[graph_name] = image_base64
        except Exception as e:
            logger.error(f"Error creating graph {graph_name}: {e}")
            raise
    return images
