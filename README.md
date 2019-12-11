# strider-gis
Desafio Técnico | Strider | 11/12/2019

## Tecnologias Utilizadas
* Python3
* Flask
* RasterIO
* Connexion

# Desafio
A imagem 319567_2331703_2016-12-07_0c0b-20161207T151953Z.tif é uma imagem de
satélite multiespectral georreferenciada em formato GeoTIFF obtida pelo microsssatélite ID 0c0b da constelação PlanetScope em 7 de dezembro de 2016, às 15h19m53s UTC.

Ela possui as seguintes bandas:

ÍNDICE       BANDA       ALCANCE ESPECTRAL (nm)
===============================================
1            Blue        455 - 515
2            Green       500 - 590
3            Red         590 - 670
4            NIR         780 - 860

Sua missão é calcular o seguinte:

- Percentual de área desta imagem que está coberto por algum tipo de vegetação
- Centróide geográfico da cena
- Área em quilômetros quadrados da cena
- Horário local da captura

Esse cálculo deverá ser fornecido através de um endpoint HTTP em formato JSON.
O arquivo swagger_api.yml contém a especificação exata do formato de retorno
e do nome do endpoint.

O servidor que serve o endpoint deve ser feito em Python/Flask.

# Acesso a Aplicação
IP: http://18.228.244.51/
DNS: http://strider.mbhosts.com/

## Especificação da API

#### GET /vegetation-cover
API para Dados da Imagem 'analytic.tif'

#### Response
* 200 - Sucesso
* 500 - Erro Interno