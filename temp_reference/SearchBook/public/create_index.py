import json
import pickle
import re
from collections import defaultdict

def create_index():
    # Read scraped book data
    books = []
    with open('/project/sandbox/user-workspace/temp_reference/web_scrap/book_list.txt', 'r') as f:
        for line in f:
            books.append(json.loads(line))

    # Create inverted index
    index = defaultdict(list)
    for book in books:
        title = book['book_title']
        words = re.findall(r'\w+', title.lower())
        for word in set(words):  # Use set to avoid duplicate words
            index[word].append({
                'title': title,
                'url': book['url'],
                'image': book['image-url'],
                'price': book['price'],
                'score': 1.0  # Simple scoring for now
            })

    # Save index
    with open('indexdb', 'wb') as f:
        pickle.dump(dict(index), f)

if __name__ == '__main__':
    create_index()