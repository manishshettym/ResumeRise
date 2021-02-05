# ResumeRise
A Resume parser and summarizer tool to classify resumes and rank the resumes according to the requirements of the user.

## Dataset
The [dataset](https://www.kaggle.com/iammhaseeb/resumes-dataset-with-labels) consists of 1000 labelled resumes (labelled according to the primary category/class that a particular resume belongs to) in a csv format. We will be using this csv formatted resume dataset to train our model for classification. Our model should then be able to work on any unseen resume.

## Files for reference:
* **Utils/Analysis.ipynb** : Data cleaning + Pre-processing + Visualizations + Insights
* **Utils/Summarize.ipynb** : Resume Summarization algorithm
* **Utils/pdftotext.ipynb** : odf to text conversion using pdfminer
* **Utils/Modelling.ipynb** :main file + representational changes + training + comparison of models + testing
* **Utils/naive_bayes.ipynb** : multinomial naive bayes implementation
* **Utils/svm.ipynb** : svm implementation 
* **Utils/clean_data1.csv**: cleaned resume dataset
