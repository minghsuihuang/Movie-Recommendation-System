# main_WEB.py
import pandas as pd  # 引入 pandas 庫，用於數據操作和分析。

# 讀取電影數據集
movies = pd.read_csv('dataset.csv')  # 從 CSV 文件中加載數據到 DataFrame。

movies.head(10)  # 查看 DataFrame 的前 10 行數據。

movies.describe()  # 提供數據集的描述性統計信息。

movies.info()  # 獲取 DataFrame 的摘要信息。

movies.isnull().sum()  # 查看每個列缺失值的數量。

movies.columns  # 獲取 DataFrame 的列名。

# 特徵選擇
movies = movies[['id', 'title', 'overview', 'genre']]  # 選取需要的列。

movies['tags'] = movies['overview'] + movies['genre']  # 組合 'overview' 和 'genre' 列作為新的 'tags' 列。

new_data = movies.drop(columns=['overview', 'genre'])  # 創建新的數據集並去除 'overview' 和 'genre' 列。

from sklearn.feature_extraction.text import CountVectorizer  # 從 scikit-learn 中引入文本特徵提取器。

# 創建 CountVectorizer 對象，用於將文本數據轉換為向量形式。
cv = CountVectorizer(max_features=10000, stop_words='english')  # 設定最大特徵數量並忽略英文停用詞。

vector = cv.fit_transform(new_data['tags'].values.astype('U')).toarray()  # 將 'tags' 列的文本數據轉換為向量。

vector.shape  # 查看向量化後的數據維度。

from sklearn.metrics.pairwise import cosine_similarity  # 引入餘弦相似度計算函數。

# 計算所有電影之間的餘弦相似度。
similarity = cosine_similarity(vector)

new_data[new_data['title'] == "The Godfather"].index[0]  # 查找特定電影 "The Godfather" 在數據集中的索引。

# 找出與第三部電影（索引為 2）最相似的五部電影。
distance = sorted(list(enumerate(similarity[2])), reverse=True, key=lambda vector: vector[1])
for i in distance[0:5]:
    print(new_data.iloc[i[0]].title)

# 定義一個推薦函數，根據給定的電影名稱推薦相似的電影。
def recommend(movies):
    index = new_data[new_data['title'] == movies].index[0]  # 獲取給定電影的索引。
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])  # 計算並排序相似度。
    for i in distance[0:5]:  # 打印前五部最相似的電影標題。
        print(new_data.iloc[i[0]].title)

recommend("Iron Man")  # 調用推薦函數並以 "Iron Man" 為例。

# 使用 pickle 序列化和保存數據
import pickle
pickle.dump(new_data, open('movies_list.pkl', 'wb'))  # 將處理後的新數據集保存到文件。
pickle.dump(similarity, open('similarity.pkl', 'wb'))  # 將餘弦相似度矩陣保存到文件。

pickle.load(open('movies_list.pkl', 'rb'))  # 加載之前保存的數據集文件。
