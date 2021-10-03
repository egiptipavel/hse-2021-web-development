from src.models.writer import Writer, list_of_writers


class Query(graphene.ObjectType):
    writer: Writer = graphene.Field(Writer, id=graphene.Int())

    def resolve_writer(self, info, id):
        for w in list_of_writers:
            if w.id == id:
                return w
