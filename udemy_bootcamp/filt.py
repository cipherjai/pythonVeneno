import statistics

data = [1.3, 2.7, 0.8, 4.1, -43.4, 5.7, 6.9, 8.9, -7.09, 8.9, 9.8, 7.8]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x:x < avg, data)))

# when data from another sources contain empty null or missing values
# removing missing data

data = ["Something", "", "", "is", "", "missing"]
print(list(filter(None, data)))


# False values
"""
""
0
0j
0.0
[]
()
{}
False
None
"""
