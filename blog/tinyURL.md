在leetcode上面遇到一个题目是设计一个短链接系统，题目描述如下：

TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.

Design the encode and decode methods for the TinyURL service. There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

也就是说，只要实现一个系统能够从长链接转换成短链接，然后还能从短链接转换回去就可以了。

参考自：[iammutex的回答](https://www.zhihu.com/question/29270034)

有几种错误的思路：

1. 实现一个算法，将长地址转成短地址。实现长和短一一对应。然后再实现它的逆运算，将短地址还能换算回长地址。

这种是不可能实现的，这种算法的很好反驳，就是不论短地址有多长，它总不可能覆盖和表示世界上所有的长地址集合。

2. 把长地址转成短地址，但是不存在逆运算。我们需要把短对长的关系存到DB中，在通过短查长时，需要查DB。

长地址到短地址的转换过程中，就有可能出现碰撞，和第一个思路是差不多的，也就是多个长地址转换成了一个短地址，那么怎么从短地址查回去？

3. 用一个hash算法，我承认它会碰撞，碰撞后我再在后面加1，2，3不就行了。

通过这个hash算法算出来之后，可能我们会需要做btree式的大于小于或者like查找到能知道现在应该在后面加1，2，或3，这个也可能由于输入的长地址集的不确定性。导致生成短地址时间的不确定性。

4. 随机生成一个短地址，去查找是否用过，用过就再随机，如此往复，直到随机到一个没用过的短地址。

这样的话，效率太低。

对于这道题，我采取的思路是，使用字典来存储，然后一个全局的变量作为发号器，每次要从长链接生成短链接的时候，发号器就自增1，然后这样将短链接和长链接对应起来存储到字典中。

在后续从短链接生成长链接的时候，因为短链接和长链接是一一对应的关系，并且短链接是key，长链接是value，所以可以直接从短链接找到长链接。

这样做的一个缺点就是，耗费空间，毕竟所有来的短链接都会给存进来，生成一个短链接。

另一种比较好的方式，就是使用缓存，LRU缓存也可以，遇到这个长链接的时候，查看最近有没有使用过，如果有，则返回相应的短链接，否则重新生成，然后缓存时间比如设置1个小时完全足够。

这样就可以避免空间的浪费了，当一个地址被频繁使用，那么它会一直在这个key-value表中，总能返回当初生成那个短地址，不会出现重复的问题。如果它使用并不频繁，那么长对短的key会过期，LRU机制自动就会淘汰掉它。