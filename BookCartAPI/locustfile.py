from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    "Content-Type": "application/json",
}
BOOK_ID = '32'
USER_NAME = 'ralutest'
USER_ID = '1920'

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

    @task
    def check_username_availability(self):
        self.client.get(url=f"/User/validateUserName/{USER_NAME}", headers=HEADERS)

    @task
    def read_count_of_items(self):
        self.client.get(url=f"/User/{USER_ID}", headers=HEADERS)

    @task
    def list_items_user_wishlist(self):
        self.client.get(url=f"/Wishlist/{USER_ID}", headers=HEADERS)

    @task
    def list_items_user_shopping_cart(self):
        self.client.get(url=f"/ShoppingCart/{USER_ID}", headers=HEADERS)

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]