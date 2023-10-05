from locust import HttpUser, task, between
class MyUser(HttpUser):
    host = "https://example.com"
    wait_time = between(1, 5)
    def on_start(self):
        # Login to the website
        self.client.post("/login", {"username": "user", "password": "password"})
    @task
    def index(self):
        # Access the home page
        self.client.get("/")
    @task
    def about(self):
        # Access the about page
        self.client.get("/about")
    @task
    def signout(self):
        # Sign out of the website
        self.client.get("/signout")