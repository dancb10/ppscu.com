from flask import current_app


class ProcessConfig:

    @staticmethod
    def get_services():
        return current_app.config['SERVICES']

    @staticmethod
    def get_loadbalancing(domain):
        for svc in ProcessConfig.get_services():
            if domain in svc["domain"]:
                return svc["loadbalancing"]

    @staticmethod
    def get_instances_by_domain(domain):
        for svc in ProcessConfig.get_services():
            if domain in svc["domain"]:
                return svc["hosts"]
