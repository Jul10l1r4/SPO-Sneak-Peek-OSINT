# -*- coding:UTF-8 -*-
__Author__ = 'Victor de Queiroz'
"""
Class for get json on RECEITA FEDERAL of Brazil
This API is for search data about CNPJ

"""
import urllib.request
import json


class CNPJ(object):

    # function for get api
    def getCNPJ(self, cnpj):
        #prepare string
        no = "./-"
        for i in range(0, len(no)):
            cnpj = cnpj.replace(no[i], "")
        # get url
        url = "http://compras.dados.gov.br/fornecedores/doc/fornecedor_pj/" + cnpj + ".json"

        # use urllib for request http and save on var
        response = urllib.request.urlopen(url)
        # read data
        data = response.read()

        return data



