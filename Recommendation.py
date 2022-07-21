from flask import Flask, request
import pandas as pd
import module.contentBased as cb

app = Flask('recommend')

@app.route("/recoProducts/asin")
def recommend():
    asin = request.args.get('asin')
    item_df = pd.read_pickle('./pickle/item_df.pkl')
    rating_df = pd.read_pickle('./pickle/rating_df.pkl')
    similar_items_list = cb.content_based(item_df, rating_df, asin)

    return similar_items_list

if __name__ == '__main__':
    app.run(debug=True, host='localhost')