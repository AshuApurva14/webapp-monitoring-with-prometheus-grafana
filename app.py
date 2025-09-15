from flask import Flask, request, Response
from prometheus_client import counter, summary, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)


REQUEST_COUNT = Counter('app_requests_total', 'Total number of requests', ['methods', 'endpoint'])
EXCEPTIONS = Counter('app_exceptions_total', 'Total number of unhandeled exceptions.', ['endpoint', 'exception_type'])
PRINT_NUMBER = Summary('app_print_number', 'Summary of the print number passed')


@app.errorhandler(Exception)
def catch_all_exceptions(e):
    EXCEPTIONS.labels(endpoint=request.path, exception_type=type(e).__name__).inc()

@app.before_request
def request_counter():
    REQUEST_COUNT.labels(method=request.method, endpoint=request.path).inc()



@app.route('/health')
def home():
    return 'Hello, Flask!'

@app.route('/print_number')
def print_number():
    try:
        number = request.args.get('number', None) 
        if number is None:
            return "No number provided", 400

        number = float(number)
        PRINT_NUMBER.observe(number)


        return f'Number received: {number}', 200


@app.route('/crash')
def crash():
    raise KeyError("This is a crash!")  


@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
