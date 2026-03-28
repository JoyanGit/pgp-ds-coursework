#!/usr/bin/env python
# coding: utf-8

# # Basic Imports and Set ups¶

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import numpy as np
import os
from faker import Faker
import matplotlib.pyplot as plt
from datetime import datetime
from IPython.display import display, HTML
import seaborn as sns
import statsmodels.api as sm


# In[2]:


import pandas as pd
from IPython.display import display, HTML

def render_book_table(title, columns, rows):
    """
    Render a documentation-style table in Jupyter.

    Parameters
    ----------
    title : str
        Title displayed above the table
    columns : list
        Column names
    rows : list of lists
        Table data rows
    """

    table_data = pd.DataFrame(rows, columns=columns)

    styled_table = (
        table_data.style
        .hide(axis="index")
        .set_table_styles([
            {"selector": "th",
             "props": [("background-color", "#f2f2f2"),
                       ("font-weight", "bold"),
                       ("text-align", "center"),
                       ("border", "1px solid #999"),
                       ("padding", "8px")]},

            {"selector": "td",
             "props": [("border", "1px solid #999"),
                       ("padding", "8px"),
                       ("white-space", "normal"),
                       ("text-align", "left")]},

            {"selector": "table",
             "props": [("border-collapse", "collapse"),
                       ("width", "100%")]}
        ])
    )

    display(HTML(f"<h3>{title}</h3>"))
    display(styled_table)



# In[3]:


import os
import json

def search_notebooks(query, directory="."):
    """Searches for a string in all .ipynb files in a directory."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                path = os.path.join(root, file)
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        # Load notebook as a dictionary
                        notebook = json.load(f)
                        for i, cell in enumerate(notebook.get("cells", [])):
                            # Combine all lines in a cell into one string
                            source = "".join(cell.get("source", []))
                            if query.lower() in source.lower():
                                print(f"Found in: {path} (Cell #{i})")
                except (json.JSONDecodeError, PermissionError):
                    # Skip files that aren't valid JSON or are restricted
                    continue

# Usage: Replace 'your_text_here' with your search term
# search_notebooks("array_archive.npz")


# In[4]:


get_ipython().run_cell_magic('html', '', '<style>\n\n.green-box {\n    border: 2px dotted #28a745;\n    background-color: #e6ffe6;\n    padding: 15px;\n    border-radius: 8px;\n    margin-top: 10px;\n}\n\n.red-box {\n    border: 2px dotted #dc3545;\n    background-color: #ffe6e6;\n    padding: 15px;\n    border-radius: 8px;\n    margin-top: 10px;\n}\n\n.blue-box {\n    border: 2px dotted #007bff;\n    background-color: #e7f1ff;\n    padding: 15px;\n    border-radius: 8px;\n    margin-top: 10px;\n}\n\n</style>\n')


# Usage : 
# <div class="blue-box">
# 
# # 🧠
# 
# `dateutil.parser` is a useful but imperfect tool. Notably, it will recognize
# some strings as dates that you might prefer that it didn’t—
# for example, '42' will be parsed as the year 2042 with today’s calendar
# date.
# 
# </div>

# Usage : 
# <div class="red-box">
# 
# # 🚨
# 
# `dateutil.parser` is a useful but imperfect tool. Notably, it will recognize
# some strings as dates that you might prefer that it didn’t—
# for example, '42' will be parsed as the year 2042 with today’s calendar
# date.
# 
# </div>

# In[5]:


get_ipython().run_cell_magic('html', '', '<style>\n\n.blue-box {\n    border: 2px dotted #007bff;\n    background-color: #e7f1ff;\n    padding: 15px;\n    border-radius: 8px;\n    margin-top: 10px;\n}\n\n.collapsible summary {\n    font-size: 16px;\n    font-weight: bold;\n    cursor: pointer;\n    outline: none;\n}\n\n</style>\n')


# <details class="collapsible blue-box">
# 
# <summary>📘 Click to expand explanation</summary>
# 
# ### Infection Spread Logic
# 
# We compute spread using parameter `beta`.

# In[6]:


get_ipython().run_cell_magic('html', '', '<style>\n.big-icon {\n    font-size: 8em;\n}\n</style>\n')


# In[7]:


get_ipython().run_cell_magic('html', '', '<style>\n.red-dashed-ruler {\n    border: none;\n    border-top: 3px dashed red;\n    margin: 12px 0;\n}\n</style>\n')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




