
# Strategy pattern allows you to switch the algorithm or strategy based upon the situation.

# In computer programming, the strategy pattern (also known as the policy pattern) is a behavioural software design pattern that enables an algorithm's behavior to be selected at runtime.


class SortStrategy:
    def sort(self, dataset):
        return []

class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset):
        print("Sorting using Bubble Sort")
        return dataset

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset):
        print("Sorting using Quick Sort")
        return dataset

class Sorter:
    
    _sorter = None
    
    def __init__(self, sorter):
        self._sorter = sorter
    
    def sort(self, dataset):
        self._sorter.sort(dataset)

dataset = [1, 5, 4, 3, 2, 8]
sorter = Sorter(BubbleSortStrategy())
sorter.sort(dataset)

sorter = Sorter(QuickSortStrategy())
sorter.sort(dataset)