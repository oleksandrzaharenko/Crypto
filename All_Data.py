from openpyxl import load_workbook
import requests


class DataFromTXT:

    def __init__(self, txt_filename):
        self.txt_filename = txt_filename
        self.data_from_file = DataFromTXT.getDataFromFile(self)

    def getDataFromFile(self):
        with open(self.txt_filename, "r") as data:
            return data.read().splitlines()


    def createListFromDataFromFile(self, index):
        result_list = []
        for element in self.data_from_file:
            result_list.append(element.split()[index])
        return result_list

class DataFromExcel:

    def __init__(self, excel_name):
        self.excel_name = excel_name


    def getValuesFromExcelToList(self, start_row, column_number):
        workbook = load_workbook(self.excel_name)
        workbook = workbook.active
        result_list = []
        while True:
            crypto = workbook.cell(row=start_row, column=column_number).value
            start_row += 1
            if crypto is None:
                break
            else:
                result_list.append(crypto)
        return result_list

class API_Data:

    def __init__(self, url='https://api.binance.com/api/v3/ticker/24hr'):
        self.url = url
        self.dataFromApi = API_Data.getDataFromAPI(self)
        self.all_tickets_from_Api = self.dataFromApi[0].keys()


    def getDataFromAPI(self): # use to check tickets names
        return requests.get(self.url).json()


    def createCryptoDictWithValues(self, crypto_dict, value_ticket, crypto_ticket):
        result_dict = {}
        for crypto in crypto_dict:
            for element in self.dataFromApi:
                if element[crypto_ticket] == crypto:
                    result_dict[crypto] = float(element[value_ticket])
        return result_dict


class CryptoData:

    def __init__(self, crypto_list, crypto_amount_list, crypto_price_transactions_list):
        self.crypto_list = crypto_list
        self.crypto_dict = dict.fromkeys(self.crypto_list)
        self.crypto_all_transactions_dict = CryptoData.createCryptoDictWithValues(self, crypto_price_transactions_list)
        self.crypto_amount_dict = CryptoData.createCryptoDictWithValues(self, crypto_amount_list)


    def createCryptoDictWithValues(self, crypto_values_list):
        result_dict = dict.fromkeys(self.crypto_list)
        for crypto in result_dict:
            result_dict[crypto] = sum([float(crypto_values_list[i]) for i in range(len(crypto_values_list)) if self.crypto_list[i] == crypto])
        return result_dict

class FinishData:

    def __init__(self, output_file_name,
                 start_crypto_list, transactions_crypto_list,
                 start_total_cost_dict, transactions_total_cost_dict,
                 start_amount_dict, transactions_amount_list_dict):

        self.output_file_name = output_file_name
        self.crypto_list = list(set(start_crypto_list + transactions_crypto_list))
        self.crypto_dict = dict.fromkeys(self.crypto_list)
        self.crypto_amount_dict = FinishData.sumStartDataAndNewData(self, start_amount_dict, transactions_amount_list_dict)
        self.crypto_total_cost_dict = FinishData.sumStartDataAndNewData(self, start_total_cost_dict, transactions_total_cost_dict)
        self.crypto_average_price_dict = FinishData.countCryptoAveragePrice(self, self.crypto_list, self.crypto_total_cost_dict, self.crypto_amount_dict)

    def sumStartDataAndNewData(self, start_data_dict, new_data_dict):
        for element in new_data_dict:
            if element in start_data_dict.keys():
                start_data_dict[element] = start_data_dict[element] + new_data_dict[element]
        return start_data_dict


    def countCryptoAveragePrice(self, crypto_list, crypto_costs, crypto_amount):
        crypto_average_prices = {}
        for crypto in crypto_list:
            crypto_average_prices[crypto] = round((crypto_costs[crypto] / crypto_amount[crypto]),3)
        return crypto_average_prices


    def countCryptoProfit(self, actual_crypto_prices_dict):
        crypto_profit = {}
        for crypto in self.crypto_dict:
            crypto_profit[crypto] = (100 * actual_crypto_prices_dict[crypto] / self.crypto_average_price_dict[crypto]) - 100
        return crypto_profit


    def save_data_to_txt(self, actual_crypto_price_dict, crypto_profit_dict):
        with open(self.output_file_name, 'w') as report_file:
            report_file.write('{0:13} {1:13} {2:20} {3:20} {4:20} {5:20}\n'.format('Crypto', 'Amount', 'Total Costs USDT', 'AveragePrice', 'Crypto Price', 'Profit%'))
            for crypto in self.crypto_dict:
                report_file.write('{0:5}'
                                  ' {1:15.4f}'
                                  ' {2:18.3f}'
                                  ' {3:18.3f}'
                                  ' {4:18.3f}'
                                  ' {5:18.3f}\n'.format(crypto, float(self.crypto_amount_dict[crypto]),
                                                        float(self.crypto_total_cost_dict[crypto]),
                                                        self.crypto_average_price_dict[crypto],
                                                        actual_crypto_price_dict[crypto],
                                                        crypto_profit_dict[crypto]))
            report_file.close()




