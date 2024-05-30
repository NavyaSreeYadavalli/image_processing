from flask import Flask, request, jsonify
import sqlite3
import pandas as pd

app = Flask(__name__)

# Path to the SQLite database
db_path = 'data/image_data.db'


# Define the API endpoint
@app.route('/get_image_frames', methods=['GET'])
def get_image_frames():
    depth_min = int(request.args.get('depth_min'))
    depth_max = int(request.args.get('depth_max'))

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    print(conn)
    query = f"SELECT * FROM images WHERE depth BETWEEN {depth_min} AND {depth_max}"
    df = pd.read_sql_query(query, conn)
    print(df)
    conn.close()

    # Convert the data to JSON and return
    return df.to_json(orient='records')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
