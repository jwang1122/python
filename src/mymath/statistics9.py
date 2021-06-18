from statistics import NormalDist

temperature_february = NormalDist(5, 2.5)  # Celsius
f = temperature_february * (9/5) + 32      # Normal distribution in Fahrenheit
print(f)

birth_weights = NormalDist.from_samples([2.5, 3.1, 2.1, 2.4, 2.7, 3.5])
drug_effects = NormalDist(0.4, 0.15)
combined = birth_weights + drug_effects
print(combined)
m=combined.mean
sd = combined.stdev
print(f"The mean of combined birth weight is {m:.3f}, and standard diviation is {sd:.3f}.")

"""
For example, given historical data for SAT exams showing 
that scores are normally distributed with a mean of 1060 
and a standard deviation of 195, determine the percentage 
of students with test scores between 1100 and 1200, after 
rounding to the nearest whole number:
"""
sat = NormalDist(1060, 195)
fraction = sat.cdf(1200 + 0.5) - sat.cdf(1100 - 0.5)
percentage = round(fraction * 100.0, 1)
print(f"Students with test score between 1100 and 1200 is {percentage}%.")
