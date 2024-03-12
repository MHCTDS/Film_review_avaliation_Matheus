import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def visualize_n_per_year(df_reviews):
    fig, axs = plt.subplots(2, 1, figsize=(16, 8))

    ax = axs[0]

    dft1 = df_reviews[['tconst', 'start_year']].drop_duplicates() \
        ['start_year'].value_counts().sort_index()
    dft1 = dft1.reindex(index=np.arange(dft1.index.min(), max(dft1.index.max(), 2021))).fillna(0)
    dft1.plot(kind='bar', ax=ax)
    ax.set_title('Número de filmes em anos')

    ax = axs[1]

    dft2 = df_reviews.groupby(['start_year', 'pos'])['pos'].count().unstack()
    dft2 = dft2.reindex(index=np.arange(dft2.index.min(), max(dft2.index.max(), 2021))).fillna(0)

    dft2.plot(kind='bar', stacked=True, label='#reviews (neg, pos)', ax=ax)

    dft2 = df_reviews['start_year'].value_counts().sort_index()
    dft2 = dft2.reindex(index=np.arange(dft2.index.min(), max(dft2.index.max(), 2021))).fillna(0)
    dft3 = (dft2/dft1).fillna(0)
    axt = ax.twinx()
    dft3.reset_index(drop=True).rolling(5).mean().plot(color='orange', label='resenhas por filme (média em 5 anos)', ax=axt)

    lines, labels = axt.get_legend_handles_labels()
    ax.legend(lines, labels, loc='upper left')

    ax.set_title('Número de resenhas em anos')

    fig.tight_layout()

def visualize_n_per_film(df_reviews):
    fig, axs = plt.subplots(1, 2, figsize=(16, 5))

    ax = axs[0]
    dft = df_reviews.groupby('tconst')['review'].count() \
        .value_counts() \
        .sort_index()
    dft.plot.bar(ax=ax)
    ax.set_title('Gráfico de Barras de resenhas por filme')

    ax = axs[1]
    dft = df_reviews.groupby('tconst')['review'].count()
    sns.kdeplot(dft, ax=ax)
    ax.set_title('Gráfico EDK de resenhas por filme')

    fig.tight_layout()
    
def visualize_distributions_score(df_reviews):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    ax = axs[0]
    dft = df_reviews.query('ds_part == "train"')['rating'].value_counts().sort_index()
    dft = dft.reindex(index=np.arange(min(dft.index.min(), 1), max(dft.index.max(), 11))).fillna(0)
    dft.plot.bar(ax=ax)
    ax.set_ylim([0, 5000])
    ax.set_title('O conjunto de treinamento: distribuição de classificações')

    ax = axs[1]
    dft = df_reviews.query('ds_part == "test"')['rating'].value_counts().sort_index()
    dft = dft.reindex(index=np.arange(min(dft.index.min(), 1), max(dft.index.max(), 11))).fillna(0)
    dft.plot.bar(ax=ax)
    ax.set_ylim([0, 5000])
    ax.set_title('O conjunto de teste: distribuição de classificações')

    fig.tight_layout()
    
def visualize_polarity_yearly(df_reviews):
    fig, axs = plt.subplots(2, 2, figsize=(16, 8), gridspec_kw=dict(width_ratios=(2, 1), height_ratios=(1, 1)))

    ax = axs[0][0]

    dft = df_reviews.query('ds_part == "train"').groupby(['start_year', 'pos'])['pos'].count().unstack()
    dft.index = dft.index.astype('int')
    dft = dft.reindex(index=np.arange(dft.index.min(), max(dft.index.max(), 2020))).fillna(0)
    dft.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('O conjunto de treinamento: número de resenhas de diferentes polaridades por ano')

    ax = axs[0][1]

    dft = df_reviews.query('ds_part == "train"').groupby(['tconst', 'pos'])['pos'].count().unstack()
    sns.kdeplot(dft[0], color='blue', label='negative', kernel='epa', ax=ax)
    sns.kdeplot(dft[1], color='green', label='positive', kernel='epa', ax=ax)
    ax.legend()
    ax.set_title('O conjunto de treinamento: distribuição de diferentes polaridades por filme')

    ax = axs[1][0]

    dft = df_reviews.query('ds_part == "test"').groupby(['start_year', 'pos'])['pos'].count().unstack()
    dft.index = dft.index.astype('int')
    dft = dft.reindex(index=np.arange(dft.index.min(), max(dft.index.max(), 2020))).fillna(0)
    dft.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('O conjunto de teste: número de resenhas de diferentes polaridades por ano')

    ax = axs[1][1]

    dft = df_reviews.query('ds_part == "test"').groupby(['tconst', 'pos'])['pos'].count().unstack()
    sns.kdeplot(dft[0], color='blue', label='negative', kernel='epa', ax=ax)
    sns.kdeplot(dft[1], color='green', label='positive', kernel='epa', ax=ax)
    ax.legend()
    ax.set_title('O conjunto de teste: distribuição de diferentes polaridades por filme')

    fig.tight_layout()