import hashlib


class Codec:

    def __init__(self):
        self.url_hash_table = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        hash = hashlib.sha1(longUrl.encode('utf-8')).hexdigest()
        short_hash = hash[-8:-2]
        self.url_hash_table[short_hash] = longUrl
        return short_hash

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.url_hash_table[shortUrl]


url = "https://leetcode.com/problems/design-tinyurl"
codec = Codec()
print(codec.decode(codec.encode(url)))
