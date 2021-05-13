# Jupyter Notebooks

Collection of Jupyter Notebooks. Here is the list of notebooks currently in this repo (see `notebooks` folder).

| Notebook Name | Description
| :------------ | ------------
| Correlation Analysis | A quick tutorial using `pd.corr()` and how to create correlation plots with `sns.regplot()` and pure `matplotlib` approach with `np.polyfit()`. Also included: custom python script for calculating 95% CI with bootstrapping method. See `scripts` folder.
| Creating Pandas DataFrame | Multiple ways to create a DataFrame.
| Hue in Matplotlib and Seaborn | With `seaborn`, we have `hue`. But, what about with `matplotlib`? We use `pd.groupby()`. Slightly longer code though. Also featuring `plt.colorbar()`.
| Project - Dr. STONE | Please refer to [Dr. STONE Text Mining Project](https://meta.caspershire.net/dr-stone-text-mining-project/) on Caspershire Meta.
| Qual Exam Stat | Basically, how to use `ax.twinx()` to plot a dual-axis plot.
| Scatterplot Random Example | How to use `np.random.normal()`. I think. Yeah that's it.
| Stacked Bar Chart | Generate a stacked bar chart with either `ax.bar()` with `bottom` keyword argument, or perhaps a slightly less painful way with `df.pivot().loc[].plot(kind=bar, stacked=True)`. Also featuring `stack_print_number()` function and looping with `lambda` for fun and profit.
| Flow Cytometry and Lognormal Dist | Notebook created to illustrate flow cytometry plot, how to generate lognormal dist, using python decorator, and using `ScalarFormatter()`.
| PCA with scikit-learn | Using `sklearn` library to perform PCA computation. Includes plotting a chart to show percent cumulative variance for all the PC, and a plot showing contributions of each feature to each PC.
| Custom Color Palette | My way of defining custom color palette with `dict`, using a function that would either return a `dict` or draw an example plot that can be later consumed by `matplotlib` or `seaborn`.
| Accessing and Reshaping | On using accessors on a Pandas DataFrame (`.loc[]`, `.iloc[]`, `.at[]`, `.iat[]`). Also, a quick note on using `numpy.where()` to change range of values in specified columns.
| Manual Jittering | Instead of using `sns.stripplot()` or `sns.swarmplot()`, I decided to jitter the points myself.
