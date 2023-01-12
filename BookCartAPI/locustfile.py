from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    "Content-Type": "application/json",
}

class TaskSet(SequentialTaskSet):

    @task
    def list_all_books(self):
        self.client.get(url=f"/Book", headers=HEADERS)

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]