from locust import TaskSet, constant, task, HttpUser


class MyHttpCat(TaskSet):
    @task
    def get_status(self):
        self.client.get('/200')
        print("Get The task in cat")
        self.interrupt()
    # adding a class side a class
    class MyOtherTask(TaskSet):
        @task
        def get_500_start(self):
            self.client.get('/500')
            print("Get The task in nest cat")
            # to stop the execution
            self.interrupt()
class MyLoadTest(HttpUser):
    host = "https://http.cat/"
    tasks = [MyHttpCat]
    wait_time = constant(1)
