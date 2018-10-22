# Sample for Bobby
import logging
import json
import datetime
from pygateway.threaded_data_provider import *
from pystrandz.pystrandz import *

logger = logging.getLogger()

CONFIG_SECTION = 'strandz'


class DataProvider(ThreadedDataProvider):

    def __init__(self, config):
        ThreadedDataProvider.__init__(self, config, CONFIG_SECTION)
        self._client = None
        self._control_list = config.get(CONFIG_SECTION, 'control_list')
        self._model = {}
        self._config_type = config.get(CONFIG_SECTION, 'type')
        self._url = config.get(CONFIG_SECTION, 'url')
        hostList = self._parse_url(self._url)
        self._hostname = hostList[0] if hostList else None
        self._port = hostList[1] if hostList else None

    def _parse_url(self, url):
        '''
        Parse url for hostname and port
        @returns list of length 2: hostname and port
        '''
        if self._url is None:
            return None
        urlList = None
        try:
            initList = self._url.split("/")
            urlList = initList[2].split(":")
        except Exception:
            logger.error("Error parsing URL to extra hostname and port.")
        return urlList

    def start(self):
        if self._client is None:
            try:
                self._client = StrandzClient(self._hostname, self._port)
            except Exception:
                logger.exception('Exception during StrandzClient init. ')
                return
        ThreadedDataProvider.start(self)

    def stop(self):
        if self._client is not None:
            try:
                ThreadedDataProvider.stop(self)
                self._client = None
            except Exception:
                logger.exception('Exception during Strandz dp stop. ')
        self._client = None

    def read(self):
        '''
        @return model with timestamp
        '''
        self._model['timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.000Z')
        return self._model

    def _update_model(self):
        """Populate model with control, control_value pairs from control_map"""
        controlNames = {}
        if self._control_list is not None:
            for control in self._control_list:
                controlList = control.split("=")
                if (len(controlList) == 2):
                    controlNames[controlList[0]] = controlList[1]
                else:
                    controlNames[controlList[0]] = controlList[0]
            try:
                datapoints = self._client.readLatestDatapointsForControlGroup(controlNames.keys())
                for dp in datapoints:
                    shortname = dp.getShortname()
                    logger.debug("Shortname: " + shortname)
                    val = dp.getValue()
                    logger.debug("Value: " + val)
                    if shortname in controlNames and val:
                        self._model[controlNames[shortname]] = val
                    else:
                        # on missing control, dp value is the control name
                        logger.info('Null value found in control {} from control list or improper control config format. '.format(val))
            except Exception:
                logger.info('Exception reading control {}. '.format(shortname))
