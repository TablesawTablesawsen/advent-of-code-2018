def compare_ids(id1, id2):
    assert len(id1) == len(id2)
    differences = 0
    for index, char in enumerate(id1):
        if char != id2[index]:
            differences = differences + 1
    return differences

def check_boxes():
    box_set = set()
    with open('input.txt') as input:
        for box1 in input:
            print(box1)
            for box2 in box_set:
                if compare_ids(box1, box2) == 1:
                    return box1, box2
            box_set.add(box1)

if __name__ == "main":
    print(check_boxes())

# 'tjxmoewpdkyaihvrndwfluwbzc', 
# 'tjxmoewpdkyaihvrndgfluwbzc'