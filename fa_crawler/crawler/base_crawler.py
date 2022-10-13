from abc import ABCMeta, abstractmethod
from typing import Any, Dict, Generator, Optional, Tuple

import pandas as pd

RESULT_DATA_TYPE = Any
PARAM_TYPE = Dict[str, Any]


class BaseCrawler(metaclass=ABCMeta):

    class Callback(metaclass=ABCMeta):

        @abstractmethod
        def on_finished(
            self,
            data: Any,
            params: Dict,
        ) -> None:
            """[summary]

            Args:
                data (Any): [description]
                params (Dict): [description]

            Raises:
                NotImplementedError: [description]
            """
            raise NotImplementedError

        @abstractmethod
        def on_failed(
            self,
            e: Exception,
            params: Dict,
        ) -> None:
            """[summary]

            Args:
                e (Exception): [description]
                params (Dict): [description]

            Raises:
                NotImplementedError: [description]
            """
            raise NotImplementedError

    class DefaultCallback(Callback):

        def on_finished(
            self,
            data: pd.DataFrame,
            params: Dict,
        ) -> None:
            pass

        def on_failed(
            self,
            e: Exception,
            params: Dict,
        ) -> None:
            raise e

    def __init__(self):
        """init"""
        pass

    @abstractmethod
    def run(
        self,
        *args,
        callback: Callback = DefaultCallback(),
        **kwargs,
    ) -> Tuple[Optional[RESULT_DATA_TYPE], Optional[PARAM_TYPE]]:
        """_summary_

        Args:
            callback (Callback, optional): _description_. Defaults to DefaultCallback().

        Raises:
            NotImplementedError: _description_

        Returns:
            Tuple[Optional[RESULT_DATA_TYPE], Optional[PARAM_TYPE]]: _description_
        """
        raise NotImplementedError

    def run_generator(
        self,
        *args,
        callback: Callback = DefaultCallback(),
        **kwargs,
    ) -> Generator:
        raise NotImplementedError
