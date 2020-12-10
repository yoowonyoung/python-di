import logging.config
from argparse import ArgumentParser

from dependency_injector import containers, providers
from dependency_injector.providers import Factory

from di.module.cli.command import CommandProccessor
from di.module.cli.time import TimeCommand
from di.module.gateways.mongodb import MongoDBClient
from di.module.gateways.mysql import MysqlClient
from di.module.models.odm import initialize_odm
from di.module.models.orm import initialize_orm
from di.module.services.time import TimeService
from di.module.services.time.logic import Logic


class Core(containers.DeclarativeContainer):
    """IoC container of core component providers"""
    config = providers.Configuration()

    configure_logging = providers.Callable(
        logging.config.dictConfig,
        config=config.logging,
    )

    bind_database = providers.Callable(
        initialize_orm
    )
    bind_odm_database = providers.Callable(
        initialize_odm
    )


class Gateways(containers.DeclarativeContainer):
    """Ioc container of gateway (API clients to remote services) providers"""
    config = providers.Configuration()

    # If you want use, please unblock here
    # mysql = providers.Singleton(
    #     MysqlClient,
    #     database=config.mysql.database,
    #     host=config.mysql.host,
    #     port=config.mysql.port,
    #     username=config.mysql.username,
    #     password=config.mysql.password,
    # )
    #
    # mongodb = providers.Singleton(
    #     MongoDBClient,
    #     database=config.mongodb.database,
    #     host=config.mongodb.host,
    #     port=config.mongodb.port,
    #     username=config.mongodb.username,
    #     password=config.mongodb.password,
    # )


class Services(containers.DeclarativeContainer):
    """IoC container of business service providers"""
    config = providers.Configuration()
    gateways = providers.DependenciesContainer()

    time_service = Factory(
        TimeService,
        logic=Factory(
            Logic,
        ),
    )


class Application(containers.DeclarativeContainer):
    """IoC container of application component providers"""
    config = providers.Configuration()

    core = providers.Container(
        Core,
        config=config.core,
    )

    gateways = providers.Container(
        Gateways,
        config=config.gateways
    )

    services = providers.Container(
        Services,
        config=config.services,
        gateways=gateways,
    )

    argument_parser = providers.Factory(
        ArgumentParser,
        prog=config.info.name,
        description=config.info.description,
    )

    subcommands = providers.List(
        providers.Factory(
            TimeCommand,
            services.time_service,
        ),
    )

    main = providers.Factory(
        CommandProccessor,
        argument_parser,
        subcommands,
        config.info.version,
    )
