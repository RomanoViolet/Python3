# URL https://leetcode.com/problems/maximum-profit-in-job-scheduling/
# Print:
import sys


class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        totalProfits = 0
        newjobsStartTime = startTime[0]
        listOfJobsWithSameStartTime = list()
        for idx in range(len(startTime)):
            if newjobsStartTime == startTime[idx]:
                listOfJobsWithSameStartTime.append(idx)
            totalProfits += self._chooseJobFromSameStartTimes(
                listOfJobsWithSameStartTime, profit)
            listOfJobsWithSameStartTime.clear()

    def _chooseJobFromSameStartTimes(self, listOfJobsWithSameStartTime, profit):
        allProfits = [profit[i] for i in listOfJobsWithSameStartTime]
        return max(allProfits)
