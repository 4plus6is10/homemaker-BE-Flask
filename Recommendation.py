from flask import Flask, request
from flask_cors import CORS
import pandas as pd
import module.ContentBased as cb

app = Flask('recommend')
cors = CORS(app, resources={r'/recoproducts/asin': {'origins': '*'}})

@app.route("/recoProducts/asin")
def recommend():
    asin = request.args.get('asin')
    item_df = pd.read_pickle('./pickle/item_df.pkl')
    rating_df = pd.read_pickle('./pickle/rating_df.pkl')
    similar_items_dict = cb.content_based(item_df, rating_df, asin)

    return similar_items_dict

if __name__ == '__main__':
    app.run(debug=True, host='localhost')


