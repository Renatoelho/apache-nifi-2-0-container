# Apache NiFi 2: Desenvolva Processadores Personalizados com Python


A utilização do ***Python*** no ***Apache NiFi 2*** permite que você crie processadores ***personalizados*** para manipular, transformar e analisar dados de forma específica. Isso significa que, além dos processadores padrão que vêm com o NiFi, você pode escrever ***seu próprio código*** Python para realizar tarefas que atendam às suas necessidades específicas de ***processamento de dados***, como filtragem, agregação, enriquecimento ou formatação de dados. Com Python, você ganha ***flexibilidade*** e poder adicional para personalizar como os dados são tratados e processados dentro do seu fluxo, aproveitando a ***simplicidade*** e a vasta gama de bibliotecas disponíveis na ***linguagem***.


<!--
https://www.youtube.com/@renato-coelho
-->

# Apresentação em vídeo

<p align="center">
  <a href="https://www.youtube.com/@renato-coelho" target="_blank"><img src="thumbnail/Apache-Nifi-Python.png" alt="Vídeo de apresentação"></a>
</p>


### Requisitos

+ ![Git](https://img.shields.io/badge/Git-2.25.1%2B-E3E3E3)

+ ![Python](https://img.shields.io/badge/Python-3.9%2B-E3E3E3)

+ ![Docker](https://img.shields.io/badge/Docker-23.0.3-E3E3E3)

+ ![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E3E3E3)

+ ![Docker-compose](https://img.shields.io/badge/Docker--compose-1.25.0-E3E3E3)


## Deploy da aplicação


### Clonando o repositório

```bash
git clone https://github.com/Renatoelho/apache-nifi-2-0-container.git apache-nifi-2-0-container
```


### Preparando o ambiente

+ Acessando o diretório clonado
```bash
cd apache-nifi-2-0-container/
```

+ Ativando o Apache Nifi
```bash
docker compose -p apache-nifi-2 -f docker-compose.yaml up -d
```

> Para desativar o serviço Docker compose, substitua ```up -d``` por ```down``` ou ```restart``` para reiniciar o servidor.

Para acessar o Apache NiFi depois que o serviço estiver ativo, vá para: [https://localhost:8443/nifi/#/login](https://localhost:8443/nifi/#/login). As credenciais de acesso são os valores das variáveis ```SINGLE_USER_CREDENTIALS_USERNAME``` e ```SINGLE_USER_CREDENTIALS_PASSWORD``` existentes em [docker-compose.yaml](docker-compose.yaml).

+ Deploy do processador

Estamos utilizando o gerenciador de volumes do próprio Docker, por isso temos que enviar os arquivos para este diretório específico.

```bash
sudo cp -r  ValidaLoteCpfCnpj/ /var/lib/docker/volumes/apache-nifi-2_nifi-python/_data
```

+ Acompanhar o deploy do novo processador

Se quiser acompanhar o deploy do novo processo em Python, que é executado logo após a disponibilização do código, utilize o seguinte comando no Docker:

```bash
docker logs -f apache-nifi-2
```

Ou

```bash
docker logs -f apache-nifi-2 | grep -Ei ValidaLoteCpfCnpj
```

# Referências

Apache NiFi Overview **NiFi Documentation.** Disponível em: <https://nifi.apache.org/documentation/v2/>. Acesso em: 14 jul. 2024.

NiFi Python Developer’s Guide, **nifi.apache.org.** Disponível em: <https://nifi.apache.org/documentation/nifi-2.0.0-M4/html/python-developer-guide.html>. Acesso em: 15 jul. 2024.

nifi-python-extensions, **github.com.** Disponível em: <https://github.com/apache/nifi-python-extensions/tree/main/src/extensions>. Acesso em: 15 jul. 2024.
