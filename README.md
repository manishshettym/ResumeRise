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
  The DataTurks tool has been used to manually annotate 220 resumes from www.indeed.com.
  
  1.Dataset :
    The first task at hand of course is to create manually annotated training data to train the model. For this purpose, 220       resumes were downloaded from an online jobs platform. These documents were uploaded to our online annotation tool and           manually annotated.

   The tool automatically parses the documents and allows for us to create annotations of important entities we are interested    in and generates json formatted training data with each line containing the text corpus along with the annotations.

   A snapshot of the dataset can be seen below :
   ![alt text](https://github.com/ManishShettyM/ResumeRise/blob/master/Utils/dataturks.png)




