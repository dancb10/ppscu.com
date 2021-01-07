import logging
from random import randrange

from exceptions import NoHealthyInstancesForDomainException
from utils.healthcheck import HealthCheck
from utils.process_config import ProcessConfig

log = logging.getLogger('proxy')


class LoadBalancing:
    def __init__(self):
        self.type = 'default'

    def pick_instance(self):
        pass

    def get_lb_algorithm(self, domain, counter):
        algorithm = ProcessConfig().get_loadbalancing(domain)
        if algorithm == 'random':
            log.info('Using load balancing algorithm: random for domain: {}'.format(domain))
            return RandomLoadBalancing(domain)
        if algorithm == 'roundrobin':
            log.info('Using load balancing algorithm: roundrobin for domain: {}'.format(domain))
            return RoundRobinLoadBalancing(domain, counter)

    def get_healthy_instances(self, domain):
        healthy_instances = []
        available_instances = ProcessConfig().get_instances_by_domain(domain)
        log.warning('Available instances: {}'.format(available_instances))
        for instance in available_instances:
            healthcheck = HealthCheck(instance['address'], instance['port'])
            if healthcheck.check_instance():
                healthy_instances.append([instance['address'], instance['port']])
        if len(healthy_instances):
            return healthy_instances
        raise NoHealthyInstancesForDomainException


class RandomLoadBalancing(LoadBalancing):
    def __init__(self, domain):
        super().__init__()
        self.type = 'random'
        self.domain = domain

    def pick_instance(self):
        healthy_instances = self.get_healthy_instances(self.domain)
        return healthy_instances[randrange(len(healthy_instances))]


class RoundRobinLoadBalancing(LoadBalancing):
    def __init__(self, domain, counter):
        super().__init__()
        self.type = 'roundrobin'
        self.domain = domain
        self.counter = counter

    def pick_instance(self):
        healthy_instances = self.get_healthy_instances(self.domain)
        return healthy_instances[self.counter['requests'] % len(healthy_instances)]
