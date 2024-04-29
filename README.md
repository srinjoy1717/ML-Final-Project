# ML-Final-Project
Fraud Detection: Neural Networks vs. Outlier Detection

The provided code is the basis for comparing two methods of fraud dectection: Neural Networks and Outlier Detection. Included in this repository is the python script that condenses the data (split.py) and the two .ipynb files that contain the training and validation for the two methods. To train and evaluate these models follow the below steps. 

1. Clone the repository onto your local machine
2. Download the full dataset of simulated financial transaction data from: https://www.kaggle.com/datasets/ealaxi/paysim1
3. Rename the downloaded file as 'transaction_data_copy.csv' (This can be renamed to whatever you want but be sure to update the path in split.py)
4. Run split.py (This should create a new file called 'half_transaction_data.csv'
5. Upload 'half_transaction_data.csv' to Google Colab in a folder named 'Colab Notebooks' (Again this can be changed, but must be changed in the .ipynb files)
6. Download both of the .ipynb files and move them to your Google Drive
7. Open both .ipynb files and run all cells, this will provide the Area Under the Curve (AUC) and F1 Scores for each model
