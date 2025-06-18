
# 🐳 OHJE: Docker-imagen lisääminen Docker Hubiin

# 1. Kirjaudu sisään Docker Hubiin (https://hub.docker.com)
```PowerShell
docker login
```

# 2. Nimeä olemassa oleva paikallinen Docker-image uudelleen Docker Hub -muotoon:
```PowerShell
docker tag <paikallinen-imagen-nimi> <dockerhub-käyttäjänimi>/<haluttu-imagen-nimi>:<versio>
```

# ESIMERKKI:
```PowerShell
docker tag my-local-image myusername/my-image:latest
```

# 3. Lähetä (pushaa) image Docker Hub -tilillesi:
```PowerShell
# docker push <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>
```

# ESIMERKKI:
```PowerShell
docker push myusername/my-image:latest
````

# 4. Tarkista selaimessa että image on ilmestynyt tilillesi:
# https://hub.docker.com/repositories

# 📥 Jos haluat ladata imagen toiselle koneelle:

```PowerShell
# docker pull <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>
```

# ESIMERKKI:
```PowerShell
docker pull myusername/my-image:latest
```

# 🏁 Voit ajaa imagen suoraan näin:

```PowerShell
# docker run -d --name <kontin-nimi> -p <host-portti>:<kontti-portti> <dockerhub-käyttäjänimi>/<imagen-nimi>:<versio>
```

# ESIMERKKI:
```PowerShell
docker run -d --name my-container -p 8080:80 myusername/my-image:latest
```
