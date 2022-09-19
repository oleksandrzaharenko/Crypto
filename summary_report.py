from All_Data import PotentialInvestment, DataFromTXT
from program import finish_data

my_crypto_coefficients = DataFromTXT("crypto_coefficient.txt")
portfel_0_6_coefficicent = DataFromTXT("0.6_crypto_percent_of_portfel.txt")
portfel_0_3_coefficicent = DataFromTXT("0.3_crypto_percent_of_portfel.txt")
portfel_0_1_coefficicent = DataFromTXT("0.1_crypto_percent_of_portfel.txt")



last_investment = PotentialInvestment(actual_crypto_cost_dict=finish_data.crypto_total_cost_dict,
                                      crypto_coefficients_dict=my_crypto_coefficients.createDictFromDataDependsOnFile(keys_list=my_crypto_coefficients.createListFromDataFromFile(index=0),
                                                                                                                           values_list=my_crypto_coefficients.createListFromDataFromFile(index=1)),
                                      investment=200)

invesment_for_portfel_0_6 = PotentialInvestment(actual_crypto_cost_dict = finish_data.crypto_total_cost_dict,
                                  crypto_coefficients_dict=portfel_0_6_coefficicent.createDictFromDataDependsOnFile(keys_list=portfel_0_6_coefficicent.createListFromDataFromFile(index=0),
                                                                                                                    values_list=portfel_0_6_coefficicent.createListFromDataFromFile(index=1)),
                                  investment = last_investment.investment_divided_by_percent['0.6'])

invesment_for_portfel_0_3 = PotentialInvestment(actual_crypto_cost_dict = finish_data.crypto_total_cost_dict,
                                  crypto_coefficients_dict=portfel_0_3_coefficicent.createDictFromDataDependsOnFile(keys_list=portfel_0_3_coefficicent.createListFromDataFromFile(index=0),
                                                                                                                    values_list=portfel_0_3_coefficicent.createListFromDataFromFile(index=1)),
                                  investment = last_investment.investment_divided_by_percent['0.3'])

invesment_for_portfel_0_1 = PotentialInvestment(actual_crypto_cost_dict = finish_data.crypto_total_cost_dict,
                                  crypto_coefficients_dict=portfel_0_1_coefficicent.createDictFromDataDependsOnFile(keys_list=portfel_0_1_coefficicent.createListFromDataFromFile(index=0),
                                                                                                                    values_list=portfel_0_1_coefficicent.createListFromDataFromFile(index=1)),
                                  investment = last_investment.investment_divided_by_percent['0.1'])



print('TOTAL SUMMARY REPORT')
print('Actual total investment: ', last_investment.actual_total_cost)
print('Investment: ', last_investment.investment)
print('Expected total investment: ', last_investment.potential_total_investment)
print('Actual portfel sitation: ', last_investment.actual_portfel_situation_main)
print('Expected portfel situation: ', last_investment.expected_portfel_situation)
print('My portfel: ', last_investment.coefficient_for_crypto_dict)
print('Expected invesment in portfel coefficients: ',last_investment.investment_divided_by_percent)
print('\n')

print('SUMMARY FOR PORTFEL 0.6')
print('Actual total investment: ', invesment_for_portfel_0_6.actual_total_cost)
print('Investment: ', invesment_for_portfel_0_6.investment)
print('Expected total investment: ', invesment_for_portfel_0_6.potential_total_investment)
print('Actual portfel sitation: ', invesment_for_portfel_0_6.actual_portfel_situation_main)
print('Expected portfel situation: ', invesment_for_portfel_0_6.expected_portfel_situation)
print('My portfel: ', invesment_for_portfel_0_6.coefficient_for_crypto_dict)
print('Expected investment in Crypto: ', invesment_for_portfel_0_6.createPotencialInvestmentByCrypto())
print('Expected invesment in portfel coefficients: ',invesment_for_portfel_0_6.investment_divided_by_percent)
print('\n')

print('SUMMARY FOR PORTFEL 0.3')
print('Actual total investment: ', invesment_for_portfel_0_3.actual_total_cost)
print('Investment: ', invesment_for_portfel_0_3.investment)
print('Expected total investment: ', invesment_for_portfel_0_3.potential_total_investment)
print('Actual portfel sitation: ', invesment_for_portfel_0_3.actual_portfel_situation_main)
print('Expected portfel situation: ', invesment_for_portfel_0_3.expected_portfel_situation)
print('My portfel: ', invesment_for_portfel_0_3.coefficient_for_crypto_dict)
print('Expected investment in Crypto: ', invesment_for_portfel_0_3.createPotencialInvestmentByCrypto())
print('Expected invesment in portfel coefficients: ',invesment_for_portfel_0_3.investment_divided_by_percent)
print('\n')

print('SUMMARY FOR PORTFEL 0.1')
print('Actual total investment: ', invesment_for_portfel_0_1.actual_total_cost)
print('Investment: ', invesment_for_portfel_0_1.investment)
print('Expected total investment: ', invesment_for_portfel_0_1.potential_total_investment)
print('Actual portfel sitation: ', invesment_for_portfel_0_1.actual_portfel_situation_main)
print('Expected portfel situation: ', invesment_for_portfel_0_1.expected_portfel_situation)
print('My portfel: ', invesment_for_portfel_0_1.coefficient_for_crypto_dict)
print('Expected investment in Crypto: ', invesment_for_portfel_0_1.createPotencialInvestmentByCrypto())
print('Expected invesment in portfel coefficients: ',invesment_for_portfel_0_1.investment_divided_by_percent)
print('\n')
