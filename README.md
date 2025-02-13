# ATM System - Simple REST API

This is a simple ATM system with a REST API built using Flask.  
The system allows you to:
- Get account balance
- Withdraw money
- Deposit money

## Deployment
The project was deployed and tested on **AWS EC2 (Ubuntu)** instance with:
- Python 3.12
- Flask
- Security Group configuration to allow port 5000 for API access.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   ```
2. Create virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install flask
   ```

## Run the Application
```bash
python3 app.py
```

## API Endpoints
### 1. Get Balance (GET):
```
GET /accounts/<account_number>/balance
```
Example:
```
GET http://127.0.0.1:5000/accounts/873214/balance
```

### 2. Withdraw (POST):
```
POST /accounts/<account_number>/withdraw
{
  "amount": 200
}
```

### 3. Deposit (POST):
```
POST /accounts/<account_number>/deposit
{
  "amount": 500
}
```

## AWS EC2 Deployment Steps (Linux):
1. Launch an EC2 Ubuntu Instance.
2. SSH into the instance:
   ```bash
   ssh -i "my-key.pem" ubuntu@<YOUR_PUBLIC_IP>
   ```
3. Install Python and Flask:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip python3-venv
   ```
4. Clone this repo and install Flask.
5. Run the server:
   ```bash
   python3 app.py
   ```

## Testing the API from EC2
### Using `curl` from the server itself:
```bash
curl -X POST http://127.0.0.1:5000/accounts/873214/withdraw \
-H "Content-Type: application/json" \
-d '{"amount": 200}'
```

## Key Learnings:
- Deployment to AWS EC2.
- Security Groups configuration.
- Flask API development.
- Using `curl` for testing API from a remote server.

## Design Desicions:
- I chose to use **Flask** because it is lightweight, quick to set up, and well-suited for small REST API projects.
- Account data is stored **in-memory (dictionary)** because this is a practice project, and it was the simplest solution without requiring a database setup.
- I deployed the project to **AWS EC2** because it gave me full control over the environment, it allowed me to gain experience working with a Linux server in the cloud, and it is common in the industry. 

## Challenges Faced:
- This was my first time working with **Flask**, so I had to learn its basics, including routing, handling JSON requests, and running a local development server.
- **I had no prior experience working with AWS cloud services**, so setting up an EC2 instance, configuring Security Groups, and deploying my API to a public server was a completely new process for me.
- **While working with POST requests, I had to learn how to test and interact with REST APIs**. Initially, I used **Postman**, which helped me understand how HTTP requests work. Later, when working directly on the EC2 server, I learned to use **curl** to send POST requests from the terminal, including sending JSON payloads.
- I had to learn new Linux commands in order to set up the development environment on an Ubuntu server.
- I also had to learn how to create and activate a virtual environment **(venv)**, which allowed me to install Flask and other Python packages in an isolated workspace.