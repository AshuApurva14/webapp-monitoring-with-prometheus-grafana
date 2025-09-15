
# webapp-monitoring-with-prometheus-grafana

This project demonstrates how to set up and configure monitoring for a Python Flask web application using Prometheus and Grafana.

## Prerequisites

- Python 3.8+
- [pip](https://pip.pypa.io/en/stable/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

## Setup Instructions

1. **Clone the repository**
	```bash
	git clone <repo-url>
	cd webapp-monitoring-with-prometheus-grafana
	```

2. **Create and activate a virtual environment**
	```bash
	python3 -m venv venv
	source venv/bin/activate
	```

3. **Install dependencies**
	```bash
	pip install -r requirements.txt
	```

4. **Run the Flask app**
	```bash
	python app.py
	```
	The app will be available at [http://localhost:5000](http://localhost:5000)

## Prometheus Integration

The project includes `prometheus_client` for exposing metrics. You can add a `/metrics` endpoint in your Flask app to expose metrics for Prometheus scraping.

## Next Steps

- Integrate Prometheus metrics endpoint in Flask app
- Set up Prometheus and Grafana for monitoring and visualization

---
Feel free to extend this project with more endpoints and monitoring features!
