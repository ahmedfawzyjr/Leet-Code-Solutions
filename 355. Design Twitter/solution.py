from typing import List
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.timestamp = 0
        # userId -> list of (timestamp, tweetId)
        self.tweets = defaultdict(list)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1 # Use negative for min-heap to act as max-heap
        self.tweets[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []
        
        # Add user's own tweets and followees' tweets to heap
        # We only need the latest 10 tweets from each
        users_to_check = self.following[userId] | {userId}
        
        for u_id in users_to_check:
            if u_id in self.tweets:
                index = len(self.tweets[u_id]) - 1
                time, t_id = self.tweets[u_id][index]
                # (timestamp, tweetId, userId, next_index)
                heapq.heappush(min_heap, (time, t_id, u_id, index - 1))
        
        while min_heap and len(res) < 10:
            time, t_id, u_id, next_idx = heapq.heappop(min_heap)
            res.append(t_id)
            if next_idx >= 0:
                next_time, next_t_id = self.tweets[u_id][next_idx]
                heapq.heappush(min_heap, (next_time, next_t_id, u_id, next_idx - 1))
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
