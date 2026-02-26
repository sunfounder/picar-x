
is_fusion_hat = False
try:
    import fusion_hat
    import os
    if os.path.exists('/sys/class/fusion_hat'):
        is_fusion_hat = True
    else:
        is_fusion_hat = False
except ImportError:
    pass