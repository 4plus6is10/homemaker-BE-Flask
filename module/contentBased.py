import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def topKItems(itemId, topK, corrMat, mapName):
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
    topK = 5
    ratedItems = item_df.loc[item_df['asin'].isin(rating_df['asin'])].copy()
    Category = ratedItems['category'].str.split(",", expand=True)
    allCategory = set()

    for c in Category.columns:
        distinctCategory = Category[c].str.lower().str.strip().unique()
        allCategory.update(distinctCategory)

    itemCategoryMat = ratedItems[['asin', 'category']].copy()
    itemCategoryMat['category'] = itemCategoryMat['category'].str.lower().str.strip()

    for Category in allCategory:
        itemCategoryMat[Category] = np.where(itemCategoryMat['category'].str.contains(Category), 1, 0)

    itemCategoryMat = itemCategoryMat.drop(['category'], axis=1)
    itemCategoryMat = itemCategoryMat.set_index('asin')

    corrMat = cosine_similarity(itemCategoryMat)

    ind2name = {ind:name for ind,name in enumerate(itemCategoryMat.index)}
    name2ind = {v:k for k,v in ind2name.items()}

    try:
        similarItems = topKItems(name2ind[searched_asin],
                            topK = topK,
                            corrMat = corrMat,
                            mapName = ind2name)
    except:
        similarItems = 'no product'

    similar_items_dict = {}
    if similarItems == 'no product':
        return similarItems
    else:
        for idx, asin in enumerate(similarItems):
            similar_items_dict[idx] =  asin

    return similar_items_dict
