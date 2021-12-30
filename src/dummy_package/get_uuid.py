from uuid import uuid1, uuid5, UUID


def get_uuid(uuid: str = None, entity: str = None) -> uuid1 or uuid5:
    """
        Generate UUID with chained uuid1 and uuid5
    """
    if not uuid:
        return uuid1()
    else:
        return uuid5(UUID(uuid), entity)
