'''
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

参考：[Design TinyURL](https://github.com/Microndgt/algorithm-in-Python/blob/master/blog/tinyURL.md)

Runtime: 45 ms

Your runtime beats 88.39 % of python submissions
'''

from functools import lru_cache


class Codec:
    count = 0
    __map = {}
    base_url = "http://tinyurl.com/"

    @lru_cache()
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short_url = self.base_url + str(self.count)
        self.__map[short_url] = longUrl
        self.count += 1
        return short_url

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.__map.get(shortUrl)

        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.decode(codec.encode(url))
