def mean():
    sample = []
    def _mean(number):
        sample.append(number)
        return sum(sample) / len(sample)
    return _mean

current_mean = mean()
print(current_mean(10))
print(current_mean(15))
print(current_mean(12))
print(current_mean(11))
print(current_mean(13))