"""
A deque-based sliding window algorithm uses a deque to maintain elements within
a fixed window size. By only storing relevant elements (e.g., indices of maximum values) and
removing elements that fall outside the window, it achieves O(n) time complexity. This
approach is efficient for tasks like finding the maximum of each window in a large array.
"""

from collections import deque


def sliding_window_maximum(nums, k):
    if not nums or k == 0:
        return []

    result = []
    dq = deque()  # Stores indices of elements in the current window

    for i in range(len(nums)):
        # Remove indices of elements not in the sliding window
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove indices of elements smaller than the current element
        # (they cannot be the maximum in this window or any subsequent window)
        while dq and nums[i] > nums[dq[-1]]:
            dq.pop()

        # Add the current element's index
        dq.append(i)

        # Append the maximum for the current window to the result
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Example Usage
numbers = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(sliding_window_maximum(numbers, k))


