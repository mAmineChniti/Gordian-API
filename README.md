
# Gordian API Documentation

Welcome to the documentation for Gordian – a basic API designed to handle user registration and login seamlessly.

## Getting Started

To start using Gordian and access its documentation, please visit the [Gordian website](https://gordian.onrender.com).

## Technologies Used

Gordian API is built using the following technologies:

- Python
- FastAPI
- MongoDB
- [Render](https://render.com/)

## Running Gordian API Locally for Development

Follow these steps to run Gordian API on your local machine:

### 1. Clone the Project

```shell
git clone https://github.com/mAmineChniti/Gordian-API.git
cd Gordian-API
```

### 2. Configure Environment Variables

#### MongoDB

Set up these environment variables in your local environment:

| Variable   | Description             |
|------------|-------------------------|
| USER       | MongoDB Username        |
| PASS       | MongoDB Password        |
| BASE       | MongoDB Database Name   |
| COLLECTION | MongoDB Collection Name |
| HOST       | MongoDB Host            |

You can adjust the configuration by modifying the code in `config/database.py` to match your environment.

### 3. Install Dependencies

Run the following command in your terminal to set up the project environment and install necessary dependencies:

```shell
make
```

The provided `Makefile` automates the setup process, creating a virtual environment, activating it, upgrading `pip`, and installing project dependencies from `requirements.txt`.

### 4. Deploy the API

To deploy the API locally, use the following command:

```shell
uvicorn Gordian:app --host 0.0.0.0 --port $PORT --reload
```

### 5. Access the API

Once the API is running locally, you can access it through your web browser at:

- <http://localhost:PORT>

Make sure to replace `PORT` with the actual port number you've specified.

Feel free to adapt and customize the provided instructions according to your preferences. If you have any questions or encounter issues, please refer to the [Gordian documentation](https://gordian.onrender.com) or reach out for assistance [Email Me](mailto:emin.chniti@esprit.tn).
