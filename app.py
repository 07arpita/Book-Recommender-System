from flask import Flask,render_template,request
import pickle
import numpy as np

# 1. Load the files
popular_df = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
similarity_scores = pickle.load(open('similarity_scores.pkl','rb'))

# 2. FIX: Merge popular_df with books to get the missing 'Book-Author' and 'Image-URL-M'
# We drop duplicates to ensure we don't get multiple rows for the same book title
popular_df = popular_df.merge(books, on='Book-Title').drop_duplicates('Book-Title')[['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_ratings'].values),
                           rating=list(popular_df['avg_rating'].values)
                           )

@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    user_input = request.form.get('user_input')

    # 1. Check if the book exists in our Pivot Table
    if user_input not in pt.index:
        # If not found, stay on the page and maybe show an error (optional)
        return render_template('recommend.html', error="Book not found! Please try another title.")

    # 2. If it exists, proceed with the logic
    index = np.where(pt.index == user_input)[0][0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        # Use drop_duplicates to ensure we only get one result per title
        final_temp = temp_df.drop_duplicates('Book-Title')

        item.extend(list(final_temp['Book-Title'].values))
        item.extend(list(final_temp['Book-Author'].values))
        item.extend(list(final_temp['Image-URL-M'].values))

        data.append(item)

    return render_template('recommend.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)