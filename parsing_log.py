def count_data(key, dict):
    if key in dict.keys():
        dict[key] += 1
    else:
        dict[key] = 1
    return dict


def get_dicts(route):
    file = open(route, 'r')

    ip_dict = {}
    url_dict = {}

    for line in file:
        if line == '\n':
            continue

        try:
            ip = line.split(' ')[0]
            ip_dict = count_data(ip, ip_dict)

            url = line.split('"', 1)[1].split(' ')[1]
            url_dict = count_data(url, url_dict)
        except IndexError:
            continue

    return ip_dict, url_dict


def sort_data(dict):
    list_dict = list(dict.items())
    list_dict.sort(key=lambda i: i[1], reverse=True)
    return list_dict


def beauty_print(data, title):
    from prettytable import PrettyTable

    th = [f'{title}', 'FREQUENCY']

    table = PrettyTable(th)
    while data:
        table.add_row(data[0])
        data = data[1:]
    print(table)


if __name__ == '__main__':
    ips = get_dicts('log.txt')[0]
    urls = get_dicts('log.txt')[1]

    beauty_print(sort_data(ips), 'IP')
    beauty_print(sort_data(urls), 'URL')
