class Twitter:
    def __init__(self):
        self.users = defaultdict(list) # userID, [tweetID1, tweetID2, ...]
        self.followers = defaultdict(list) # userID, [following1, following2, ...]
        self.tweets = [] # [tweetID1, tweetID2, ...]

    # publish new tweet with tweetID 
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.users[userId].append(tweetId)
        self.tweets.append(tweetId)

    # get 10 most recent tweet IDs from userID's/following tweets
    def getNewsFeed(self, userId: int) -> List[int]:
        # loop through self.tweets and check if it is in myself or my followers

        # initial set of tweets with only my tweets
        twts = set(self.users[userId])
        # list of userId's that I follow
        fllwrs = self.followers[userId]
        # add each tweet from my followers into set of tweets
        for f in fllwrs:
            twts = twts | set(self.users[f])
        # counter to make sure we dont go over 10 tweets
        counter = 0
        res = []
        # loop from most recent to least recent, building res array with tweets until 10 tweets or no more
        for i in range(len(self.tweets) - 1, -1, -1):
            if counter == 10:
                break
            if self.tweets[i] in twts:
                res.append(self.tweets[i])
                counter += 1
        return res

    # follower follows followee
    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.followers[followerId]:
            self.followers[followerId].append(followeeId)

    # follower unfollows followee
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId) # O(n)
