import typer
from matplotlib import pyplot as plt

from oxymouse.config import mouses

app = typer.Typer()


function_names_to_function_map = {
    "gc": "generate_coordinates",
    "grc": "generate_random_coordinates",
    "gsc": "generate_scroll_coordinates",
}


@app.command()
def visualize_mouse_movements(algorithm: str, fn: str) -> None:
    print(f"Visualizing {algorithm} with {fn} function")

    algorithm_instance = mouses[algorithm]
    function_name = function_names_to_function_map[fn]

    coordinates = getattr(algorithm_instance, function_name)()

    x_coordinates = [point[0] for point in coordinates]
    y_coordinates = [point[1] for point in coordinates]

    plt.figure(figsize=(16, 9))  # Set the figure size for 1080p
    plt.plot(x_coordinates, y_coordinates, marker="o", linestyle="-")
    plt.title(f"Simulated mouse movement path - {algorithm_instance} - {function_name}")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    app()
