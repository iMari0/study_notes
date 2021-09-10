import scipy.stats as stats
import numpy as np
import pandas as pd

conv_a = 1513
non_c_a = 14133
sessions_a = conv_a + non_c_a

conv_b = 1853
non_c_b = 13277
sessions_b = conv_b + non_c_b

e_conv_a = sessions_a * ((conv_a + conv_b) / (sessions_a + sessions_b))
e_conv_b = sessions_b * ((conv_a + conv_b) / (sessions_a + sessions_b))
e_nconv_a = sessions_a * ((non_c_a + non_c_b) / (sessions_a + sessions_b))
e_nconv_b = sessions_b * ((non_c_a + non_c_b) / (sessions_a + sessions_b))

