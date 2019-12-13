
import json
import logging
import datetime


def read_file():
	
	 filename = 'D:/rule-java'


	 with open(filename, 'r', encoding='utf-8') as f:
	 	lines = f.read()

	 	jsons = json.loads(lines)
	 	datas = jsons['data']
	 	jdCheckRules = datas['jdCheckRules']
	 
	 	
	 count = 0
	 nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M%S')


	 with open('D:/files_store/result' + nowTime , 'w') as re:

		 for content in jdCheckRules:

		 	count = count + 1
		 	result = content['brief'].replace('\r\n',' ')

		 	re.writelines(result + '\n')



	 print('count = ', count)



if __name__ == '__main__':
	read_file()
