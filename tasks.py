import os

from invoke import task

# Parameterizing tasks with invoke
# https://docs.pyinvoke.org/en/0.11.1/getting_started.html#parameterizing-tasks


@task
def t(c):
    """
    Train Rasa bot
    """
    c.run(f"rasa train", pty=True)


@task
def sh(c):
    """
    Rasa shell
    """
    c.run(f"rasa shell", pty=True)
