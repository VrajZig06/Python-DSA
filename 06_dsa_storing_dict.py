# Create Hash Map 

def create_map(nums: list):
    data_map = {}

    for i in range(len(nums)):
        data_map[nums[i]] = data_map.get(nums[i], 0) + 1

    return data_map

print(f"Dictionary :: {create_map([1,1,12,3,4,56,1])}")