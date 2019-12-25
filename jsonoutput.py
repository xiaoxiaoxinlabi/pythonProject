# coding: utf-8
import json
import datetime


def get_datas():

	file_path = 'D:/datas/rule-jdbianma'

	with open(file_path, 'r', encoding = 'utf-8') as f:

		lines = f.read()
		contents = json.loads(lines)
		datasarr = contents['data']
		

	arrdata = []


	count = 0


	with open('D:/files_store/rule-jdbianma-result.json' , 'w') as fw:


		# for key in contents:
		for key in datasarr:

			if 'jdCheckRules'==key:

				rules = datasarr[key]

				for i in rules:

					datas = {}
					count = count + 1

		
					# datas['type'] = i['type']
					datas['id'] = count
					datas['type'] = i['error_level']
					datas['name'] = i['rule_name']
					datas['brief'] = i['brief']
					datas['language'] = 'android'

					arrdata.append(datas)
					
						



	
		# print(json.dumps(arrdata, sort_keys=True, indent=4, separators=(',', ':')))
		format_data = json.dumps(arrdata, sort_keys=True, indent=0, ensure_ascii = False)
		print('count =',count)
		print(format_data)

		

		fw.write(format_data)


		



if __name__ == '__main__':
	get_datas()