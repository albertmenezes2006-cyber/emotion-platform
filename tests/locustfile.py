"""Locust — locust -f tests/locustfile.py --host=https://emotion-platform-albert.onrender.com --users=100 --spawn-rate=10 --headless --run-time=60s"""
from locust import HttpUser, task, between
import random

class Usuario(HttpUser):
    wait_time = between(1, 3)
    @task(4)
    def home(self): self.client.get("/")
    @task(3)
    def avaliacao(self): self.client.get("/app/avaliacao")
    @task(3)
    def chat_api(self):
        msgs = ["Ola","Estou ansioso","Me ajuda","Respiracao","TCC"]
        self.client.post(f"/api/v1/chat-ia/mensagem?user_id=locust_{random.randint(1,9999)}&mensagem={random.choice(msgs)}", json={})
    @task(2)
    def phq9(self): self.client.get("/api/v1/phq9-clinico/perguntas")
    @task(1)
    def health(self): self.client.get("/health")
