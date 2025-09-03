import statistics as st
sample = [10, 8, 10, 8, 2, 7, 9, 3, 34, 9, 5, 9, 25]

# The mean before removing outliers
mean = st.mean(sample)
print(mean)

stdev = st.stdev(sample)
low = mean - 2 * stdev
high = mean + 2 * stdev

clean_sample = list(filter(lambda x: low <= x <= high, sample))
print(clean_sample)

# The mean after removing outliers
print(st.mean(clean_sample))