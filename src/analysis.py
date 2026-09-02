from scipy.stats import pearsonr, spearmanr
import pandas as pd


def analyze_missing(df):
    missing = df.isnull().sum()
    missing_pct = (df.isnull().mean() * 100).round(1)
    missing_df = pd.DataFrame({'Пропуски': missing, '%': missing_pct})
    missing_with = missing_df[missing_df['Пропуски'] > 0]
    if len(missing_with) > 0:
        print('Пропуски:')
        print(missing_with.sort_values('%', ascending=False))
    else:
        print('Пропусков нет')
    print(f'Всего строк с пропусками: ...')
    print(df.describe().round(2))
    print(df.describe(include=['object', 'category']))
    return missing_df


def handle_missing(df, fill_median=None, fill_mode=None, drop_cols=None):
    print('До:', df.shape, f'пропусков: {df.isnull().sum().sum()}')
    if drop_cols:
        df = df.drop(columns=drop_cols)
    if fill_median:
        for col in fill_median:
            df[col] = df[col].fillna(df[col].median())
    if fill_mode:
        for col in fill_mode:
            df[col] = df[col].fillna(df[col].mode()[0])
    print('После:', df.shape, f'пропусков: {df.isnull().sum().sum()}')
    return df


def compute_correlations(df, pairs):
    for c1, c2 in pairs:
        clean = df[[c1, c2]].dropna()
        p, _ = pearsonr(clean[c1], clean[c2])
        s, _ = spearmanr(clean[c1], clean[c2])
        print(f'{c1} vs {c2}: Пирсон r={p:.3f} Спирмен p={s:.3f}')


def groupby_stats(df, groupby_cols, value_cols, agg='mean'):
    return df.groupby(groupby_cols)[value_cols].agg(agg).round(2)
