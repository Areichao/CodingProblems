import itertools
import collections
import heapq
class Twitter:

    def __init__(self):
        """ initialize the original time stamp, user following list, and user posts """  
        self.time = itertools.count(step=-1) # automatically goes down, so smallest value (newest post) will be "highest" in heap
        self.following = collections.defaultdict(set) # userId: set
        self.tweets = collections.defaultdict(collections.deque) # userId: collections.deque

    def postTweet(self, userId: int, tweetId: int) -> None:
        """ user with userId posts a tweet tweetId """
        self.tweets[userId].appendleft((next(self.time), tweetId)) # append left because newest (kind of like stack from left) and next() iterates counter

    def getNewsFeed(self, userId: int) -> List[int]:
        """ gets 10 most recent with items posted by user or people user follows in order from most to least recent """
        users = self.following[userId] | {userId} # combine all following + the user themselved
        newTweets = [] # the max heap that we will use, python automatically does a min heal
        top10 = []

        # create original with all recent tweets
        for user in users:
            if self.tweets[user]: # if the user has atleast one tweet
                time, id = self.tweets[user][0]
                heapq.heappush(newTweets, (time, id, user, 0)) # (time, tweetId, userId, index of user post)

        # while top10 is less than 10 append the newest tweet from heapq
        while newTweets and len(top10) < 10:
            # take the newest tweet of them all.... pop from heapq
            _, id, user, index = heapq.heappop(newTweets)

            # append newest to our answer
            top10.append(id)

            # if the user we took from has a next tweet, append that into the heap of tweets
            if len(self.tweets[user]) > index + 1:
                time, id = self.tweets[user][index + 1]
                heapq.heappush(newTweets, (time, id, user, index + 1))
            
        return top10



    def follow(self, followerId: int, followeeId: int) -> None:
        """ function called when a user follows another user """
        # default dict will set it to set() automatically, then .add() will just do nothing if its a duplicate.
        # error check we can do is check if value is an integer for both, and also to make sure its not the same ID (cannot follow self)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """ function called when a user unfollows another user """
        # error check we can do is check that followerId is an integer
        self.following[followerId].discard(followeeId) # discard does nothing if value doesnt exist

            
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)