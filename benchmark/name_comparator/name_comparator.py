def is_int(c):
    try:
        int(c)
        return True
    except:
        return False


def are_same_type(c1, c2):
    return is_int(c1) == is_int(c2)


def get_parts(name):
    parts = []
    subPart = ""
    previousC = None
    i = 0
    for c in name:
        if are_same_type(previousC, c):
            subPart += c
        else:
            parts.append(subPart)
            subPart = c
        if i == len(name) -1:
            parts.append(subPart)
        previousC = c
        i += 1
    return parts


def compare_names(name1, name2):
    name1Parts = get_parts(name1)
    name2Parts = get_parts(name2)
    print(name1Parts)
    print(name2Parts)


compare_names("Bob001LOL", "Bob002")
