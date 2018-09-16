# !python3.6
# -*- coding: utf-8 -*-

import sys
import pandas as pd
import matplotlib.pyplot as plt

# column['name'] and column['sid']
NUM_DUMMY_COL = 2

df = pd.read_csv(sys.argv[1], delimiter=',', encoding='utf-8')
df = df.replace('-', 0)
df.iloc[:, NUM_DUMMY_COL:] = df.iloc[:, NUM_DUMMY_COL:].astype(float)

bottom = df.iloc[:, NUM_DUMMY_COL:].quantile(.25).values.tolist()
center = df.iloc[:, NUM_DUMMY_COL:].quantile(.5).values.tolist()
top = df.iloc[:, NUM_DUMMY_COL:].quantile(.75).values.tolist()

axis_x = [n for n in range(len(df.columns) - NUM_DUMMY_COL)]
for index, row in df.iterrows():
	plt.title(row.iloc[1])
	plt.xticks(axis_x, list(df)[NUM_DUMMY_COL:], rotation=90)
	plt.ylim(-5, 105)
	plt.plot(axis_x, bottom, linewidth=0.5, linestyle='--', marker='x', markersize=5, color='grey', label='25%')
	plt.plot(axis_x, center, linewidth=0.5, linestyle='--', marker='+', markersize=5, color='grey', label='50%')
	plt.plot(axis_x, top, linewidth=0.5, linestyle='--', marker='*', markersize=5, color='grey', label='75%')
	plt.plot(axis_x, df.iloc[index, NUM_DUMMY_COL:], linewidth=0.5, linestyle='-', marker='o', markersize=5, color='red', label='my_score')
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
	plt.savefig('%s %s.png' %(row.iloc[1], row.iloc[0]), dpi=200, bbox_inches='tight')
	plt.clf()