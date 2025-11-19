class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception("Author must be of type Author")
        if not isinstance(magazine, Magazine):
            raise Exception("Magazine must be of type Magazine")
        if not isinstance(title, str):
            raise Exception("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise Exception("Title must be between 5 and 50 characters, inclusive")
        
        self._title = title
        self._author = author
        self._magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        
        if hasattr(self, '_title'):
            pass  
        else:
            self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception("Magazine must be of type Magazine")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be of type str")
        if len(name) == 0:
            raise Exception("Name must be longer than 0 characters")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        if hasattr(self, '_name'):
            pass  
        else:
            self._name = value

    def articles(self):
        """Returns a list of all articles the author has written"""
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        """Returns a unique list of magazines the author has contributed to"""
        return list(set([article.magazine for article in self.articles()]))

    def add_article(self, magazine, title):
        """Creates and returns a new Article instance"""
        return Article(self, magazine, title)

    def topic_areas(self):
        """Returns a unique list of categories of magazines the author has contributed to"""
        articles = self.articles()
        if not articles:
            return None
        return list(set([article.magazine.category for article in articles]))


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            pass  
        elif not (2 <= len(value) <= 16):
            pass  
        else:
            self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            pass  
        elif len(value) == 0:
            pass  
        else:
            self._category = value

    def articles(self):
        """Returns a list of all articles the magazine has published"""
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        """Returns a unique list of authors who have written for this magazine"""
        return list(set([article.author for article in self.articles()]))

    def article_titles(self):
        """Returns a list of titles of all articles written for this magazine"""
        articles = self.articles()
        if not articles:
            return None
        return [article.title for article in articles]

    def contributing_authors(self):
        """Returns authors who have written more than 2 articles for the magazine"""
        from collections import Counter
        articles = self.articles()
        if not articles:
            return None
        
        author_counts = Counter([article.author for article in articles])
        contributors = [author for author, count in author_counts.items() if count > 2]
        
        return contributors if contributors else None

    @classmethod
    def top_publisher(cls):
        """Returns the Magazine instance with the most articles"""
        if not Article.all:
            return None
        
        magazine_counts = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_counts[magazine] = magazine_counts.get(magazine, 0) + 1
        
        if not magazine_counts:
            return None
        
        return max(magazine_counts, key=magazine_counts.get)