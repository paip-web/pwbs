# -*- coding: utf-8 -*-
"""PAiP Web Build System - Docker Runner Class

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
import platform
import os
from subprocess import run
from pwbs.runner.runner import Runner

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'

# Docker Exceptions


class DockerNotSupportedException(Exception):
    """
    Docker is not supported on user platform
    """
    pass


class DockerCommandFailedException(Exception):
    """
    Docker command has failed
    """
    pass


class DockerCommandPermissionErrorException(Exception):
    """
    Docker command has failed
    """
    pass

# Decode to String


def convert_to_string(text) -> str:
    """
    Convert to String
    :param text: What to convert to string
    :return: Converted string
    """
    if text is None:
        return ''
    if isinstance(text, bytes):
        return text.decode('utf-8')
    return str(text)

# Docker Runner Class


class DockerRunner(Runner):
    """Docker Runner Class"""
    def __init__(self):
        """
        Runner Constructor
        """
        self.sudo_needed = False
        self.docker_image = 'paipweb/pwbs'
        self.docker_image_tag = 'edge-dev'
        if platform.system() == "Windows":
            self.run_command_template = "run -it --rm -v %cd%:/app {image}:{tag} {command}"
        else:
            self.run_command_template = "run -it --rm -v `pwd`:/app {image}:{tag} {command}"
        super().__init__()

    def init(self):
        """
        Runner Initialization Method
        """
        pass

    @staticmethod
    def execute_docker_command(command, sudo=False, capture_output=False):
        """
        Execute Docker Command
        :param command: Command to execute
        :param sudo: Has sudo should be used
        :param capture_output: Do capture all output from docker command
        :raises DockerCommandFailedException: Raised when command failed
        """
        sudo_prefix = "sudo " if sudo else ""
        docker_command = "{}docker {}".format(sudo_prefix, command)
        if capture_output:
            process = run(docker_command, shell=True, capture_output=True, check=False)
        else:
            process = run(docker_command, shell=True, check=False)
        if capture_output and 'connect: permission denied' in convert_to_string(process.stderr):
            raise DockerCommandPermissionErrorException("Command {} failed by Permissions".format(docker_command))
        if capture_output and process.returncode != 0:
            raise DockerNotSupportedException(
                "Command {} failed by status code {} with: {}".format(
                    docker_command,
                    process.returncode,
                    ' '.join((convert_to_string(process.stdout), convert_to_string(process.stderr)))
                )
            )
        if process.returncode != 0:
            raise DockerCommandFailedException(
                "Command {} failed with: {}".format(
                    docker_command,
                    ' '.join((convert_to_string(process.stdout), convert_to_string(process.stderr)))
                )
            )
        return process

    @staticmethod
    def is_it_docker() -> bool:
        """
        Check is PWBS running inside Docker Container
        :return: Result
        """
        if os.path.exists('/.dockerenv'):
            return True
        try:
            return any('docker' in line for line in open('/proc/self/cgroup'))
        except FileNotFoundError:
            return False

    def check_docker(self) -> None:
        """
        Check whether docker is available
        """
        try:
            try:
                # Check is Docker Accessible
                DockerRunner.execute_docker_command('ps', capture_output=True)
            except DockerCommandPermissionErrorException:
                # Check is Docker Accessible through sudo
                DockerRunner.execute_docker_command('ps', sudo=True, capture_output=True)
                self.sudo_needed = True
        except DockerCommandFailedException:
            raise DockerNotSupportedException("Docker commands failed to run")

    def execute_in_container(self, command: str):
        """
        Execute Command in PWBS Docker Container
        :param command: Command To Execute
        """
        return DockerRunner.execute_docker_command(
            self.run_command_template.format(
                image=self.docker_image,
                tag=self.docker_image_tag,
                command=command
            ),
            sudo=self.sudo_needed
        )

    def execute(self, command: str, *args, **kwargs):
        """
        Command Execution Method
        """
        self.check_docker()
        return self.execute_in_container(command)
