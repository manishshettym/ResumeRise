import json
import spacy



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
					

					





def main():

	train_data = convert_json_to_spacy("/home/manish/ACADEMICS/PROJECTS/ResumeRise/Data/ResumesDataset.json")

	spacy_pipeline = spacy.blank('en')

	if('ner' not in spacy_pipeline.pipe_names):
		ner = spacy_pipeline.create_pipe('ner')
		spacy_pipeline.add_pipe(ner,last=True)


	for item in train_data: #in tuple
		for en in item.get('entities'): #in entities
			print(en)







if __name__ == '__main__':
    main()