import graphene


class Book(graphene.ObjectType):
    title: str = graphene.String()
    description: str = graphene.String()
    number_of_pages: int = graphene.Int()

    def __init__(self, title: str, description: str, number_of_pages: int):
        self.title = title
        self.description = description
        self.number_of_pages = number_of_pages
