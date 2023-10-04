def trap(heights):
    water = 0
    (left , right) = (0 , len(heights) -1 )
    max_left = heights[left]
    max_right = heights[right]
    while left < right:
        if heights[left] <= heights[right]:
            left += 1
            max_left = max(max_left, heights[left])
            water += (max_left - heights[left])
        else :
            right -= 1
            max_right = max(max_right , heights[right])
            water += (max_right - heights[right])
    
    return water
            


if __name__ == '__main__':
 
    heights = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5]
    print("The maximum amount of water that can be trapped is", trap(heights))