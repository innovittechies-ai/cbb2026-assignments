# The AI Hiring Challenge
# Ask for the total number of elements in the array
n_input = input("Enter the number of elements in the array: ")
n = int(n_input)

# If there are less than 2 elements, it's trivially sorted
if n < 2:
    if n == 1:
        input("Enter the single element: ")
    print("YES")
else:
    #  array elements separated by spaces
    elements_input = input("Enter the array elements separated by spaces: ")
    arr = list(map(int, elements_input.split()))

    # Create a perfectly sorted version to compare against
    target = sorted(arr)
    mismatch_indices = []

    # Finding where the original array differs from the sorted version
    for i in range(n):
        if arr[i] != target[i]:
            mismatch_indices.append(i)

    # 1. If 0 mismatches: It's already sorted
    if len(mismatch_indices) == 0:
        print("YES")
    # 2. If exactly 2 mismatches: Check if swapping them fixes the array
    elif len(mismatch_indices) == 2:
        i, j = mismatch_indices
        # Perform the swap
        arr[i], arr[j] = arr[j], arr[i]
        
        # Verify if the swap resulted in the target sorted array
        if arr == target:
            print("YES")
        else:
            print("NO")
    # 3. If more than 2 mismatches: It cannot be fixed by a single swap
    else:
        print("NO")