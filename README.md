# PrometheusWorkshop

Um Prometheus und die benötigten Tools im Workshop aufzusetzen verwenden wir Docker.

Docker kann mit folgenden Anleitungen installiert werden.

Mac:

Bitte auf die Version des Prozessors (Intel / Apple Silicon) achten!
https://docs.docker.com/desktop/install/mac-install/


Windows:

Bitte beachtet, dass die Installation von Docker abhängig von der Windows Version (Home / Pro) ist!
https://docs.docker.com/desktop/install/windows-install/
 

Linux:

https://docs.docker.com/desktop/install/linux-install/

---

Nachdem Docker installiert wurde, muss abhängig von der Prozessorarchitektur in den entsprechenden Ordner [arm64](./arm64) oder [amd64](./amd64) gewechselt werden.

Die Bereitstellung erfolgt mit folgendem Kommando:

```
docker-compose up -d
```

Die Dienste sind unter folgenden URLs erreichbar:

Dienst | URL | Passwort
-------- | -------- | --------
Prometheus   | localhost:9090   | 
Cadvisor   | localhost:8080   | 
Node-Exporter   | localhost:9100   | 
Visual Studio Code   | localhost:5000   | prometheusWorkshop
Grafana   | localhost:3000   | prometheusWorkshop

---

Im Ordner [examples](./examples) befinden sich die Übungen aus dem Workshop und die Lösungen.
