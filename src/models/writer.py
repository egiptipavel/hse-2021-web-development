from typing import List

import graphene
from src.models.book import Book


class Writer(graphene.ObjectType):
    id: int = graphene.Int()
    name: str = graphene.String()
    biography: str = graphene.String()
    books: List[Book] = graphene.List(Book)

    def __init__(self, id: int, name: str, biography: str, books: List[Book]):
        self.id = id
        self.name = name
        self.biography = biography
        self.books = books


list_of_writers: List[Writer] = [
    Writer(1, "Leo Tolstoy", "Born to an aristocratic Russian family in 1828.",
           [Book("War and peace",
                 "War and Peace is a novel by the Russian author Leo Tolstoy.",
                 2080),
            Book("Anna Karenina",
                 "Anna Karenina is a novel by the Russian author Leo Tolstoy, first published in book form in 1878.",
                 864)]),
    Writer(2, "Fyodor Dostoevsky", "Born in Moscow in 1821.",
           [Book("Crime and Punishment",
                 "Crime and Punishment is a novel by the Russian author Fyodor Dostoevsky.",
                 331)]),
    Writer(3, "Anton Chekhov",
           "Anton Chekhov was born in 1860 in Taganrog",
           [Book("The man in a case",
                 "",
                 12)])
]
