
import re  # RegEx - regular expression


endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-123"

# o cep sao 5 digitos, um hifen e 3 digitos

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)  # Match

if busca :
    cep = busca.group()
    print(cep)