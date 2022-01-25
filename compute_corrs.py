#!/usr/bin/env python3

# %%
import pandas as pd
import dask.dataframe as dd
from dask.distributed import Client

# %%
client = Client()

# %%
df = pd.read_csv('10.16_LeagueOfLegends_Games.csv', sep=';')
df = df.head(100)  # Dla testów na szybko
df = dd.from_pandas(df, chunksize=1000)

# %%
# Popraw gold graczy
for team in [1, 2]:
    for player in range(1, 6):
        for minute in [10, 15]:
            df[f't{team}p{player}_min{minute}_gold_fixed'] = df[f't{team}p{player}_min{minute}_gold'] * 10

# %%
df['t1_min10_gold_advantage'] = (df['t1p1_min10_gold_fixed']+df['t1p2_min10_gold_fixed']+df['t1p3_min10_gold_fixed']+df['t1p4_min10_gold_fixed']+df['t1p5_min10_gold_fixed'])-(
    df['t2p1_min10_gold_fixed']+df['t2p2_min10_gold_fixed']+df['t2p3_min10_gold_fixed']+df['t2p4_min10_gold_fixed']+df['t2p5_min10_gold_fixed'])

df['t1_min15_gold_advantage'] = (df['t1p1_min15_gold_fixed']+df['t1p2_min15_gold_fixed']+df['t1p3_min15_gold_fixed']+df['t1p4_min15_gold_fixed']+df['t1p5_min15_gold_fixed'])-(
    df['t2p1_min15_gold_fixed']+df['t2p2_min15_gold_fixed']+df['t2p3_min15_gold_fixed']+df['t2p4_min15_gold_fixed']+df['t2p5_min15_gold_fixed'])

# %%
# df.describe().loc[:, ['t1p1_min10_gold_fixed', 't1p1_min15_gold_fixed', 't1_min15_gold_advantage']]
# df.compute().describe()

# %%
# corrs = df.corrwith(df['t1_win'])
corrs = df.corr().compute()

# %%
# corrs.to_csv('t1_win_correlation.csv')
# corrs.loc[['t1p1_min10_gold_fixed', 't1p1_min15_gold_fixed', 't1_min10_gold_advantage', 't1_min15_gold_advantage']]
corrs['t1_win'].to_csv('t1_win_correlation.csv')
# corrs.loc[['t1_min10_gold_advantage', 't1_min15_gold_advantage'], ['t1_win']]
