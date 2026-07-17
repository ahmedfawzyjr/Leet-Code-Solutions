import heapq
from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Calculates the room that held the most meetings.
        If there are multiple such rooms, returns the room with the lowest number.
        """
        # Sort meetings by their start time
        meetings.sort(key=lambda x: x[0])
        
        # Min-heap of free rooms
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        
        # Min-heap of busy rooms storing tuples of (end_time, room_index)
        busy_rooms = []
        
        # Count of meetings held in each room
        room_count = [0] * n
        
        for start, end in meetings:
            # Release all rooms that have finished their meetings by the start time of the current meeting
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                # If there is a free room, allocate the lowest numbered one
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (end, room))
                room_count[room] += 1
            else:
                # If all rooms are busy, delay the current meeting
                earliest_end, room = heapq.heappop(busy_rooms)
                new_end = earliest_end + (end - start)
                heapq.heappush(busy_rooms, (new_end, room))
                room_count[room] += 1
                
        # Find the room with the maximum number of meetings
        max_meetings = max(room_count)
        for room in range(n):
            if room_count[room] == max_meetings:
                return room
        return 0

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    print(f"Example 1: {sol.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]])}")  # Expected: 0
    # Example 2
    print(f"Example 2: {sol.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]])}")  # Expected: 1
