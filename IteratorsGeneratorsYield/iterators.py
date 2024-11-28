class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list
        self.len_list = len(self.list_of_lists)
        self.main_index = -1
        self.inner_index = -1


    def __iter__(self):
        self.main_index += 1
        return self

    def __next__(self):
        self.inner_index += 1
        if self.inner_index == len(self.list_of_lists[self.main_index]):
            self.main_index += 1
            self.inner_index = 0
        if self.main_index == self.len_list:
            raise StopIteration
        item = self.list_of_lists[self.main_index][self.inner_index]
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('iterators task 1 complete')

# if __name__ == '__main__':
#     test_1()