#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           ���[�K��ilv?*	/F��wC�^y~r��:��X(���Aq���`��6F�[M����en�?����Y��[��{��w��q�E�CL�l��*���G�;(�=r�P��ha|�cH�b��`��
"""
from hashlib import sha256
print sha256(blob).hexdigest()
