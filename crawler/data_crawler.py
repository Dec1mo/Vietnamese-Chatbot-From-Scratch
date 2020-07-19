import requests
import json

def get_data(url):
	dishes = {}
	response = requests.get(url, verify=False)
	json_response = json.loads(response.content)

	for dish_metadata in json_response['data']:
		dish_list = []
		for dish_data in dish_metadata['dishes']:
			one_dish = {}
			one_dish['id'] = dish_data['id']
			one_dish['name'] = dish_data['name']
			one_dish['price'] = dish_data['price']
			one_dish['rawPrice'] = dish_data['rawPrice']
			one_dish['image'] = dish_data['image']
			one_dish['description'] = dish_data['description']
			one_dish['customs'] = dish_data['customs']
			dish_list.append(one_dish)

		dishes[dish_metadata['name']] = dish_list

	return dishes

def main():
	URL = 'https://mocha.lozi.vn/v1/eateries/slug:tra-sua-chain-quan-go-vap-ho-chi-minh-1588262175839750197/menu'
	dishes = get_data(URL)
	with open('data/dishes_data.json', 'w+', encoding='utf-8') as f:
		json.dump(dishes, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
	main()