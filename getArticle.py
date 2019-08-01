import os
from newspaper import Article

articleCount = 3
newsList_dir = os.path.dirname(__file__)
rel_path = "newslist/recentarticles.txt"
full_file_path = os.path.join(newsList_dir, rel_path)
recentFileList = open(full_file_path, 'r')

i = 1 
for line in recentFileList:
    line = line.strip()
    print('################### Start ###################')
    print('################### Article ',i,' ###################')
    print('Article URL: ',line)
    currentArticle = Article(url=line)
    #currentArticle = Article(url='http://cnn.com/2019/07/30/africa/erick-kabendera-arrest-tanzania-intl/index.html')
    # Download the article 
    currentArticle.download()
    # Parse the article 
    currentArticle.parse()
    # Save the article 
    #currentArticle.parse() 
    rel_path = 'articlelist/' + currentArticle.title + '.html'
    full_file_path = os.path.join(newsList_dir, rel_path)
    print('full path is', full_file_path)
    #articlecontent = open('fanfan1.txt', 'w')
    articlecontent = open(full_file_path, 'a+')
    articlecontent.write(currentArticle.html)
    #articlecontent.write('hihihi')
    articlecontent.close()
    # Display the title 
    print('Article title:', currentArticle.title)
    # Display the author 
    print('Article author:', currentArticle.authors)
    # Display the images 
    print('Article Image list:', currentArticle.images)
    # Display the movies 
    print('Article Videos', currentArticle.movies)
    # Display the text 
    print('Artitle Text:', currentArticle.text)
    # NLP 
    currentArticle.nlp()
    # NLP - summary 
    print('Artitle summary:', currentArticle.summary)
    # NLP - keywords 
    print('Artitle keywords:', currentArticle.keywords)
    print('################### End ###################')
    print('################### Article ',i,' ###################')
 
    i = i + 1 
    if i >= articleCount + 1   :
        break
recentFileList.close()