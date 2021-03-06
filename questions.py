{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "from fake_useragent import UserAgent\n",
    "from xlsxwriter import Workbook"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "main_url= \"https://codingbat.com/java\"\n",
    "links_file_1= \"page_links.txt\"\n",
    "question_list= list()\n",
    "\n",
    "ua= UserAgent()\n",
    "user= {\"user-agent\":\"ua.chrome\"}                            \n",
    "page= requests.get(main_url, headers= user)                       #getting response object from the server\n",
    "\n",
    "with open(links_file_1, \"w\") as file:\n",
    "    file.write(page.content.decode(\"utf-8\")) if type(page.content)== bytes else file.write(page.content)    #writing contents of page to a text file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def read_file(file_name):                            #reading contents of text file\n",
    "    file= open(file_name, \"r\")\n",
    "    data= file.read()\n",
    "    file.close()\n",
    "    return data\n",
    "\n",
    "soup_1= BeautifulSoup(read_file(links_file_1), \"html.parser\")     #parsing \n",
    "base_url= \"https://codingbat.com\"\n",
    "link_1= [(base_url + div.a.get(\"href\")) for div in soup_1.find_all(\"div\", class_= \"summ\")]\n",
    "\n",
    "\n",
    "\n",
    "    \n",
    "    \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "for link in link_1:\n",
    "    \n",
    "    inner_page= requests.get(link, headers= user)\n",
    "    \n",
    "    links_file_2= \"inner_page_links.txt\"\n",
    "    with open(links_file_2, \"w\") as file:\n",
    "        file.write(inner_page.content.decode(\"utf-8\")) if type(inner_page.content)== bytes else file.write(inner_page.content)\n",
    "    \n",
    "    soup_2= BeautifulSoup(read_file(links_file_2), \"html.parser\")\n",
    "    \n",
    "    link_2= [base_url + td.a.get(\"href\") for td in soup_2.find_all(\"td\", width= \"200\")]\n",
    "    \n",
    "    for link_question in link_2:\n",
    "        \n",
    "        question_page= requests.get(link_question, headers= user)\n",
    "        \n",
    "        question_file= \"questions.txt\"\n",
    "        \n",
    "        with open(question_file, \"w\") as file:\n",
    "              file.write(question_page.content.decode(\"utf-8\")) if type(question_page.content)== bytes else file.write(question_page.content)\n",
    "        \n",
    "        soup_3= BeautifulSoup(read_file(question_file), \"html.parser\")\n",
    "        \n",
    "        question_tag= soup_3.find(\"p\", class_=\"max2\")\n",
    "        \n",
    "        question_list.append(question_tag.string)\n",
    "           \n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "workbook= Workbook(\"Questions With Example\")             #writing question to workbook\n",
    "worksheet= workbook.add_worksheet()\n",
    "\n",
    "for i in range(len(question_list)):\n",
    "    worksheet.write(i, 0, question_list[i])\n",
    "        \n",
    "workbook.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
