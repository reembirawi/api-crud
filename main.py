import requests

class API:
    def __init__(self):
        self.link = "https://jsonplaceholder.typicode.com"

    def get_data(self, id: int):
        req = requests.get(f'{self.link}/posts/{id}')
        if req.status_code == 404:
            print(f"Post not found: {req.status_code}")
        elif req.status_code == 500:
            print(f"Internal server error: {req.status_code}")
        elif req.status_code == 200:
            print(f"Ok: {req.status_code}")
            print(req.text)
        else:
            print(f"Unexpected error: {req.status_code}")


    def create_data(self, title: str, body: str):
        data = {'title': title, 'body': body}
        req = requests.post(f'{self.link}/posts', data=data)
        print(f"Created: {req.status_code}")
        print(req.text)


    def update_data(self, id: int, data: dict):
        req = requests.put(f'{self.link}/posts/{id}', data=data)

        if req.status_code == 500:
            print(f"Internal server error: {req.status_code}")
        elif req.status_code == 200:
            print(f"Ok: {req.status_code}")
            print(req.text)
        else:
            print(f"Unexpected error: {req.status_code}")


    def delete_data(self, id: int):
        req = requests.delete(f'{self.link}/posts/{id}')
        print(f"Ok: {req.status_code}")

if  __name__ == "__main__":
    api = API()
    while True:
        try:
            event = int(input("""Choose an action:
            1: Create
            2: Delete
            3: Update
            4: Get
            5: Exit
    """))
        except ValueError:
            print("Please enter a number")
            continue

        match event:
            case 1:
                title = input("Enter title: ")
                body = input("Enter body: ")
                api.create_data(title, body)
            case 2:
                id = input("Enter id: ")
                api.delete_data(id)
            case 3:
                id = input("Enter id: ")
                title = input("Enter new title: ")
                body = input("Enter new body: ")
                data = {"title": title, "body": body}
                api.update_data(id, data)
            case 4:
                id = input("Enter id: ")
                api.get_data(id)
            case 5:
                break
            case _:
                print("wrong input...")