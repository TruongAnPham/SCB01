
def sort_balls(balls):
    red, white, blue = 0, 0, len(balls) - 1

    while white <= blue:
        if balls[white] == 'red':
            balls[red], balls[white] = balls[white], balls[red]
            red += 1
            white += 1
        elif balls[white] == 'white':
            white += 1
        else:  # balls[white] == 'blue'
            balls[white], balls[blue] = balls[blue], balls[white]
            blue -= 1

    return balls


balls = ['blue', 'white', 'red', 'red', 'blue', 'white']
sorted_balls = sort_balls(balls)
print(sorted_balls)

def intersection(nums1, nums2):
    result = []
    nums1_sorted = sorted(nums1)
    nums2_sorted = sorted(nums2)
    
    i, j = 0, 0
    while i < len(nums1_sorted) and j < len(nums2_sorted):
        if nums1_sorted[i] < nums2_sorted[j]:
            i += 1
        elif nums1_sorted[i] > nums2_sorted[j]:
            j += 1
        else:
            if not result or nums1_sorted[i] != result[-1]:
                result.append(nums1_sorted[i])
            i += 1
            j += 1
    return result


