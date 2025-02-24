import pytest


class Article:
    _all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise Exception
        if not isinstance(magazine, Magazine):
            raise Exception
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise Exception
        self._author = author
        self._magazine = magazine
        self._title = title
        Article._all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise Exception
        self._magazine = value