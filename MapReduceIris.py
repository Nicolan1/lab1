#https://github.com/astan54321/PA3/blob/44628868dcc7f00feec9e4c4bdb9391558391ac7/problem2_3.py

from mrjob.job import MRJob
from mrjob.step import MRStep
import re

DATA_RE = re.compile(r"[\w.-]+")


class MRProb2_3(MRJob):


    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_sepW_setosa,
                   reducer=self.reducer_get_avg)
        ]

    def mapper_get_sepW_setosa(self, _, line):
        # yield each petal width
        data = DATA_RE.findall(line)
        if "Mexican" in data:
            sep_W = float(data[0])
            yield ("Mexican cosine", sep_W)

    def reducer_get_avg(self, key, values):
        # get max of the petal widths
        size=0
        for val in values:
            size += 1
        yield ("Total maxican cusine", size)
if __name__ == '__main__':
    MRProb2_3.run()