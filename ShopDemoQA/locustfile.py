from locust import HttpUser, SequentialTaskSet, task

HEADERS = {
    'accept': 'application/json, text/plain, */*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9,ro;q=0.8'
}

class ShopDemoUITaskSet(SequentialTaskSet):

    @task
    def get_homepage_page(self):
        self.client.get(url = '', headers = HEADERS)

    @task
    def get_wishlist_page(self):
        self.client.get(url = f'/wishlist', headers = HEADERS)

    @task
    def get_cart_page(self):
        self.client.get(url = f'/cart', headers = HEADERS)

    @task
    def get_shop_page(self):
        self.client.get(url = f'/shop', headers = HEADERS)

    @task
    def get_category_dress_page(self):
        self.client.get(url = f'/product-category/dress', headers = HEADERS)

    @task
    def get_category_clothing_page(self):
        self.client.get(url = f'/product-category/clothing', headers = HEADERS)

    @task
    def get_product_jacket_page(self):
        self.client.get(url = f'/product/black-ultimate-boxy-faux-leather-biker-jacket', headers = HEADERS)

    @task
    def get_blog_page(self):
        self.client.get(url = f'/blog', headers = HEADERS)

    @task
    def get_blog_tag_bedroom_page(self):
        self.client.get(url = f'/tag/bedroom', headers = HEADERS)

    @task
    def get_blog_category_furniture_tips_page(self):
        self.client.get(url = f'/category/furniture-tips', headers = HEADERS)

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """
    tasks = [ShopDemoUITaskSet]
    host = "https://shop.demoqa.com"