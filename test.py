#imports
import fastapi
from fastapi import FastAPI, Request
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles