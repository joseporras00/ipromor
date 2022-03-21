import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output,Input,State
from data_reader import con

from app import app

server = app.server

app.layout =html.Div([
html.Div(
dcc.Input(id="email", type="text", placeholder="Escribe tu email",className="inputbox1",
style={'margin-left':'35%','width':'450px','height':'45px','padding':'10px','margin-top':'60px',
'font-size':'16px','border-width':'3px','border-color':'#a0a3a2'
}),
),
html.Div(
dcc.Input(id="passw", type="text", placeholder="Escribe tu contraseña",className="inputbox2",
style={'margin-left':'35%','width':'450px','height':'45px','padding':'10px','margin-top':'10px',
'font-size':'16px','border-width':'3px','border-color':'#a0a3a2',
}),
),
html.Div(
html.Button('Entrar', id='verify', n_clicks=0, style={'border-width':'3px','font-size':'14px'}),
style={'margin-left':'45%','padding-top':'30px'}),
html.Div(id='output1')
])

@app.callback(
    dash.dependencies.Output('output1', 'children'),
   [dash.dependencies.Input('verify', 'n_clicks')],
    state=[State('email', 'value'),
                State('passw', 'value')])
def update_output(n_clicks, email, passw):
    if email =='' or email == None or passw =='' or passw == None:
        return html.Div(children='',style={'padding-left':'550px','padding-top':'10px'})
    sql='select * from usuarios'
    df=pd.sql_read_query(sql, con=con)
    if email not in df:
        return html.Div(children='Email incorrecto',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
    is_true = df.loc[:, 'email'] == email
    df2 = df.loc[is_true]
    if df2['password']==passw:
        return html.Div(dcc.Link('Sesión iniciada con éxito', href='/dash1.py',style={'color':'#183d22','font-family': 'serif', 'font-weight': 'bold', "text-decoration": "none",'font-size':'20px'}),style={'padding-left':'605px','padding-top':'40px'})
else:
    return html.Div(children='Contraseña incorrecta',style={'padding-left':'550px','padding-top':'40px','font-size':'16px'})
