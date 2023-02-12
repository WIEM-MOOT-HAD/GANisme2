#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash import html
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output
from app import app

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow import keras

TF_CPP_MIN_LOG_LEVEL="2"


def generate_latent_points(batch_size, latent_dim ):
	random_latent_vectors = tf.random.normal(shape=(batch_size, latent_dim))
	return random_latent_vectors 
 
def plot_generated(generated_images):
    plt.axis("off")
    plt.imshow((generated_images*255).astype("int32")[0])
    plt.savefig("plot.png") 

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1(" I am your painter 3.0", className="text-center")
                    , className="mb-4 mt-4")
        ]),
        # dbc.Row([
        #     dbc.Col(html.H4(children='Avatar Generator'
        #                              ))
        #     ]),
        dbc.Row([
            dbc.Col(html.H5(children='Please press here to get a new painting')                        
                    , className="mb-4")
            ]),
        dbc.Button(
        id='click-here',
        children=html.Div([
            'Click Here!'
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '40px',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px',
            'background-color':'green'
        },
        ),
        html.Div(id='output-avatar', className="mb-4"),
        html.A("Get the full code of app on my github repositary",
               href="https://github.com/")
])])

@app.callback(Output('output-avatar', 'children'),
              Input('click-here', 'n_clicks'),)
def on_button_click(n):
    if n is None:
        return "Not clicked."
    else:
        im = None
        model = keras.models.load_model('/home/wiem/Documents/PROJET/GANisme/application_streamlit/assets/generator-400x400.h5')
        model.compile()
        latent_points = generate_latent_points(20, 400)
        generated_images = model.predict(latent_points)



    
        return html.Div([
            html.Img(src=im, style={'height':'100%', 'width':'100%'}),
            html.Hr(),
            ], className="text-center")
