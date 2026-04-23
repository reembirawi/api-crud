import requests

class API:
    def __init__(self):
        self.link = "https://jsonplaceholder.typicode.com"

    def get_data(self, post_id: int):
        res = requests.get(f'{self.link}/posts/{post_id}')
        if res.status_code == 404:
            print(f"Post not found: {res.status_code}")
        elif res.status_code == 500:
            print(f"Internal server error: {res.status_code}")
        elif res.status_code == 200:
            print(f"Ok: {res.status_code}")
            print(res.text)
        else:
            print(f"Unexpected error: {res.status_code}")


    def create_data(self, title: str, body: str):
        data = {'title': title, 'body': body}
        req = requests.post(f'{self.link}/posts', data=data)
        print(f"Created: {req.status_code}")
        print(req.text)


    def update_data(self, post_id: int, data: dict):
        res = requests.put(f'{self.link}/posts/{post_id}', data=data)

        if res.status_code == 500:
            print(f"Internal server error: {res.status_code}")
        elif res.status_code == 200:
            print(f"Ok: {res.status_code}")
            print(res.text)
        else:
            print(f"Unexpected error: {res.status_code}")


    def delete_data(self, post_id: int):
        res = requests.delete(f'{self.link}/posts/{post_id}')
        print(f"Ok: {res.status_code}")

def get_int(statement):
    while True:
        try:
            return int(input(statement))
        except ValueError:
            print("Please enter a number")

if  __name__ == "__main__":
    api = API()
    while True:
        event = get_int("""Choose an action:
        1: Create
        2: Delete
        3: Update
        4: Get
        5: Exit
""")

        match event:
            case 1:
                title = input("Enter title: ")
                body = input("Enter body: ")
                api.create_data(title, body)
            case 2:
                post_id = get_int("Enter id: ")
                api.delete_data(post_id)
            case 3:
                post_id = get_int("Enter id: ")
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                data = {"title": title, "body": body}
                api.update_data(post_id, data)
            case 4:
                post_id = get_int("Enter id: ")
                api.get_data(post_id)
            case 5:
                break
            case _:
                print("wrong input...")