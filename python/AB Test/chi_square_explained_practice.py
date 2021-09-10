import numpy as np
import pandas as pd
import scipy.stats as stats

clicked_a = 25
n_clicked_a = 75
sessions_a = 100

clicked_b = 20
n_clicked_b = 100
sessions_b = 120

clicks = clicked_a + clicked_b
n_clicks = n_clicked_b + n_clicked_a

sessions = sessions_a + sessions_b

ratio_a = clicked_a / sessions_a
ratio_b = clicked_b / sessions_b

# Print the contingency table
T = pd.DataFrame({"Groups": ['A', 'B'],
                  "Conversions": [clicked_a, clicked_b],
                  "Not Converted": [n_clicked_a, n_clicked_b],
                  "Sessions": [sessions_a, sessions_b]})

print("The null hypothesis stats that there is no difference between the 2 groups. \n "
      "The observed values are coming from the same underlying distribution.")
print("Under this condition --> A = B")

# What should we expect if the null hypothesis were true?
e_clicks_a = sessions_a * (clicks / sessions)
e_clicks_b = sessions_b * (clicks / sessions)
e_nclicks_a = sessions_a * (n_clicks / sessions)
e_nclicks_b = sessions_b * (n_clicks / sessions)

x_squared = ((20 - 24.5) ** 2 / 24.5) + \
            ((25 - 20.5) ** 2 / 20.5) + \
            ((100 - 95.5) ** 2 / 95.5) + \
            ((75 - 79.5) ** 2 / 79.5)
# = 2.3
ab_test = np.array([[clicked_a, n_clicked_a],
                    [clicked_b, n_clicked_b]])


#Running CHI2 with scipy.stats
chi2, pval, dof, expected = stats.chi2_contingency(ab_test, correction=False)

print("An alpha level of 0.05 has been set up.\n The pval resulting from the test = ", pval,".")
print("We fail to reject the Null Hypothesis.")