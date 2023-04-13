# python-sdk
Python SDK for GetTestMail



```python
from gettestmail.client import GetTestMailClient


def main():
  client = GetTestMailClient("your-api-key")
  test_mail = client.create_new()
  print(test_mail.emailAddress)

  test_mail = client.wait_for_message(test_mail.emailAddress)
  print(test_mail.message)


main()
```