def db_write(name, age):
    """
    Receives and insert data

    :param name: The name inside the body request
    :param age: The age inside the body request
    """

    print(
        "Data saved\n"
        f"-- Name: {name}\n"
        f"-- Age: {age}"
    )
