class Solution:
    def numUniqueEmails(self, emails: 'List[str]') -> 'int':
        result = []
        for i in emails:
            local = i.split("@")[0]
            far = i.split("@")[1]
            if '+' in local:
                local = local.split("+")[0]
            if '.' in local:
                local = local.replace('.', '')
            email = local + far
            if email not in result:
                result.append(email)
        return len(result)
