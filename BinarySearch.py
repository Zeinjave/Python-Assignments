# Global variables to count recursions and comparisons
recursions = 0
comparisons = 0

def binary_search(nums, target, lower, upper):
    global recursions, comparisons
    
    # Increment the recursion count for each function call
    recursions += 1

    # Base case: if the bounds are invalid, the target is not in the list
    if lower > upper:
        return -1
    
    # Find the middle index
    mid = (lower + upper) // 2
    
    # Increment the comparison count (this is a comparison)
    comparisons += 1
    
    # Check if the target is at the middle index
    if nums[mid] == target:
        return mid
    # If target is greater, search the right half
    elif nums[mid] < target:
        return binary_search(nums, target, mid + 1, upper)
    # If target is smaller, search the left half
    else:
        return binary_search(nums, target, lower, mid - 1)

if __name__ == '__main__':
    # Input a list of nums from the first line of input
    nums = [int(n) for n in input().split()]
    
    # Input a target value
    target = int(input())

    # Start off with default values: full range of list indices
    index = binary_search(nums, target, 0, len(nums) - 1)

    # Output the index where target was found in nums, and the
    # number of recursions and comparisons performed
    print(f'index: {index}, recursions: {recursions}, comparisons: {comparisons}')
