__Author__ = 'Victor de Queiroz'
# -*- coding:UTF-8 -*-
"""
Crawler for jurisprudence. www.jusbrasil.com.br

This is a Brazilian site for lawyers publications about jurisprudence and others informations
such as "diário da união" posts.

This crawler search jurisprudence for CNPJ
(CNPJ is a Brazilian documentation about companies)
"""

# query for search format
# https://www.jusbrasil.com.br/jurisprudencia/busca?q=07.170.938%2F0001-07
# format cnpj reciverd = 07.170.938/0001-07
# format query serch cnpj = 07.170.938%2F0001-07

import urllib.request
from bs4 import BeautifulSoup


class Jurisprudence():

    def jurisprudence(self,cnpj):
        # replace / to %2F on cnpj
        sub = "/"
        for i in range(0, len(sub)):
            cnpj = cnpj.replace(sub[i], "%2F")

        # connect to jusbrasil for request a html content
        with urllib.request.urlopen("https://www.jusbrasil.com.br/jurisprudencia/busca?q=" + cnpj) as url:
            # open html
            url_dump = url.read()

        # instance of beautifulsoup
        soup = BeautifulSoup(url_dump, "lxml")

        # example of data
        """
        <div class="i juris" data-content-copyable data-doc-artifact="JURISPRUDENCIA" data-doc-id="435830624">
          <h2 class="title small"> 
           <a href="https://tj-pr.jusbrasil.com.br/jurisprudencia/435830614/processo-civel-e-do-trabalho-recursos-recurso-inominado-ri-901826201681600140-pr-0009018-2620168160014-0-acordao/inteiro-teor-435830624"> TJ-PR - Inteiro Teor. PROCESSO C\xc3\x8dVEL E DO TRABALHO - Recursos - Recurso Inominado: RI 901826201681600140 PR 0009018-26.2016.8.16.0014/0 (Ac\xc3\xb3rd\xc3\xa3o)</a></h2>
            <p class="info">  Data de publica\xc3\xa7\xc3\xa3o: 03/03/2017  </p>
              <p class="snippet">  <strong class="header-name">Decis\xc3\xa3o: </strong>.025-130 Recorrido(s): CNOVA COMERCIO ELETRONICO S.A. (CPF/CNPJ: <b>07.170.938/0001-07</b>) Rua Gomes de Carvalho, 1609 4  </p>
        </div>
    
        """
        # search div class "i juris" on url_dump
        result_not_treated = soup.findAll("div", {"class": "i juris"})

        #search number of pages on result and create a links for crawler
        links_of_pages_not_treated = soup.findAll("a", {"class":"number"})
        if links_of_pages_not_treated:
            #initialize link list
            links_number_pages = {}
            #get last page
            number = len(links_of_pages_not_treated)
            links_of_pages_not_treated = links_of_pages_not_treated[number - 1]
            links_of_pages_last = str(links_of_pages_not_treated).replace("<a class=\"number\"","")
            links_of_pages_last = links_of_pages_last.replace("data-filter-name=\"page\"","")
            links_of_pages_last = links_of_pages_last.replace("data-filter-value=\"","")
            links_of_pages_last = links_of_pages_last.replace("rel=\"nofollow\">","")
            links_of_pages_last = links_of_pages_last.replace("</a>","")
            links_of_pages_last = links_of_pages_last.replace("\"","")
            links_of_pages_last = links_of_pages_last.split()
            links_of_pages_last = links_of_pages_last[1]
            links_of_pages_last = links_of_pages_last.replace("href=","")
            links_of_pages_last = links_of_pages_last.replace("&amp","&p=")
            links_of_pages_last = links_of_pages_last.split(";")
            last_page = links_of_pages_last[1].split("p=")

            #create a list for urls
            for i in range(int(last_page[1]) + 1):
                if i == 0:
                    i += 1
                links_number_pages.update({ i:"https://www.jusbrasil.com.br"+links_of_pages_last[0]+str(i)+"&amp%3B"+str(links_of_pages_last[1])})


        if not links_of_pages_not_treated:
            # treat result_not_treated for show date of jurisprudence and link to show
            #initializate data_trated
            data_treated = {}

            #update data_treated with link and data_link extrated from beautifulsoup
            for i in range(len(result_not_treated)):
                link = str(result_not_treated[i].find_all("a"))
                link = link.replace("<a href=\"", "")
                link = link.split("\"")
                link = link[0]
                link = link.replace("[","")
                data_link = str(result_not_treated[i].find_all("p", {"class":"info"}))
                data_link = data_link.replace("<p class=\"info\"> ","")
                data_link = data_link.replace(" </p>","")
                data_link = data_link.replace("Data de publicação: ","")
                data_link = data_link.replace("[ ","")
                data_link = data_link.replace(" ]","")
                if data_link in data_treated:
                    data_treated.update({data_link+"("+str(i)+")":link})
                data_treated.update({data_link:link})

            return data_treated
        else:
            # treat result_not_treated for show date of jurisprudence and link to show
            # initializate data_trated
            data_treated = {}

            # update data_treated with link and data_link extrated from beautifulsoup
            for i in range(len(result_not_treated)):
                link = str(result_not_treated[i].find_all("a"))
                link = link.replace("<a href=\"", "")
                link = link.split("\"")
                link = link[0]
                link = link.replace("[", "")
                data_link = str(result_not_treated[i].find_all("p", {"class": "info"}))
                data_link = data_link.replace("<p class=\"info\"> ", "")
                data_link = data_link.replace(" </p>", "")
                data_link = data_link.replace("Data de publicação: ", "")
                data_link = data_link.replace("[ ", "")
                data_link = data_link.replace(" ]", "")
                if data_link in data_treated:
                    data_treated.update({data_link + "(" + str(i) + ")": link})
                data_treated.update({data_link: link})

        for i in range(1,len(links_number_pages)):
            # connect to jusbrasil for request a html content
            with urllib.request.urlopen(links_number_pages[i]) as url:
                # open html
                url_dump = url.read()

            # instance of beautifulsoup
            soup = BeautifulSoup(url_dump, "lxml")

            # search div class "i juris" on url_dump
            result_not_treated = soup.findAll("div", {"class": "i juris"})

            # treat result_not_treated for show date of jurisprudence and link to show
            # initializate data_trated
            data_treated = {}

            # update data_treated with link and data_link extrated from beautifulsoup
            for i in range(len(result_not_treated)):
                link = str(result_not_treated[i].find_all("a"))
                link = link.replace("<a href=\"", "")
                link = link.split("\"")
                link = link[0]
                link = link.replace("[", "")
                data_link = str(result_not_treated[i].find_all("p", {"class": "info"}))
                data_link = data_link.replace("<p class=\"info\"> ", "")
                data_link = data_link.replace(" </p>", "")
                data_link = data_link.replace("Data de publicação: ", "")
                data_link = data_link.replace("[ ", "")
                data_link = data_link.replace(" ]", "")
                if data_link in data_treated:
                    data_treated.update({data_link + "(" + str(i) + ")": link})
                data_treated.update({data_link: link})

            return data_treated

        return data_treated