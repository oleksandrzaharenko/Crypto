from All_Data import CryptoCoefficient, DataFromTXT
from program import finish_data

crypto_coefficient_file_main = DataFromTXT('crypto_coefficient.txt')

create_crypto_files_divided_by_coefficient = CryptoCoefficient(crypto_coefficient_dict = finish_data.crypto_dict,
                                                               crypto_base_filename_2_lvl='crypto_percent_of_portfel.txt')
create_crypto_files_divided_by_coefficient.createCrypto_coefficient_files_by_coefficient()