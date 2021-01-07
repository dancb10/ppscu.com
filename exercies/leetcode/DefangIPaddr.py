class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

address = "1.1.1.1"
s = Solution()
print(s.defangIPaddr(address))
