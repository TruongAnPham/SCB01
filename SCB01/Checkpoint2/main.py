def merge_arrays(nums1, nums2):
    merged_array = [0] * (len(nums1) + len(nums2))
    
    i, j, k = 0, 0, 0
    
    while i < len(nums1) and j < len(nums2): #dung cho den khi 1 trong 2 dieu kien khong con dung nua
        if nums1[i] <= nums2[j]:
            merged_array[k] = nums1[i]
            i += 1
        else:
            merged_array[k] = nums2[j]
            j += 1
        k += 1
    
    while i < len(nums1): #Vong lap while sao chep cac du lieu con lai trong num vao mang cho den khi het data
        merged_array[k] = nums1[i]
        i += 1
        k += 1
    
    while j < len(nums2):
        merged_array[k] = nums2[j]
        j += 1
        k += 1
    
    return merged_array

nums1 = [1, 3, 5, 7]
nums2 = [1, 2, 4, 7, 8, 9]
result = merge_arrays(nums1, nums2)
print(result)