# initialize using environment variables
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask
app = Flask(__name__)

# or configure to use ELASTIC_APM in your application's settings
from elasticapm.contrib.flask import ElasticAPM
app.config['ELASTIC_APM'] = {
# Set the required service name. Allowed characters:
# a-z, A-Z, 0-9, -, _, and space
'SERVICE_NAME': 'test-app-pm',

# Use if APM Server requires a secret token
'SECRET_TOKEN': '',

# Set the custom APM Server URL (default: http://localhost:8200)
'SERVER_URL': 'http://192.168.25.110:8200',

# Set the service environment
'ENVIRONMENT': 'production',
}

apm = ElasticAPM(app)
