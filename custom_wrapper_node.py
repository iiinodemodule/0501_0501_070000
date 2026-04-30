import torch
from .src.BrightnessAdj import adjust_brightness


class BrightnessNode_0501_070000:
    """
    A custom node to adjust the brightness of an image.
    """

    CATEGORY = "0501_070000自訂演算法/未分類"

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "strength": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.1,
                }),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "execute"

    def execute(self, image, strength):
        return adjust_brightness(image, strength)
