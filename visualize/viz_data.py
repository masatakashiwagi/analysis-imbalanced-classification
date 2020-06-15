import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("darkgrid")
sns.set(font=["IPAexGothic"])


def plot_scatter(df, index=None, both_plot=False):
    plt.figure(figsize=(8, 6))
    plt.subplots_adjust(wspace=0.2, hspace=0.3)
    major = df[df['target'] == 0]
    minor = df[df['target'] == 1]
    plt.scatter(major['feat1'], major['feat2'], c="#ff9966", alpha=.5)
    plt.scatter(minor['feat1'], minor['feat2'], c="#007fff", alpha=.8)
    if both_plot:
        if index is not None:
            plt.scatter(df.loc[index:, 'feat1'], df.loc[index:, 'feat2'], c="#03c03c", alpha=.5)
    plt.xlabel('feat1', fontsize=15)
    plt.ylabel('feat2', fontsize=15)
    plt.legend(["target=0", "target=1"], fontsize=15)
    plt.tick_params(labelsize=15)
    plt.tight_layout()
