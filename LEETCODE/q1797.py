from collections import OrderedDict
import logging

logging.basicConfig(level=logging.INFO)

log = logging.getLogger(__name__)
class AuthenticationManager:
    def __init__(self, timeToLive: int):
        """ constructs authentication and time to live """
        # Time O(1) space O(n)
        self.lifespan = timeToLive
        self.tokens = OrderedDict() # STORE EXPIRY TIMES FOR EASIER ACCESS
    def generate(self, tokenID: str, currentTime: int) -> None:
        """ generates a new token with the given tokenID at the current currentTime in seconds. """
        # error handling
        if not isinstance(tokenID, str) or not isinstance(currentTime, int):
            raise TypeError("Token must be string and current time must be integer (seconds)")
        if currentTime < 0:
            raise ValueError("Current time must be a positive integer")
        # O(n) worst case for deletion of old tokens, O(1) insert. O(1) space
        # delete old tokens so old instance can be nuked (same id but expired)
        self._evictExpired(currentTime)
        # otherwise, add it if its not already generated
        if tokenID not in self.tokens:
            self.tokens[tokenID] = currentTime + self.lifespan
        # in an interview maybe ask if it should be renewed here
    def renew(self, tokenID: str, currentTime: int) -> None:
        """ renews UNEXPIRED token with tokenID at currentTime in seconds. if expired, ignore. """
        # O(n) worst case deletion, O(1) otherwise. O(1) space
        expiry = self.tokens.pop(tokenID, None) # pops and deletes
        # if it exists, and its not expired, add with new current time
        if expiry and currentTime < expiry:
            self.tokens[tokenID] = currentTime + self.lifespan
    def countUnexpiredTokens(self, currentTime: int) -> int:
        """ returns number of unexpired tokens at currentTime in seconds """
        # O(n) worst case deletion, O(1) for length returning. O(1 space)
        # garbage cleanup yay
        self._evictExpired(currentTime)
        # now just return length
        return len(self.tokens)
        
    def _evictExpired(self, currentTime: int) -> None:
        """ garbage cleanup like function to get rid of tokens which are expired """
        # O(n) worst case for case where they are all inside
        while self.tokens:  
            # gets the next item of iterator version of dict
            expiry = next(iter(self.tokens.values()))
            # if the time is not expired, break loop
            if currentTime < expiry:
                break
            # otherwise, delete item 
            self.tokens.popitem(last=False)
    