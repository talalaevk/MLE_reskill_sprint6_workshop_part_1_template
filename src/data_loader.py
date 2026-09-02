import seaborn as sns

def load_data(name, sample_n=None, random_state=42):
    df = sns.load_dataset(name)
    if sample_n:
        df = df.sample(sample_n, random_state=random_state)
    print(f'Размер: {df.shape}')
    print(f'Столбцы: {list(df.columns)}')
    df.info()
    return df
