class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        filtered_emails = set()
        for email in emails:
            local, server = email.split('@')
            local = local[:local.index('+')]
            local = local.replace('.', '')
            filtered_emails.add('{}@{}'.format(local, server))
        return len(filtered_emails)
