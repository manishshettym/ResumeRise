import json
import spacy
from spacy.gold import GoldParse
import random
import os
import sys
import argparse
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score
from sklearn.metrics import precision_recall_fscore_support as prfs
def convert_json_to_spacy(json_file_path):

	#try:

		train_data = []

		lines = [] #each line as element of list

		with open(json_file_path, 'r') as f:
			lines = f.readlines()

		#each line = 1 resume
		for line in lines:
			data = json.loads(line)
			
			#print(data)
			#print("\n\n\n\n\n\n\n")

			#Data = {"content":..... ,
			#		 "annotation":
			#				[{"label": .....},
			#				 {	....        }, 
			#					....
			#				}
			#		"extras": ...	
			#		 }


			text = data['content']
			entities = []

			#for each annotated entry(dictionary) in the list of dicts 
			for annotation in data['annotation']:
				
				#label may be a list of labels / 1 label
				labels = annotation['label']

				#points is a array-> actually only one element
				# but is returned as a dict element
				point = annotation['points'][0] 

				#if only one item is label still convert to list
				if not isinstance(labels,list):
					labels = [labels]

				#print(labels)

				#store label entries
				for label in labels:

					entities.append( (point['start'],point['end']+1,label) )


			train_data.append( (text,{"entities": entities}) )


		return train_data
					

					
def train(data,iteration=10,batchsize=10):
	model=spacy.blank('en')
	if "ner" not in model.pipe_names:
		n = model.create_pipe('ner')
		model.add_pipe(n,last=True)

	for cont,annot in data:
		for entity in annot.get('entities'):
			n.add_label(entity[2])
	not_ner = [i for i in model.pipe_names if i!='ner']
	with model.disable_pipes(*(not_ner)):
		opt = model.begin_training()
		#batch=data
		for i in range(iteration):
			batch=random.sample(data,batchsize)
			#print(batch)
			loss={}
			for raw,annot in batch:
				model.update([raw],[annot],drop=0.1,sgd=opt,losses=loss)
			print(loss)
	return model

def test(model,data):
	for context,annot in data:
		text=model(context)
		d={}
		for item in text.ents:
			if item.label_ not in d:
				d[item.label_]=[0,0,0,0,0,0]
			doc_gold_text= model.make_doc(context)
			gold = GoldParse(doc_gold_text, entities=annot.get("entities"))
			y_true = [item.label_ if item.label_ in x else 'Not '+item.label_ for x in gold.ner]
			y_pred = [x.ent_type_ if x.ent_type_ ==item.label_ else 'Not '+item.label_ for x in text]  
			if(d[item.label_][0]==0):
				(p,r,f,s)= prfs(y_true,y_pred,average='weighted')
				a=accuracy_score(y_true,y_pred)
				d[item.label_][0]=1
				d[item.label_][1]+=p
				d[item.label_][2]+=r
				d[item.label_][3]+=f
				d[item.label_][4]+=a
				d[item.label_][5]+=1
	for i in d:
		print("\nReport of '%s' class\n"%(i))
		print("Accuracy : %.2f"%((d[i][4]/d[i][5])*100))
		print("Precision : %.2f"%(d[i][1]/d[i][5]))
		print("Recall : %.2f"%(d[i][2]/d[i][5]))
		print("F-score : %.2f"%(d[i][3]/d[i][5]))





def main():
	parse=argparse.ArgumentParser(description="Input Number of iteration ( --iter) and/or batch size (--batchsize) ")
	parse.add_argument("--iter",type=int,help="Number of iterations")
	parse.add_argument("--batch",type=int,help="Batch size")
	args = parse.parse_args()
	#args=sys.argv
	data = convert_json_to_spacy("./Data/ResumesDataset.json")
	usedata=data
	random.shuffle(usedata)
	split = int(0.8*len(usedata))
	train_data=usedata[:split+1]
	test_data=usedata[split::]
	spacy_pipeline = spacy.blank('en')

	if('ner' not in spacy_pipeline.pipe_names):
		ner = spacy_pipeline.create_pipe('ner')
		spacy_pipeline.add_pipe(ner,last=True)


	for _, item in train_data: #in tuple
		for en in item.get('entities'): #in entities
			print(en)
	if(args.iter and args.batch):
		model=train(train_data,args.iter,args.batch)
	elif args.iter:
		model=train(train_data,iteration=args.iter)
	elif args.batch:
		model=train(train_data,batch=args.batch)
	else:
		model=train(train_data)

	test(model,test_data)







if __name__ == '__main__':
	main()