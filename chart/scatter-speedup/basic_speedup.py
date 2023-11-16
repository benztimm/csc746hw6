import pandas as pd
import matplotlib.pyplot as plt

plot_fname = "scatter_speedup.png"

fname = "speedup_scatter.csv"
df = pd.read_csv(fname, comment="#")
var_names = list(df.columns)

# split the df into individual vars
# assumption: column order - 0=problem size, 1=blas time, 2=basic time

problem_sizes = df[var_names[0]].values.tolist()
code1_time = df[var_names[1]].values.tolist()
code2_time = df[var_names[2]].values.tolist()
code3_time = df[var_names[3]].values.tolist()


plt.figure()

plt.title("Speedup of Scatter time for each Decomposition method")

xlocs = [i for i in range(len(problem_sizes))]

plt.xticks(xlocs, problem_sizes)

plt.plot(code1_time, "r-o",label = var_names[1])
plt.plot(code2_time, "b-x",label = var_names[2])
plt.plot(code3_time, "g-+",label = var_names[3])


#plt.xscale("log")
#plt.yscale("log")

plt.xlabel("Concurrency level")
plt.ylabel("Speedup")

plt.legend(loc="best")

plt.grid(axis='both')


# save the figure before trying to show the plot
plt.savefig(plot_fname, dpi=300)


plt.show()

# EOF
