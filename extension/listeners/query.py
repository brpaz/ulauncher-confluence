import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent

logger = logging.getLogger(__name__)


class KeywordQueryEventListener(EventListener):
    """ Listener that handles the user input """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event: KeywordQueryEvent, extension: Extension):
        """ Handles the event """
        kw_id = self.get_keyword_id(event.get_keyword(), extension.preferences)
        query = event.get_argument()

        is_favorites_search = False

        if kw_id == 'kw_favorites':
            is_favorites_search = True

        if query:
            query_parts = query.strip().split(">")

            # Zero or more search on spaces.
            if len(query_parts) < 2:
                return extension.list_spaces(event, is_favorites_search)

            search_query = query_parts[1:]
            search_query_parts = search_query[0].strip().split(" ")
            space_key = search_query_parts[0]

            if len(search_query_parts) >= 2:
                search_query = " ".join(search_query_parts[1:])
            else:
                search_query = None
            return extension.search_on_space(space_key, search_query)
        else:
            return extension.list_spaces(event, is_favorites_search)

    def get_keyword_id(self, keyword, preferences):
        """ Returns the keyword id, that matches the keyword name passed as argument """
        kw_id = None
        for key, value in preferences.items():
            if value == keyword:
                kw_id = key
                break

        return kw_id
