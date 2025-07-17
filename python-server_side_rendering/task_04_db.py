from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    with open("products.json", "r") as f:
        return json.load(f)

def read_csv():
    products = []
    with open("products.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row["id"] = int(row["id"])
            row["price"] = float(row["price"])
            products.append(row)
    return products

def read_sql():
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM Products")
        rows = cur.fetchall()
        return [dict(row) for row in rows]
    except:
        return []

@app.route("/products")
def products():
    source = request.args.get("source")
    id_param = request.args.get("id")
    data = []
    error = None

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    elif source == "sql":
        data = read_sql()
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
