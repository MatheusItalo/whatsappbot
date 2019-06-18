from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

person = input("Informe qual pessoa voce deseja enviar mensagem")
msg = input("informe a mensagem a ser enviada")
count = int(input("Informe quantas vezes deseja enviar essa mensagem"))

input("aperte enter depois de scannear o qrcode")

user = driver.find_element_by_xpath('//span[@title="{}"]'.format(person))
user.click()

msg_box = driver.find_element_by_class_name('_13mgZ')


for i in range(count):
    msg_box.send_keys(msg)
    buttonSend = driver.find_element_by_class_name('_3M-N-')
    buttonSend.click()