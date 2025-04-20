# This module uses LayoutParser to identify layout elements in a document image.
# -*- coding: utf-8 -*-
import numpy as np
import layoutparser as lp

def detect_layout_elements(image: np.ndarray) -> list:
    """Identify headings, paragraphs, tables using LayoutParser."""
    model = lp.Detectron2LayoutModel(config_path="configs/layout_config.yaml")
    layout = model.detect(image)
    return sorted(layout, key=lambda x: x.coordinates[1])  # Sort by Y-position