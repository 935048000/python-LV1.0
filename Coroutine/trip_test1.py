import trip
"""
TRIP，Tornado和Pairs Requests，一个用于Python的异步HTTP库。
简单的请求，trip让你摆脱恼人的网络阻塞。

随着trip，你可以在一个时间内完成一百个要求。
trip得到两个强大的网站包名称，旨在将它们结合在一起。trip指的是“tornado和 Requests”，TRIP。为了把它们放在一起，我重新使用了许多关于结构和处理的代码。
其实我只是做了一点点的努力来混合。感谢tornado 和 Requests。
通过使用Trip，您可以充分利用请求，其中包括：具有Cookie持久性，浏览器式SSL验证，自动内容解码，基本/摘要式身份验证，优雅的键/值Cookies的会话。
同时，你的请求像使用Tornado的AsyncHTTPClient一样是协程，网络阻塞不会是一个问题。
发现很难优化蜘蛛的时间消耗？发现使用asyncio http软件包棘手？发现重大的大蜘蛛框架？尝试trip，你不会后悔！
"""
# 在python3中使用异步和等待
# async def main():
#     r = await trip.get('https://httpbin.org/get', auth=('user', 'pass'))
#     print(r.content)
#
# trip.run(main)


# 与Cookie持久性
# @trip.coroutine
# def main():
#     s = trip.Session()
#     r = yield s.get(
#         'https://httpbin.org/cookies/set',
#         params={'name': 'value'},
#         allow_redirects=False)
#     r = yield s.get('https://httpbin.org/cookies')
#     print(r.content)
#
# trip.run(main)


# 事件钩子
# @trip.coroutine
# def main():
#     def print_url(r, *args, **kwargs):
#         print(r.url)
#     def record_hook(r, *args, **kwargs):
#         r.hook_called = True
#         return r
#     url = 'http://httpbin.org/get'
#     r = yield trip.get('http://httpbin.org', hooks={'response': [print_url, record_hook]})
#     print(r.hook_called)
#
# trip.run(main)


# 超时设定
# @trip.coroutine
# def main():
#     r = yield trip.get('http://github.com', timeout=0.001)
#     print(r)
#
# trip.run(main)


# 代理
# proxies = {
#     'http': '127.0.0.1:8080',
#     'https': '127.0.0.1:8081',
# }
#
# @trip.coroutine
# def main():
#     r = yield trip.get('https://httpbin.org/get', proxies=proxies)
#     print(r.content)
#
# trip.run(main)















