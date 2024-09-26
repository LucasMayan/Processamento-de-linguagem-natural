#pip install spacy
#pip install -U pip setuptools wheel
#pip install -U spacy
#python -m spacy download en_core_web_sm
#python -m spacy download pt_core_news_sm

import spacy

#preparação
nlp = spacy.load("pt_core_news_sm")
texto = 'O Brasil foi descoberto por Pedro Álvares Cabral e é um país da América do Sul'
doc = nlp(texto)

#mostrar as entidades nomeadas
print(doc.ents)

#tokens
for token in doc:
    print(token, token.idx, token.shape_, token.tag_)

#mostrando informação sobre o tipo de entidade
for entidade in doc.ents:
    print(entidade.text,' | ', entidade.label_)


#explica o significado
resultado = spacy.explain('PER')
print(resultado)



#Extraindo nomes de marcas com NER
artigo = """ O Brasil possui grandes empresas nas áreas de tecnologia. Por exemplo, na área de telefonia móvel o grande destaque vai para empresas como Vivo e Claro.
Outra grande empresa de tecnologia é a IBM que, juntamente com a Amazon, se destacam na entrega de computação em nuvem. 
Outra empresa que merece destaque é a Samsung, a qual desenvolve smartphones e dispositivos tecnológicos. 
O estado de São Paulo é o que lidera com o maior número de empresas e indústrias de tecnologia, seguido pelo Rio de Janeiro. 
Uma característica importante é o crescimento de startups na região Sul, principalmente na cidade de Florianópolis em Santa Catarina. 
Em São Paulo, em 2011, o Facebook (empresa criada por Mark Zuckerberg) inaugurou um escritório no bairro do Itaim Bibi.
"""
doc = nlp(artigo)

#mostrando informação sobre o tipo de entidade
for entidade in doc.ents:
    print(entidade.text,' | ', entidade.label_)


#LISTA DAS ORGANIZAÇÕES
lista_organizacoes=[]

for entidade in doc.ents:
  if entidade.label_=='ORG':
    lista_organizacoes.append(entidade.text)

print(lista_organizacoes)