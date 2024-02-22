from itertools import combinations

class SubsetGenerate:
    def __init__(self, input_list):
        self.input_list = input_list

    def get_subsets(self):
        subsets = []
        for i in range(1, len(self.input_list)+1):
            subsets.extend(list(combinations(self.input_list, i)))
        return [list(subset) for subset in subsets]

input_l = [4, 5, 6]
subset_generator = SubsetGenerate(input_l)
print(subset_generator.get_subsets())
