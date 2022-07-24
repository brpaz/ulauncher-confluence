""" Main Module """

import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction
from extension.listeners.query import KeywordQueryEventListener
from extension.listeners.item_enter import ItemEnterEventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.event import PreferencesEvent, PreferencesUpdateEvent
from extension.listeners.preferences import PreferencesEventListener, PreferencesUpdateEventListener
from atlassian import Confluence

logger = logging.getLogger(__name__)


class ConfluenceExtension(Extension):
    """ Main Extension Class  """

    confluence_client: Confluence

    def __init__(self):
        """ Initializes the extension """
        super(ConfluenceExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())

        self.subscribe(PreferencesEvent, PreferencesEventListener())
        self.subscribe(PreferencesUpdateEvent,
                       PreferencesUpdateEventListener())

    def show_message(self, message):
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name=message,
                                on_enter=HideWindowAction())
        ])

    def list_spaces(self, event: KeywordQueryEvent, is_favorites_search: bool):
        query = event.get_argument()
        kw = event.get_keyword()

        if is_favorites_search:
            cql_query = 'favourite = currentUser() and type = "page"'
            spaces = self.confluence_client.cql(cql=cql_query,
                                                limit=50,
                                                expand="space")
            result = spaces["results"]

            mapped_result = []
            for row in result:
                key = row["content"]["_expandable"]["space"].split("/")[-1]
                mapped_result.append({
                    "name": row["title"],
                    'key': key,
                    'url': row["url"]
                })
            result = mapped_result
        else:
            spaces = self.confluence_client.get_all_spaces(
                space_status='current', limit=50)
            result = spaces["results"]

        if query:
            result = [x for x in result if query.lower() in x["name"].lower()]

        if len(result) == 0:
            return self.show_message("No spaces found")

        items = []
        for space in result:

            space_url = self.preferences["server_url"]
            if "url" in space:
                space_url = self.preferences["server_url"] + "/wiki" + space[
                    "url"]
            elif "_links" in space:
                space_url = self.preferences["server_url"] + "/wiki" + space[
                    "_links"]["webui"]

            items.append(
                ExtensionResultItem(icon='images/icon.png',
                                    name=space["name"],
                                    description=space["key"],
                                    on_alt_enter=OpenUrlAction(space_url),
                                    on_enter=SetUserQueryAction(
                                        "{} > {} ".format(kw, space["key"]))))

        return RenderResultListAction(items)

    def search_on_space(self, space_key: str, query: str):

        if query:
            cql_query = 'space = "{}" and type=page and title ~ "{}*"'.format(
                space_key, query)
            pages = self.confluence_client.cql(cql=cql_query, limit=15)
            pages = pages["results"]
        else:
            pages = self.confluence_client.get_all_pages_from_space(
                space_key, limit=10, content_type='page', expand=True)

        if not pages:
            return self.show_message("no results found")

        items = []
        for page in pages:
            items.append(self.map_page_detail(page))

        return RenderResultListAction(items)

    def map_page_detail(self, page):
        if "content" in page:
            title = page["content"]["title"]
        else:
            title = page["title"]

        description = ""

        if "url" in page:
            url = self.preferences["server_url"] + "/wiki" + page["url"]
        else:
            url = self.preferences["server_url"]

        if 'excerpt' in page:
            description = page["excerpt"][:100]

        return ExtensionResultItem(icon='images/icon.png',
                                   name=title,
                                   description=description,
                                   on_enter=OpenUrlAction(url))

    def create_confluence_client(self, server: str, email: str,
                                 access_token: str):
        self.confluence_client = Confluence(url=server,
                                            username=email,
                                            password=access_token,
                                            cloud=True)
