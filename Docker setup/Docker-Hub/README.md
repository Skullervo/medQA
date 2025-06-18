```bash
# 🐳 OHJE: Docker-imagen lisääminen Docker Hubiin

# 1. Kirjaudu sisään Docker Hubiin (https://hub.docker.com)
docker login

# 2. Nimeä olemassa oleva paikallinen Docker-image uudelleen Docker Hub -muotoon:
# YLEINEN MUOTO:
# docker tag <paikallinen-imagen-nimi> <dockerhub-käyttäjänimi>/<haluttu-imagen-nimi>:<versio>

# ESIMERKKI:
docker tag my-local-image myusername/my-image:latest

# 3. Lähetä (pushaa) image Docker Hub -tilillesi:
# YLEINEN MUOTO:
# docker push <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>

# ESIMERKKI:
docker push myusername/my-image:latest

# 4. Tarkista selaimessa että image on ilmestynyt tilillesi:
# https://hub.docker.com/repositories

# 📥 Jos haluat ladata imagen toiselle koneelle:
# YLEINEN MUOTO:
# docker pull <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>

# ESIMERKKI:
docker pull myusername/my-image:latest

# 🏁 Voit ajaa imagen suoraan näin:
# YLEINEN MUOTO:
# docker run -d --name <kontin-nimi> -p <host-portti>:<kontti-portti> <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>

# ESIMERKKI:
docker run -d --name my-container -p 8080:80 myusername/my-image:latest
```
