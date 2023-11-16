import re #RegEx

class ExtratorURL :
    def __init__(self, url) :
        self.url = self.sanitiza_url(url)
        self.valida_url(url)

    def sanitiza_url(self, url) :
        if type(url) == str :
            return url.strip()
        else :
            return ""
    
    def valida_url(self, url) :
        if not self.url :
            raise ValueError("A Url está vazia")
        
        padrao_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrao_url.match(url)
        if not match :
            raise ValueError("A url não é válida")
            
    def get_url_base(self) :
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base
    
    def get_url_parametros(self) :
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao+1:]
        return url_parametros
        
    def get_valor_parametro(self, parametro_busca) :
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)
        if indice_e_comercial == -1 :
            valor = self.get_url_parametros()[indice_valor:]
        else :
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor
    
    def __len__(self) :
        return len(self.url)
    
    def __str__(self) :
        return self.url + "\n" + "Url Base: " + self.get_url_base() + "\n" + "Parâmetros: " + self.get_url_parametros()
    
    def __eq__(self, outro) :
        return self.url == outro.url
    
        
url = "https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

extrator_url = ExtratorURL(url)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)

parametro = "quantidade"
valor_parametro = extrator_url.get_valor_parametro(parametro)
float_valor_quantidade = float(extrator_url.get_valor_parametro("quantidade"))
print("O Parâmetro " + parametro + " é " + valor_parametro)

conversao_dolar_real = float(5.5)
print("O valor em dólar é: ", float_valor_quantidade*conversao_dolar_real)

# aprendendo sobre equidade e endereço de memoria
extrator_url_2 = ExtratorURL(url)
print(extrator_url == extrator_url_2)
print(extrator_url is extrator_url_2)
