
from .ids import Nav
import dash_bootstrap_components as dbc
from dash import html,dcc


header_navbar =  dbc.NavbarSimple(
        children=[

            # info about the app
            dbc.NavItem(
                
                    dbc.NavLink(
                        dbc.Row(
                        [
                            dbc.Col(html.I(className="bi bi-question-circle fs-4"), width="auto", style={"marginRight": "0.5rem"}),
                            dbc.Col(html.H5("Instructions",style={"marginTop": "9px"}))
                        ],
                        align="center", className="g-0"
                    ),
                    href=None,
                    className="d-flex align-items-center h-100 nav-link",
                    style={"height": "100%",'cursor':'pointer'},
                    id=Nav.INSTRUCTIONS,
                ),
                className="h-100"
            ),

            


            # Upload (keep dcc.Upload id="upload" for sl2_dash.callbacks)
            dbc.NavItem(
                dcc.Upload(
                    dbc.NavLink(
                        dbc.Row(
                        [
                            dbc.Col(html.I(className="bi bi-upload fs-4"), width="auto", style={"marginRight": "0.5rem"}),
                            dbc.Col(html.H5("Upload .tsl",style={"marginTop": "9px"}))
                        ],
                        align="center", className="g-0"
                    ),
                        
                        href="#",
                        className="d-flex align-items-center h-100 nav-link",
                        style={"height": "100%"}
                    ),
                    id=Nav.UPLOAD,
                    style={ "height": "100%"}
                ),
                className="h-100"
            ),

            # Choose default as a nav-link
            dbc.NavItem(
                dbc.NavLink(
                    dbc.Row(
                        [
                            dbc.Col(html.I(className="bi bi-folder2-open fs-4"), width="auto", style={"marginRight": "0.5rem"}),
                            dbc.Col(html.H5("Load Default .tsl",style={"marginTop": "9px"})) 
                        ],
                        align="center", className="g-0"
                    ),
                    href="#",
                    id=Nav.DEFAULT_CHOICE,
                    
                    className="d-flex align-items-center h-100 nav-link",
                    style={ "height": "100%"}
                ),
                className="h-100"
            ),


            # Download as a nav-link (preserve id "download_button")
            dbc.NavItem(
                dbc.NavLink(
                    dbc.Row(
                        [
                            dbc.Col(html.I(className="bi bi-download fs-4"), width="auto", style={"marginRight": "0.5rem"}),
                            dbc.Col(html.H5("Download .tsl",style={"marginTop": "9px"})),
                            dcc.Download(id=Nav.DOWNLOAD)
                        ],
                        align="center", className="g-0"
                    ),
                    href="#",
                    id=Nav.DOWNLOAD_BUTTON,
                    className="d-flex align-items-center h-100 nav-link",
                    style={"height": "100%"}
                ),
                className="h-100"
            ),

            # info about the app
            dbc.NavItem(
                    dbc.NavLink(
                        dbc.Row(
                        [
                            dbc.Col(html.I(className="bi bi-info-circle fs-4"), width="auto", style={"marginRight": "0.5rem"}),
                            dbc.Col(html.H5("About",style={"marginTop": "9px"}))
                        ],
                        align="center", className="g-0"
                    ),
                        
                        href=None,
                        active=False,
                        className="d-flex align-items-center h-100 nav-link",
                        style={"height": "100%",'cursor':'pointer'},
                     id=Nav.INFO,
                ),
                className="h-100"
            ),
            ## GitHub link at end 
            #dbc.NavItem(
            #    dbc.NavLink(
            #        dbc.Row(
            #            [
            #                dbc.Col(html.I(className="bi bi-github fs-4"), width="auto", style={"marginRight": "0.5rem"}),
            #                dbc.Col(html.H4("View on GitHub",style={"marginTop": "9px"}))
            #            ],
            #            align="center", className="g-0"
            #        ),
            #        href="https://github.com/lturica/midi_work",
            #        className="d-flex align-items-center h-100 nav-link",
            #        style={"height": "100%"}
            #    ),
            #    className="h-100"
            #),
            
        ],
        brand=html.H2("SL-2 Live Set Editor"),
        brand_href="#",
        color="primary",
        links_left=False,
        dark=True,
        fluid=True
    )
