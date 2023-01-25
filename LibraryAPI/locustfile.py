from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    "Content-Type": "application/json",
}
BOOK_ID_FICTION = 'qpBhlLWbJmqgg'
SEARCH_KEY = 'borges'
GENRE = 'fiction'

class TaskSet(SequentialTaskSet):

    @task
    def list_all_books(self):
        self.client.get(url="/books", headers=HEADERS)

    @task
    def filter_books_with_search_parameter(self):
        self.client.get(url=f"/books?search={SEARCH_KEY}", headers=HEADERS)

    @task
    def filter_books_with_checkedOut_parameter(self):
        self.client.get(url=f"/books?checkedOut=false", headers=HEADERS)

    @task
    def filter_books_with_genre_parameter(self):
        self.client.get(url=f"/books?genre={GENRE}", headers=HEADERS)

    @task
    def read_one_book(self):
        self.client.get(url=f"/books/{BOOK_ID_FICTION}", headers=HEADERS)

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]