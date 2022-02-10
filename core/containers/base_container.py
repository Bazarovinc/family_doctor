from dependency_injector import containers, providers

from core.config_constants import WIRING_MODULES
from core.containers.repo_container import ReposContainer
from core.containers.service_container import ServicesContainer


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()
    wiring_config = containers.WiringConfiguration(modules=WIRING_MODULES)
    repos = providers.Container(ReposContainer)
    services = providers.Container(ServicesContainer, repos=repos)
