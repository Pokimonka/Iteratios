class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.main_index = 0
        self.tmp_index = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.main_index >= len(self.list_of_lists):
            if self.tmp_index:
                self.list_of_lists, self.main_index = self.tmp_index.pop()
                return next(self)
            else:
                raise StopIteration

        item = self.list_of_lists[self.main_index]
        self.main_index += 1

        if isinstance(item, list):
            self.tmp_index.append((self.list_of_lists, self.main_index))
            self.list_of_lists = item
            self.main_index = 0
            return next(self)
        else:
            return item


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    print('iterators task 3 complete')

# if __name__ == '__main__':
#      test_3()