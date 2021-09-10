import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats.contingency import expected_freq

conv_a = 17649
non_conv_a = 58892
sessions_a = conv_a + non_conv_a

conv_b = 77020
non_conv_b = 59193
sessions_b = conv_b + non_conv_b

conv = conv_a + conv_b
sessions = conv_a + non_conv_a + conv_b + non_conv_b

# Expected Values
# 	      Grade				      Grade
# Goals   | 4  	5     6	    Total  	Goals   | 4  	5     6
# ---------------------------------	---------------------------
# Grades  | 49 	50    69    168		Grades  | 46.1 	54.2  67.7
# Popular | 24 	36    38     98		Popular | 26.9 	31.6  39.5
# Sports  | 19 	22    28     69		Sports  | 18.9 	22.2  27.8
# ---------------------------------
e_a = round(sessions_a * (conv / sessions), 1)
e_b = round(sessions_b * (conv / sessions), 1)

ab_test = np.array([[conv_a, non_conv_a], [conv_b, non_conv_b]])
chi2_stat, p_val, dof, expected = stats.chi2_contingency(ab_test)

contingency_table = pd.DataFrame({'Groups': ['A', 'B', 'Total'],
                                  'Clicks': [conv_a, conv_b, (conv_a + conv_b)],
                                  'Non Clicks': [non_conv_a, non_conv_b, (non_conv_a + non_conv_b)],
                                  'Sessions': [(conv_a + non_conv_a), (conv_b + non_conv_b),
                                               (conv_a + non_conv_a) + (conv_b + non_conv_b)]})

e_conv_a = round(sessions_a * ((conv_a + conv_b) /
                               ((conv_a + non_conv_a) + (conv_b + non_conv_b))), 2)
e_conv_b = round(sessions_b * ((conv_a + conv_b) /
                               ((conv_a + non_conv_a) + (conv_b + non_conv_b))), 2)
e_nconv_a = round(sessions_a * ((non_conv_a + non_conv_b) /
                                ((conv_a + non_conv_a) + (conv_b + non_conv_b))), 2)
e_nconv_b = round(sessions_b * ((non_conv_a + non_conv_b) /
                                ((conv_a + non_conv_a) + (conv_b + non_conv_b))), 2)
e_table = pd.DataFrame({'Groups': ['A', 'B'],
                        'Expected Clicks': [e_conv_a, e_conv_b],
                        'Expected Non Clicks': [e_nconv_a, e_nconv_b]})

_ = plt.bar(["A", "B"], [(conv_a / sessions_a), (conv_b / sessions_b)], color=["b", "g"])
_ = plt.title("Conversion Rate A and B")
_ = plt.xlabel("Groups")
_ = plt.ylabel("Conv %")
plt.show()


# Link at http://www.stat.yale.edu/Courses/1997-98/101/chisq.htm
