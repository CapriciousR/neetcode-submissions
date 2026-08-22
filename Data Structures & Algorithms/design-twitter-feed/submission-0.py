class Twitter:

    def __init__(self):
        from collections import defaultdict
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.following[userId].add(userId)

        for followeeId in self.following[userId]:
            if self.tweets[followeeId]:
                index = len(self.tweets[followeeId]) - 1
                time, tweetId = self.tweets[followeeId][index]
                min_heap.append((time, tweetId, followeeId, index - 1))
        
        heapq.heapify(min_heap)

        while min_heap and len(res) < 10:
            time, tweetId, followeeId, next_idx = heapq.heappop(min_heap)
            res.append(tweetId)
            
            if next_idx >= 0:
                next_time, next_tweetId = self.tweets[followeeId][next_idx]
                heapq.heappush(min_heap, (next_time, next_tweetId, followeeId, next_idx - 1))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
