from collections.abc import Iterable, Generator


def count_elements(iterable: Iterable) -> dict:
    """Count elements in any iterable object"""
    _dict = dict()
    for elem in iterable:
        _dict[elem] = _dict.get(elem, 0) + 1
    else:
        return _dict


def iter_chain(iterable: Iterable) -> Generator:
    """Chain multiple iterable objects"""
    for obj in iterable:
        yield from obj


def flatify(data: dict or list) -> dict:
    flat_path = list()
    flat_dict_index = list()
    flat_layer = 0
    temp_dict = dict()

    def recursive_call(data: object, key: str = None) -> None:
        nonlocal flat_path
        nonlocal flat_layer
        nonlocal flat_dict_index
        nonlocal temp_dict

        if type(data) is list:
            for index, item in enumerate(data):
                flat_dict_index.insert(flat_layer, index)
                if key is not None:
                    flat_path.append(f'{key}{index}')
                    flat_layer += 1
                recursive_call(item)
                flat_dict_index.pop()
                if key is not None:
                    flat_path.pop()
                    flat_layer -= 1
        elif type(data) is dict:
            if key is not None:
                flat_path.append(key)
                flat_layer += 1
            for k in data:
                recursive_call(data[k], k)
            if key is not None:
                flat_path.pop()
                flat_layer -= 1
        else:
            flat_path.append(key)
            flat_layer += 1
            temp_dict[tuple(flat_path)] = data
            flat_path.pop()
            flat_layer -= 1

    recursive_call(data)

    return temp_dict
