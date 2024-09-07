import docker

TEST_SUCCESS_STR = "test_input_format.py ......                                              [100%]"

client = docker.from_env()
client.images.build(path=".", tag="my-cicd")

print(client.images.list())

test_result = client.containers.run("my-cicd").decode('utf-8', errors='ignore')

if TEST_SUCCESS_STR in test_result:
    print("OK")
else:
    print("FAIL")