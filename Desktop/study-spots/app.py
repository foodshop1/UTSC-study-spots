from flask import Flask, render_template
from utscScraper import Scrape
import json


app = Flask(__name__)

@app.route('/')
def home():
    
    raw_data = Scrape.data()

    # If Scrape.data() returns a JSON string, convert to Python dict
    study_spots = json.loads(raw_data) 

    return render_template('index.html', spots=study_spots)

if __name__ == '__main__':
    app.run(debug=True)
