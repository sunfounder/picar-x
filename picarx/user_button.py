from .get_hat import is_fusion_hat
if is_fusion_hat:
    from fusion_hat.user_button import UserButton
else:
    from robot_hat.user_button import UserButton
