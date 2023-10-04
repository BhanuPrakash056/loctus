from locust import FastHttpUser, constant, task
import logging


class MyRequest(FastHttpUser):
    host = 'http://localhost:8000'
    wait_time = constant(1)

    @task
    def getPlanets(self):
        self.client.get('/planets')
        logging.info("request is getting processed")


