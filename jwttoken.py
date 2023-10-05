from locust import HttpUser, task, between
class MyUser(HttpUser):
    host = "http://localhost:3000/"
    @task
    def index(self):
        self.client.get("/", headers={"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImJoYW51IHByYWthc2ggciIsImFnZSI6MjEsImlhdCI6MTUxNjIzOTAyMn0._wbx2E1k85-hDh6Wq_41j510_JfBQQmXG4_CbOHpA_M"})
    @task
    def profile(self):
        self.client.get("/profile", headers={"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImJoYW51IHByYWthc2ggciIsImFnZSI6MjEsImlhdCI6MTUxNjIzOTAyMn0._wbx2E1k85-hDh6Wq_41j510_JfBQQmXG4_CbOHpA_M"})
    @task
    def logout(self):
        self.client.post("/logout", headers={"Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6ImJoYW51IHByYWthc2ggciIsImFnZSI6MjEsImlhdCI6MTUxNjIzOTAyMn0._wbx2E1k85-hDh6Wq_41j510_JfBQQmXG4_CbOHpA_M"})
    wait_time = between(1, 5)