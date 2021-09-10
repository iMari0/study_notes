import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

conv_a = 1513
non_c_a = 14133
sessions_a = conv_a + non_c_a

conv_b = 1853
non_c_b = 13277
sessions_b = conv_b + non_c_b

#Build contingency table as pandas dataframe
T = pd.DataFrame({"Groups": ['A', 'B'],
                  "Conversions": [conv_a, conv_b],
                  "Not Converted": [non_c_a, non_c_b],
                  "Sessions": [sessions_a, sessions_b]})

#Calculate expected values
e_conv_a = sessions_a * ((conv_a + conv_b) / (sessions_a + sessions_b))
e_conv_b = sessions_b * ((conv_a + conv_b) / (sessions_a + sessions_b))
e_nconv_a = sessions_a * ((non_c_a + non_c_b) / (sessions_a + sessions_b))
e_nconv_b = sessions_b * ((non_c_a + non_c_b) / (sessions_a + sessions_b))

#Expected values table
e_T = pd.DataFrame({"Groups": ['A', 'B'],
                    "Conversions": [e_conv_a, e_conv_b],
                    "Not Converted": [e_nconv_a, e_nconv_b],
                    "Sessions": [sessions_a, sessions_b]})

x_square = "sum of (observed - expected)2/expected"

# Contingency table
ab_test = np.array([[conv_a, non_c_a],
                   [conv_b, non_c_b]])

chi2_stat, p_val, dof, expected = stats.chi2_contingency(ab_test, correction=False)
# Link https://medium.com/bukalapak-data/meet-the-engine-of-a-b-testing-chi-square-test-30e8a8ab44c5