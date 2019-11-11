class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        out = [self.helper(e) for e in emails]
        
        return len(set(out))
        
    
    
    def helper(self, email):
        
        local, domain = email.split("@")
        local = local.split("+")[0].replace(".","")
        return local + "@" + domain
