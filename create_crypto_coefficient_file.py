from All_Data import CryptoCoefficient
from program import finish_data

create_my_crypto_coefficient_file = CryptoCoefficient(crypto_coefficient_dict = finish_data.crypto_dict)
create_my_crypto_coefficient_file.createCrypto_coefficient_file(crypto_list_file_name='crypto_coefficient.txt',
                                                                 crypto_list=finish_data.crypto_list)