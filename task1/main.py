def geo_logs(geo_logs_data):
    return [k for visit in geo_logs_data for k, v in visit.items() if v[1] == 'Россия']


def uniq_ids(ids):
    result = []
    for numbers in ids.values():
        for num in numbers:
            if num not in result:
                result.append(num)
    return result


def max_sales(max_sales_data):
    if max_sales_data:
        return max(max_sales_data, key=max_sales_data.get)
    else:
        return None
