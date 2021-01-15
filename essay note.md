
# essay note

## Online to offline (O2O) service recommendation method based on multi-dimensional similarity measurement

-   Xiao and Dong [10] proposed a new reputation management system (HSMM-RMS) using asemi-Markov model by combining observable online and offline raw reputation information
    
-   CF-based[18, 19], and memory-based recommendation [21] collaborative filtering (CF) has been the most common approach
    
-   The Pearson Correlation Coefficient( PCC) as the most common similarity measurement, which can generate the numerical distances among users accurately [26]. However, PCC doesn’t work with **sparse matrices**, and most O2O applications are extremely sparse
    
-   Kendall Rank Correlation Coefficient (KRCC) [27], Spearman Rank Correlation Coefficient (SRCC) [28], and AP Correlation Coefficient [29]. Considering service consumption, Jaccard’s Coefficient [30] has been adopted [31, 32] to estimate service recommendation similarity.
    
-   ​ is the collaborative similarity of ​and ​, which ranges from -1 to 1.
    

The negative value is present the pairs have no correlation, rather than opposite behaviors.

-   [10]S. Xiao, M. Dong, Hidden semi-Markov model-based reputation management system for online to offline (O2O) e-commerce markets, Decision Support Systems 77 (2015) 87-99.
    
-   [18]H. Sun, Z. Zheng, J. Chen, M.R. Lyu,Personalized Web Service Recommendation via Normal Recovery Collaborative Filtering, IEEE Transactions on Services Computing 6(4) (2013)
    
-   [19]Z. Zheng, H. Ma, M.R. Lyu, I King, QoS-Aware Web Service Recommendation by Collaborative Filtering, IEEETransactions on Services Computing 4(2) (2011) 140-152
    
-   [21]X. Wang, J. Zhu, Zheng, W. Song, Y. Shen, M.R. Lyu, A Spatial-Temporal QoS Prediction Approach for Time-aware Web Service Recommendation, ACM Transactions on the Web 10(1) (2016) 1-25
    
-   [26]P. Ahlgren, B. Jarneving, R. Rousseau, Requirements for a cocitation similarity measure, with special reference to Pearson's correlation coefficient, Journal of the American Society for Information Science and Technology 54(6) (2003) 550-560
    
-   [27]H. Abdi, The Kendall rank correlation coefficient, Encyclopedia of Measurement and Statistics (2007) 508-510
    
-   [28]J.H. Zar, Significance testing of the Spearman rank correlation coefficient, Journal of the American Statistical Association 67(339) (1972) 578-580.
    
-   [29]E. Yilmaz, J.A. Aslam, S. Robertson, A new rank correlation coefficient for information retrieval, Proceedings of the 31st Annual International ACM SIGIR Conference on Research and Development in Information Retrieval (2008) 587-594
    
-   [30]H. Seifoddini, M. Djassemi, The production data-based similarity coefficient versus Jaccard’s similarity coefficient, Computers & Industrial Engineering 21 (1991) 263-266.
    
-   [31]S. Ding, S. Yang, Y. Zhang, and et al, Combining QoS prediction and customer satisfaction estimation to solve cloud service trustworthiness evaluation problems, Knowledge-Based Systems 56 (2014) 216-225.
    
-   [32]S. Ding, Z. Wang, D. Wu, D.O. Olson, Utilizingcustomer satisfaction in ranking prediction for personalized cloud service selection,Decision Support Systems 90 (2017) 1-10
    

## A Comprehensive Survey on Transfer Learning

-   homogeneous-domain are the same, marginal distribution may be different
    
-   Some interesting transfer learning topics are notcovered in this survey, such as reinforcement transfer learning [8], lifelong transfer learning [9], and online transferlearning [10]
    
-   ![image-20201230184146819](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20201231003.png)
    
-   the transfer learning approaches can be categorized into four groups: instance-based, feature-based, parameter-based, and relational-based approaches.
    
-   ![Image-20201231003](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20201230184146819.png)
    
-   KMM[5]:![Image-20201231004](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20201231004.png)
    
-   KLIEP depends on the minimization of the Kullback-Leibler (KL) divergence and incorporates a built-in model selection procedure.[6]
    
-   TrAdaBoost [31] in TrAdaBoost,the labeled source-domain and labeled target-domain instances are combined as a whole, update:![Image-20210101004](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20210101004.png)
    
-   Multi-Source TrAdaBoost (MsTrAdaBoost) algorithm[33]: 2 steps in each iteration: candidate classifier construction & instance weighting (update weights of instances)->TaskTrAdaBoost
    
    -   labeled target-domain instance (min cross-entropy loss)
        
    -   unlabeled target-domain instance (true conditional distributions ![Image-20210101005](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20210101006.png)
        
    -   labeled source-domain instance
        

![Image-20210101006](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20210101005.png)

-   Find the common latent features (e.g., latent topics) through feature transformation and use them as a bridge to transfer knowledge.
    
    Maximum Mean Discrepancy
    
    ![image-20210102092622813](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20210102092622813.png)
    
    MK-MMD [62], which takes advantage of multiple kernels. ​ is a kind of (nonlinear) mapping.
    
    naive (FAM, not work well in heterogeneous TL): ![image-20210102095522382](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20210102095522382.png)
    
    HFA[66,67]:![image-20210102101325863](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20210102101325863.png)
    
-   ![image-20210102105213024](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20210102105213024.png)​ is nontrivial, apply linear technique.

## Smart City Development with Urban Transfer Learning

   1. urban computing:predict traffic demand or air quality [2][8]. Fine-gained/missing-value prediction & Future prediction; detect abnormal events or objects; find appropriate sites for deploying.
   2. transfer learning. In some field, not-best decision may cause a minor trouble, while in some decision making process that is of high cost (like site choosing).
   3. Heterogeneous Data Modalities. Compare with traditional transfer learning, witch transfers knowledge between domains of the same data modality; the smart city build on heterogeneous data with diverse formats.
### What to transfer?
1. cross-modality: Use data modalities collected from existing services to learn the patterns in the new data modality of the targeted service. *e.g* taxi$\rightarrow$ ride-sharing cars. Users’ social posts and activities can be seen as useful proxies of urban dynamics.
2. cross-city: Using the similar area of known cities (CBD for example).
3. Leverage & combine: If the historical records are not sufficient, we can rely on social media check-ins.

## Bayesian Discovery of Multiple Bayesian Networks via Transfer Learning
Bayesian: minimize weighted risk by classifying
$P(c|x)=\frac{P(c)P(x|c)}{P(x)}$ 

## Transfer Learning via Learning to Transfer

![Image-20210113001](https://raw.githubusercontent.com/sailTo/picturebase/master/Image-20210113001.png)By using L2T agent learns a function $f$ such that $f(S_e,T_e,W_e)$ approximates $l_e$, optimize the $W$ by maximizing the value of $f$.
- Common Latent Space Based
  $Z=\phi(X)$, $G=(X)Z(Z)^T [X^T]$ according to $XG(X)^T=Z(Z)^T$.
- Manifold Ensemble Based
    $Z=[\phi_1(X),\phi_2(X),\dots,\phi_n(X)], n\rightarrow \infty$
- difference between a source and a target domain![image-20210114212107696](https://raw.githubusercontent.com/sailTo/picturebase/master/image-20210114212107696.png)
## To Transfer or Not To Transfer
**Hierarchical Naive Bayes**: *flat naive Bayes* proven to be effective in classifiers in non-transfer settings， avoid negative transfer, it does well compared to the flat algorithm.
transfer will hurt performance if the sources of data are too dissimilar.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4ODc0MDE1NjksLTExNjI5OTQwODAsMj
AyMzM3MTQ5NywtMTE5NTE3NDM1NiwtNjc5NDk5NSwyMDY2MDE5
NTgzLDE4MDg2Mjk3NzMsMTEyOTk4NjQwMSwyMDk5NTU3NDY0LC
0yMDQ4NTc0Mzc2LC0xODA0MDM2NTMwLDE0MjQwMjkyNTgsLTg2
ODYzODk0LDE5MzI4ODk0MDMsMTkxMjUwMDQ3OCwtMTEyNTAzOD
A5MCw4MTM4MTMzMDldfQ==
-->