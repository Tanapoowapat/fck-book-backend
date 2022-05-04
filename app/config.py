postgresql = {
    "USER": "FlaskPython",
    "PASSWORD": "xH616H6aeB4wpmzm",
    "PUBLIC_IP_ADDRESS": "34.142.255.3",
    "PORT": "5432",
    "DBNAME": "cloud",
    "PROJECT_ID": "woven-solution-347820",
    "INSTANCE_NAME": "cloud-project",
}

# ON client
postgresqlConfig = "postgresql+pg8000://{}:{}@{}:{}/{}".format(
    postgresql["USER"],
    postgresql["PASSWORD"],
    postgresql["PUBLIC_IP_ADDRESS"],
    postgresql["PORT"],
    postgresql["DBNAME"],
)
