# Amazon_Vine_Analysis
Module #16 Big Data

## Project Overview
Analize Amazon reviews written by members of the paid Amazon Vine program. The Amazon Vine program is a service that allows manufacturers and publishers to receive reviews for their products. Companies like SellBy pay a small fee to Amazon and provide products to Amazon Vine members, who are then required to publish a review.

## Resources
- Data Source: https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_Music_v1_00.tsv.gz 
- Data Source2: vine_table.csv
- Software: Python 3.7, Pandas, VS Code, AWS. PostgreSQL, PYSPARK


## Analysis Results
Once the reviews where filtered by customers who had greater of equal to 20 total zones, and of which greater than 50% were helpful, the following analysis could be performed on vine vs non-vine customers. 

### Figure 1: Vine Subscribers
![Pay](https://github.com/Jarney903/Amazon_Vine_Analysis/blob/main/analysis/Figure1.jpg)
<br />

### Figure 2: Vine Non-Subscribers
![Non-Pay](https://github.com/Jarney903/Amazon_Vine_Analysis/blob/main/analysis/Figure2.jpg)
<br />

## Analysis Summary
According to Figure 1 vs Figure 2, there is no positivity bias for reviews in the Vine program. 

One additional analysis that could be performed with the dataset to support this is to limit the filter to allow 4-star reviews as well as 5 star reviews. Also, average the 'star_rating' column for both vine and non-vine customers. 



    
  