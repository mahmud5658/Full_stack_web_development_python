def find_max(li):
    if len(li)==0:
        return None
    max_item = li[0]
    for item in li:
        if item> max_item:
            max_item = item
    return max_item


numbers = [2,50,5,71,20,51,70]

print(find_max(numbers))