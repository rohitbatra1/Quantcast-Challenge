#!/usr/bin/python3



import argparse
import sys


def parseCSV(file):
    with open(file) as f:
        s = f.read() + '\n'

    return s

def getMostActiveCookie(inputString, day):
    if not inputString or not day:
        return []    


    # the exact time is irrelevant for the purpsoses of this problem
    withoutTime = []

    # disregard the first line (cookie, timestamp)
    cookies = inputString.split()[1:]
    for cookie in cookies:
        withoutTimeString = cookie.split("T")[0]
        withoutTime.append(withoutTimeString)
    
    # map the cookies and the day they occured to the number of times they occured that day
    cookieDayToCount = {}

    for cookie in withoutTime:
        cookieDayToCount[cookie] = cookieDayToCount.get(cookie, 0) + 1
    
    maxCookies = []
    maxCount = float('-inf')

    for cookieDay in cookieDayToCount:
        if cookieDay.split(",")[1] == day:
            # this is a new max cookie, set it as the only max cookie
            if cookieDayToCount[cookieDay] > maxCount:
                maxCount = cookieDayToCount[cookieDay]
                maxCookies = [cookieDay.split(",")[0]]
            # this is an equal max cookie, add it to the list
            elif cookieDayToCount[cookieDay] == maxCount:
                maxCookies.append(cookieDay.split(",")[0])
        

    return maxCookies

def main():
    date = sys.argv[-1]


    testString = """cookie,timestamp
    AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
    SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
    5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
    AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
    SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
    4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
    fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
    4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00
    """

    # edge case no cookies on this day
    assert(getMostActiveCookie(testString, '2018-12-06') == [])

    # sample cases
    assert(getMostActiveCookie(testString, '2018-12-09') == ["AtY0laUfhglK3lC7"])
    assert(getMostActiveCookie(testString, '2018-12-08') == ["SAZuXPGUrfbcn5UA", "4sMM2LxV07bPJzwf", "fbcn5UAVanZf6UtG"])

    csvSTRING = parseCSV(sys.argv[-3])

    answers = getMostActiveCookie(csvSTRING, date)

    for cookie in answers:
        print(cookie)



if __name__ == "__main__":
    main()

