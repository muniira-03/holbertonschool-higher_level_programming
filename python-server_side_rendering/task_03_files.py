from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except:
        return []

def read_csv():
    data = []
    try:
        with open("products.csv", newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["id"] = int(row["id"])
                row["price"] = float(row["price"])
                data.append(row)
    except:
        pass
    return data

@app.route("/products")
def show_products():
    source = request.args.get("source")
    id_param = request.args.get("id")
    data = []
    error = None

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        error = "Wrong source"

    if not error and id_param:
        try:
            id_param = int(id_param)
            data = [item for item in data if item["id"] == id_param]
            if not data:
                error = "Product not found"
        except:
            error = "Invalid ID"

    return render_template("product_display.html", products=data, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
