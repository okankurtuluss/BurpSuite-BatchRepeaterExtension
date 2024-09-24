# BurpSuite-BatchRepeaterExtension
A Python (Jython) extension for Burp Suite that allows sending multiple HTTP requests to the Repeater in bulk

## Installation Steps
Click the Add button in the Extensions tab.

![](https://github.com/okankurtuluss/BurpSuite-BatchRepeaterExtension/blob/okankurtuluss/main/screenshots/step1.png)

In the window that opens, select Python as the Extension Type. For the Extension file, choose the BatchRepeaterSender.py file.

![](https://github.com/okankurtuluss/BurpSuite-BatchRepeaterExtension/blob/okankurtuluss/main/screenshots/step2.png)

Once loaded, go to the HTTP history tab, select the requests you want, right-click, and navigate to Extensions -> Batch Repeater Sender -> Send requests to Repeater. All selected requests will be sent to the Repeater.

![](https://github.com/okankurtuluss/BurpSuite-BatchRepeaterExtension/blob/okankurtuluss/main/screenshots/step3.png)
