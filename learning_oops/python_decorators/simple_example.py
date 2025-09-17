import json
from pathlib import Path

EMAIL_FILE_NAME = "email.jsonl"


class Person:
    def __init__(self, f_name: str, l_name: str) -> None:
        self.f_name = f_name
        self.l_name = l_name

    @property
    def full_name(self) -> str:
        return f"{self.f_name} {self.l_name}"

    @property
    def email_address(self) -> str:
        return f"{self.f_name}.{self.l_name}@gmail.com"

    @staticmethod
    def delete_email_file(cls, file_name: str) -> None:
        file_path = Path(file_name)
        file_path.unlink()

    @staticmethod
    def if_email_exists(email_address: str, file_name: str) -> bool:
        print(f"Checking if {file_name} exists in {email_address}")
        try:
            with open(
                Path(__file__).parent.parent.joinpath("data", file_name), "r"
            ) as f:
                for line in f:
                    data = json.loads(line)
                    if data.get("email_address") == email_address:
                        return True
        except FileNotFoundError:
            print(f"File {file_name} not found")
            return False

    @staticmethod
    def email_file_exists(file_name: str) -> bool:
        files = Path(__file__).parent.parent.joinpath("data").iterdir()
        for file in files:
            if file.name == file_name:
                return True
        return False

    def write_to_file(self, file_name: str, data: dict) -> None:
        with open(Path(__file__).parent.parent.joinpath("data", file_name), "a+") as f:
            f.write(json.dumps(data))
            f.write("\n")

    def save_email(self, file_name: str) -> None:
        if not self.email_file_exists(file_name):
            details = {"email_address": self.email_address}
            self.write_to_file(file_name, details)
            return

        if self.if_email_exists(email_address=self.email_address, file_name=file_name):
            print(f"Email {self.email_address} already exists")
            raise ValueError("Email address already exists")
        else:
            details = {"email_address": self.email_address}

        self.write_to_file(file_name, details)

    @staticmethod
    def list_emails(file_name: str) -> list:
        if not Path(__file__).parent.parent.joinpath("data").exists():
            raise ValueError("File not found")

        with open(
            Path(__file__).parent.parent.joinpath("data", file_name), "r"
        ) as file:
            for line in file:
                print(type(line))
                data = json.loads(line)
                print(type(data))
                yield data["email_address"]

        ###########load vs loads ## below is something extra
        with (
            Path(__file__).parent.parent.joinpath("data", "email.json").open("r")
        ) as file:
            data = json.load(file)
            print(data)
            print(type(data))

            for line in data:
                print(type(line))
                print(line)


if __name__ == "__main__":
    # person = Person(f_name='kidki', l_name='kumar')
    # person.save_email(file_name=EMAIL_FILE_NAME)

    emails = Person.list_emails(file_name=EMAIL_FILE_NAME)
    print("_________")
    for email in emails:
        print(email)
