# 使用普通的 Requests
# import requests
#
# url = "http://httpbin.org"
# s = requests.Session()
#
# def fetch(times=10):
#     s.get("%s/cookies/set?name=value" % url)
#     r = [s.get("%s/get" % url) for i in range(times)]
#     print(r)
#
# fetch()



# 使用 Trip
import trip
url = "http://httpbin.org"
s = trip.Session()

@trip.coroutine
def fetch(times=10):
    s.get("%s/cookies/set?name=value" % url)
    r = [s.get("%s/get" % url) for i in range(times)]
    print(r)

trip.run(fetch)