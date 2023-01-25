from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    "Content-Type": "application/json",
}
BOOK_ID_FICTION = 'qpBhlLWbJmqgg'
SEARCH_KEY = 'borges'
GENRE = 'fiction'
SEARCH_KEY_MATCH = 'The Dispossessed'

ADD_BOOK_TITLE = 'The Dispossessed: An Ambiguous Utopia'
ADD_BOOK_AUTHOR = 'Ursula K. Le Guin'

ADD_BOOK_BODY = {
    "title": f"{ADD_BOOK_TITLE}",
    "author": f"{ADD_BOOK_AUTHOR}",
    "genre": f"{GENRE}",
    "yearPublished": 1994
}

UPDATE_BOOK_BODY = {
    "checkedOut": True
}

def assert_contains(response,text):
    with response as r:
        if text not in r.text:
            r.failure("Expected "+ response.text + " to contain "+ text)
        return r

class TaskSet(SequentialTaskSet):

    book_id_created_list = []

    @task
    def list_all_books(self):
        self.client.get(url = "/books", headers = HEADERS)

    @task
    def filter_books_with_search_parameter(self):
        self.client.get(url = f"/books?search={SEARCH_KEY}", headers = HEADERS)

    @task
    def filter_books_with_checkedOut_parameter(self):
        self.client.get(url = f"/books?checkedOut=false", headers = HEADERS)

    @task
    def filter_books_with_genre_parameter(self):
        self.client.get(url = f"/books?genre={GENRE}", headers = HEADERS)

    @task
    def read_one_book(self):
        self.client.get(url = f"/books/{BOOK_ID_FICTION}", headers = HEADERS)

    @task
    def add_one_book(self):
        self.client.post(url = "/books",
                        json = ADD_BOOK_BODY, 
                        headers = HEADERS)

    @task
    def filter_books_matching(self):

        resp = assert_contains(self.client.get(url = f"/books?search={SEARCH_KEY_MATCH}", 
                            catch_response = True,
                            json = {"flag":'true'}),
                        ADD_BOOK_TITLE)
        json_response_dict = resp.json()
        new_book_id = json_response_dict[0]['id']
        self.book_id_created_list.append(new_book_id)

    @task
    def read_one_book_created(self):
        self.client.get(url = f"/books/{self.book_id_created_list[0]}", 
                        headers = HEADERS)

    @task
    def update_one_book_created(self):
        self.client.patch(url = f"/books/{self.book_id_created_list[0]}",
                        json = UPDATE_BOOK_BODY,
                        headers = HEADERS)
        
class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]