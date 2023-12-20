# WEB.py
import streamlit as st
import pickle
import requests
import random
import streamlit.components.v1 as components

# 使用 Streamlit 的 Markdown 功能來插入自定義的 CSS 樣式。
st.markdown("""
<style>
    /* 設定大字體和粗體樣式給搜尋框 */
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    /* 設定搜尋框的排版樣式 */
    .search-box {
        display: flex;
        justify-content: center;
        margin: 1em;
    }
    /* 設定搜尋框內文字顏色 */
    .stTextInput>div>div>input {
        color: white;
    }
    /* 自定義按鈕樣式 */
    .stButton>button {
        width: 100%;
        height: 2.5em;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 20px;
        transition: background-color 0.3s, box-shadow 0.3s;
    }
    /* 按鈕懸停效果 */
    .stButton>button:hover {
        background-color: #45a049;
        box-shadow: 0 2px 4px #999;
    }
    /* 電影標題樣式 */
    .movie-title {
        color: white;
        font-size: 18px;
        text-align: center;
        margin: 0;
    }
    /* 圖片容器，用於定位和樣式 */
    .image-container {
        position: relative;
        text-align: center;
        color: white;
    }
    /* 設定圖片最大寬度和高度 */
    .image-container img {
        margin-top: 16px;
        margin-bottom: 8px;
        max-width: 100%; /* 控制大小 */
        max-height: 300px; /* 設定最大高度 */
    }
    /* 電影標題的絕對定位和背景樣式 */
    .image-container .title {
        position: absolute;
        bottom: 8px;
        left: 0;
        right: 0;
        background-color: rgba(0, 0, 0, 0.5);
        padding: 4px;
    }
</style>
""", unsafe_allow_html=True)

# 頁面標題
st.markdown("<h1 style='text-align: center; color: white;'>Movie Recommender System</h1>", unsafe_allow_html=True)

# 從 TMDB API 獲取電影海報
def fetch_poster(movie_id):
     # 構造請求 URL
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data = requests.get(url).json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
     return full_path

# 載入電影數據和相似度矩陣
movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))

# 使用 Streamlit 声明自定義組件的位置
imageCarouselComponent = components.declare_component("image-carousel-component", path="frontend/public")

# 創建一個表單用於輸入搜索詞並提交
with st.form(key='my_form'):
    search_term = st.text_input("Search for a movie", key="search_box", on_change=None)
    submit_button = st.form_submit_button(label='Show Recommend')

# 結果顯示區的占位符
results_placeholder = st.empty()

# 生成隨機推薦電影的函數
def random_recommend():
    random_indices = random.sample(range(len(movies)), 10)
    recommend_movie = [movies.iloc[i].title for i in random_indices]
    recommend_poster = [fetch_poster(movies.iloc[i].id) for i in random_indices]
    return recommend_movie, recommend_poster

# 根據輸入的電影名稱推薦電影的函數
def recommend(movie):
    if movie:
        indices = movies[movies['title'].str.contains(movie, case=False)].index
        if not indices.empty:
            index = indices[0]
            distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
            recommend_movie = []
            recommend_poster = []
            for i in distance[1:7]:  # 取前六部電影
                movies_id = movies.iloc[i[0]].id
                recommend_movie.append(movies.iloc[i[0]].title)
                recommend_poster.append(fetch_poster(movies_id))
            return recommend_movie, recommend_poster
    return [], []

# 根據用戶的搜索詞顯示推薦電影
if submit_button:
    if search_term:
        movie_name, movie_poster = recommend(search_term)
        if movie_name:
            with results_placeholder.container():
                st.write(f"Results for '{search_term}':")
                # 分兩排顯示六部推薦電影
                for i in range(0, 6, 3):
                    cols = st.columns(3)
                    for col, name, poster in zip(cols, movie_name[i:i+3], movie_poster[i:i+3]):
                        with col:
                            st.markdown(f"<div class='image-container'><img src='{poster}' class='img-fluid'><p class='movie-title'>{name}</p></div>", unsafe_allow_html=True)
        else:
            results_placeholder.error("No movies found. Try another search term.")
    else:
        results_placeholder.error("Please enter a movie name to search.")
else:
    # 頁面加載但沒有搜索提交時，顯示隨機推薦
    movie_name, movie_poster = random_recommend()
    with results_placeholder.container():
        # 分兩排顯示六部隨機推薦電影
        for i in range(0, 6, 3):
            cols = st.columns(3)
            for col, name, poster in zip(cols, movie_name[i:i+3], movie_poster[i:i+3]):
                with col:
                    st.markdown(f"<div class='image-container'><img src='{poster}' class='img-fluid'><p class='movie-title'>{name}</p></div>", unsafe_allow_html=True)
