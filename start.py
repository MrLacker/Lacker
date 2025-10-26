import os
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Мой Minecraft сервер работает! Подключайся!"

if __name__ == "__main__":
    # Запускаем Minecraft сервер
    print("Запускаю Minecraft сервер...")
    subprocess.Popen(["java", "-Xmx512M", "-jar", "server.jar", "nogui"])
    
    # Запускаем веб-сервер для Railway
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
