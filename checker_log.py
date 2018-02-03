from utils.bcolors import bColors as C

class CheckerLogs:

    def __init__(self, accepted=True):
        self.logs = list()
        self.time = 0
        self.accepted = accepted


    def _colorIt(self, value, color):
        return color+value+C.ENDC


    def logIt(self, dump, tsn, time, verdict, mem=None, exit_code=None):
        data = ''
        v = ''
        if verdict=="OK": v = self._colorIt(verdict, C.OKGREEN)
        elif verdict=="FAIL": v = self._colorIt(verdict, C.FAIL)
        else: v = self._colorIt(verdict, C.WARNING)
        data += "\n\tTest: #{0}, time: {1} ms, verdict: {2}\n".format(tsn, time, v)
        data += "\n\tInput\n"
        data += dump['Testcase']
        data += "\n\tOutput\n\t"
        data += "\n\t".join(dump['Output'].split())
        data += "\n\n\tExpected\n\t"
        data += "\n\t".join(dump['Expected'].split())

        self.logs.append(data)
        self.time += time
        if (verdict=="FAIL"): self.accepted = False


    def setFinalVerdict(self, finalVerdict):
        self.accepted = finalVerdict


    def getAverageApplicationTime(self):
        return self.time / (int(len(self.logs)))
