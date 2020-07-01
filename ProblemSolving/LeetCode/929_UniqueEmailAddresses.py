class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = set()
        for email in emails:
            local, domain = email.split("@")
            mod_local = ""
            for s in local:
                if s == '.':
                    continue
                elif s == '+':
                    break
                mod_local += s
            valid_emails.add('{}@{}'.format(mod_local, domain))
            
        return len(valid_emails)
