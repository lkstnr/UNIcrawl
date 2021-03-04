# UNIcrawl

Performantes Crawling-System für Webauftritte von Hochschulen.

## Installation

### Docker installieren

Es müssen sowohl [Docker Engine](https://docs.docker.com/engine/install/) als auch [Docker Compose](https://docs.docker.com/compose/install/) installiert werden. **Docker Desktop (macOS, Windows)** umfasst beide Pakete.

Alternativ (macOS): [Docker über Homebrew installieren](https://www.robinwieruch.de/docker-macos)

### Projekt klonen

```bash
git clone https://github.com/lkstnr/UNIcrawl.git
cd UNIcrawl/
```

## Nutzung

### Starten der Docker-Container

```bash
# Falls die docker-machine nicht läuft:
# docker-machine start default
# eval $(docker-machine env default)

docker-compose up -d
```

Beim ersten Start kann das etwas Zeit in Anspruch nehmen, da Docker-Images heruntergeladen werden und auch das unicrawl-Image gebaut wird.

(Bei Änderungen am `Dockerfile` (unicrawl-Image) sicherstellen, dass `docker-compose` diese Änderungen übernimmt `docker-compose up -d --build`)

Folgende Ausgabe bestätigt das erfolgreiche Starten der Docker-Container:

```
# Starting unicrawl_adminer_1 ... done
# Starting unicrawl_db_1      ... done
# Starting unicrawl           ... done
```

### Öffnen einer Bash-Shell im Docker-Container

```bash
docker-compose exec unicrawl bash

# nun seid ihr in der Bash-Shell
root@<...>:/code#

# zum Verlassen der Bash-Shell
root@<...>:/code# exit
```

### Deployen eines Crawlers

Innerhalb der **Bash-Shell** `root@<...>:/code#` folgendes ausführen:

```bash
# unicrawl-Projekt zu Scrapyd hinzufügen
scrapyd-client deploy

# Spider (Crawler) deployen
# Monitoring über http://localhost:6800
# Default-Konfiguration des Crawlers stoppt nach ~100 gecrawlten Websites
# scrapyd-client schedule -p <project-name> <spider-name>
scrapyd-client schedule -p unicrawl unicrawl_basic
```

### Stoppen der Docker-Container

```bash
docker-compose stop

# Falls auch die docker-machine beenden werden soll:
# docker-machine stop default
```

Folgende Ausgabe bestätigt das erfolgreiche Stoppen der Docker-Container:

```
# Stopping unicrawl_adminer_1 ... done
# Stopping unicrawl_db_1      ... done
# Stopping unicrawl           ... done
```

## Dienste

Nach dem **Starten der Docker-Container** sollten folgende Dienste laufen:

- **MySQL-Server** mit Benutzer **unicrawl**, Passwort **scrapy2mysql**, Datenbank **unicrawl**
- **Adminer** zur Verwaltung der Datenbank, erreichbar unter `http://localhost:8080`
- **Scrapyd**, zum Monitoring laufender Spider (Crawler), erreichbar unter `http://localhost:6800`

Eventuell müssen Anpassungen vorgenommen werden, damit die Dienste unter [localhost erreichbar sind](https://www.jhipster.tech/tips/020_tip_using_docker_containers_as_localhost_on_mac_and_windows.html).

## Hilfreiche Befehle

```bash
# Entfernt ungenutzte Daten
docker system prune

# Zeigt laufende Container + Infos (Container-ID, Status, ...)
docker ps

# Laufende Container stoppen
docker stop <container-name>
docker stop <container-id>

# oder
# docker kill <container-name>
# docker kill <container-id>

# Zeigt installierte Images + Infos (Image-ID, ...)
docker images

# Entfernt Images
docker rmi <image-id>
```
