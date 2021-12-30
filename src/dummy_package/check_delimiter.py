from collections import Counter


def check_delimiter(data_sample: list) -> str:
    """
        Check separator from any text data sample
    """
    common_delimiter = list(',;:|\t')
    struct_counter = Counter()
    counter = Counter()
    for i, line in enumerate(data_sample, 1):
        if isinstance(line, bytes):
            line = line.decode('utf-8', 'replace')
        delimiter_count = dict(
            zip(
                common_delimiter,
                map(line.count, common_delimiter)
            )
        )
        struct_counter.update(delimiter_count.items())
        counter.update(delimiter_count)
    else:
        num_of_lines = i

    for k, v in struct_counter.items():
        # Remove any delimiter that is not present in every line
        # Any error raised means that the value has already been removed
        if v != num_of_lines or k[1] == 0:
            try:
                counter.pop(k[0])
            except KeyError:
                pass
    return counter.most_common(1)[0][0]
