class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def is_ipv4(ip):
            parts = ip.split('.')
            if len(parts) != 4:
                return False
            for part in parts:
                if not part.isdigit():
                    return False
                if not 0 <= int(part) <= 255:
                    return False
                if len(part) > 1 and part[0] == '0':
                    return False
            return True

        def is_ipv6(ip):
            parts = ip.split(':')
            if len(parts) != 8:
                return False
            hexdigits = "0123456789abcdefABCDEF"
            for part in parts:
                if not 1 <= len(part) <= 4:
                    return False
                for char in part:
                    if char not in hexdigits:
                        return False
            return True

        if is_ipv4(queryIP):
            return "IPv4"
        if is_ipv6(queryIP):
            return "IPv6"
        return "Neither"
