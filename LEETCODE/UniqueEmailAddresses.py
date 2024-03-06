class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
    # Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
        emailslist = {} # dictionary with all emails
        counter = 0 # counts number of unique emails
        for email in emails:
            localDomain = email.split("@") # separate local and domain
            local = localDomain[0].split("+") # take first for local
            newLocal = local[0].replace(".", "") # replace all periods
            newEmail = newLocal + "@" + localDomain[1] # new email address

            if newEmail not in emailslist: # if not in dictionary, add 1
                emailslist[newEmail] = 1
                counter += 1 
        return counter 



