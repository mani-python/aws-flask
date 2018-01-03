import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import pandas as pd
import flask

app = dash.Dash(__name__)
server = app.server

# app.scripts.config.serve_locally = True
# app.css.config.serve_locally = True
shieldstatus = pd.read_csv(
    'https://raw.githubusercontent.com/mani-python/aws-flask/master/shieldstatus.csv',error_bad_lines=False)


DF_SIMPLE = pd.DataFrame({
    'x': ['A', 'B', 'C', 'D', 'E', 'F'],
    'y': [4, 3, 1, 2, 3, 6],
    'z': ['a', 'b', 'c', 'a', 'b', 'c']
})


dataframes = {'shieldstatus': shieldstatus,
              'DF_SIMPLE': DF_SIMPLE}


def get_data_object(user_selection):
    '''
    For user selections, return the relevant in-memory data frame.
    '''
    return dataframes[user_selection]


app.layout = html.Div([
    html.H4('DataTable'),
    html.Label('Report type:', style={'font-weight': 'bold'}),
    dcc.Dropdown(
        id='field-dropdown',
        options=[{'label': df, 'value': df} for df in dataframes],
        value='shieldstatus',
        #clearable=False
    ),
    dt.DataTable(
        # Initialise the rows
        rows=[{}],
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[],
        id='table'
    ),
    html.Div(id='selected-indexes')
], className="container")


@app.callback(Output('table', 'rows'), [Input('field-dropdown', 'value')])
def update_table(user_selection):
    '''
    For user selections, return the relevant table
    '''
    df = get_data_object(user_selection)
    return df.to_dict('records')


app.css.append_css({
    "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
})

if __name__ == '__main__':
    app.run_server(debug=True)
