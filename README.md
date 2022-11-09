# Selenium
Exemplo da biblioteca Selenium 
Instalação ds bibliotecas
# instala o selenium para controle de web browser
!pip install selenium
# instala chromium-chromedrive para simular uma Google Chrome que sera controlado
!apt install chromium-chromedriver
Execução do Código
# importa a biblioteca do Selenium que fara simulação e controle de uma navegador WEB
from selenium import webdriver
# O Objeto By é usado para encontrar elementos dentro do HTMl da pagina por ( Tag, Class, ID, XPath)
from selenium.webdriver.common.by import By
# Cria um objeto de opções do navegador
chrome_options = webdriver.ChromeOptions()
# Headless é uma opção para executar seus testes sem a necessidade de abrir o browser
# em um ambiente gráfico, essa função executa o serviço em background,
#onde toda manipulação acontece por debaixo dos panos
chrome_options.add_argument('--headless')
# no-sandbox indica que você quer desabilitar algumas proteções do chrome para usar sua aplicação
# essas proteções existem ara que os usuarios não executem algumas coisas do chome,
# mas como vc esta programando "Acredita-se que você sabe oque esta fazendo e manipulando"
chrome_options.add_argument('--no-sandbox')
# Cria um objeto de navegador com as opções escolhidas acima
driver = webdriver.Chrome('chromedriver',chrome_options=chrome_options)
# Vai até a url do IF
driver.get('https://bra.ifsp.edu.br/servidores')
# Procura o elemento ul que esta dentro de div dentro de div dentro de id="content-section"
# ou seja id="content-section" > div > div > ul
lista = driver.find_element(By.XPATH, '//*[@id="content-section"]/div/div[1]/ul')
# pega todas as tags "li" que estão dentro da UL e transforma numa lista python
linhas = lista.find_elements(By.TAG_NAME, "li")
"Percorre a lista e mostra o texto de item por item"
for l in linhas:
print(l.text)
#links para estudo
# http://pythonclub.com.br/selenium-parte-1.html
# https://www.treinaweb.com.br/blog/o-que-e-selenium
# https://www.youtube.com/watch?v=I336I7vT0Xo
