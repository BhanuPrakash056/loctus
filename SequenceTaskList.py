from locust import SequentialTaskSet, HttpUser, task, constant


class MySeqTask(SequentialTaskSet):
    @task
    def get_status_200(self):
        self.client.get("/200")
        print("status of 200")

    @task
    def get_status_400(self):
        self.client.get("/400")
        print("status of 400")

    @task
    def get_status_500(self):
        self.client.get("/500")
        print("status of 500")

class MyLoadTest(HttpUser):
    host = "https://http.cat/"
    tasks = [MySeqTask]
    wait_time = constant(1)