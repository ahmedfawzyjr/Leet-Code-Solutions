class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """
        Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.
        
        The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).
        The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).
        
        Total Area = Area of Rectangle A + Area of Rectangle B - Area of Intersection.
        
        Area of Intersection:
        The intersection is also a rectangle (if it exists).
        The width of intersection is overlap in x-axis: min(ax2, bx2) - max(ax1, bx1).
        The height of intersection is overlap in y-axis: min(ay2, by2) - max(ay1, by1).
        If width < 0 or height < 0, there is no intersection.
        """
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)
        
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)
        
        overlap_area = 0
        if overlap_width > 0 and overlap_height > 0:
            overlap_area = overlap_width * overlap_height
            
        return area_a + area_b - overlap_area
