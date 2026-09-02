from src.data_loader import load_data
from src.analysis import analyze_missing, handle_missing, compute_correlations, groupby_stats
from src.charts import plot_histograms, plot_boxplots, plot_bars, plot_heatmap, plot_scatter


def run_eda(name, sample_n=None,
            hist_cols=None, box_configs=None, bar_configs=None,
            corr_pairs=None, heatmap_cols=None,
            scatter_configs=None, groupby_configs=None,
            missing_kw=None):

    # Блок 1: Чтение
    df = load_data(name, sample_n=sample_n)
    print(df.head())

    # Блок 2: Пропуски
    analyze_missing(df)
    if missing_kw:
        df = handle_missing(df, **missing_kw)

    # Блок 3: Графики
    if hist_cols:
        plot_histograms(df, hist_cols)
    if box_configs:
        plot_boxplots(df, box_configs)
    if bar_configs:
        for grp, val in bar_configs:
            plot_bars(df, grp, val)

    # Блок 4: Корреляции и статистики
    if corr_pairs:
        compute_correlations(df, corr_pairs)
    if heatmap_cols:
        plot_heatmap(df, cols=heatmap_cols)
    if scatter_configs:
        for x, y, hue in scatter_configs:
            plot_scatter(df, x, y, hue)
    if groupby_configs:
        for grp, cols in groupby_configs:
            print(groupby_stats(df, grp, cols))

    return df


# Пример запуска для Титаника:
titanic = run_eda(
    'titanic',
    hist_cols=['age', 'fare'],
    box_configs=[('pclass', 'age'), ('pclass', 'fare')],
    bar_configs=[('sex', 'survived'), ('pclass', 'survived')],
    corr_pairs=[('age', 'fare'), ('fare', 'survived'), ('pclass', 'survived')],
    scatter_configs=[('age', 'fare', 'survived'), ('age', 'fare', 'pclass')],
    groupby_configs=[('sex', 'survived'), ('pclass', 'survived')],
    missing_kw=dict(fill_median=['age'], fill_mode=['embarked', 'embark_town'], drop_cols=['deck']),
)
