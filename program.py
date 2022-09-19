import os.path
from All_Data import DataFromTXT, API_Data, DataFromExcel, CryptoData, FinishData, PotentialInvestment

data_from_excel = DataFromExcel("Actual_Average_data.xlsx")
data_from_txt = DataFromTXT("buy_data.txt")


start_data = CryptoData(
    crypto_list = data_from_excel.getValuesFromExcelToList(start_row=3,column_number=1),
    crypto_amount_list = data_from_excel.getValuesFromExcelToList(start_row=3,column_number=2),
    crypto_price_transactions_list = data_from_excel.getValuesFromExcelToList(start_row=3,column_number=4)
)

last_transactions_data = CryptoData(
    crypto_list = data_from_txt.createListFromDataFromFile(index=0),
    crypto_amount_list = data_from_txt.createListFromDataFromFile(index=1),
    crypto_price_transactions_list=data_from_txt.createListFromDataFromFile(index=2)
)

finish_data = FinishData(
    output_file_name='my_average_crypto_price.txt',
    start_crypto_list=start_data.crypto_list,
    transactions_crypto_list=last_transactions_data.crypto_list,
    start_total_cost_dict=start_data.crypto_all_transactions_dict,
    transactions_total_cost_dict=last_transactions_data.crypto_all_transactions_dict,
    start_amount_dict=start_data.crypto_amount_dict,
    transactions_amount_list_dict=last_transactions_data.crypto_amount_dict,
)

data_from_api = API_Data()
crypto_prices_dict = data_from_api.createCryptoDictWithValues(finish_data.crypto_dict, 'lastPrice', 'symbol')
crypto_profit_dict = finish_data.countCryptoProfit(crypto_prices_dict)

finish_data.save_data_to_txt(actual_crypto_price_dict=crypto_prices_dict,
                             crypto_profit_dict=crypto_profit_dict)
