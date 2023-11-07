from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class Whatsbot:
    def __init__(self):
        # Parte 1 - A mensagem que você quer enviar
        self.mensagem = "Bom dia, Seja Bem vindo à loja Vizeu Design MDF"
        # Parte 2 - Nome dos grupos ou pessoas a quem você deseja enviar a mensagem
        self.grupos_ou_pessoas = ["grupo de teste"]
        service = Service(executable_path='./chromedriver.exe')
        option = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options = option)
        option.add_argument('lang=pt-br')
        self.driver.quit()
        

    def enviar_mensagem(self):
        #<span dir="auto" title="grupo de teste" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr" style="min-height: 0px;">grupo de teste</span>
        #<div class="_1VZX7">
        #<span data-icon="send" class="">
        #<span dir="auto" title="grupo de vendas" aria-label="" class="ggj6brxn gfz4du6o r7fjleex g0rxnol2 lhj4utae le5p0ye3 l7jjieqr _11JPr" style="min-height: 0px;">grupo de vendas</span>
        driver=webdriver.Chrome()
        driver.get('https://web.whatsapp.com')
        time.sleep(30)
        for grupo_ou_pessoa in self.grupos_ou_pessoas:
            campo_grupo = self.driver.find_element(By.XPATH, f'//span[@title="{grupo_ou_pessoa}"]')
            time.sleep(3)
            campo_grupo.click()
            chat_box = self.driver.find_element(By.CLASS_NAME, '_1VZX7')
            time.sleep(3)
            chat_box.click()
            chat_box.send_keys(self.mensagem)
            botao_enviar = self.driver.find_element(By.XPATH, '//span[@data-icon="send"]')
            time.sleep(3)
            botao_enviar.click()
            time.sleep(5)
        


if __name__ == "__main__":
    bot = Whatsbot()
    
bot.enviar_mensagem()