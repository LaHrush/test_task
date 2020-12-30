--------
Description:
	test task

Install required packages:
- source venv/bin/activate
- pip install -r requirements.txt
- python -m pytest tests.py>tests.log && python ssh_connect.py


Note:
    You should be added REMOTE_HOST, SERVER_USER, SERVER_SECRET to your environment variables