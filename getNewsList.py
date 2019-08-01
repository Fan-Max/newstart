import newspaper
import os

#Build source

cnn_paper= newspaper.build('http://cnn.com', language='en')
# for category in cnn_paper.category_urls():
#     print(category)

#Extracting recent articles
newsList_dir = os.path.dirname(__file__)
rel_path = "newslist/recentarticles.txt"
full_file_path = os.path.join(newsList_dir, rel_path)
recentarticles = open(full_file_path, 'w')
for article in cnn_paper.articles:
    print(article.url)
    recentarticles.write(article.url)
    recentarticles.write('\n')
print('There are ',cnn_paper.size(),' articles.')
recentarticles.close()


#Extracting source categories
i = 1 
rel_path = "newslist/newscategory.txt"
full_file_path = os.path.join(newsList_dir, rel_path)
newscategory = open(full_file_path, 'w')
for category in cnn_paper.category_urls():
    print('Category: ', i ,' :', category)
    i = i + 1 
    newscategory.write(category)
    newscategory.write('\n')
newscategory.close()

#Extracting source feeds
i = 1 
rel_path = "newslist/newsfeed.txt"
full_file_path = os.path.join(newsList_dir, rel_path)
newsfeed = open(full_file_path, 'w')
for feed_url in cnn_paper.feed_urls():
    print('feed ',i, ' :',feed_url)
    newsfeed.write(feed_url)
    newsfeed.write('\n')
newsfeed.close()