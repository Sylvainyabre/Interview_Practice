"""
@Asssessment from codility given by SISCO.
John starts playing at time A and ends at time B. Each round starts every 15 minutes. If B is earlier than A, John has played overnight
(from time A to midnight and from midnight to time B). What is the maximum number of full
rounds that can be played by John?
Write a function:
def solution(A, B)
that, given two strings A and B (in HH : MM format), representing the start time and end time, returns
an integer denoting the maximum number of full rounds that John can play within the given period
of time.
Examples:
1. Given A = "12:01" and B = "12: 44", the function should return 1. John can play only one round
(from 12: 15 to 12:30). He starts too late to play the round from 12 : 00 to 12: 15 and he will not
be able to finish the 12:30-12:45 round.
2. Given A = "20: 00" and B = "06: 00", the function should return 40. John can play 16 game
rounds from 20: 00 to 00: 00 and 24 game rounds from 00: 00 to 06:00.
3. Given A = "00: 00" and B = "23:59, the function should return 95. John can play four rounds
every hour except for the last hour, in which he can play only three rounds (23: 00-23: 15, 23: 15-
23:30,23:30-23: 45). The next round would be 23:45-00:00 but John has to end 1 minute
sooner, so he cannot take part in it.
4. Given A = "12: 03" and B = "12: 03", the function should return 0. John cannot play any round
during an empty period of time.
Assume that:
strings A and B represent valid times in a HH: MM format.
In your solution, focus on correctness. The performance of your solution will not be the focus of
the assessment.
    """

"""
Approach:
 OVERNIGHT CASES:
    - The hours are the same and the minutes of B are less than the minutes of A
    - The hours of B are less than the hours of A
    - A is "00:00" and B is not
    """

"""
TEST CASES:
- solution("12:01","12:44") = 1
- solution("20:00","6:00") = 40
- solution("00:00","23:59") = 95
- solution("12:03","12:03") = 0

"""


def solution(loginTime, logoutTime):
        gamePeriod = 15
        dayMinutes = 24*60
        hourMinute = 60
        loginHour, loginMinute = loginTime.split(":")
        logoutHour, logoutMinute = logoutTime.split(":")
        # convert to ints
        loginHour = int(loginHour)
        logoutHour = int(logoutHour)
        loginMinute = int(loginMinute)
        logoutMinute = int(logoutMinute)

        if loginHour == logoutHour:
            if loginMinute == logoutMinute:
                return 0
            # example: loginTime = 12:10; logoutTime= 12: 35
            elif logoutMinute > loginMinute:
                logoutMinute -= logoutMinute % gamePeriod
                if loginMinute % gamePeriod != 0:
                    loginMinute += gamePeriod - (loginMinute % gamePeriod)
                if logoutMinute <= loginMinute:
                    # if after adjusting minutes to game periods, the starting minutes are greater than                           #the ending minutes
                    return 0
                else:
                    return (logoutMinute-loginMinute)/gamePeriod

            elif loginMinute > logoutMinute:  # Played overnight
                logoutMinute -= logoutMinute % gamePeriod
                if loginMinute % gamePeriod != 0:
                    loginMinute += gamePeriod - (loginMinute % gamePeriod)

                duration1 = dayMinutes-loginHour*hourMinute-loginMinute
                duration2 = logoutHour*hourMinute + logoutMinute
                return (duration1+duration2)/gamePeriod
        elif logoutHour > loginHour:
            logoutMinute -= logoutMinute % gamePeriod
            if loginMinute % gamePeriod != 0:
                loginMinute += gamePeriod - (loginMinute % gamePeriod)
            duration = (logoutHour-loginHour)*hourMinute - \
                        loginMinute+logoutMinute
            return duration/gamePeriod
        else:  # when logout hour is less than loginHour; ex: loginTIme = 9:30 and logoutTime = 8:45
            logoutMinute -= logoutMinute % gamePeriod
            if loginMinute % gamePeriod != 0:
                    loginMinute += gamePeriod - (loginMinute % gamePeriod)
            duration1 = dayMinutes-loginHour*hourMinute-loginMinute
            duration2 = logoutHour*hourMinute+logoutMinute
            duration = duration1+duration2
            return duration/gamePeriod

"""
    tests is a list of objects with the format
    {
        A:12:23
        B: 12:56
        expected: 1
    }
    """


def testSolution(tests):
    for test in tests:
        print("solution({},{}) returned {} and {} was expected."
              .format(test["A"], test["B"], solution(test["A"], test["B"]), test["expected"]))


tests = [
    {"A": "12:01",
     "B": "12:44",
     "expected": 1
     },
    {"A": "20:00",
     "B": "6:00",
     "expected": 40
     },
    {"A": "00:00",
     "B": "23:59",
     "expected": 95
     },
    {"A": "12:03",
     "B": "12:03",
     "expected": 0
     },
    {"A": "12:16",
     "B": "12:31",
     "expected": 0
     },
     {"A": "17:16",
     "B": "19:51",
     "expected": 9
     },
     {"A": "12:05",
     "B": "12:26",
     "expected": 0
     },
     {"A": "12:05",
     "B": "12:06",
     "expected": 0
     }
     

]
# 17:30-19:30 = 120/15+1

testSolution(tests)


