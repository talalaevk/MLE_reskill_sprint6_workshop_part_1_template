import matplotlib.pyplot as plt
import seaborn as sns


def plot_histograms(df, cols, figsize=(14, 5)):
    fig, axes = plt.subplots(1, len(cols), figsize=figsize)
    if len(cols) == 1:
        axes = [axes]
    for ax, col in zip(axes, cols):
        sns.histplot(df[col], bins=30, kde=True, ax=ax, color='steelblue')
        m, md = df[col].mean(), df[col].median()
        ax.set_title(f'{col} (mean={m:.1f}, median={md:.1f})')
    plt.tight_layout()
    plt.show()


def plot_boxplots(df, configs, figsize=(14, 5)):
    fig, axes = plt.subplots(1, len(configs), figsize=figsize)
    if len(configs) == 1:
        axes = [axes]
    for ax, (x, y) in zip(axes, configs):
        sns.boxplot(data=df, x=x, y=y, palette='Set2', ax=ax)
        ax.set_title(f'{y} по {x}')
    plt.tight_layout()
    plt.show()

def plot_bars(df, groupby_col, value_col, agg='mean', figsize=(7, 5)):
    fig, ax = plt.subplots(figsize=figsize)
    df.groupby(groupby_col)[value_col].agg(agg).plot.bar(
        ax=ax, color='steelblue', edgecolor='white')
    ax.set_title(f'{value_col} по {groupby_col}')
    plt.tight_layout()
    plt.show()


def plot_heatmap(df, cols=None, figsize=(10, 8)):
    fig, ax = plt.subplots(figsize=figsize)
    data = df[cols] if cols else df.select_dtypes(include='number')
    sns.heatmap(data.corr(), annot=True, fmt='.2f', cmap='RdBu_r', center=0, ax=ax)
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x, y, hue, figsize=(10, 6), **kwargs):
    fig, ax = plt.subplots(figsize=figsize)
    sns.scatterplot(data=df, x=x, y=y, hue=hue, alpha=0.6, ax=ax, **kwargs)
    ax.set_title(f'{x} vs {y}')
    plt.tight_layout()
    plt.show()
