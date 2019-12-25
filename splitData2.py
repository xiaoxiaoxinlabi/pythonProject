
import json
import datetime


def get_datas():

	file_path = 'D:/datas/rule-sonar'

	with open(file_path, 'r', encoding = 'utf-8') as f:

		lines = f.read()
		contents = json.loads(lines)

	nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

	codeSemll = []
	bugs = []
	vulnerability = []
	datas = {}



	with open('D:/files_store/rule-sonar-result' + nowTime, 'w', encoding = 'utf-8') as fw:


		for key in contents:

			if 'rules'==key:

				rules = contents[key]

				for i in rules:


					if 'CODE_SMELL'==i['type']:
					
						codeSemll.append(i['name'])


					elif 'VULNERABILITY'==i['type']:

						vulnerability.append(i['name'])
						

					elif 'BUG'==i['type']:
						bugs.append(i['name'])
						



		datas['CODE_SMELL'] = codeSemll
		datas['VULNERABILITY'] = vulnerability
		datas['BUG'] = bugs

		print(json.dumps(datas, sort_keys=True, indent=4, separators=(',', '\n')))
		format_data = json.dumps(datas, sort_keys=True, indent=4, separators=(',', '\n'))

		fw.writelines(format_data)


		


						



			
				



			
				

		

			

			




if __name__ == '__main__':
	get_datas()