# sample codes using imbalanced-learn.
Purpose: over-sampling and under-sampling for imbalanced classifications.<br>
imbalanced-learn: https://github.com/scikit-learn-contrib/imbalanced-learn

I create this notebook to understand over and under-sampling technique for imbalanced classifications for myself.

Over-sampling technique: SMOTE (Synthetic Minority Oversampling Technique) & ADASYN (Adaptive Synthetic sampling)<br>
Under-sampling technique: Tomek’s links and ClusterCentroids

### The following is in Japanese.
不均衡データの分類について考えます。<br>
不均衡データとは、positiveクラスとnegativeクラスの比率が極端に異なるデータのことを言っています。

不均衡データの場合には以下の点を意識することが多いと思います。

- 評価指標: Accuracyではなく、Precision/Recallを見る（PR曲線）
- バリデーションの方法: Stratified K-Foldなどを使う
- データ: 少数クラスのover-sampling・多数クラスのunder-sampling

このノートブックでは、`imbalanced-learn`というpythonライブラリーを使って、不均衡データに関する対策の1つであるover-sampling・under-samplingのサンプルコードを載せています。

## My Japanese Article
hoge
