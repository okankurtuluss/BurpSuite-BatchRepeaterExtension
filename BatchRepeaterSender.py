from burp import IBurpExtender, IContextMenuFactory
from javax.swing import JMenuItem
from java.util import List, Arrays

class BurpExtender(IBurpExtender, IContextMenuFactory):
    
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        callbacks.setExtensionName("Batch Repeater Sender")
        callbacks.registerContextMenuFactory(self)
    
    def createMenuItems(self, invocation):
        menu_item = JMenuItem("Send Requests to Repeater", actionPerformed=lambda x: self.send_requests_to_repeater(invocation))
        return Arrays.asList(menu_item)

    def send_requests_to_repeater(self, invocation):
        selected_items = invocation.getSelectedMessages()
        for item in selected_items:
            request = item.getRequest()
            host = item.getHttpService().getHost()
            port = item.getHttpService().getPort()
            use_https = item.getHttpService().getProtocol() == "https"
            self._callbacks.sendToRepeater(host, port, use_https, request, None)
