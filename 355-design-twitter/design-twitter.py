class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        import heapq

        users = self.following.get(userId, set()) | {userId}
        heap = []

        for user in users:
            if user in self.tweets:
                for time, tweetId in self.tweets[user][-10:]:
                    heapq.heappush(heap, (-time, tweetId))

        result = []

        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1])

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)