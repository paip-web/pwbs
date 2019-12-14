# -*- coding: utf-8 -*-
"""PAiP Web Build System - Pipeline Pattern

NAME - PAiP Web Build System
AUTHOR - Patryk Adamczyk <patrykadamczyk@paipweb.com>
LICENSE - MIT

"""
# Imports
from typing import Union
from typing import Dict
from typing import Any
from typing import List

# Underscore Variables

"""Author of the module"""
__author__ = 'Patryk Adamczyk'
"""Module License"""
__license__ = 'MIT'
"""Documentation format"""
__docformat__ = 'restructuredtext en'


# Pipeline Class
StageDict = Dict[str, Any]


def finisher_stage(this, *a, nf, **kw, ):
    """Finish Stage"""
    if len(kw) != 0:
        # noinspection PyRedundantParentheses
        return (*a, *(kw.values()))
    if len(a) == 1:
        return a[0]
    if len(a) != 0:
        return a
    return None


def forwarder_stage(*a, nf, **kw):
    """Forwarder Stage"""
    return nf(*a, **kw)


class Pipeline:
    """
    Pipeline Class

    Example: test = lambda x,nf: nf(x**2)
    """

    """Stages in Pipeline"""
    stages: StageDict = {}

    """Default Stage"""
    default_stage = finisher_stage

    def __init__(self, stages: Union[StageDict, None] = None):
        """Pipeline Constructor"""
        if stages is None:
            stages = {}
        self.stages = stages

    def __setitem__(self, stage_name: str, stage: Any) -> None:
        """Stage Registration"""
        if stage is None:
            return
        self.stages[stage_name] = stage

    def __getitem__(self, stage_name: str) -> Any:
        """Pipeline Get Stage Method"""
        if stage_name in self.stages.keys():
            return self.stages[stage_name]
        return None

    def __delitem__(self, stage_name: str) -> None:
        """Pipeline Delete Stage Method"""
        del self.stages[stage_name]

    def __contains__(self, stage_name: str) -> bool:
        """Pipeline Is in Method"""
        return stage_name in self.stages.keys()

    def __call__(self, *args, **kwargs):
        """Pipeline Executor"""
        kwargs['nf'] = self.__call__
        if len(self.stages) <= 0:
            return self.default_stage(*args, **kwargs)
        current_stage_key, current_stage = None, None
        for k, v in self.stages.items():
            current_stage_key, current_stage = k, v
            break
        del self[current_stage_key]
        return current_stage(*args, **kwargs)

    @staticmethod
    def from_list(stages: Union[List[Any], None]):
        """
        Generate Pipeline from list
        :param stages: List of Stages Function
        :return: Created Pipeline
        """
        p = Pipeline()
        if stages is None:
            return p
        for k, stage in enumerate(stages):
            p[str(k)] = stage
        return p
