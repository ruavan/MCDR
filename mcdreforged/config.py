"""
MCDR config file stuffs
"""
from logging import Logger

from mcdreforged.utils.yaml_data_storage import YamlDataStorage

CONFIG_FILE = 'config.yml'
DEFAULT_CONFIG_RESOURCE_PATH = 'resources/default_config.yml'


class Config(YamlDataStorage):
	def __init__(self, logger: Logger):
		super().__init__(logger, CONFIG_FILE, DEFAULT_CONFIG_RESOURCE_PATH)
		self.storage = ()

	def read_config(self, allowed_missing_file):
		return self._load_data(allowed_missing_file)

	def __getitem__(self, item):
		return self.data[item]

	# -------------------------
	#   Actual data analyzers
	# -------------------------

	def is_debug_on(self):
		for value in self.data['debug']:
			if value is True:
				return True
		return False
