"""
A job corresponds to a microservice, a link in the workflow, and the `Jobs`
table in the database.

Initialization of `Job` objects is typically done via a `JobChain`,
corresponding to a chain in the workflow. The `JobChain` object handles
determining the next job to be run, and passing data between jobs.

The `Job` class is a base class for other job types. There are various
concrete types of jobs, handled by subclasses:
    * `ClientScriptJob`, handling Jobs to be execute on MCPClient
    * `DecisionJob`, handling workflow decision points
    * `LocalJob`, handling work done directly on MCPServer
"""
from a3m.server.jobs.base import Job
from a3m.server.jobs.chain import JobChain
from a3m.server.jobs.client import ClientScriptJob
from a3m.server.jobs.client import DirectoryClientScriptJob
from a3m.server.jobs.client import FilesClientScriptJob
from a3m.server.jobs.decisions import DecisionJob
from a3m.server.jobs.decisions import NextChainDecisionJob
from a3m.server.jobs.decisions import UpdateContextDecisionJob
from a3m.server.jobs.local import GetUnitVarLinkJob
from a3m.server.jobs.local import LocalJob
from a3m.server.jobs.local import SetUnitVarLinkJob

__all__ = (
    "ClientScriptJob",
    "DecisionJob",
    "DirectoryClientScriptJob",
    "FilesClientScriptJob",
    "GetUnitVarLinkJob",
    "Job",
    "JobChain",
    "LocalJob",
    "NextChainDecisionJob",
    "SetUnitVarLinkJob",
    "UpdateContextDecisionJob",
)
