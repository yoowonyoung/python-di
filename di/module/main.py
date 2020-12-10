from di.module.containers import Application


def override_config_from_env(app):
    app.config.gateways.mysql.database.from_env(
        'DI_EXAMPLE_MYSQL_DATABASE',
        app.config.gateways.mysql.database()
    )

def main():
    app = Application()

    app.config.from_yaml('data/logger/config.yml')
    app.config.from_yaml('data/di/config.yml')
    override_config_from_env(app)
    # app.core.configure_logging()
    #app.core.bind_database(app.gateways.mysql().get_database_instance())
    #app.core.bind_odm_database(app.gateways.mongodb().get_database_instance())

    app.main()
