# Data Analysis & Learning Methods - Lecture 4

Q: What is the primary goal of clustering?
A: To group data points into clusters based on similarity, such that points within a group are more similar to each other than to those in other groups (page 4).

Q: List three practical applications of clustering.
A: Data compression (replacing groups with representatives), visualization (creating high-level overviews), and subgraph detection (finding communities in networks) (pages 5-7).

Q: What is the main difference between agglomerative and divisive hierarchical clustering?
A: Agglomerative clustering is a "bottom-up" approach that starts with individual points and merges them, while divisive clustering is a "top-down" approach that starts with one cluster and splits it (page 9).

Q: What does the "single-linkage" distance metric refer to in agglomerative clustering?
A: It defines the distance between two clusters as the minimum distance between any two points in the respective clusters (page 10).

Q: What are two significant limitations of hierarchical clustering?
A: It has a high computational cost ($O(N^2)$) due to the need for all pairwise distances, and you cannot pre-specify the number of clusters to speed up the process (page 18).

Q: What is a "centroid" in the context of K-means clustering?
A: A centroid is the multidimensional average of all points within a cluster; it acts as the cluster's representative center but is not part of the original dataset (page 20).

Q: Briefly describe the two main steps of the iterative K-means algorithm.
A: 1. Assignment step: Assign each data point to the nearest centroid. 2. Update step: Recalculate the centroids as the mean of all points assigned to them (page 20).

Q: What is a major drawback of the K-means algorithm when dealing with non-globular or unevenly sized clusters?
A: K-means is blind to the natural size and shape of clusters and can get stuck in unintuitive solutions, such as splitting a large cluster or merging two distinct small ones (page 31).

Q: How does fuzzy clustering differ from crisp (or hard) clustering?
A: In crisp clustering, each data point belongs to exactly one cluster, while in fuzzy clustering, each point can belong to multiple clusters with a varying degree of membership (page 32).

Q: What is the role of the "fuzziness parameter" (m) in the Fuzzy c-means (FCM) algorithm?
A: The parameter $m \in (1, \infty)$ controls the degree of fuzziness or overlap between clusters; a higher 'm' results in fuzzier clusters (page 34, 54).

Q: What constraint is imposed on the membership values ($\mu_{ik}$) for any given data point in FCM?
A: The sum of a data point's membership values across all clusters must equal 1, which is known as the probabilistic constraint: $\sum_{i=1}^{C} \mu_{ik} = 1$ (page 34, 51).

Q: How are the cluster centers ($v_i$) updated in the FCM algorithm?
A: The cluster centers are calculated as the weighted mean of all data points, where the weight of each point is its membership value raised to the power of m: $v_i = \frac{\sum_{k=1}^{N} \mu_{ik}^m x_k}{\sum_{k=1}^{N} \mu_{ik}^m}$ (page 35).

Q: What is the main advantage of the Gustafson-Kessel (GK) algorithm compared to FCM?
A: The GK algorithm uses an adaptive distance metric based on a fuzzy covariance matrix, allowing it to find clusters of different shapes and orientations, not just spherical ones (page 39).

Q: Why is data normalization often a necessary pre-processing step for clustering?
A: To ensure that features measured on different scales contribute equally to the distance calculation; without it, features with larger ranges can dominate the clustering process (page 43).

Q: What is the purpose of using cluster validity measures?
A: They are used to quantitatively evaluate the quality of clustering results and can help determine the optimal number of clusters for a given dataset (page 46).

Q: What is a significant problem caused by the probabilistic constraint in FCM, especially concerning outliers?
A: Outliers far from all cluster centers are still forced to have memberships summing to 1, which can pull cluster centers away from their true locations and distort the results (page 51).

Q: How does Possibilistic c-means (PCM) address the outlier problem of FCM?
A: PCM relaxes the probabilistic constraint, allowing a data point's membership in a cluster to be independent of its membership in other clusters. Outliers can thus have low membership in all clusters (page 52-53).

Q: In Possibilistic c-means (PCM), how is the membership value $\mu_{ik}$ calculated?
A: It is calculated using the formula $\mu_{ik} = \frac{1}{1 + (\frac{d_{ik}^2}{\eta_i})^{1/(m-1)}}$, which depends only on the distance to its own cluster center and a cluster-specific parameter $\eta_i$ (page 53).


Overview: Fourth lecture

Date: 12 Sep 2025
