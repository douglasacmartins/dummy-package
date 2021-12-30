from datetime import (
        datetime as dt_datetime,
        timedelta as dt_timedelta
    )
from _strptime import TimeRE


def date_parser(
        date_range: str,
        input_format: str = '%Y%m%d',
        output_format: str = '%Y%m%d',
        reverse: bool = True
) -> list:
    """
        Generates an ordered list with all dates from specified range

        Hyphen return a date range from most recent to least one.
            e.g.: A-Z => Z,Y,...,A
        Comma return ordered date from most recent to least one.
            e.g.: C,D,A,B => D,C,B,A
        You can use any combination of both, that will not incur in duplicate
    data.
            e.g.: L,A-D,C,N => N,L,D,C,B,A
    """
    date_pattern = TimeRE().compile(input_format)
    sanitized_date = date_pattern.split(date_range)

    sanitized_length = len(sanitized_date)
    null_items = sanitized_date.count('')
    valid_items = sum(map(sanitized_date.count, ['-', ',']))
    groups = date_pattern.groups

    invalid_split = (sanitized_length - valid_items - null_items) % groups != 0

    if null_items != 2 or invalid_split:
        raise ValueError(f'Invalid date format: {date_range}')

    date_range = ''.join(sanitized_date[1:-1])

    input_format = input_format.replace('-', '').replace(',', '')

    dates = date_range.split(',')

    result = set()

    for date in dates:
        if '-' not in date:
            result.add(dt_datetime.strptime(date, input_format).date())
        else:
            _date = date.split('-')
            if len(_date) > 2:
                raise ValueError(f'Invalid range: {date}')
            _date = [
                dt_datetime.strptime(x, input_format).date()
                for x in _date
            ]
            _date_start = min(_date)
            _date_end = max(_date)
            _date_difference = abs(_date_end - _date_start).days
            result.update([(
                _date_start + dt_timedelta(days=x))
                for x in range(_date_difference+1)
            ])

    return [x.strftime(output_format) for x in sorted(result, reverse=reverse)]
