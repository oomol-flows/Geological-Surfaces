from oocana import Context
import plotly.graph_objects as go

import pandas as pd

# "in", "out" is the default node key.
# Redefine the name and type of the node, change it manually below.
# Click on the gear(⚙) to configure the input output UI

def main(inputs: dict, context: Context):
  # Read data from a csv
  geological_data = inputs.get("geological_data")
  z_data = pd.read_csv(geological_data)

  fig = go.Figure(data=[go.Surface(z=z_data.values)])
  fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                    highlightcolor="limegreen", project_z=True))
  fig.update_layout(title='Mt Bruno Elevation', autosize=False,
                    scene_camera_eye=dict(x=1.87, y=0.88, z=-0.64),
                    width=500, height=500,
                    margin=dict(l=65, r=50, b=65, t=90)
  )

  fig.show()

  return { "out": None }
