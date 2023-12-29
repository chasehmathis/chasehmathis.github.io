class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    def longestConsecutive1(self, nums: List[int]) -> int:

        d = collections.defaultdict(set)

        lst = [None]*len(nums)

        lookfor_set = set()

        for num in nums:
            if num in lookfor_set:

                # find the number we already saw
                # for 2 we are looking for 1 or 3

                if num - 1 in d:
                    d[num -1].add(num)

                if num + 1 in d:
                    d[num + 1].add(num)

                if num +1 in d and num-1 in d:
                    # add the higher to the lower
                    d[num-1] = d[num-1].union(d[num+1])
                    
                    # delete the higher
                    d.pop(num+1)

            if num in d:
                continue

            d[num] = set([num])
            lookfor_set.add(num - 1)
            lookfor_set.add(num + 1)

        print(d)

        return 5

