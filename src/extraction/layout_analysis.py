# This module uses LayoutParser to identify layout elements in a document image.
# -*- coding: utf-8 -*-
import numpy as np
import layoutparser as lp
from typing import List, Any

def detect_layout_elements(image: np.ndarray) -> List[Any]:
    """
    Identify headings, paragraphs, tables using LayoutParser.
    
    Args:
        image: numpy array containing the document image
        
    Returns:
        List of layout elements sorted by vertical position
    """
    # Initialize with pre-trained PubLayNet model
    model = lp.Detectron2LayoutModel(
        config_path="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
        label_map={
            0: "Text",
            1: "Title", 
            2: "List",
            3: "Table",
            4: "Figure"
        }
    )
    
    # Detect layout elements
    layout = model.detect(image)
    
    # Sort elements by vertical position
    return sorted(layout, key=lambda x: x.coordinates[1])