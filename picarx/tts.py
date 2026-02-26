from .get_hat import is_fusion_hat
if is_fusion_hat:
    from fusion_hat.tts import *
else:
    from robot_hat.tts import *
