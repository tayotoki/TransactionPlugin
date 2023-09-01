from datetime import datetime

from transactionsinfo.dto import Operation
from utils.json_handler import JSONHandler

json_reader = JSONHandler()
datas = json_reader.get_data()


def main():
    operations = []

    for data in datas:

        operation = Operation()
        operation.id = data.get("id")
        operation.state = data.get("state")
        operation.date = data.get("date")
        operation.amount = data.get("amount")
        operation.currency_name = data.get("name")
        operation.currency_code = data.get("code")
        operation.description = data.get("description")
        operation.from_ = data.get("from")
        operation.to = data.get("to")

        if operation.state == "EXECUTED":
            operations.append(operation)

    print(
        *sorted(
            operations,
            key=lambda operation_: datetime.strptime(operation_.date, "%d.%m.%Y"),
            reverse=True
        )[:5],
        sep="\n"
    )


if __name__ == "__main__":
    main()
