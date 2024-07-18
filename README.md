
# Apache Nifi 2.0 - Extensões em Python

<!--
# docker compose -p apache-nifi-2 -f docker-compose.yaml up -d
# docker compose -p apache-nifi-2 -f docker-compose.yaml restart
# sudo chmod -R 777 ./nifi
# https://localhost:8443/nifi/#/login
# https://github.com/joewitt/nifi-python-examples/blob/main/UpdateAttributeFileLookup.py
# https://github.com/apache/nifi-python-extensions/tree/main/src/extensions
# https://nifi.apache.org/documentation/nifi-2.0.0-M4/html/python-developer-guide.html

# sudo cp -r  ValidaLoteCpfCnpj/ /var/lib/docker/volumes/apache-nifi-2_nifi-python/_data

# Local onde são criados os ambientes virtuais dos novos processos

./work/python/extensions/descobreColunasArquivo/0.0.1-Python/
./work/python/extensions/descobreColunasArquivo2/0.0.2-Python

# Comando para ver os logs de criação dos processos Python

docker logs apache-nifi-2 | grep -Ei descobreColunasArquivo


-->

```bash
docker compose -p apache-nifi-2 -f docker-compose.yaml up -d
```
