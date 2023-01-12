from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    "Content-Type": "application/json",
}
BOOK_ID = '32'

class TaskSet(SequentialTaskSet):

    @task
    def list_all_books(self):
        self.client.get(url="/Book", headers=HEADERS)

    @task
    def read_one_book(self):
        self.client.get(url=f"/Book/{BOOK_ID}", headers=HEADERS)

    @task
    def list_all_categories(self):
        self.client.get(url="/Book/GetCategoriesList", headers=HEADERS)

    @task
    def list_5_similar_books(self):
        self.client.get(url=f"/Book/GetSimilarBooks/{BOOK_ID}", headers=HEADERS)

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]