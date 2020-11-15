import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
import math
from statsmodels.formula.api import ols

chikW = pd.read_csv('C:\\Users\\ghadi\\Documents\\DataSet\\Chick Weights.txt')

# separate to 2 columns [because when import the dataset has combining 2 columns into 1 (weight\t feed)]
# dropping null value columns to avoid errors 
chikW.dropna(inplace = True) 

# new data frame with split value columns 
new = chikW['weight\t feed'].str.split("\t", n = 1, expand = True) 

# making separate first name column from new data frame 
chikW["weight"]= new[0] 

# making separate last name column from new data frame 
chikW["feed"]= new[1] 

# Dropping old Name columns 
chikW.drop(columns =['weight\t feed'], inplace = True) 

# df display 
print(chikW)

# change columns types 

chikW["weight"]=pd.to_numeric(chikW["weight"])
chikW["feed"] = chikW.feed.astype('object')

chikW.info()
chikW.head()
chikW.describe()
chikW.shape
chikW.columns
chikW.head()

#Q2: Calculate the number of chicks in each group.
chikW['feed'].value_counts()

np.mean(chikW['weight'])

#summary statistics
chikW.groupby(['weight']).describe()

chikW.groupby(['feed']).describe()

##Q1 :Calculate the mean and standard deviation for each group.
chikW.groupby('feed')['weight'].mean() #m for each group
np.mean(chikW['weight']) #m for all weight

chikW.groupby('feed')['weight'].std()
np.std(chikW['weight'])

#Q3 :Produce a strip chart showing each chick as an individual data point
sns.stripplot(x='feed', y='weight', data=chikW, jitter=0.2)
#sns.boxplot(x='feed', y='weight', data=chikW)

# T-test 
# fit a linear model
# specify model
chikmodel = ols("weight ~ feed", chikW)
results = chikmodel.fit()# fit model
# extract coefficients
results.params.Intercept
results.params["feed[T.soybean]"]
results.summary()


#Q4: Calculate a 1-way ANOVA.
aov_table = sm.stats.anova_lm(results, typ=2)
aov_table


#Q5: Calculate Tukey’s post-hoc test (i.e. p-values for all pair-wise t-tests)
from statsmodels.stats.multicomp import pairwise_tukeyhsd
m_comp = pairwise_tukeyhsd(endog=chikW['weight'], groups=chikW['feed'], alpha=0.05)
print(m_comp)


