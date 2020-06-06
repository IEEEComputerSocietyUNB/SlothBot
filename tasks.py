import os
import platform
from invoke import task
from functools import wraps


# Parameterizing tasks with invoke
# https://docs.pyinvoke.org/en/0.11.1/getting_started.html#parameterizing-tasks
@task
def b(c):
    """
    Formats code according to PEP8's pattern
    """
    c.run("black actions.py tasks.py")


@task
def t(c):
    """
    Train Rasa bot
    """
    if platform.system() != "Windows":
        c.run(f"rasa train", pty=True)
    else:
        c.run(f"rasa train")


@task
def s(c):
    """
    Rasa shell
    """
    if platform.system() != "Windows":
        c.run(f"rasa shell", pty=True)
    else:
        c.run(f"rasa shell")


@task
def sh(c):
    """
    Rasa shell and server
    """
    if platform.system() != "Windows":
        c.run(f"rasa run actions & rasa shell", pty=True)
    else:
        c.run(f"rasa run actions & rasa shell")



@task
def sv(c):
    """ Start Rasa server """
    if platform.system() != "Windows":
        c.run(f"rasa run actions", pty=True)
    else:
        c.run(f"rasa run actions")


@task
def stop(c):
    """
    Stop Rasa server
    """
    if platform.system() != "Windows":
        c.run("pkill -f rasa", pty=True)
        print("Rasa server stopped.")
    else:
        # hope it works ok for windows :(
        c.run("tskill -f rasa")
        print("Rasa server stopped.")


@task
def dm(c):
    """
    Remove all models on models folder
    """
    if platform.system() != "Windows":
        c.run("rm -f models/*", pty=True)
        print("All model files removed.")
    else:
        c.run("rd /s /q models/*")
        print("All model files removed.")

@task
def dt(c):
    """
    Remove all models on models folder and retrain
    """
    dm(c)
    t(c)
