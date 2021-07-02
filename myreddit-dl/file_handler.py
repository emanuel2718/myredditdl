import os
import re
import utils
import json
from defaults import Defaults
from urllib.parse import urlparse
from pprint import pprint


class FileHandler():
    def __init__(self, cls: 'Downloader', item=None) -> None:
        self.cls = cls
        self.item = item
        self.log = utils.setup_logger(__name__, self.cls.args['debug'])
        self.defaults = Defaults(
            True) if self.cls.args['debug'] else Defaults()
        # TODO: refactor all of this to their own functions. So we can instantitate
        #       file_handler without getting paths and stuff.
        self.media_url = self.cls.curr_media_url if self.cls.curr_media_url else ''
        self.path = self.defaults.config_media_path
        self.path = self.path if self.path.endswith(
            '/') else self.path + os.sep
        self.json_file = self.defaults.metadata_file

    def create_path(self):
        if os.path.isdir(self.path):
            return
        try:
            os.makedirs(self.path)
            self.log.info(f'Path created: {self.path}')
        except BaseException:
            self.log.error(f'Invalid path: {self.path}')

    def get_path(self) -> str:
        return self.path

    def get_prefix(self) -> str:
        sub = self.get_subreddit_without_prefix(self.item.get_subreddit_prefixed())
        username = str(self.item.author)
        current_set_prefix = self.defaults.config_prefix
        if current_set_prefix == 'username':
            return username + '_'
        elif current_set_prefix == 'subreddit':
            return sub + '_'
        elif current_set_prefix == 'subreddit_username':
            return sub + '_' + username + '_'
        return username + '_' + sub + '_'

    @property
    def gallery_data(self) -> list:
        data = []
        for index, url in enumerate(self.media_url):
            self.cls.set_media_url(url)
            data.append({'url': url, 'path': self.path +
                         self.get_filename(url, str(index))})
        return data

    @property
    def absolute_path(self) -> list or str:
        if isinstance(self.media_url, list):
            return self.gallery_data
        return self.path + self.get_filename(self.media_url)

    @property
    def file_exist(self) -> bool:
        if isinstance(self.absolute_path, list):
            try:
                if os.path.isfile(self.absolute_path[0]['path']):
                    return True
            except BaseException:
                self.log.error(
                    f"File not found: {self.absolute_path[0]['path']}")
                return False

        elif os.path.isfile(self.absolute_path):
            return True
        return False

    @property
    def remove_file(self) -> None:
        if isinstance(self.absolute_path, list):
            for data in self.gallery_data:
                if os.path.exists(data['path']):
                    os.remove(data['path'])
                    self.log.debug(f"File removed: {data['path']}")
        else:
            if os.path.exists(self.absolute_path):
                os.remove(self.absolute_path)
                self.log.debug(f"File removed: {self.absolute_path}")

    def delete_database(self) -> None:
        try:
            if os.path.isfile(self.json_file):
                os.remove(self.json_file)
                self.log.debug('Database deleted')
        except IOError:
            self.log.error('While deleting database')

    @property
    def is_video(self) -> bool:
        if isinstance(self.media_url, list):
            return True if self.get_filename(
                self.media_url[0]).endswith('mp4') else False
        return True if self.get_filename(
            self.media_url).endswith('mp4') else False

    def get_filename(self, url: str, index='') -> str:
        # TODO: modify. Now all the urls are list. Figure out how to change this
        url = url[0] if isinstance(url, list) else url
        extension = str(self.get_file_extension(url))

        return str(self.get_prefix() + self.item.item_id + index + extension)

    def get_subreddit_without_prefix(self, sub: str) -> str:
        ''' Receive a r/subreddit string and return subreddit without
            the r/ prefix
        '''
        return sub.split('/')[1]

    def get_file_extension(self, url: str) -> str:
        try:
            parsed = urlparse(url)
            _, ext = os.path.splitext(parsed.path)
            return ext if not ext.endswith('.gifv') else '.mp4'
        except BaseException:
            self.log.error(f'Getting file extension of {url}')

    def get_filename_from_path(self, path: str):
        return path.rpartition(os.sep)[-1]

    def _get_item_metadata(self) -> dict:
        return {'Author': self.item.author,
                'Subreddit': self.item.get_subreddit_prefixed(),
                'Title': self.item.title,
                'Link': self.item.link,
                'Upvotes': self.item.upvotes_amount,
                'NSFW': self.item.is_nsfw(),
                'Post creation date': self.item.get_creation_date()
                }

    def save_metadata(self, path: str, filename: str):
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                if filename not in data:
                    data[filename] = self._get_item_metadata()
                    if self.cls.args['verbose']:
                        self.log.debug(f'Added to database: {filename}')
                else:
                    self.log.debug(f'Already in database: {filename}')

        except IOError:
            self.log.debug(f'Database created for {self.cls.user}')
            data = {f'{filename}': self._get_item_metadata()}

        with open(self.json_file, 'w') as f:
            json.dump(data, f, indent=4)

    def get_metadata(self, filename, meta_type=None):
        try:
            with open(self.json_file, 'r') as f:
                data = json.load(f)
                if filename in data.keys():
                    if meta_type:
                        utils.print_data(
                            f'[{meta_type.upper()}] {data[filename][meta_type]}')
                    else:
                        utils.print_metadata(f'{data[filename]}')
                else:
                    self.log.error(f'No data found for {filename}')

        except IOError:
            self.log.error('Database not found. Must download content first')

    def clean_debug(self):
        try:
            os.removedirs(self.defaults.debug_path)
            self.log.info('debug_media/ removed')

        except:
            self.log.info('No debug_media folder to delete')

        try:
            os.remove(self.defaults.debug_log_file)
            self.log.info('debug_log file removed')

        except:
            self.log.info('No debug_log file found')
        exit(0)


if __name__ == '__main__':
    utils.print_warning(utils.DONT_RUN_THIS_FILE)
