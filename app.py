from locust import User, task, constant


class MyFirstTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("Launching the url")

    @task
    def searching(self):
        print("Searching the url")


class MySecondTest(User):
    weight = 2
    wait_time = constant(1)

    @task
    def launch2(self):
        print("Launching the 2 class in mysecondtest")

    @task
    def searching2(self):
        print("Searching in the 2 class of the url")
