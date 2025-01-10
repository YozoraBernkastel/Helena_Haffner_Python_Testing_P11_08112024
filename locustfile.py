from locust import HttpUser, task, between

class LocustBenchmark(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")

    @task
    def show_summary(self):
        self.client.post("/showSummary", {"email": "kate@shelifts.co.uk"})

    @task
    def book(self):
        self.client.get("/book/Spring Festival/She Lifts")

    @task
    def points_table(self):
        self.client.get("/points_table")

    @task
    def purchase(self):
        self.client.post('/purchasePlaces', {"club": "She Lifts", "competition": "Spring Festival", "places": 0})

    @task
    def logout(self):
        self.client.get("/logout")