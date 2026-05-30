class BrowserHistory:
    def __init__(self, homepage: str):
        """ initializes the homepage of the browser """
        self.homepage = homepage
        self.history = [self.homepage]
        self.current = 0

    def _is_valid_url(self, url: str) -> bool:
        """ returns true if valid url """
        return url.startswith(("http://", "https://"))
    
    def visit(self, url: str) -> None:
        """ visits url from current page. clears all forward history """
        # error handling
        if not isinstance(url, str):
            raise TypeError("url must be a string")
        elif not self._is_valid_url(url):
            raise ValueError("Invalid url link")
        # clear everything after current index
        del self.history[self.current + 1:]
        self.history.append(url)
        self.current += 1
    
    def back(self, steps: int) -> str:
        """ move steps back in history or go back to the original url if steps > history. return current url """
        # error check for input
        if steps < 0:
            raise ValueError("Steps must be non negative")
        # if there are more steps than visited urls, go back to homepage
        self.current = 0 if steps >= self.current else self.current - steps
        return self.history[self.current]
    
    def forward(self, steps: int) -> str:
        """ move steps foward in history returns current url. go to last possible url if steps is greater than foward urls """
        if steps < 0:
            raise ValueError("Steps must be non negative")
        self.current = (len(self.history) - 1) if steps >= (len(self.history) - self.current - 1) else self.current + steps
        return self.history[self.current]


    