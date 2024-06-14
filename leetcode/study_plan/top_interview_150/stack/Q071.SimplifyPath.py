class Solution:
    def simplifyPath(self, path: str) -> str:

        ans = ['']

        path = path.replace('//', '/')
        path = path.split('/')
        for d in path:
            if d == '..':
                if ans:
                    ans.pop()
                if not ans:
                    ans.append('')
            elif d == '.' or d == '':
                continue
            else:
                ans.append(d)

        return '/'.join(ans) if len(ans) > 1 else '/'
