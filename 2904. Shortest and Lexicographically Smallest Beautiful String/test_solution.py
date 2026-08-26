from solution import Solution


def test_shortest_beautiful_substring():
    solution = Solution()

    assert solution.shortestBeautifulSubstring("100011001", 3) == "11001"
    assert solution.shortestBeautifulSubstring("1011", 2) == "11"
    assert solution.shortestBeautifulSubstring("000", 1) == ""


if __name__ == "__main__":
    test_shortest_beautiful_substring()