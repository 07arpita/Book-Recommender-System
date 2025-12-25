# Book Recommender System 📚

A comprehensive Machine Learning project that suggests books to users based on their interests. This system uses **Collaborative Filtering** and is served via a **Flask** web application.
# Features:
- **Top 50 Books:** Displays the most popular books based on average ratings and number of votes.
- **Search-Based Recommendation:** Recommends 4-5 similar books when a user enters a title they like.
- **Responsive UI:** A clean, user-friendly interface built with HTML, CSS, and Bootstrap.

# How it Works:
The recommendation engine is built using **Collaborative Filtering**.
1. **Data Cleaning:** Filtered users who have provided more than 200 ratings and books with more than 50 ratings to ensure data quality.
2. **Matrix Pivoting:** Created a pivot table with `Book-Title` as the index and `User-ID` as columns.
3. **Similarity Calculation:** Used **Cosine Similarity** to calculate the distance between book vectors in a high-dimensional space.

# Tech Stack:
- **Language:** Python 3.12
- **Data Analysis:** Pandas, NumPy
- **Machine Learning:** Scikit-Learn (Cosine Similarity)
- **Web Framework:** Flask
- **Frontend:** HTML, CSS, Bootstrap

# Project Structure:
├── app.py              # Flask server & Recommendation Logic
├── popular.pkl         # Serialized data for the homepage
├── pt.pkl              # Pivot Table for similarity search
├── books.pkl           # Cleaned book metadata
├── similarity_scores.pkl # Pre-computed Cosine Similarity matrix
├── templates/          # HTML files (index.html, recommend.html)
└── static/             # CSS & Image assets

INSTALLATION AND SETUP:
- git clone [https://github.com/YOUR_USERNAME/Book-Recommender-System.git](https://github.com/YOUR_USERNAME/Book-Recommender-System.git)
- pip install -r requirements.txt
- python app.py
- Open your browser and go to thw given http



