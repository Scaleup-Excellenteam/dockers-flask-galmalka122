import requests


def send_file_and_check_response(file_name):
    url = "http://localhost:5000/"  # Replace with your endpoint URL

    # Set the file path of the file to be sent
    file_path = f"{file_name}"  # Replace with your file path

    # Send the file as a POST request
    with open(file_path, "rb") as file:
        response = requests.post(url, files={"file": file})

    # Check the response status code and content
    assert response.status_code == 200, f"Request failed with status code: {response.status_code}"

    json_data = response.json()
    assert "file_id" in json_data, "Response does not contain 'uuid' key."

    print("Send file passed!")
    send_uuid_and_check_response(json_data["file_id"])


def send_uuid_and_check_response(uuid):
    url = f"http://localhost:5000/?file_id={uuid}"  # Replace with your endpoint URL

    # Send the UUID as a GET request
    response = requests.get(url)
    # Check the response status code and content
    assert response.status_code == 200, f"Request failed with status code: {response.status_code}"
    json_data = response.json()
    assert json_data["output"] == "Hello World\n", "Response does not match expected content."

    print("Test passed!")


if __name__ == "__main__":

    for extension in ["java", "py", "dart"]:
        send_file_and_check_response(f"HelloWorld.{extension}")
