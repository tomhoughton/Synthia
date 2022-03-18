#%%
import os
import pandas as pd

df_path = os.path.join('TrainingData', 'Datasets')
df = pd.read_csv(os.path.join(df_path, 'Mar-16-2022.csv'))
# %%

pluck_df = df[df['Type'] == 'Pluck']

pluck_df.count()


# %%

df['Type'].value_counts()['Pluck']
df['Type'].value_counts()['Bass']
df['Type'].value_counts()['Pad']
df['Type'].value_counts()['Lead']
df['Type'].value_counts()['808']

# %%

df['Type']
# %%
df.head()

# %%

# Number of occurances for each degree
df['Consistency'].value_counts()
df['Brightness'].value_counts()
df['Evolution'].value_counts()
df['Dynamics'].value_counts() 

# %%

# Number of occurances for each combination:

a = df.loc[(df['Consistent'] == True) & (df['Bright'] == False) & (df['Evolves'] == False) & (df['Dynamic'] == False)]
r, c = a.shape
print(r)
# %%
