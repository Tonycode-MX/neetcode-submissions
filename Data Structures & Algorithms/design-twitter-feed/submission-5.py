class Twitter:

    def __init__(self):
        self.users = {}
        self.tweets = []
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = set()

        self.tweets.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []


        for i in range(len(self.tweets)-1,-1,-1):
            author = self.tweets[i][0]
            tweet = self.tweets[i][1]

            if author == userId or (userId in self.users and author in self.users[userId]):
                feed.append(tweet)

            if len(feed) == 10:
                break

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId not in self.users:
            self.users[followerId] = set()

        self.users[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            self.users[followerId].discard(followeeId)
        
