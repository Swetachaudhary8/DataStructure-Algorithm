import collections

actions = """
When that action is replicated over the course of a week, you begin to scratch the surface of change.
When that action is replicated over the course of a month, you begin to notice a slight difference.
When that action replicated over the course of a year, or two years, or five years, you may no longer recognize yourself — you will have changed, in that particular way, completely.
"""
n = 2
words = actions.split()
word_count = collections.Counter(words)
print ("Top {0} words".format(n))
for word,count in word_count.most_common(n):
	print ("{0}:{1}".format(word,count))

