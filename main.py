import uvicorn

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"


SETTINGS = {
    'host': "0.0.0.0",
    'port': 8081,
    'reload': True,
    'use_colors': True,
    'log_level': "info",
    'access_log': True,
    'log_config': log_config
}

if __name__ == "__main__":
    print('Server Running at: http://localhost:8081/')
    uvicorn.run("app.api:app", **SETTINGS)
