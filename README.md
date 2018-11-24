# ResumeRise
  A Resume parser and summarizer tool to classify resumes and rank the resumes according to the requirements of the user.
  
  
  
  ## Git commands:
  1. git init
  2. git remote add origin https://github.com/ManishShettyM/ResumeRise.git 
  3. DO NOT forget to pull :  git pull origin master
  4. STEPS TO PUSH :
      * git add --all
      * git commit -m "<message>"
      * git push origin master
  
  ## Pre-Processing
  Cleaning the dataset and creating converters for any format of a resume to be parsed
  
  1.Dataset :
    The [dataset](https://www.kaggle.com/iammhaseeb/resumes-dataset-with-labels) consists of 1000 labelled resumes (labelled according to the primary category/class that a particular resume belongs to) in a csv format.<br>We will be using this csv formatted resume dataset to train our model for classification. Our model should then be able to work on any unseen resume.

## Files for reference:
* **Utils/Analysis.ipynb** : Data cleaning + Pre-processing + Visualizations + Insights
* **Utils/Summarize.ipynb** : Resume Summarization algorithm
* **Utils/pdftotext.ipynb** : odf to text conversion using pdfminer
* **Utils/Modelling.ipynb** :main file + representational changes + training + comparison of models + testing
* **Utils/naive_bayes.ipynb** : multinomial naive bayes implementation
* **Utils/svm.ipynb** : svm implementation 

## Clean dataset: 

* **Utils/clean_data1.csv**

