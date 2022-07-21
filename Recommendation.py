from flask import Flask, request
import pandas as pd
import pymysql
import module.contentBased as cb

app = Flask('recommend')

@app.route("/recoProducts/asin")
def recommend():
    #?? asin정보 이렇게 받나??
    asin = request.args.get('asin')
    
    item_df = pd.read_pickle('./pickle/item_df.pkl')
    rating_df = pd.read_pickle('./pickle/rating_df.pkl')
    
    similar_items_list = cb.content_based(item_df, rating_df, asin)

    return similar_items_list

# @app.route("/products")
# def getAllproducts():
#     host = '43.200.48.164'
#     port = 3306
#     user = 'root'
#     pd = '1234'
#     prodb = 'projectdb'
#     enc = 'utf8'
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=pd, db=prodb, charset=enc)
#     curs = conn.cursor()
#     sql = """SELECT * FROM product"""
#     curs.execute(sql)
#     rows = curs.fetchall()

#     # res = []
#     # for row in rows:
#     #     product = {'seq': row[0], 'name': row[1], 'asin': row[2], 'price': row[3], 'buylink': row[4], 'imglink': row[5], 'category': row[6]}
#     #     res.append(product)

#     conn.close()
    
#     return rows # jsonify(res)

# # @app.route("/reviews")
# def getAllreviews():
#     host = '43.200.48.164'
#     port = 3306
#     user = 'root'
#     pd = '1234'
#     prodb = 'projectdb'
#     enc = 'utf8'
#     conn = pymysql.connect(host=host, port=port, user=user, passwd=pd, db=prodb, charset=enc)
#     curs = conn.cursor()
#     sql = """SELECT * FROM review"""
#     curs.execute(sql)
#     rows = curs.fetchall()

#     # res = []
#     # for row in rows:
#     #     product = {'seq': row[0], 'name': row[1], 'asin': row[2], 'price': row[3], 'buylink': row[4], 'imglink': row[5], 'category': row[6]}
#     #     res.append(product)

#     conn.close()
    
#     return rows # jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='localhost')