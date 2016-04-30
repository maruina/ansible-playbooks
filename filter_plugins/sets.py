"""To be deleted once https://github.com/ansible/ansible/pull/15062 has been merged"""

def issubset(a, b):
    return set(a) <= set(b)

def issuperset(a, b):
    return set(a) >= set(b)


class FilterModule(object):

    def filters(self):
        return {
            'issubset': issubset,
            'issuperset': issuperset,
        }
