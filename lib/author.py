import pytest


class Author:
    _all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string")
        self._name = name
        Author._all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError("Name is immutable")

    def articles(self):
        from article import Article
        return [article for article in Article._all if article.author == self]

    def magazines(self):
        from magazine import Magazine
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        from article import Article
        return Article(self, magazine, title)

    def topic_areas(self):
        if not self.articles():
            return None
        return list(set(article.magazine.category for article in self.articles()))