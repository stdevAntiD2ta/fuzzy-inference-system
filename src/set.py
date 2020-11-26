from .membership import Membership
from numpy import arange

class Set:
    def __init__(self, membership, step=0.05, name="Fuzzy Set"):
        self.membership = membership
        self.step = step
        self.name = name

    def __or__(self, other_set):
        return self.union(other_set)

    def union(self, other_set):
        '''
        T-conorm union
        '''
        items = self.membership.items + other_set.membership.items
        items.sort()
        memb = Membership(
            lambda x: max(
                self.membership(x),
                other_set.membership(x)
            ),
            items
        )
        return Set(memb, step=min(self.step, other_set.step), name=f'{self.name}_union_{other_set.name}')

    def __and__(self, other_set):
        return self.intersection(other_set)

    def intersection(self, other_set):
        '''
        T-norm union
        '''
        items = self.membership.items + other_set.membership.items
        items.sort()
        memb = Membership(
            lambda x: min(
                self.membership(x),
                other_set.membership(x)
            ),
            items
        )
        return Set(memb, step=min(self.step, other_set.step), name=f'{self.name}_intersection_{other_set.name}')

    def domain(self):
        d = set(arange(self.membership.items[0], self.membership.items[-1], self.step))
        d.update(set(self.membership.items))
        if len(d) > 100:
            d = list(d)
            d.sort()
        return list(d)

    def __iter__(self):
        return iter(self.domain())

    def __len__(self):
        return len(self.domain())

    def __str__(self):
        return self.name