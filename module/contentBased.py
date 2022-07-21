import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity


def topKItems(itemId, topK, corrMat, mapName):
    # 상관계수 정렬 &nd topK 제품 선택
    topItemsNums = corrMat[itemId,:].argsort()[-topK:][::-1]
    topItems = []
    for e in topItemsNums:
        try:
            item = mapName[e]
            topItems.append(item)
        except:
            pass
        
    return topItems

def content_based(item_df, rating_df, searched_asin):
    # 추천
    topK = 5

    # preprocessing
    ratedItems = item_df.loc[item_df['asin'].isin(rating_df['asin'])].copy()

    # extract the Category
    Category = ratedItems['category'].str.split(",", expand=True)

    # get all possible Category
    allCategory = set()
    for c in Category.columns:
        distinctCategory = Category[c].str.lower().str.strip().unique()
        allCategory.update(distinctCategory)

    # create item-Category matrix
    itemCategoryMat = ratedItems[['asin', 'category']].copy()
    itemCategoryMat['category'] = itemCategoryMat['category'].str.lower().str.strip()

    # OHE the genres column
    for Category in allCategory:
        itemCategoryMat[Category] = np.where(itemCategoryMat['category'].str.contains(Category), 1, 0)
    itemCategoryMat = itemCategoryMat.drop(['category'], axis=1)
    itemCategoryMat = itemCategoryMat.set_index('asin')

    # compute similarity matix
    corrMat = cosine_similarity(itemCategoryMat)


    # get topK similar items
    ind2name = {ind:name for ind,name in enumerate(itemCategoryMat.index)}
    name2ind = {v:k for k,v in ind2name.items()}

    try:
        similarItems = topKItems(name2ind[searched_asin],
                            topK = topK,
                            corrMat = corrMat,
                            mapName = ind2name)
    except:
        similarItems = 'no product'

    return str(similarItems)