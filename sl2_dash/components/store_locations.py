
from sl2_dash.components.ids import JSON_STORE,CURRENT_PATCH_ID, ChannelCopy
from sl2_dash.utils.initial_json import DEFAULT_STORE_DATA

from dash import html, dcc, Output, Input, State

import datetime

stores=(dcc.Store(id=JSON_STORE,data=DEFAULT_STORE_DATA),   # main json storage location
        dcc.Store(id=CURRENT_PATCH_ID,data=0),              # number of the current patch
        dcc.Store(id=ChannelCopy.DOUBLE_CLICK_TIMESTAMP,    # date and time of the most recent click on the copy channel button
                  data=datetime.datetime.now().strftime(r'%d/%m/%y %H:%M:%S.%f')))