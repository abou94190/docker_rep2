import json
import matplotlib.pyplot as plt


def load_json_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def create_graphs_from_json(data):
    # Par exemple, data pourrait avoir une structure comme :
    # {
    #     "graph1": {"x": [1, 2, 3], "y": [4, 5, 6]},
    #     "graph2": {"x": [1, 2, 3], "y": [7, 8, 9]}
    # }

    for graph_name, graph_data in data.items():
        plt.figure()
        plt.plot(graph_data['x'], graph_data['y'])
        plt.title(graph_name)
        plt.xlabel('X-axis label')
        plt.ylabel('Y-axis label')
        plt.savefig(f"{graph_name}.png")  # Sauve chaque graph en fichier PNG
        plt.close()

    print("Graphiques créés et sauvegardés.")
