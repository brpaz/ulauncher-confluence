from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction


class ItemEnterEventListener(EventListener):
    """ Listener that handles the click on an item """

    # pylint: disable=unused-argument,no-self-use
    def on_event(self, event: ItemEnterEvent, extension: Extension):
        """ Handles the event """
        data = event.get_data()
        return RenderResultListAction([
            ExtensionResultItem(icon='images/icon.png',
                                name=data['new_name'],
                                on_enter=HideWindowAction())
        ])
