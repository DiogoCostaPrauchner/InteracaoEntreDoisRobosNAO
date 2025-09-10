# Interação Entre Dois Robôs NAO 🤖

 Este repositório servirá para armazenar apresentações que seram importadas para os robôs e, além disso, um script Python, que utiliza da API NAOqi e o SDK para Python, para realizar a interação entre dois robôs NAO.
 
 Choregraphe foi utilizado para criar arquivos *behavior* (.xar) que serão instalados nos robôs, e a edição comunitária de PyCharm para o desenvolvimento do script.

# Como utilizar 💻

 É apenas rodar o script usando o seu método de preferência, como por exemplo, no terminal, após ter instalado Python 2.7.9.
 
 Os arquivos *Behavior* (.xar) necessários já estão instalados dentro dos robôs.

# Manutenção do script 🪛

 Primeiramente, é necessário instalar Python 2.7.9, pois é a versão que o SDK Python utiliza.
 
 Além disso, também é necessário instalar o SDK Python do site oficial da Aldebaran, o projeto foi desenvolvido utilizando a SDK 2.8.6 para Windows.

 Após ter descompactado a pasta do SDK Python no disco *C:*, é necessário configurar as váriaveis de ambiente Path e PYTHONPATH na máquina onde será executado o script.

 *Path* deve apontar para a pasta do Python 2.7.9, e *PYTHONPATH* deve apontar para a pasta *lib* do SDK.
 
# Considerações finais 🌟

 Vale lembrar que existe um SDK para Python 3 chamado **libqi**, mas ao considerar que para utilizar esta versão é necessário instalar pacotes dentro dos robôs, a versão antiga foi escolhida pela sua facilidade de manutenção.

 [Link para o download do SDK Python](https://aldebaran.com/en/support/kb/nao6/downloads/nao6-software-downloads/)

 [Link para o download do Python versão 2.7.9](https://www.python.org/downloads/release/python-279/)

### *Feito para a área de robótica da bolsa PIBEX da Universidade Regional do Noroeste do Estado do Rio Grande do Sul (UNIJUÍ).*
